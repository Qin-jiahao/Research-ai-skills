# Static Validation Record / 静态验证记录

## 中文

本记录只证明静态结构和本地安装边界检查执行过，不证明科研结果正确，也不证明所有客户端都能自动发现 Skill。

- 日期：2026-10-17
- 命令：`python3 scripts/validate_repo.py`
- 检查范围：15 个 Skill 的 frontmatter 和必需章节、21 个双语 Prompt 的必需章节、全部 Markdown 本地链接、README 索引、资源 JSON/TSV、安装器普通复制和源目录保护。
- 其他命令：`git diff --check`。
- 未执行：真实论文、公开 RNA-seq 数据、科研代码运行、许可证法律审查和客户端自动调用测试。

## English

This record documents structural checks and the local installer safety boundary only. It does not prove scientific correctness or automatic Skill discovery in every client.

- Date: 2026-10-17
- Command: `python3 scripts/validate_repo.py`
- Scope: Skill frontmatter and required sections for 15 Skills, required sections for 21 bilingual Prompts, all Markdown local links, README indexes, JSON/TSV catalogs, normal installer copying, and source-directory protection.
- Additional command: `git diff --check`.
- Not executed: real-paper review, public RNA-seq analysis, research-code execution, legal license review, or client-level Skill invocation.
