# Reproducible Research Code Review Plan / 可复现科研代码审查计划

## 中文

请根据我提供的科研代码、目录结构、配置、运行记录和数据说明，制定一份可执行的代码审查与复现计划。请先界定审查范围，再识别缺失信息。没有实际运行证据时，不要声称代码运行成功、测试通过、结果一致或分析可以复现。

### 输入

```text
研究目标与分析单位：
[填写研究问题、分析单位、主要结局或估计目标]

代码与目录：
[粘贴目录树、入口文件、关键脚本或审查范围]

输入数据契约：
[数据来源、版本、字段、类型、单位、编码、主键、缺失值规则和许可范围]

预期输出契约：
[表格、图形、模型对象、报告或中间文件；格式、命名和验收条件]

运行环境：
[操作系统、语言或运行时版本、依赖记录、硬件或资源限制]

现有运行记录：
[命令或执行方式、日志、错误、警告、代码版本和数据版本]

隐私与共享限制：
[不得出现的字段、路径、凭据、原始数据片段和可共享文件范围]
```

### 要求

1. 先列出审查范围、已提供材料、缺失材料和不能据此判断的事项。缺失信息请写成具体问题，不要用默认值补全。
2. 为主要步骤建立输入输出契约。每一步说明输入来源、字段和单位、转换规则、输出、失败条件、日志字段和验收检查。
3. 检查环境和来源记录，包括运行时、依赖、配置、数据版本、代码版本、随机性、并行设置、时间或区域设置，以及外部服务。没有版本信息时标记为“待补充”。
4. 检查数据安全。指出代码、配置、缓存、日志和输出中可能出现的个人信息、敏感标识符、访问令牌、内部路径和未经批准的数据片段。不要复制或推测真实敏感内容。
5. 制定测试计划，至少覆盖输入契约、关键转换、边界条件、缺失数据、错误路径和输出格式。区分静态检查、已执行测试和待执行测试。
6. 检查日志和错误处理。说明哪些警告可以继续，哪些警告会影响解释，哪些错误必须停止流程。指出是否可能在失败后写出看似完整的结果。
7. 制定结果核验计划。对关键计数、摘要、图形数据、单位、分组和导出文件提出独立复算或交叉核对方法。没有执行核验时只能写“待核验”。
8. 按 `阻断问题 / 需要修复 / 改进项` 分级报告发现。每条发现都要包含文件或步骤位置、证据、影响和可执行的修复建议。
9. 不假设具体编程语言、包管理器、操作系统或代码托管平台。只有输入中明确提供后，才给出对应命令或配置格式。
10. 不生成数据、测试通过记录、日志、版本号、性能数字、统计结果或科学结论。示例内容必须明确标注为占位符或合成示例。

### 输出格式

请按以下顺序输出：

1. 审查范围与证据状态
2. 缺失信息与需要确认的问题
3. 工作流和输入输出契约表
4. 环境、依赖与来源记录检查
5. 数据安全与共享检查
6. 测试、诊断和错误路径计划
7. 日志与失败处理检查
8. 结果核验计划
9. 分级审查发现
10. 优先级明确的下一步

每个结论都要说明它来自代码阅读、现有运行记录，还是尚未验证的建议。

## English

Using the research code, directory structure, configuration, execution records, and data description that I provide, prepare an actionable code-review and reproduction plan. Define the review scope before making findings and identify missing information explicitly. Without execution evidence, do not claim that the code ran successfully, tests passed, results agree, or the analysis is reproducible.

### Input

```text
Research objective and unit of analysis:
[Research question, unit of analysis, primary outcome, or estimand]

Code and directory:
[Directory tree, entry points, key scripts, or review scope]

Input data contract:
[Source, version, fields, types, units, encodings, keys, missing-value rules, and permission scope]

Expected output contract:
[Tables, figures, model objects, reports, or intermediate files; format, naming, and acceptance criteria]

Execution environment:
[Operating system, language or runtime versions, dependency records, hardware or resource limits]

Existing execution records:
[Command or execution method, logs, errors, warnings, code revision, and data version]

Privacy and sharing constraints:
[Fields, paths, credentials, source-data fragments, and files that must not be exposed]
```

### Requirements

1. State the review scope, supplied materials, missing materials, and questions that cannot be answered from the evidence. Turn missing information into specific questions instead of filling it with defaults.
2. Build input/output contracts for the major steps. For each step, specify the input source, fields and units, transformation rules, outputs, failure conditions, log fields, and acceptance checks.
3. Inspect environment and provenance records, including runtime, dependencies, configuration, data version, code revision, randomness, parallel settings, time or locale settings, and external services. Mark unknown versions as “to be provided.”
4. Inspect data safety. Identify possible personal information, sensitive identifiers, access tokens, internal paths, and unapproved data fragments in code, configuration, caches, logs, and outputs. Do not copy or infer real sensitive content.
5. Plan tests covering input contracts, key transformations, boundary conditions, missing data, failure paths, and output formats. Distinguish static checks, executed tests, and pending tests.
6. Review logging and error handling. State which warnings permit continuation, which affect interpretation, and which errors must stop the workflow. Check whether a failed run could still write apparently complete results.
7. Plan result verification. Propose independent recalculation or cross-checks for key counts, summaries, figure data, units, groups, and exported files. If a check was not run, label it “to be verified.”
8. Classify findings as `blocking / required fix / improvement`. Every finding must include a file or step location, evidence, impact, and an actionable remediation.
9. Do not assume a programming language, package manager, operating system, or code-hosting platform. Give tool-specific commands or configuration only when the input identifies the tool.
10. Do not fabricate data, test-pass records, logs, version numbers, performance values, statistical results, or scientific conclusions. Mark examples as placeholders or synthetic examples.

### Output format

Return the sections in this order:

1. Review scope and evidence status
2. Missing information and questions for confirmation
3. Workflow and input/output contract table
4. Environment, dependency, and provenance review
5. Data-safety and sharing review
6. Test, diagnostic, and failure-path plan
7. Logging and failure-handling review
8. Result-verification plan
9. Severity-ranked review findings
10. Prioritized next actions

For every conclusion, state whether it is based on code reading, an existing execution record, or an unverified recommendation.

## Source / 来源

来源于网络，自行整理汇总。

## Prompt contract / 提示词契约

### 中文

- **使用场景：** 审查科研代码的输入输出契约、环境、数据安全、错误处理和结果核验。
- **输入要求：** 代码树、研究任务、数据和文件位置、依赖版本、运行命令、测试样例和已有日志。
- **输出要求：** 范围与状态、输入输出契约、环境来源、隐私检查、测试计划、日志建议、分级问题和下一步。
- **禁止编造：** 不得编造运行结果、通过记录、版本号、性能、统计结果或科学结论。
- **信息不足：** 把缺少的代码、数据契约、依赖或日志列为待补充，只做静态审查和核验计划。
- **双语示例：** 完整输入含代码目录、锁定依赖和测试日志，输出可追溯问题表；信息不足时只有片段，输出缺失字段，不声称已复现。

### English

- **Use case:** Review research-code contracts, environment, data safety, failure handling, and result verification.
- **Required inputs:** Code tree, research task, data and file locations, dependency versions, run commands, test cases, and existing logs.
- **Expected output:** Scope and status, input/output contract, provenance, privacy review, test plan, logging advice, severity-ranked findings, and next actions.
- **Fabrication ban:** Do not invent execution results, pass records, versions, performance, statistics, or scientific conclusions.
- **Missing information:** Mark missing code, data contracts, dependencies, or logs as to be provided and limit the review to static checks and a verification plan.
- **Bilingual example:** With a code tree, locked dependencies, and test logs, return a traceable findings table; with only a snippet, list missing fields and do not claim reproduction.

## Source / 来源

来源于网络和用户提供的科研代码审查材料，自行整理汇总；未复制第三方代码或审查报告。

Source: online materials and user-provided research-code review material, independently organized. No third-party code or review report was copied.
