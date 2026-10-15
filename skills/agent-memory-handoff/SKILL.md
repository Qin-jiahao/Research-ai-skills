---
name: agent-memory-handoff
description: Maintain explicit project memory and handoff records across research-agent sessions without inventing state; 在科研 Agent 会话间维护可核验的项目记忆和交接记录。
---
# Agent Memory and Handoff / Agent 记忆与交接

**Status / 状态:** v0.1.0 draft

## Use / 适用场景

用于长周期科研项目、跨会话交接、阶段复盘和恢复工作。记录目标、已完成事项、证据、当前阻塞、下一步和禁止重复的失败路径。

Use it for long-running research projects, cross-session handoffs, reviews, and recovery.

## Boundaries / 边界

记忆文件是工作记录，不是事实数据库。没有文件、日志或用户确认的状态必须标记为“待核验”。不得把模型记忆当成实验结果、代码已运行或权限已获得的证据。

## Required inputs / 必需输入

项目目标、当前分支或版本、已完成工作、证据链接、未完成事项、阻塞原因、下一步、数据和权限边界。

## Workflow and output / 工作流程与输出

输出 `HANDOFF.md` 风格记录：目标、范围、已完成、已检查、待核验、阻塞、下一步、失败路径、风险和更新时间。每次恢复工作先读取记录，再用当前文件和状态重新核对。

## Quality checks / 质量检查

检查日期、提交号、路径和状态是否有证据；区分事实、推断和计划；删除过期状态；不得写入密码、令牌、个人敏感信息或未经授权的数据。

## Examples / 示例

信息完整时生成带提交号和检查结果的交接记录。信息不足时列出缺少的日志、文件或确认，不猜测上次进度。

## Source / 来源

根据用户提供的交接类截图整理，未直接复制第三方文本；具体工具项目需另行核验。

## English

Use the same structure and evidence rules in English. Treat memory as a work record, not proof of execution or scientific truth.
