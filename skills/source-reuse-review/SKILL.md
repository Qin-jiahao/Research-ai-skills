---
name: source-reuse-review
description: Review whether an existing open-source repository or tool can be reused for a research task before new implementation; 在科研开发前审查是否存在可复用的开源项目或工具。
---

# Source and Reuse Review / 来源与复用审查

**Maturity / 成熟度:** draft

## Purpose / 用途

在开始编写代码或 Skill 前，系统检查已有项目、维护状态、许可证、功能边界和部署成本。审查结果不是自动采用建议，最终选择仍需研究者确认。

This Skill checks existing projects, maintenance status, licenses, scope, and deployment cost before new implementation. It does not automatically recommend adoption.

## Required inputs / 必需输入

研究任务、目标功能、输入输出、运行环境、允许的许可证、隐私限制、候选仓库或检索范围。缺少仓库链接或版本时，不能声称已完成审查。

## Workflow / 工作流程

1. 将需求拆成可比较的功能和验收标准。
2. 检索官方仓库、文档、发行版本和许可证。
3. 核对最近维护、依赖、安装方式、数据访问和安全风险。
4. 比较直接使用、二次开发和自行实现三种路径。
5. 记录证据链接、访问日期、未知项和许可义务。
6. 给出条件化建议，并说明需要人工确认的事项。

## Output format / 输出格式

候选项目表、功能匹配表、许可证与来源表、维护与部署风险、三种实施路径比较、推荐条件、待核验事项。不得把截图中的 star 数或宣传语当作质量证据。

## Examples / 示例

### Complete input / 完整输入

输入包含研究任务、候选仓库 URL、目标版本、运行环境、数据访问限制和许可证要求。输出应给出功能匹配、维护和依赖风险、许可证义务、直接使用/二次开发/自研三种路径及条件化建议。

### Incomplete input / 信息不足

输入只有一个项目名称或截图。输出应说明无法核验仓库维护状态、许可证兼容性、依赖和数据安全边界，列出需要补充的官方 URL、版本和运行环境，不给出确定的采用建议。

## Quality checks / 质量检查

- 是否使用官方仓库、文档、许可证和版本页面作为证据；
- 是否记录访问日期、提交或版本标识；
- 是否把许可证义务与功能评价分开；
- 是否检查依赖、权限、网络访问和数据传输；
- 是否区分截图线索、静态阅读和实际运行结果。

- Are official repositories, documentation, licenses, and releases used as evidence?
- Are access dates and commit or release identifiers recorded?
- Are license obligations separated from functional assessment?
- Are dependencies, permissions, network access, and data transfer checked?
- Are screenshot leads, static reading, and execution results distinguished?

## Limitations / 局限性

网页状态、版本和许可证可能变化。审查结论必须带访问日期，不能替代法律许可意见或安全审计。

## Source / 来源

截图仅作为主题参考，具体项目和许可需通过官方来源重新核验；本文为仓库维护者独立整理。

## English

### Use, boundaries, and inputs

Use this Skill before implementing a research tool when an existing repository may be reused. It compares direct use, adaptation, and independent implementation. Popularity metrics, screenshots, and promotional claims are not evidence. Provide the task, candidate URLs, target version, execution environment, data-access limits, and license requirements.

### Workflow and output

Check official documentation, releases, maintenance, license, dependencies, permissions, data access, and security. Record access dates, evidence links, unknowns, and license obligations. Return a comparison table, risks, conditions, and items requiring human confirmation.

### Quality checks and limitations

Separate static inspection from execution. Mark inaccessible or unverified information as “to be verified.” Web pages and licenses can change; this review is not legal advice, a security audit, or proof that a project will work in a particular environment.

### Complete-input example

Input: a research task, two repository URLs, a target release, a container environment, a data-permission rule, and an MIT-only constraint. Expected output: an evidence-linked comparison and conditional recommendation.

### Incomplete-input example

Input: only a screenshot and a project name. Expected handling: list the missing official URL, version, license, dependencies, and data-access information and avoid a definitive recommendation.

### Source

This Skill was independently organized from the supplied open-source reuse screenshots and public-project review requirements. No upstream text was copied.
