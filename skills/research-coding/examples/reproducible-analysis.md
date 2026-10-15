# Reproducible Analysis Example / 可复现分析示例

**Status / 状态:** planning example; no code was executed / 规划示例，未执行代码

## Scenario / 场景

研究者有一组经过批准可以使用的实验数据和一套零散分析脚本。研究目标、字段含义、运行环境和预期输出仍需要整理。示例只展示如何规划工作流，不包含真实数据、真实路径、真实版本号或分析结果。

A researcher has an approved dataset and a collection of scattered analysis scripts. The research objective, field meanings, execution environment, and expected outputs still need to be organized. This example demonstrates workflow planning only; it contains no real data, paths, version numbers, or analysis results.

## Input / 输入

```text
Research objective / 研究目标:
[Describe the research question and primary estimand.]

Source data / 输入数据:
[Approved dataset or data interface; provide a data dictionary separately.]

Available code / 现有代码:
[List entry points, scripts, configuration files, and known execution errors.]

Expected outputs / 预期输出:
[Tables, figures, model objects, or reports; specify format and acceptance criteria.]

Environment / 运行环境:
[Operating system, language/runtime, dependency records, and resource limits if known.]

Privacy constraints / 隐私约束:
[Fields that must not appear in code, logs, examples, or shared outputs.]
```

## Planned workflow / 计划工作流

| Step / 步骤 | Input and contract / 输入与契约 | Operation / 操作 | Output and check / 输出与检查 |
| --- | --- | --- | --- |
| 1. Intake / 接收 | Approved source, data dictionary, access scope | Check required fields, units, keys, missing-value codes, and data version | Intake record; stop if the contract is unclear |
| 2. Read-only staging / 只读暂存 | Source identifier and immutable copy or approved interface | Create a traceable staging reference without changing source data | Staging record and row/field counts; do not log sensitive values |
| 3. Transformation / 转换 | Staging data and declared transformation rules | Apply documented renaming, unit conversion, filtering, and derivation | Derived dataset with transformation log; check counts, ranges, and units |
| 4. Analysis / 分析 | Derived data, analysis specification, environment record | Run the declared analysis steps with recorded configuration | Analysis objects and summaries; record warnings and failures |
| 5. Independent check / 独立核对 | Key summaries and an approved checking procedure | Recalculate selected summaries or compare with an independent implementation | Check report; mark unexecuted checks as pending |
| 6. Export / 导出 | Checked results and output specification | Write tables, figures, and report files to a versioned output location | Manifest with file names, code revision, data version, and timestamp |

## Example contract / 契约示例

### Input contract / 输入契约

- The source must be approved for this analysis and identified by a stable version or access record.
- Required fields, units, encodings, keys, and missing-value codes must be listed in the data dictionary.
- The workflow must fail with a useful message when a required field is absent or has an incompatible type.
- Sensitive identifiers must be excluded from examples and logs, or replaced with an approved pseudonymous identifier whose re-identification risk has been assessed.

- 输入数据必须获得本分析所需的使用许可，并有稳定版本或访问记录。
- 数据字典必须列出必需字段、单位、编码、主键和缺失值代码。
- 缺少必需字段或字段类型不符合契约时，流程必须给出可定位的错误并停止相关步骤。
- 敏感标识符必须从示例和日志中排除，或者使用经批准的假名化标识替代，并评估重识别风险。

### Output contract / 输出契约

- Every table or figure must state its source step, data version, code revision, units, and relevant configuration.
- Output names and formats must be stable enough for downstream reports or manual review.
- A failed or partial run must not be presented as a complete result set.
- The manifest must distinguish generated files, temporary files, and files requiring manual approval.

- 每个表格或图形都要记录来源步骤、数据版本、代码版本、单位和相关配置。
- 输出文件名和格式要稳定，便于下游报告或人工复核。
- 失败或不完整的运行不能标记为完整结果集。
- 文件清单要区分生成文件、临时文件和需要人工批准的文件。

## Environment and provenance record / 环境与来源记录

```text
Code revision / 代码版本: [revision identifier]
Data version / 数据版本: [version or access record]
Runtime / 运行时: [language or runtime and version]
Dependencies / 依赖: [lock file, manifest, or verified list]
Configuration / 配置: [analysis settings and non-sensitive paths]
Randomness / 随机性: [whether randomness is used and how it is recorded]
External services / 外部服务: [none, or service and retrieval record]
Execution record / 执行记录: [date, status, log location]
```

如果某一项未知，应填写“待补充”，并把它列入复现前的阻断条件。示例不把占位符当作已知事实。

If an item is unknown, enter “to be provided” and list it as a blocking condition before reproduction. Placeholders in this example are not facts.

## Test and verification plan / 测试与核验计划

1. **Contract checks / 契约检查**：用不含敏感信息的最小样例检查必需字段、类型、单位、键和缺失值代码。
2. **Transformation checks / 转换检查**：对每个派生字段检查输入字段、公式或规则、记录数变化和范围。
3. **Failure-path checks / 错误路径检查**：分别测试缺失字段、非法类型、空输入和不可访问资源，并确认错误不会被静默忽略。
4. **Recalculation checks / 复算检查**：对预先指定的摘要、分组计数或图形数据重新计算，并记录差异和容许范围。
5. **Output checks / 输出检查**：核对文件格式、单位、图例、表头、数据版本和代码版本。
6. **Privacy checks / 隐私检查**：扫描代码、配置、日志和输出，确认没有凭据、敏感标识符、内部路径或未经批准的数据片段。

1. **契约检查 / Contract checks**: Use a non-sensitive minimal example to check required fields, types, units, keys, and missing-value codes.
2. **转换检查 / Transformation checks**: For every derived field, check its inputs, formula or rule, record-count changes, and range.
3. **错误路径检查 / Failure-path checks**: Test missing fields, invalid types, empty input, and inaccessible resources; confirm that errors are not silently ignored.
4. **复算检查 / Recalculation checks**: Recalculate prespecified summaries, group counts, or figure data and record differences and tolerances.
5. **输出检查 / Output checks**: Check file format, units, legends, headers, data version, and code revision.
6. **隐私检查 / Privacy checks**: Inspect code, configuration, logs, and outputs for credentials, sensitive identifiers, internal paths, and unapproved data fragments.

## Expected review record / 预期审查记录

| Finding / 问题 | Evidence / 证据 | Impact / 影响 | Action / 建议 |
| --- | --- | --- | --- |
| Input version is not recorded / 未记录输入版本 | The intake step has no stable data identifier | Results cannot be traced to a specific input | Add a data-version field to the contract and manifest |
| Error path is ambiguous / 错误路径不明确 | A failed transformation still writes a result file | Partial output may be mistaken for a complete result | Stop the dependent steps and mark the run as failed |
| Log may expose identifiers / 日志可能泄露标识符 | Debug output includes unsanitized values | Sharing the log may breach the data restriction | Redact or aggregate values before logging |
| Independent check is pending / 独立核对待执行 | No check record is supplied | Numerical agreement is unconfirmed | Run the approved check and attach the record |

这些问题是审查示例，不代表某个真实仓库已经存在这些缺陷。实际审查必须引用可定位的文件、步骤或运行记录。

These findings are illustrative and do not claim that a real repository has these defects. An actual review must cite a specific file, step, or execution record.

## Source / 来源

来源于网络，自行整理汇总。

Source: collected from public online materials and reorganized by the repository maintainer.
