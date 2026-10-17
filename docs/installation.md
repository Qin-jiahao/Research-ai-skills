# Installation and Use / 安装与使用

## 中文

本仓库提供统一的 Markdown Skill 源文件。不同客户端的自动发现目录可能不同，未核验的平台不能保证自动调用。

### Codex CLI、IDE 或桌面客户端

1. 克隆仓库或下载目标 Skill 目录。
2. 将目标目录复制到客户端文档支持的用户级或项目级 `skills/` 目录。
3. 保留目录名和 `SKILL.md` 文件名，不要只复制正文。
4. 重新打开会话，先用一个明确任务测试 Skill 是否被发现。

可以只安装一个 Skill，例如 `skills/rnaseq-analysis/`。不要默认覆盖已有同名目录；先备份或比较差异。卸载时删除对应目录即可。

### Windows PowerShell

```powershell
Copy-Item -Recurse .\skills\rnaseq-analysis <supported-skill-directory>\rnaseq-analysis
```

### macOS/Linux

```bash
cp -R skills/rnaseq-analysis <supported-skill-directory>/rnaseq-analysis
```

上面的 `<supported-skill-directory>` 必须替换为目标客户端官方文档确认的目录。仓库不假设所有客户端共用同一路径。仓库提供 `scripts/install_skill.py` 作为本地复制工具；它不会自动探测客户端路径，也不会安装插件或 Marketplace 包。

```bash
python3 scripts/install_skill.py skills/research-planning --destination /path/to/supported/skills
python3 scripts/install_skill.py skills/research-planning --destination /path/to/supported/skills --dry-run
```

`--force` 只用于明确比较过差异的目标目录。脚本会拒绝源目录本身或源目录内部的目标路径。

## English

This repository provides a shared Markdown source format. Automatic discovery directories differ across clients, and unsupported clients are not guaranteed to load Skills automatically.

Clone or download the repository, copy one Skill directory into a user-level or project-level `skills/` directory documented by the target client, keep the directory name and `SKILL.md`, and reopen the session. Do not overwrite an existing same-named Skill without a backup or diff review. Remove that directory to uninstall it.

The PowerShell and POSIX examples above are templates only. Replace `<supported-skill-directory>` with a path confirmed by the target client’s official documentation. The repository provides `scripts/install_skill.py` as a local copy utility; it does not discover client paths or install plugins or Marketplace packages.

```bash
python3 scripts/install_skill.py skills/research-planning --destination /path/to/supported/skills
python3 scripts/install_skill.py skills/research-planning --destination /path/to/supported/skills --dry-run
```

Use `--force` only after reviewing the destination. The script rejects the source directory itself and destinations inside the source directory.
