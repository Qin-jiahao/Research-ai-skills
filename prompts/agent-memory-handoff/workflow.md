# Agent Memory and Handoff Workflow / Agent 记忆与交接工作流

## 中文

### 使用场景

用于长周期科研项目的跨会话交接、阶段复盘和恢复工作，需要把状态、证据、阻塞点和下一步写成可核对记录时使用。

### 输入要求

提供项目目标、当前分支或提交号、已完成工作、检查命令和结果、未完成事项、阻塞原因、下一步、数据与权限边界及更新时间。

### 输出要求

输出 `HANDOFF.md` 风格记录，至少包括目标、范围、已完成、已检查、待核验、阻塞、下一步、失败路径、风险、证据链接和更新时间。

### 禁止编造的内容

不得编造提交号、运行状态、测试结果、权限、数据位置、实验结论或完成时间。模型记忆不能作为执行证据。

### 信息不足时的处理方式

把缺少的文件、日志、提交号或用户确认列为“待补充/待核验”，暂停相关状态判断，不把“上次完成了”写成事实。

### 双语示例

**完整输入：** 提供当前提交号、修改文件、测试输出和阻塞原因。**预期输出：** 生成带证据链接的交接记录，并区分已完成和未执行步骤。

**信息不足：** 只说“上次分析做完了”。**预期处理：** 列出提交号、数据文件、日志和结果位置待补充，不声称分析已完成。

### 来源说明

来源于网络和用户提供的交接类截图，自行整理汇总；未复制第三方文本。

## English

### Use case

Use this Prompt for cross-session handoffs, stage reviews, and recovery in long-running research projects when status, evidence, blockers, and next steps must be recorded.

### Required inputs

Provide the project objective, branch or commit, completed work, check commands and results, unfinished items, blockers, next steps, data and permission boundaries, and update time.

### Expected output

Return a `HANDOFF.md`-style record containing objective, scope, completed work, checked work, items to verify, blockers, next steps, failed paths, risks, evidence links, and update time.

### Fabrication ban

Do not invent commits, execution status, test results, permissions, data locations, scientific conclusions, or completion dates. Model memory is not execution evidence.

### Missing information

List missing files, logs, commits, or user confirmations as “to be provided/to be verified.” Pause the affected status judgment instead of treating “it was done last time” as a fact.

### Bilingual example

**Complete input:** Supply the current commit, changed files, test output, and blockers. **Expected output:** Return an evidence-linked handoff that separates completed and unexecuted steps.

**Incomplete input:** Only “the analysis was done last time” is supplied. **Expected handling:** Mark the commit, data files, logs, and result location as missing and do not claim completion.

### Source note

Source: online materials and user-provided handoff screenshots, independently organized. No third-party text was copied.
