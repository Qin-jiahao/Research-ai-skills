# Basic Bulk RNA-seq Workflow Example / 基础 Bulk RNA-seq 流程示例

## Scenario / 场景

研究者有两个处理组的 bulk RNA-seq 数据，每组预计有生物学重复。研究者希望比较处理组与对照组的基因表达差异，并进行后续通路分析。当前示例只演示如何组织分析计划，不代表任何真实结果。

A researcher has bulk RNA-seq data from two treatment groups, with biological replicates expected in each group. The goal is to compare gene expression between treatment and control and then perform pathway analysis. This example shows how to structure a plan; it does not represent real results.

## Minimum input record / 最低输入记录

```text
study_id: example-bulk-rnaseq-001
species: to be provided
reference_genome: to be provided
annotation_version: to be provided
read_type: paired-end or single-end, to be provided
library_strandedness: to be provided
sample_metadata: metadata.tsv, checksum to be provided
fastq_manifest: fastq_manifest.tsv, checksums to be provided
primary_contrast: treatment - control
biological_replicates: to be confirmed from metadata
batch_factors: to be provided
```

上述字段中，“待补充”表示不能从场景描述推断，必须由真实文件或实验记录确认。样本 ID、个体 ID、组别、批次和文件路径应在正式分析前完成一一对应。

“To be provided” means that the value cannot be inferred from the scenario and must be confirmed from real files or laboratory records. Sample IDs, subject IDs, groups, batches, and file paths must be mapped one to one before formal analysis.

## Planned workflow / 计划流程

### 1. Metadata and design / 元数据与设计

先检查每个样本是否有唯一 ID，确认每组的生物学重复数，区分技术重复和生物学重复，确认批次是否与处理组完全混杂。若一个个体在多个时间点被重复测量，应在设计中加入个体项，而不是把时间点当成独立样本。

Check that every sample has a unique ID, confirm the number of biological replicates per group, distinguish technical from biological replicates, and determine whether batch is fully confounded with treatment. If one subject is measured at multiple time points, include the subject structure in the design rather than treating time points as independent samples.

**Design record / 设计记录:**

```text
design_formula: ~ batch + treatment       # use only if batch is justified and estimable
contrast: treatment - control
reference_level: control
unit_of_analysis: biological sample or subject, to be confirmed
```

这个公式只是示意。实际公式必须根据元数据、实验设计和可估计性确认，不能机械复制。

This formula is illustrative. The actual formula must be confirmed from metadata, design, and estimability; do not copy it mechanically.

### 2. Raw-read QC / 原始读段 QC

对每个 FASTQ 文件运行或读取 FastQC/MultiQC 类报告，记录读段数、质量分布、接头污染、GC 分布、N 含量、过度代表序列和读长。若需要修剪，保存软件版本、参数和前后读段数。不要在看见下游结果后修改 QC 规则。

Run or inspect FastQC/MultiQC-like reports for every FASTQ file. Record read counts, quality distributions, adapter contamination, GC distribution, ambiguous bases, overrepresented sequences, and read length. If trimming is needed, save software versions, parameters, and before/after read counts. Do not change QC rules after looking at downstream results.

**QC decision table / QC 决策表:**

| Check / 检查项 | Observed value / 实际值 | Decision / 决定 | Evidence / 证据 |
|---|---|---|---|
| Adapter contamination / 接头污染 | 待补充 | 待补充 | FastQC/MultiQC report |
| Per-base quality / 碱基质量 | 待补充 | 待补充 | FastQC/MultiQC report |
| Library size / 文库大小 | 待补充 | 待补充 | read-count log |
| Sample exclusion / 样本排除 | 无法预先决定 | 依据预设规则和技术证据 | exclusion log |

### 3. Alignment or quantification / 比对或定量

根据研究目的和数据类型选择 STAR/HISAT2 等基因组比对，或 Salmon/kallisto 等转录本定量。记录参考基因组、注释版本、索引、链特异性和关键参数。若从转录本定量汇总到基因层面，应记录汇总方法和 ID 映射版本。

Choose genome alignment with tools such as STAR/HISAT2 or transcript quantification with tools such as Salmon/kallisto according to the question and data type. Record the reference genome, annotation version, index, strandedness, and key parameters. If transcript estimates are summarized to gene level, record the summarization method and identifier-mapping version.

必须从实际输出读取比对率、唯一比对率、多重比对和覆盖指标。没有日志时，结果栏保持“待补充”。

Alignment rate, unique mapping, multimapping, and coverage metrics must be read from actual outputs. Without logs, keep the result field as “to be provided.”

### 4. Count object and filtering / 计数对象与过滤

差异分析应明确使用何种表达对象。若使用 DESeq2 或 edgeR，通常输入原始整数 counts，并在模型内完成适当标准化。过滤规则要在分析前写清楚，例如根据最小样本数和预设表达水平过滤低信息特征。过滤后的特征数量和规则都要记录。

State which expression object is used for differential analysis. DESeq2 or edgeR generally use raw integer counts and perform compatible normalization within the model. Define filtering before analysis, for example using a minimum number of samples and a prespecified expression level. Record both the rule and the number of features retained.

### 5. Differential expression / 差异表达

使用与设计矩阵匹配的模型，指定对照组、对比式和批次或其他协变量。结果表至少保留 gene ID、log2 fold change、标准误或置信区间、原始 P 值、调整后 FDR 和注释版本。结果解释应同时考虑效应大小、方向、不确定性和统计效能。

Fit a model compatible with the design matrix and specify the control level, contrast, batch, and other covariates. The result table should retain gene ID, log2 fold change, standard error or confidence interval, raw p-value, adjusted FDR, and annotation version. Interpretation should consider effect size, direction, uncertainty, and power together.

**Result status / 结果状态:**

```text
significant_features: not computed in this example
p_values: not computed in this example
pathways: not computed in this example
```

### 6. Enrichment and reporting / 富集分析与报告

在真实结果产生后，先固定输入基因集和背景集，再选择 ORA、GSEA 或其他方法。ORA 使用阈值化的选定基因集和 tested universe；GSEA 使用带排序统计量的 gene-level statistic vector 与明确的基因集数据库，不能把阈值化 DEG 列表当作 GSEA 输入。记录数据库版本、访问日期、ID 映射失败数量和多重检验方法。富集结果需要报告富集方向、效应或统计量、FDR 和背景集，不能只复制通路名称。

After real results are produced, define the input and background gene sets before selecting ORA, GSEA, or another method. ORA uses a thresholded selected gene set and a tested universe; GSEA uses a gene-level statistic vector ranked across the measured features and an identified gene-set database, not a thresholded DEG list. Record database version, access date, failed ID mappings, and multiplicity correction. Report enrichment direction, effect or statistic, FDR, and the universe rather than copying pathway names alone.

## Reproducibility checklist / 可复现性清单

- [ ] 元数据、FASTQ 清单和校验和已保存；
- [ ] 参考基因组和注释版本已记录；
- [ ] 软件版本、参数、环境文件和日志已保存；
- [ ] QC、修剪、定量、过滤和样本排除决定可追溯；
- [ ] 设计矩阵和对比式与预设研究问题一致；
- [ ] 原始 counts、标准化对象和展示矩阵已区分；
- [ ] 差异结果包含效应量、不确定性和 FDR；
- [ ] 富集分析记录背景集、数据库版本和 ID 映射；
- [ ] 所有“待补充”字段在正式报告中已解决或明确保留。

- [ ] Metadata, FASTQ manifest, and checksums are saved.
- [ ] Reference genome and annotation versions are recorded.
- [ ] Software versions, parameters, environment files, and logs are saved.
- [ ] QC, trimming, quantification, filtering, and exclusion decisions are traceable.
- [ ] The design matrix and contrast match the prespecified question.
- [ ] Raw counts, normalized objects, and display matrices are distinguished.
- [ ] Differential results include effect sizes, uncertainty, and FDR.
- [ ] Enrichment records the universe, database version, and ID mapping.
- [ ] Every “to be provided” field is resolved or explicitly retained in the final report.

## Interpretation boundary / 解释边界

即使分析流程成功运行，也只能说明数据在给定设计和模型下支持某些统计关联。差异表达和富集结果不能单独证明因果机制、细胞类型变化或通路被激活。研究者还需要结合实验设计、独立验证和领域知识。

Successful execution supports statistical associations under the specified design and model. Differential expression and enrichment alone do not prove causal mechanisms, cell-composition changes, or pathway activation. Interpretation still requires the experimental design, independent validation, and domain knowledge.

## Source / 来源

来源于网络，自行整理汇总。
