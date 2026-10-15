# Second-batch Evaluation / 第二批评估

## 中文

第二批包含 `rnaseq-analysis`、`research-coding` 和 `research-presentation`。每个 Skill 和 Prompt 都需要使用一个完整输入案例和一个信息不足案例进行评估。评估记录应保留输入摘要、模型输出、人工核查、发现的问题和修改版本。

### RNA-seq 分析

- 完整案例应包含样本元数据、FASTQ 或 counts 清单、参考基因组和预设对比式。
- 信息不足案例应缺少至少一个会影响设计或模型的字段，例如生物学重复、链特异性或批次信息。
- 检查模型是否区分技术重复与生物学重复，是否保留 raw counts、FDR、背景集和版本记录。
- 没有真实结果时，输出只能停留在计划和待补充字段，不能生成差异基因或 P 值。

### 科研代码

- 完整案例应包含代码目录、输入输出说明、环境信息、测试样例和一份可核对的结果记录。
- 信息不足案例应缺少数据契约、依赖版本或运行日志中的一项。
- 检查输入输出契约、错误处理、日志、敏感信息和结果核验是否被分别记录。
- 静态审查不能被表述为代码已经运行或结果已经复现。

### 科研汇报

- 完整案例应包含受众、总时长、研究问题、证据材料、图表和引用来源。
- 信息不足案例应只提供一张图或几句结论，检查 Skill 是否先列出不能判断的内容。
- 检查每个关键主张是否有证据或引用，图表是否注明单位和不确定性，结论是否超过研究设计。
- 演练记录应区分已核查、待核查和无法判断的事项。

## English

The second batch contains `rnaseq-analysis`, `research-coding`, and `research-presentation`. Evaluate every Skill and Prompt with one complete-input case and one incomplete-input case. Keep an input summary, model output, human checks, observed issues, and revision version for each evaluation.

### RNA-seq analysis

- The complete case should include sample metadata, a FASTQ or count manifest, a reference genome, and a prespecified contrast.
- The incomplete case should omit at least one field that changes the design or model, such as biological replication, strandedness, or batch information.
- Check that the workflow distinguishes technical and biological replicates and records raw counts, FDR, the enrichment universe, and versions.
- Without real results, the output must remain a plan with missing fields; it must not generate genes or p-values.

### Research coding

- The complete case should include a code tree, input/output description, environment information, test data, and a checkable result record.
- The incomplete case should omit a data contract, dependency version, or execution log.
- Check that contracts, error handling, logs, sensitive-data checks, and result verification are reported separately.
- A static review must not be described as executed code or a successful reproduction.

### Research presentation

- The complete case should include the audience, total time, research question, evidence, figures, and citations.
- The incomplete case should provide only one figure or a few conclusions, so that the Skill must list what cannot be determined.
- Check claim-evidence alignment, units and uncertainty in figures, and whether the conclusion exceeds the design.
- Rehearsal records should separate checked, to-be-checked, and undetermined items.
