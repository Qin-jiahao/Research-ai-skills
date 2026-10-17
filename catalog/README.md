# Resource catalog / 资源目录

`resources.json` is the canonical inventory for the 31 resource themes extracted from the collected screenshots. It separates local released content from external references. `released` means included in this repository; it does not mean that a Skill has been validated on real research data.

`resources.json` 是从截图整理出的 31 个资源主题的唯一目录。它把本仓库已发布内容和外部参考项目分开记录。`released` 表示已纳入本仓库版本，不表示 Skill 已通过真实科研数据验证。

`resources.tsv` is a separate, human-readable index of external projects. It is not a second copy of the R01–R31 inventory. The TSV uses `to_verify` for license fields that still require an upstream check; the JSON status remains the source of truth for repository resource states.

`resources.tsv` 是外部项目的独立索引，不是 R01–R31 目录的第二份副本。TSV 中的 `to_verify` 表示许可证仍需核验；仓库资源状态以 JSON 为准。

The image-by-image evidence ledger is [`../docs/screenshot-intake-2026-10.md`](../docs/screenshot-intake-2026-10.md). External project links, attribution, license notes, and unresolved provenance are maintained in [`../docs/external-projects.md`](../docs/external-projects.md).

逐张截图的证据台账见 [`../docs/screenshot-intake-2026-10.md`](../docs/screenshot-intake-2026-10.md)。外部项目链接、作者归属、许可证说明和未解决的来源问题见 [`../docs/external-projects.md`](../docs/external-projects.md)。

Status values are `collected`, `reviewed`, `tested`, and `released`. `collected` means that a source or topic has been recorded, but repository behavior testing is incomplete. `reviewed` means that the recorded public source, purpose, and license information have been checked. `tested` means that static or local testing has been completed in this repository. A collected external project is not an installable Skill in this repository. URLs and licenses must be checked against the upstream repository before claiming compatibility.

状态包括 `collected`、`reviewed`、`tested` 和 `released`。`collected` 表示已记录来源或主题，但尚未完成本仓库行为测试；`reviewed` 表示已核对记录的公开来源、用途和许可证信息；`tested` 表示已在本仓库的静态或本地测试中验证。标记为 collected 的外部项目不是本仓库可安装的 Skill。只有核对上游仓库后，才能说明兼容性或许可证。

The catalog records evidence status, not scientific validity. A screenshot, repository README, or badge cannot substitute for a real-data test, a reproducible run, or a license review.

目录状态只表示证据整理进度，不表示科研结论有效。截图、仓库 README 或徽章不能替代真实数据测试、可复现运行记录或许可证审查。
