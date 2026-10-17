---
name: research-coding
description: Plan and review reproducible research-code workflows when code, data contracts, execution records, or result checks need structure; 在需要整理科研代码、输入输出契约、运行记录或结果核验时使用。
---

# Research Coding / 科研代码

**Maturity / 成熟度:** draft

## Purpose / 用途

帮助研究者整理分析脚本、明确输入输出契约、记录运行环境，并审查科研代码的可复现性和结果核验流程。这个 Skill 适用于已有代码、待整理的分析流程或需要审查的仓库。

This Skill helps researchers organize analysis scripts, define input/output contracts, record execution environments, and review reproducibility and result-verification practices. It applies to existing code, an analysis workflow that needs structure, or a repository that needs review.

它不根据代码猜测研究结论，不生成虚构数据、运行日志、测试结果或性能数字。代码建议必须区分“已检查”“待运行”和“需要研究者确认”。

It must not infer research conclusions from code or fabricate data, logs, test results, or performance numbers. Every recommendation must distinguish what was inspected, what still needs to be run, and what the researcher must confirm.

## When to use / 适用场景

- 整理零散的分析脚本、配置文件和结果文件；
- 设计从原始数据到分析结果的可复现工作流；
- 为分析代码补充输入输出契约、环境记录、日志和错误处理；
- 在提交、复现或共享前审查科研代码；
- 根据已有代码制定测试和结果核验计划。

Use it to:

- organize scattered analysis scripts, configuration files, and result files;
- design a reproducible workflow from source data to analysis outputs;
- add input/output contracts, environment records, logging, and error handling;
- review research code before submission, reproduction, or sharing; and
- plan tests and result checks from supplied code.

## Scope and boundaries / 范围与边界

这个 Skill 关注代码和工作流的可检查性。它可以帮助拆分模块、发现隐含依赖、提出测试和审查问题，但不能证明某个科学假设成立，也不能替代数据治理、统计咨询、伦理审查或同行评审。

This Skill focuses on inspectable code and workflows. It can help separate modules, expose hidden dependencies, and propose tests and review questions. It cannot establish that a scientific hypothesis is true or replace data governance, statistical consultation, ethics review, or peer review.

它不预设编程语言、包管理器、操作系统、云平台或版本控制平台。只有在用户提供了具体环境后，才可以使用相应的命令或配置格式。

It does not assume a programming language, package manager, operating system, cloud platform, or version-control host. Use tool-specific commands or configuration formats only after the environment is supplied.

## Required inputs / 所需输入

尽量收集以下信息。缺失项要标记为“待补充”，不能用看似合理的默认值替代。

Collect the following information where possible. Mark missing items as “to be provided” rather than replacing them with plausible defaults.

1. **研究目标 / Research objective**：研究问题、分析单位、主要结局或估计目标，以及允许的解释范围。
2. **数据契约 / Data contract**：输入文件或数据接口、字段名、类型、单位、编码、主键、缺失值规则、预期行列范围和数据许可。
3. **代码现状 / Code state**：目录结构、入口、配置、辅助脚本、当前错误、已知输出和未完成部分。
4. **输出契约 / Output contract**：预期表格、图形、模型对象、报告或中间文件，文件格式、命名规则和验收条件。
5. **运行环境 / Execution environment**：操作系统、语言和运行时版本、直接依赖、系统依赖、硬件或资源限制，以及可用的环境锁定文件。
6. **可复现要求 / Reproducibility requirements**：随机性、并行设置、固定时间或外部服务、网络访问、数据版本和提交记录要求。
7. **隐私与安全 / Privacy and security**：数据是否含个人信息、受限字段、机构内部路径、访问令牌或其他敏感内容，以及可以共享的范围。
8. **验证资料 / Verification materials**：数据字典、已知基准结果、人工核对结果、测试样例、运行日志和审查范围。

如果只有代码而没有数据，先做静态审查和契约审查。不能声称代码已经成功运行，也不能把示例输入当作真实数据。

When only code is available, perform a static and contract review first. Do not claim that the code ran successfully, and do not present example inputs as real data.

## Core workflow / 核心流程

### 1. Define the task and acceptance criteria / 明确任务和验收条件

先写出研究任务、分析边界和可检查的完成条件。把“代码更整洁”“结果可信”拆成具体条件，例如某个输入字段必须存在、某个中间文件必须带版本信息、某个结果必须通过独立计算核对。对无法客观检查的目标注明限制。

State the research task, analysis boundary, and checkable completion criteria first. Translate goals such as “cleaner code” or “trustworthy results” into concrete conditions, such as required fields, versioned intermediate files, or an independently checked result. Mark goals that cannot be checked objectively.

### 2. Build an input/output contract / 建立输入输出契约

为每个主要步骤记录：输入来源、字段和单位、允许的缺失情况、转换规则、输出字段、文件格式、异常行为和验收检查。契约要区分原始数据、派生数据和最终报告。任何字段重命名、单位换算、筛选和排除都要有可追踪记录。

For each major step, record the input source, fields and units, allowed missingness, transformation rules, output fields, file format, failure behavior, and acceptance checks. Distinguish source data, derived data, and final reports. Record every field rename, unit conversion, filter, and exclusion so that it can be traced.

如果输入格式或字段含义不确定，暂停该步骤并列出需要确认的问题。不要通过猜测列名、补齐缺失值或改变单位来让流程继续。

If the input format or field meaning is uncertain, pause that step and list the questions that require confirmation. Do not guess column names, fill missing values, or change units merely to keep the workflow moving.

### 3. Map the workflow and isolate side effects / 绘制流程并隔离副作用

把读取、清洗、转换、建模、汇总、绘图和导出分成可识别的步骤。说明每一步依赖哪些输入，是否会写文件、修改数据或访问网络。原始数据应保持只读，生成文件应进入明确的输出位置，临时文件应与最终结果分开。

Separate loading, cleaning, transformation, modeling, summarization, plotting, and export into identifiable steps. State each step's inputs and whether it writes files, mutates data, or accesses the network. Keep source data read-only, write generated files to an explicit output location, and separate temporary files from final outputs.

### 4. Record the environment and provenance / 记录环境和来源

记录操作系统、语言或运行时版本、直接依赖、系统级依赖、关键配置、数据版本、代码提交标识和运行时间。优先使用项目已有的环境描述或锁定文件，不要替用户虚构版本号。若依赖会从网络获取，记录来源、版本和获取时间，并说明离线运行是否可行。

Record the operating system, language or runtime version, direct and system dependencies, key configuration, data version, code revision, and execution time. Prefer supplied environment manifests or lock files and never invent version numbers. If dependencies are fetched from a network, record their source, version, and retrieval time, and state whether offline execution is possible.

随机数、并行计算、时间戳、区域设置和外部服务都可能影响结果。应记录可控设置和仍然存在的不确定性；固定随机种子不能替代对算法和数据的核验。

Randomness, parallel execution, timestamps, locale settings, and external services can affect results. Record controlled settings and remaining uncertainty; a fixed random seed does not replace algorithm or data verification.

### 5. Protect data and credentials / 保护数据和凭据

代码审查和示例输出不得暴露原始数据、个人信息、机构内部路径、访问令牌、密钥或可推断敏感内容。日志只记录排查问题所需的上下文，不记录完整行、令牌或未经脱敏的标识符。共享前检查配置文件、缓存、临时目录和生成的报告。

Code reviews and examples must not expose source data, personal information, internal paths, access tokens, secrets, or inferable sensitive content. Logs should contain only the context needed for diagnosis and must not include full rows, tokens, or unredacted identifiers. Check configuration files, caches, temporary directories, and generated reports before sharing.

如果无法确认数据许可或脱敏状态，只提供结构级建议，并明确不能检查的内容。不要为了演示而复制真实数据片段。

When data permission or de-identification cannot be confirmed, provide structural guidance only and state what cannot be checked. Do not copy real data fragments for demonstration.

### 6. Plan tests and diagnostics / 设计测试和诊断

测试计划至少覆盖输入契约、关键转换、边界条件、缺失值和错误路径。可以使用不含敏感信息的最小样例、合成样例或已批准的基准结果，但必须标明其性质。测试通过只能说明测试条件下的行为符合预期，不能证明真实研究结论正确。

The test plan should cover input contracts, key transformations, boundary conditions, missingness, and failure paths. Use a non-sensitive minimal example, a synthetic example, or an approved benchmark when appropriate, and label its nature. Passing tests show behavior under the tested conditions; they do not establish that the research conclusion is correct.

对统计结果、图形和汇总表，安排独立核对或可复算检查，例如重新计算关键摘要、比较记录数和分组总数、检查单位和范围、核对图表与导出表。没有执行核对时，输出“待核验”，不能写成“已验证”。

For statistical results, figures, and summary tables, plan an independent or reproducible check, such as recalculating key summaries, comparing record and group counts, checking units and ranges, or matching figures to exported tables. If the check was not run, label it “to be verified” rather than “verified.”

### 7. Specify logging and error handling / 规定日志和错误处理

日志应记录步骤名称、输入版本、关键计数、开始和结束时间、警告、异常类型和输出位置。错误信息要包含足以定位问题的上下文，并在关键契约不满足时停止流程或明确标记失败。不要捕获所有异常后继续生成看似完整的结果。

Logs should record the step name, input version, key counts, start and end times, warnings, error type, and output location. Errors should include enough context to locate the problem. Stop the workflow or mark it failed when a critical contract is violated. Do not catch every exception and continue producing apparently complete results.

警告需要分级：可以继续但需记录的警告、会影响解释的警告、必须停止的错误。研究者应能从日志判断流程执行到哪一步以及哪些文件已经生成。

Classify messages into warnings that permit continuation, warnings that affect interpretation, and errors that require stopping. A researcher should be able to determine from the log how far the workflow ran and which files were produced.

### 8. Review code and report findings / 审查代码并报告问题

审查时同时看正确性、可复现性、可维护性和数据安全。每条问题包含文件或步骤位置、证据、影响、严重程度和修复建议。建议分为阻断问题、需要修复的问题和改进项。没有看到的文件或没有运行的步骤要明确写出。

Review correctness, reproducibility, maintainability, and data safety together. For each finding, provide the file or step location, evidence, impact, severity, and a concrete remediation. Classify findings as blocking, required fixes, or improvements. State which files were unavailable and which steps were not run.

## Output format / 输出格式

根据任务范围输出以下部分。无关部分可以省略，但不能省略关键不确定性。

Use the following sections as appropriate to the task. Omit irrelevant sections, but retain material uncertainty.

1. **任务范围与状态 / Scope and status**：审查了什么，未审查什么，哪些结论基于静态阅读，哪些需要运行确认。
2. **输入输出契约 / Input/output contract**：每个步骤的输入、转换、输出、单位、格式、失败条件和验收检查。
3. **环境与来源 / Environment and provenance**：已知版本、依赖、配置、数据和代码标识；未知内容标记为待补充。
4. **工作流图或步骤表 / Workflow map or step table**：依赖关系、读写操作、网络访问和副作用。
5. **隐私与共享检查 / Privacy and sharing check**：敏感信息风险、脱敏状态、可共享文件和需要删除的内容。
6. **测试与诊断计划 / Test and diagnostic plan**：测试样例、边界情况、错误路径、独立核对和通过标准。
7. **日志与错误处理 / Logging and error handling**：应记录的字段、错误分级和停止条件。
8. **审查发现 / Review findings**：按严重程度列出位置、证据、影响和修复建议。
9. **结果核查 / Result verification**：已经执行的检查、结果、尚未执行的检查和研究者需要确认的事项。
10. **下一步 / Next actions**：按优先级列出可执行任务，不把计划写成已完成事实。

当用户要求修改代码时，先说明拟修改的文件和行为，再提供最小修改或补丁。代码中不要写入凭据、真实敏感数据或未经确认的研究结论。

When code changes are requested, state the files and behavior to be changed before showing the minimal patch or edit. Do not write credentials, real sensitive data, or unconfirmed research conclusions into code.

## Quality checks / 质量检查

- 输入字段、单位、编码、主键和缺失值规则是否明确；
- 每个输出能否追溯到输入、代码版本和配置；
- 原始数据是否保持只读，临时文件是否与最终结果分开；
- 依赖和运行环境是否有可复核记录，是否避免凭空填写版本；
- 是否检查随机性、并行、时间、区域设置和外部服务的影响；
- 测试是否覆盖正常输入、边界条件、缺失数据和错误路径；
- 日志是否足以定位问题，同时不泄露数据和凭据；
- 关键错误是否会停止流程，而不是被静默忽略；
- 统计摘要、图形、表格和报告是否有独立或可复算核对；
- 是否明确区分代码审查意见、实际运行结果和科学结论。

- Are fields, units, encodings, keys, and missing-value rules explicit?
- Can every output be traced to its inputs, code revision, and configuration?
- Is source data read-only, with temporary files separated from final outputs?
- Are dependencies and the execution environment recorded without invented versions?
- Are the effects of randomness, parallelism, time, locale, and external services considered?
- Do tests cover normal inputs, boundary conditions, missing data, and failure paths?
- Do logs support diagnosis without exposing data or credentials?
- Do critical errors stop the workflow instead of being silently ignored?
- Are summaries, figures, tables, and reports independently or reproducibly checked?
- Is the distinction between review comments, executed results, and scientific conclusions explicit?

## Limitations / 限制

可复现性取决于数据许可、数据版本、环境记录、依赖可获得性和运行过程。完整的代码审查不能证明算法实现没有任何错误，也不能单独证明统计结论、因果关系或研究结论成立。

Reproducibility depends on data permissions, data versions, environment records, dependency availability, and execution history. A complete code review cannot prove that an implementation contains no errors, nor can it establish statistical validity, causality, or a research conclusion by itself.

当数据、环境或执行权限不可用时，输出应限于静态结构、风险和核查计划。任何“通过”“复现成功”或“结果一致”的表述都必须有可追溯的运行证据。

When data, the environment, or execution access is unavailable, limit the output to static structure, risks, and a verification plan. Statements such as “passed,” “reproduced,” or “consistent results” require traceable execution evidence.

## Complete-input example / 完整输入示例

输入包含代码目录、输入输出契约、锁定的依赖文件、最小测试数据、运行命令、日志和一份可核对的结果记录。输出应指出已执行的检查、未执行的检查、阻断问题和最小修复方案。

The input contains a code tree, input/output contract, locked dependencies, minimal test data, run commands, logs, and a checkable result record. The output should distinguish executed and unexecuted checks, blocking findings, and the smallest repair plan.

## Incomplete-input example / 信息不足示例

输入只有代码片段，没有数据契约、依赖版本或运行日志。输出应把这些字段列为待补充，只能做静态风险审查，不能声称代码已经运行或结果可复现。

If the input is only a code fragment without a data contract, dependency versions, or an execution log, list those fields as missing and limit the output to static risks. Do not claim that the code ran or that results were reproduced.

## Source / 来源

来源于网络，自行整理汇总。

Source: collected from public online materials and reorganized by the repository maintainer.
