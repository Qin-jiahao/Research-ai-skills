# Changelog

## [Unreleased]

- 补齐旧版 Skill 和 Prompt 的适用场景、输入、输出、禁止编造、信息不足处理、双语示例和来源说明。
- 统一 Skill 的成熟度标记与资源目录的发布状态，明确 `draft` 与 `released` 的含义不同。
- 改进本地安装器，拒绝源目录本身或源目录内部的目标路径，避免 `--force` 误删源文件。
- 修正安装说明、截图主题对应表、资源目录说明和贡献指南中的状态与范围表述。
- 更新静态校验边界，准备检查全部 Prompt 的结构、资源目录和安装器边界。

- Added use cases, inputs, outputs, fabrication limits, missing-information handling, bilingual examples, and provenance notes to the older Skills and Prompts.
- Separated Skill maturity from catalog release state and documented the distinct meanings of `draft` and `released`.
- Hardened the local installer so a forced install cannot target the source directory or a directory inside it.
- Corrected status and scope wording in the installation guide, screenshot matrix, catalog documentation, and contribution guide.
- Extended the static-validation boundary to cover all Prompt structure, the resource catalog, and installer edge cases.

## 0.2.0 - 2026-10-16

- 建立双语 R01–R31 资源目录，区分 collected、reviewed、tested 和 released。
- 加入本地 Skill 安装脚本，并记录安装测试边界。
- 建立 35 张截图的双语整理台账，区分独立改写的 Prompt、外部项目线索和待核验内容。
- 新增需求文档、CI 失败诊断、数据先行绘图、五视角审查、期刊元数据核验和证据边界内的语言润色 Prompt。
- 补充外部项目链接、作者归属、许可证边界和复用限制。

- Added a bilingual R01–R31 resource catalog with collected, reviewed, tested, and released states.
- Added a local Skill installer and documented its test boundaries.
- Added a bilingual intake ledger for all 35 screenshots, separating rewritten Prompts, external project leads, and unresolved provenance.
- Added Prompts for requirements before implementation, CI failure diagnosis, data-first figures, five-perspective review, journal metadata checks, and evidence-bounded naturalization.
- Added external project links, attribution, license boundaries, and reuse limitations.

## 0.1.0 - 2026-10-14

- 建立双语 README 和基础仓库结构。
- 确定 Skills 与 Prompts 共存于一个仓库。
- 加入基础双语 Skill、Prompt、示例和测试清单。
- 为 Skill 补充标准 YAML frontmatter，并更新索引和维护说明。

- Added the bilingual README and initial repository structure.
- Established one repository for Skills and Prompts.
- Added initial bilingual Skills, Prompts, examples, and checklists.
- Added standard YAML frontmatter for Skills and updated indexes and maintenance notes.
