# CI Failure Diagnosis / CI 失败诊断

## 中文

### 使用场景

在 GitHub Actions、持续集成测试、构建或部署检查失败时使用。这个 Prompt 只负责定位和验证问题，不把日志中的猜测当成根因。

### 输入要求

请提供失败的工作流链接或完整日志、失败提交、相关 diff、工作流 YAML、运行环境、预期行为和已经尝试过的修复。没有实际日志时，只能制定诊断计划。

### 输出要求

请输出：失败步骤和证据行、可排除的假设、仍未区分的候选根因、最小修复方案、需要修改的文件、复现命令、验证结果和残余风险。每项标记为“已观察”“推断”“待运行”或“无法判断”。

### 禁止编造的内容

不得声称 CI 已通过、补丁已部署、测试已运行或问题已解决，除非输入中有对应日志或本次确实执行了验证。不得为了让 CI 变绿而删除有意义的测试或放宽科学分析的质量门槛。

### 信息不足时的处理方式

先请求最小必要信息：失败 job、错误段落、提交范围和运行环境。只有静态配置可检查时，输出静态检查结果，并把运行结论标为待运行。

### 双语示例

#### 中文输入

一个 RNA-seq 报告项目的 CI 在“生成报告”步骤失败。现在只有一行 `file not found`，没有工作流文件和目录树。

#### 中文输出要点

根因无法判断。需要补充失败 job 的完整上下文、工作目录、输入文件清单、工作流 YAML 和最近一次成功提交。可以先检查路径大小写、相对路径和产物上传配置，但不能直接修改测试或声称修复完成。

#### English input

The report-generation step of an RNA-seq project failed with one `file not found` line. The workflow file and directory tree are not available.

#### English output points

The root cause is undetermined. Request the job context, working directory, input-file list, workflow YAML, and the last successful commit. Path case, relative paths, and artifact configuration can be inspected conditionally, but no fix or successful run may be claimed.

### 来源说明

本 Prompt 根据截图中 `gh-fix-ci` 和“读取日志、定位问题、修复后复核”的主题独立整理。截图没有提供可确认的完整上游文件，因此不复制任何实现。来源说明：`来源于网络，自行整理汇总`。

## English

### Use case

Use this Prompt when GitHub Actions, continuous-integration tests, builds, or deployment checks fail. It separates observed log evidence from hypotheses and requires verification after a fix.

### Required inputs

Provide the workflow link or full log, failing commit, relevant diff, workflow YAML, runtime environment, expected behavior, and attempted fixes. Without logs, produce only a diagnostic plan.

### Expected output

Return the failing step and evidence lines, eliminated hypotheses, unresolved candidate causes, the smallest repair, affected files, reproduction commands, verification results, and residual risks. Label each item as observed, inferred, to be run, or undetermined.

### Fabrication ban

Do not claim that CI passed, a patch was deployed, tests ran, or the issue was fixed without corresponding evidence. Do not remove meaningful tests or weaken research-quality gates merely to make CI green.

### Missing information

Request the failing job, error context, commit range, and runtime first. Static configuration findings must remain separate from execution results.

### Bilingual example

The example above is bilingual and must produce the same evidence boundary in both languages.

### Source note

This is an independent rewrite of the `gh-fix-ci` theme and the log-to-repair-to-recheck workflow shown in the supplied screenshots. No upstream implementation was copied.
