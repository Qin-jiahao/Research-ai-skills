# Research AI Skills / 科研 AI Skills

面向科研工作的双语 AI Skills 与 Prompts 资源库<br>
Bilingual AI Skills and Prompts for research work

[中文](#中文) · [English](#english) · [Skills](skills/README.md) · [Prompts](prompts/README.md) · [安装说明](docs/installation.md) · [贡献指南](CONTRIBUTING.md) · [许可证说明](docs/license-and-attribution.md)

## 中文

`Research-ai-skills` 提供可复用的 Markdown 工作流规范和任务级 Prompt，帮助研究生和科研人员拆解、规划和检查常见科研任务。当前内容覆盖论文写作、文献分析、统计方法、科研图表、bulk RNA-seq、科研代码、科研汇报、科研计划和开源项目复用审查。

Skill 适合多步骤任务，通常包含输入要求、工作流程、输出格式和质量检查。Prompt 适合单个任务或短流程。使用前请阅读对应文件的适用场景、边界、必需输入和局限性。

本仓库不提供真实研究数据、科研结论，也不声称分析软件已经在所有环境中验证。模型输出需要结合原始数据、全文文献和研究设计核对。信息不足时，应先列出缺失项和待核验内容，不应补写数据、文献、统计结果、实验结论或运行结果。

### 快速入口

- [Skills 索引](skills/README.md)：多步骤科研工作流。
- [Prompts 索引](prompts/README.md)：单任务和短流程提示词。
- [安装与使用](docs/installation.md)：复制本地 Skill，并说明不同客户端的目录差异。
- [资源状态](docs/resource-status.md)：解释 `collected`、`reviewed`、`tested`、`released` 和 `draft`。
- [来源与归因](docs/sources-and-attribution.md)：说明原创内容、已知来源内容和来源不明材料的处理方式。
- [外部项目记录](docs/external-projects.md)：记录项目链接、作者、许可证和仍待核验的信息。
- [兼容性与限制](docs/compatibility.md)：说明客户端差异和当前使用边界。
- [机器可读资源目录](catalog/resources.json)：查看本地资源的结构化记录；外部项目索引见 [resources.tsv](catalog/resources.tsv)。
- [截图整理台账](docs/screenshot-intake-2026-10.md)：查看逐张整理结果和待核验项。
- [许可证与署名说明](docs/license-and-attribution.md)：说明 MIT License 的适用范围和第三方材料边界。

### 状态和使用边界

| 标记 | 含义 | 不代表 |
| --- | --- | --- |
| Skill `draft` | 内容成熟度仍有限，行为测试或真实数据测试尚不充分 | 不代表内容已经过科研验证 |
| Catalog `collected` | 已记录来源或主题，但尚未完成本仓库行为测试 | 不代表可以安装或复用 |
| Catalog `reviewed` | 已核对记录的公开来源、用途和许可证信息 | 不代表运行结果正确 |
| Catalog `tested` | 已在本仓库的静态或本地测试中验证 | 不代表科研结论正确 |
| Catalog `released` | 已作为本仓库内容发布 | 不代表科学有效、法律审查完成或所有客户端都能自动调用 |

### 当前收录的 Skills

- `academic-writing`：论文段落和章节写作
- `paper-review`：论文结构、方法和论证检查
- `literature-analysis`：文献检索、筛选和证据整理
- `statistical-analysis`：统计方法选择和结果解释
- `figure-generation`：科研图表设计和生成规范
- `rnaseq-analysis`：bulk RNA-seq 分析规划、质量控制和结果审查
- `research-coding`：科研代码整理、可复现性和代码审查
- `research-presentation`：科研汇报的故事线、逐页结构和证据核查
- `research-planning`：科研计划、风险、里程碑和任务交接
- `figure-evidence-audit`：科研图表的数据、主张、方法和来源审查
- `source-reuse-review`：开源项目复用、许可证和维护状态审查
- `agent-memory-handoff`：跨会话项目记忆和任务交接
- `multi-agent-review`：多角色科研审查和分歧记录
- `academic-language-polish`：保留科学含义的学术语言润色
- `scientific-interface-design`：科研软件界面和交互设计

### 本地使用

先阅读目标 Skill 的 `SKILL.md`，再根据目标客户端官方文档确认支持的 `skills/` 路径。仓库提供的脚本只复制一个本地 Skill，不会自动探测客户端路径，也不会安装插件或 Marketplace 包：

```bash
git clone https://github.com/Qin-jiahao/Research-ai-skills.git
cd Research-ai-skills

python3 scripts/install_skill.py skills/research-planning \
  --destination /path/to/supported/skills --dry-run
python3 scripts/install_skill.py skills/research-planning \
  --destination /path/to/supported/skills
```

`--force` 只应在比较过目标目录后使用。脚本会拒绝源目录本身和源目录内部的目标路径。Prompt 可以直接阅读 Markdown 文件，再根据具体任务补充输入。

### 目录结构

```text
Research-ai-skills/
├── skills/       # 多步骤科研工作流；每个目录含双语 SKILL.md
├── prompts/      # 单任务或短流程 Prompt
├── catalog/      # 本地资源和外部项目索引、状态记录
├── docs/         # 安装、兼容性、限制、来源和维护说明
├── tests/        # 静态检查和评估边界
├── scripts/      # 本地安装和仓库校验脚本
└── tools/        # 外部工具记录规范
```

### 来源、许可证和贡献

仓库根目录的 [MIT License](LICENSE) 适用于维护者创作，或贡献者明确按 MIT 提交且本仓库有权分发的原创内容。已知来源的材料会保留原作者、原项目链接和原始许可证。来源无法可靠确认的内容只作为参考，标记为“来源于网络，自行整理汇总”，不复制原文。截图只用于记录线索，仓库不上传原始截图；外部项目的许可证标签仍需在复用前对照上游仓库和目标版本核验。

请参阅 [贡献指南](CONTRIBUTING.md) 和 [维护规则](docs/maintenance.md)。

## English

`Research-ai-skills` provides reusable Markdown workflow specifications and task-level Prompts for graduate students and researchers. The current scope covers academic writing, literature analysis, statistical methods, research figures, bulk RNA-seq, research code, scientific presentations, research planning, and open-source reuse review.

A Skill is intended for a multi-step task and normally documents inputs, workflow, output format, and quality checks. A Prompt is intended for one task or a short workflow. Read the relevant use case, boundaries, required inputs, and limitations before using either one.

This repository does not provide real research data or scientific conclusions, and it does not claim that the analysis software has been validated in every environment. Check generated output against the original data, full-text sources, and study design. When information is missing, list the missing and unverified items instead of inventing data, references, statistical results, experimental conclusions, or execution results.

### Quick links

- [Skills index](skills/README.md): multi-step research workflows.
- [Prompts index](prompts/README.md): prompts for individual tasks and short workflows.
- [Installation and use](docs/installation.md): local Skill copying and client-specific directory notes.
- [Resource status](docs/resource-status.md): meanings of `collected`, `reviewed`, `tested`, `released`, and `draft`.
- [Sources and attribution](docs/sources-and-attribution.md): treatment of original, known-source, and unclear-provenance material.
- [External project records](docs/external-projects.md): project links, authors, licenses, and unresolved checks.
- [Compatibility and limitations](docs/compatibility.md): client differences and current usage boundaries.
- [Machine-readable resource catalog](catalog/resources.json): structured local-resource records; external projects are indexed in [resources.tsv](catalog/resources.tsv).
- [Screenshot intake ledger](docs/screenshot-intake-2026-10.md): image-by-image notes and unresolved items.
- [License and attribution scope](docs/license-and-attribution.md): MIT License coverage and third-party material boundaries.

### Status and boundaries

| Label | Meaning | Does not certify |
| --- | --- | --- |
| Skill `draft` | Content maturity is limited; behavioral or real-data testing remains incomplete | Scientific validation |
| Catalog `collected` | A source or topic has been recorded, but repository behavior testing is incomplete | Installability or permission to reuse |
| Catalog `reviewed` | The recorded public source, purpose, and license information have been checked | Correct execution results |
| Catalog `tested` | Static or local testing has been completed in this repository | Correct scientific conclusions |
| Catalog `released` | The item has been published as repository content | Scientific validity, completed legal review, or automatic discovery in every client |

### Skills currently included

- `academic-writing`: writing research paragraphs and sections
- `paper-review`: checking structure, methods, and reasoning
- `literature-analysis`: searching, screening, and organizing evidence
- `statistical-analysis`: choosing methods and interpreting results
- `figure-generation`: specifications for research figures and charts
- `rnaseq-analysis`: planning, quality control, and auditing bulk RNA-seq workflows
- `research-coding`: organizing research code and checking reproducibility
- `research-presentation`: storylines, slide structures, and claim-evidence checks
- `research-planning`: research plans, risks, milestones, and handoff records
- `figure-evidence-audit`: auditing links among figures, data, claims, methods, and provenance
- `source-reuse-review`: reviewing open-source reuse, licenses, and maintenance status
- `agent-memory-handoff`: cross-session project memory and handoffs
- `multi-agent-review`: role-based research review and disagreement tracking
- `academic-language-polish`: academic language polishing with meaning preservation
- `scientific-interface-design`: research-software interface and interaction planning

### Use a local Skill

Read the target `SKILL.md` first. Confirm a supported `skills/` directory in the target client’s official documentation. The included script copies one local Skill; it does not discover client paths or install plugins or Marketplace packages:

```bash
git clone https://github.com/Qin-jiahao/Research-ai-skills.git
cd Research-ai-skills

python3 scripts/install_skill.py skills/research-planning \
  --destination /path/to/supported/skills --dry-run
python3 scripts/install_skill.py skills/research-planning \
  --destination /path/to/supported/skills
```

Use `--force` only after reviewing the destination. The script rejects the source directory itself and destinations inside the source directory. Prompts can be read as Markdown files and filled with task-specific inputs.

### Repository structure

```text
Research-ai-skills/
├── skills/       # Multi-step research workflows; each directory contains a bilingual SKILL.md
├── prompts/      # Prompts for individual tasks or short workflows
├── catalog/      # Local-resource and external-project indexes and status records
├── docs/         # Installation, compatibility, limitations, provenance, and maintenance notes
├── tests/        # Static checks and evaluation boundaries
├── scripts/      # Local installer and repository validator
└── tools/        # External-tool recording guidance
```

### Sources, license, and contribution

The root [MIT License](LICENSE) applies to original content created by the maintainers, or explicitly submitted under MIT by contributors when this repository has the right to distribute it. Materials with known sources retain the original author, project link, and upstream license. Material with unclear provenance is used only as a reference, marked as “Source: online materials, independently organized and summarized,” and not copied verbatim. Screenshots are used only as leads; the original screenshots are not included in this repository. License labels for external projects must still be checked against the upstream repository and target version before reuse.

See the [contribution guide](CONTRIBUTING.md) and [maintenance rules](docs/maintenance.md).
