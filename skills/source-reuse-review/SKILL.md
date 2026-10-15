---
name: source-reuse-review
description: Review whether an existing open-source repository or tool can be reused for a research task before new implementation; 在科研开发前审查是否存在可复用的开源项目或工具。
---

# Source and Reuse Review / 来源与复用审查

**Status / 状态:** v0.1.0 draft

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

完整输入应包含任务、候选仓库和运行环境；信息不足时应明确写出无法核验仓库维护状态、许可证兼容性或数据安全边界。

## Limitations / 局限性

网页状态、版本和许可证可能变化。审查结论必须带访问日期，不能替代法律许可意见或安全审计。

## Source / 来源

截图仅作为主题参考，具体项目和许可需通过官方来源重新核验；本文为仓库维护者独立整理。

## English

Use official project pages and record access dates. Treat popularity metrics and promotional claims as non-evidence. Mark unknown license, maintenance, security, and compatibility items as “to be verified.”
