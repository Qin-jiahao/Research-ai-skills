---
name: agent-memory-handoff
description: Maintain explicit project memory and handoff records across research-agent sessions without inventing state; 在科研 Agent 会话间维护可核验的项目记忆和交接记录。
---
# Agent Memory and Handoff / Agent 记忆与交接

**Maturity / 成熟度:** draft

## Use / 适用场景

用于长周期科研项目、跨会话交接、阶段复盘和恢复工作。记录目标、范围、已完成事项、证据、当前阻塞、下一步和禁止重复的失败路径。

Use this Skill for long-running research projects, cross-session handoffs, stage reviews, and recovery work. Record the objective, scope, completed work, evidence, blockers, next steps, and failed paths that should not be repeated.

## Boundaries / 边界

记忆文件是工作记录，不是事实数据库。没有文件、日志或用户确认的状态必须标记为“待核验”。不得把模型记忆当成实验结果、代码已运行或权限已获得的证据。

A memory file is a work record, not a fact database. Mark states without a file, log, or user confirmation as “to be verified.” Model memory is not evidence that an experiment ran, code executed, or permission was granted.

## Required inputs / 必需输入

项目目标、当前分支或版本、已完成工作、证据链接、未完成事项、阻塞原因、下一步、数据和权限边界、更新时间。缺失字段写“待补充 / to be provided”。

Provide the project objective, branch or version, completed work, evidence links, unfinished items, blockers, next steps, data and permission boundaries, and update time. Mark missing fields as “待补充 / to be provided.”

## Workflow / 工作流程

1. 先读取现有交接记录，再用当前文件、版本控制状态和日志核对。
2. 区分已完成、已检查、待核验、阻塞和计划中的步骤。
3. 记录每项状态的证据位置，不把推断写成事实。
4. 输出 `HANDOFF.md` 风格记录：目标、范围、状态、证据、风险、阻塞、下一步、失败路径和更新时间。

1. Read the existing handoff record, then compare it with current files, version-control state, and logs.
2. Separate completed, checked, to-be-verified, blocked, and planned steps.
3. Record the evidence location for each state and do not turn inferences into facts.
4. Return a `HANDOFF.md`-style record with objective, scope, status, evidence, risks, blockers, next steps, failed paths, and update time.

## Output format / 输出格式

使用 `HANDOFF.md` 风格的固定字段：Objective、Scope、Completed、Checked、To verify、Blocked、Next steps、Failed paths、Risks、Evidence、Updated at。中文记录可以同时保留对应中文字段。

Use stable `HANDOFF.md` fields: Objective, Scope, Completed, Checked, To verify, Blocked, Next steps, Failed paths, Risks, Evidence, and Updated at. Chinese records may keep the corresponding Chinese labels.

## Quality checks / 质量检查

- 提交号、日期、路径和状态是否有证据；
- 是否区分事实、推断和计划；
- 是否删除过期状态并保留失败原因；
- 是否隐藏密码、令牌、个人敏感信息和未授权数据；
- 新会话能否仅根据记录找到下一步和阻塞点。

- Are commits, dates, paths, and statuses supported by evidence?
- Are facts, inferences, and plans separated?
- Are stale states removed while failure reasons are retained?
- Are passwords, tokens, personal data, and unauthorized data excluded?
- Can a new session identify the next step and blocker from the record alone?

## Limitations / 局限性

交接记录不能恢复缺失的原始数据、日志或权限，也不能证明科学结论。记录质量取决于使用者及时保存证据和更新状态。

A handoff record cannot recover missing raw data, logs, or permissions, and it cannot establish a scientific conclusion. Its quality depends on timely evidence capture and status updates.

## Complete-input example / 完整输入示例

输入包含项目目标、当前提交号、已修改文件、测试命令和输出、未完成任务及阻塞原因。输出应生成可直接交给下一次会话的记录，并链接到实际文件和日志。

The input contains the project objective, current commit, changed files, test commands and outputs, unfinished tasks, and blockers. The output should be a handoff record that a later session can use directly, with links to actual files and logs.

## Incomplete-input example / 信息不足示例

输入只有“上次已经做完分析”。输出应标记提交号、数据文件、运行日志和结果位置均待补充，不得写成分析已完成或结果已复现。

If the only input is “the analysis was completed last time,” mark the commit, data files, execution log, and result location as missing. Do not state that the analysis finished or was reproduced.

## Source / 来源

根据用户提供的交接类截图和科研项目记录要求独立整理，未复制第三方文本。外部记忆工具仅作为参考线索。

This Skill was independently organized from the supplied handoff-related screenshots and research-record requirements. No third-party text was copied. External memory tools are reference leads only.
