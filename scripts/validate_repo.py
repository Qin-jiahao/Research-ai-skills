#!/usr/bin/env python3
"""Dependency-free structural checks for the bilingual research resource repository."""

from pathlib import Path
import json
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def has_any(text: str, markers: tuple[str, ...]) -> bool:
    return any(marker.lower() in text.lower() for marker in markers)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        error(f"{path}: not valid UTF-8 ({exc})")
        return ""


def check_frontmatter(path: Path, expected_name: str) -> None:
    text = read(path)
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        error(f"{path}: missing YAML frontmatter")
        return
    block = text.split("---\n", 2)[1]
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", block, re.M)
    description = re.search(r"^description:\s*(.+)$", block, re.M)
    if not name:
        error(f"{path}: invalid name")
    elif name.group(1) != expected_name:
        error(f"{path}: name {name.group(1)!r} does not match directory {expected_name!r}")
    if not description or not description.group(1).strip():
        error(f"{path}: missing description")

    required = {
        "use case": ("适用场景", "use case", "when to use", "## use", "## purpose"),
        "boundaries": ("边界", "boundaries", "scope and boundaries", "limitations", "限制"),
        "inputs": ("必需输入", "所需输入", "required inputs", "## inputs"),
        "workflow": ("工作流程", "workflow", "core workflow"),
        "output": ("输出格式", "output format", "expected output", "## output"),
        "quality checks": ("质量检查", "quality checks"),
        "limitations": ("局限性", "limitations", "## 限制", "## limitations"),
        "complete example": ("完整输入", "complete input", "完整案例"),
        "incomplete example": ("信息不足", "incomplete input", "incomplete case"),
        "source": ("来源", "source"),
    }
    for label, markers in required.items():
        if not has_any(text, markers):
            error(f"{path}: missing required Skill section: {label}")


def check_prompt(path: Path) -> None:
    text = read(path)
    if not has_any(text, ("中文", "Chinese")):
        error(f"{path}: missing Chinese section")
    if not has_any(text, ("English", "英文")):
        error(f"{path}: missing English section")
    required = {
        "use case": ("使用场景", "use case", "when to use"),
        "inputs": ("输入要求", "required inputs", "input requirements", "### input"),
        "output": ("输出要求", "expected output", "output requirements", "output format"),
        "fabrication ban": ("禁止编造", "fabrication ban", "do not invent", "不得编造"),
        "missing information": ("信息不足", "missing information", "to be provided", "待补充"),
        "bilingual example": ("双语示例", "bilingual example", "complete input", "完整输入"),
        "source": ("来源", "source"),
    }
    for label, markers in required.items():
        if not has_any(text, markers):
            error(f"{path}: missing required Prompt section: {label}")


def check_markdown_links() -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = read(path)
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = target.strip().split()[0]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local = (path.parent / target.split("#", 1)[0]).resolve()
            if not local.exists():
                error(f"{path}: broken local link {target}")


def check_catalog() -> None:
    catalog_path = ROOT / "catalog" / "resources.json"
    if not catalog_path.exists():
        error("catalog/resources.json: missing")
        return
    try:
        catalog = json.loads(read(catalog_path))
        resources = catalog["resources"]
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        error(f"catalog/resources.json: invalid catalog ({exc})")
        return
    ids = [item.get("id") for item in resources]
    if len(ids) != len(set(ids)):
        error("catalog/resources.json: duplicate resource IDs")
    if any(not isinstance(item_id, str) or not re.fullmatch(r"R\d{2,}", item_id) for item_id in ids):
        error("catalog/resources.json: IDs must use R followed by at least two digits")
    allowed = {"collected", "reviewed", "tested", "released"}
    required = {"id", "name", "type", "category", "status", "path", "source_url", "reason"}
    for item in resources:
        item_id = item.get("id", "?")
        missing = required - item.keys()
        if missing:
            error(f"catalog/{item_id}: missing fields {sorted(missing)}")
        if item.get("status") not in allowed:
            error(f"catalog/{item_id}: invalid status")
        local_path = item.get("path")
        if local_path and not (ROOT / local_path).exists():
            error(f"catalog/{item_id}: missing local path {local_path}")

    tsv = ROOT / "catalog" / "resources.tsv"
    if not tsv.exists():
        error("catalog/resources.tsv: missing")
    else:
        lines = [line for line in read(tsv).splitlines() if line.strip()]
        expected = "name\ttype\tpurpose\turl\tauthor_or_maintainer\tlicense\tstatus\tverified_date\tcompatibility\tlimitations"
        if not lines or lines[0] != expected:
            error("catalog/resources.tsv: invalid header")
        for index, line in enumerate(lines[1:], 2):
            if len(line.split("\t")) != 10:
                error(f"catalog/resources.tsv:{index}: expected 10 tab-separated fields")


def check_indexes() -> None:
    skills = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
    prompts = {f"{p.parent.name}/{p.name}" for p in (ROOT / "prompts").glob("*/*.md")}
    for relative, expected in (("skills/README.md", {f"{name}/SKILL.md" for name in skills}),
                               ("prompts/README.md", prompts)):
        path = ROOT / relative
        if not path.exists():
            error(f"{relative}: missing")
            continue
        links = set(re.findall(r"\[[^]]+\]\(([^)]+)\)", read(path)))
        local_links = {link for link in links if not link.startswith(("http://", "https://", "#"))}
        missing = expected - local_links
        for item in sorted(missing):
            error(f"{relative}: missing index entry {item}")
    root_readme = read(ROOT / "README.md")
    root_names = set(re.findall(r"- `([a-z0-9-]+)`(?:：|:)", root_readme))
    if skills - root_names:
        error(f"README.md: missing Skill names {sorted(skills - root_names)}")
    if root_names - skills:
        error(f"README.md: unknown Skill names {sorted(root_names - skills)}")


def check_installer() -> None:
    installer = ROOT / "scripts" / "install_skill.py"
    source = ROOT / "skills" / "research-planning"
    with tempfile.TemporaryDirectory() as temporary:
        destination = Path(temporary)
        result = subprocess.run([sys.executable, str(installer), str(source), "--destination", str(destination)], capture_output=True, text=True)
        if result.returncode != 0 or not (destination / source.name / "SKILL.md").exists():
            error(f"installer: normal copy failed ({result.returncode})")
        result = subprocess.run([sys.executable, str(installer), str(source), "--destination", str(source.parent), "--force"], capture_output=True, text=True)
        if result.returncode != 4 or not (source / "SKILL.md").exists():
            error("installer: source-equals-target safety check failed")


skill_paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
prompt_paths = sorted((ROOT / "prompts").glob("*/*.md"))
for skill_path in skill_paths:
    check_frontmatter(skill_path, skill_path.parent.name)
for prompt_path in prompt_paths:
    check_prompt(prompt_path)
check_markdown_links()
check_catalog()
check_indexes()
check_installer()

if ERRORS:
    print("\n".join(ERRORS))
    sys.exit(1)

print(f"validated {len(skill_paths)} Skills and {len(prompt_paths)} bilingual Prompt files")
