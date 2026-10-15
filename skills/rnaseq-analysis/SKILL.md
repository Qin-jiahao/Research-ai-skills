---
name: rnaseq-analysis
description: Plan and audit bulk RNA-seq workflows when real sample metadata, raw reads, or count matrices are available; 在已有真实样本元数据、原始读段或计数矩阵、需要审查 bulk RNA-seq 流程时使用。
metadata:
  short-description: Plan and audit reproducible bulk RNA-seq workflows
---

# RNA-seq Analysis / RNA-seq 分析

**Status / 状态:** v0.2.0 draft

## Purpose / 用途

这个 Skill 面向有真实 bulk RNA-seq 数据的研究者，帮助制定分析计划、审查分析记录、解释质量控制和统计结果。它优先处理样本元数据、实验设计、原始数据质量和可复现记录，再讨论生物学解释。

This Skill is for researchers working with real bulk RNA-seq data. It helps plan workflows, audit analysis records, and interpret quality-control and statistical outputs. It prioritizes sample metadata, experimental design, raw-data quality, and reproducible records before biological interpretation.

## Scope and boundaries / 适用范围与边界

- 默认范围是 bulk RNA-seq。单细胞、空间转录组、低输入特殊建库或长读长数据需要单独确认流程，不能直接套用本 Skill。
- 必须使用用户提供的真实 FASTQ、比对文件、计数矩阵或明确的数据摘要。没有数据时只能输出计划、检查表或待补充字段。
- 不能根据截图、论文摘要或少量基因名称虚构测序深度、P 值、差异基因、通路或图形。
- 工具和参数应根据物种、参考基因组、建库方式、测序类型和研究问题选择；本 Skill 不把某个软件或阈值当成普遍标准。

- The default scope is bulk RNA-seq. Single-cell, spatial, unusual low-input libraries, and long-read data require a separate workflow review.
- Use real FASTQ files, alignment files, count matrices, or an explicit data summary supplied by the researcher. Without data, return a plan, checklist, or missing-field list only.
- Never invent sequencing depth, p-values, differentially expressed genes, pathways, or figures from screenshots, abstracts, or a short gene list.
- Select tools and parameters according to species, reference assembly, library protocol, read type, and research question. No single software package or cutoff is universally correct.

## Required inputs / 所需输入

在开始分析前，先检查下列信息。缺失信息要标记为“待补充”，并说明它会影响哪一步。

Before analysis, check the following inputs. Mark missing items as “to be provided” and state which decision they affect.

1. **研究问题和实验设计 / Research question and design:** 生物学问题、主要比较、预设主要结局、组别、时间点、处理因素、协变量、配对或重复测量关系。
2. **样本元数据 / Sample metadata:** 每个样本唯一 ID、个体或生物学重复 ID、组别、批次、性别或其他预设协变量、建库批次、测序批次、组织或细胞来源、排除规则。元数据表中的每一行应对应一个可追溯的样本。
3. **原始数据和技术信息 / Raw data and technical information:** FASTQ 路径或校验和、单端或双端、读长、测序平台、读段方向、文库链特异性、测序深度、参考基因组和注释版本。
4. **数据对象 / Data objects:** 已有的 QC 报告、比对或准比对结果、基因或转录本计数矩阵、过滤记录、样本排除记录和脚本。必须说明计数矩阵是原始整数 counts、长度校正值还是其他表达量。
5. **可复现环境 / Reproducibility context:** 软件名称和版本、参数、容器或环境文件、随机种子、运行日期、输出目录和日志。

## Core workflow / 核心流程

### 1. Clarify the design before touching the reads / 先确认设计，再处理读段

先把研究问题写成可检验的比较或模型。区分生物学重复和技术重复，确认分析单位，避免把同一个个体的技术重复当成独立样本。对于配对、重复测量或多因素设计，设计矩阵应显式包含个体、时间点、批次和交互项等必要结构。批次因素不能因为 PCA 看起来明显就事后随意加入，也不能因为不显著就自动删除；是否调整要根据实验流程和预设分析目标决定。

Translate the question into prespecified comparisons or model terms. Distinguish biological from technical replicates and define the unit of analysis. Do not treat technical replicates from one individual as independent samples. For paired, repeated-measures, or factorial designs, represent subject, time, batch, and relevant interactions explicitly in the design matrix. Do not add or remove a batch factor solely because it appears prominent or nonsignificant in PCA; decide from the experimental process and analysis objective.

### 2. Audit metadata and sample identity / 审查元数据和样本身份

检查 FASTQ 文件名、样本 ID、元数据表和计数矩阵列名能否一一对应。记录缺失样本、重复文件、样本交换风险、未说明的批次和任何排除决定。样本身份不清时暂停下游统计，不要用表达相关性替代样本身份验证。

Check one-to-one correspondence among FASTQ names, sample IDs, metadata rows, and count-matrix columns. Record missing samples, duplicate files, possible swaps, undocumented batches, and every exclusion decision. If identity is uncertain, pause downstream statistics; expression correlation is not a substitute for identity verification.

### 3. Run or inspect raw-read QC / 执行或审查原始读段 QC

根据真实报告检查碱基质量、接头污染、过度代表序列、N 含量、读段长度、GC 分布和测序深度。可以使用 FastQC/MultiQC 或同类工具，但工具名称不等于质量结论。接头和低质量修剪必须保留参数、版本和前后读段统计。任何“通过”或“失败”都要结合物种、建库类型和预设研究目的解释，不能套用单一百分比阈值。

Inspect base quality, adapter contamination, overrepresented sequences, ambiguous bases, read length, GC distribution, and sequencing depth from actual reports. FastQC/MultiQC or comparable tools may be used, but a tool label is not a quality conclusion. Record trimming parameters, versions, and before/after read counts. Interpret pass/fail in the context of species, library protocol, and study aim rather than applying one universal percentage cutoff.

### 4. Choose alignment or quantification deliberately / 有依据地选择比对或定量

说明选择全基因组比对、转录本准比对或直接计数的理由。全基因组比对可使用 STAR、HISAT2 等；转录本定量可使用 Salmon、kallisto 等；基因计数可使用 featureCounts 或经过验证的等效方法。记录参考基因组、注释文件、版本、索引构建方式、链特异性和关键参数。比对率、唯一比对率、多重比对、外显子覆盖和 rRNA 比例必须来自实际输出。

State why genome alignment, transcript-level quasi-mapping, or direct counting is appropriate. STAR or HISAT2 are possible genome aligners; Salmon or kallisto are possible transcript quantifiers; featureCounts or a validated equivalent can produce gene counts. Record genome and annotation versions, index construction, strandedness, and key parameters. Alignment rate, uniquely mapped reads, multimapping, exon coverage, and rRNA fraction must come from actual outputs.

### 5. Build an analysis-ready expression object / 构建可分析的表达对象

明确基因 ID 体系和注释版本，检查重复 ID、未注释 ID、零计数样本和极低表达特征。差异表达通常应使用适合原始整数 counts 的模型；TPM、FPKM 等长度校正表达量可用于描述或可视化，不能直接当作大多数 count-based 差异模型的输入。过滤规则应在分析记录中说明，避免根据最终显著性反复调阈值。

Document gene identifiers and annotation version, and check duplicated IDs, unannotated IDs, zero-count samples, and very lowly expressed features. Differential-expression models generally expect raw integer counts; TPM or FPKM can support description or visualization but should not be used as input to most count-based differential models. State filtering rules in the analysis record and do not repeatedly tune them to obtain desired significance.

### 6. Normalize and diagnose sample structure / 标准化并诊断样本结构

选择与模型匹配的标准化方法，例如 DESeq2 size factors、edgeR 的 TMM 或 limma-voom 的相应流程。标准化不是批次校正，也不会修复样本污染、标签错误或严重测序失败。用 PCA、样本相关性、层次聚类、库大小和离群诊断检查组间结构；任何样本剔除都必须有原始 QC、技术原因或预先规定的标准作为依据，并保留敏感性分析。

Use a normalization method compatible with the model, such as DESeq2 size factors, edgeR TMM, or the corresponding limma-voom workflow. Normalization is not batch correction and cannot repair contamination, mislabeled samples, or major sequencing failure. Use PCA, sample correlations, hierarchical clustering, library sizes, and outlier diagnostics to inspect structure. Any exclusion must be supported by raw QC, a technical reason, or a prespecified rule, with a sensitivity analysis retained.

### 7. Fit differential-expression models / 拟合差异表达模型

根据设计选择 DESeq2、edgeR、limma-voom 或其他有明确依据的方法。完整记录设计矩阵、参考水平、对比式、协变量、独立过滤和离散度估计。报告效应量（例如 log2 fold change）、置信区间或标准误、原始 P 值和多重检验校正后的 FDR。Benjamini-Hochberg 是常见选择，但校正方法和筛选阈值要与研究目标一致。不能只报告“上调/下调基因数量”，也不能把 FDR 阈值当成生物学重要性的证明。

Choose DESeq2, edgeR, limma-voom, or another justified method according to the design. Record the design matrix, reference levels, contrasts, covariates, independent filtering, and dispersion estimation. Report effect sizes such as log2 fold changes, confidence intervals or standard errors, raw p-values, and multiplicity-adjusted FDR. Benjamini–Hochberg is common, but the correction method and cutoffs should match the research aim. Do not report only counts of up- or down-regulated genes, and do not treat an FDR cutoff as proof of biological importance.

### 8. Interpret enrichment with the correct universe / 使用正确的背景集解释富集

在富集分析前明确输入基因集、背景基因集、ID 映射版本、方向性和多重检验方法。ORA 使用预先选定的基因集和 tested universe；GSEA 使用带有基因层面排序统计量的完整向量和明确的基因集数据库，不能把阈值化 DEG 列表当作 GSEA 输入。GO、KEGG、Reactome 或 GSEA 的选择要与研究问题、物种和排序统计量匹配。背景集通常应来自通过表达过滤且有机会被检测到的特征，而不是默认全基因组。富集结果是统计关联，不能单独证明通路被激活、机制成立或存在因果关系。记录数据库版本和访问日期。

Before enrichment, define the input gene set, background universe, identifier-mapping version, directionality, and multiplicity correction. ORA uses a prespecified selected gene set and tested universe; GSEA uses a complete gene-level vector with a ranking statistic and an identified gene-set database, so a thresholded DEG list must not be used as a GSEA input. Choose GO, KEGG, Reactome, GSEA, or another method to match the question, species, and ranking statistic. The background should usually reflect features that passed expression filtering and could have been detected, rather than the entire genome by default. Enrichment is a statistical association; it does not by itself prove pathway activation, mechanism, or causality. Record database versions and access dates.

### 9. Preserve a reproducible record / 保留可复现记录

保存原始数据校验和、元数据快照、脚本、配置文件、环境文件、软件版本、参数、日志、随机种子、输入输出清单和图表生成代码。报告每次人工决定，包括样本排除、过滤、批次处理和对比式修改。最终报告应能从样本 ID 追溯到数据文件、计数矩阵、模型和图表。若只能提供汇总结果，要明确说明哪些步骤无法独立复核。

Preserve raw-data checksums, a metadata snapshot, scripts, configuration and environment files, software versions, parameters, logs, random seeds, input/output manifests, and plotting code. Report every manual decision, including sample exclusion, filtering, batch handling, and contrast changes. A final report should trace each sample ID to data files, the count matrix, model, and figures. If only summaries are available, state which steps cannot be independently audited.

## Output format / 输出格式

在没有真实数据时，输出一份带有“待补充”标记的分析计划；在有真实结果时，输出下列内容并引用实际文件或表格。

When real data are unavailable, return an analysis plan with explicit “to be provided” fields. When results are available, return the following and cite the actual files or tables.

```text
Study and design check / 研究设计检查
- Research question, unit of analysis, biological replicates, paired or repeated structure
- 研究问题、分析单位、生物学重复、配对或重复测量结构

Metadata and data audit / 元数据与数据审查
- Sample mapping, missing fields, batches, read type, strandedness, reference versions
- 样本对应关系、缺失字段、批次、读段类型、链特异性、参考版本

QC and preprocessing / QC 与预处理
- Observed metrics, decisions, parameters, and unresolved issues
- 实际指标、处理决定、参数和未解决问题

Quantification and model / 定量与模型
- Tool versions, count object, design matrix, contrasts, normalization, filtering
- 工具版本、计数对象、设计矩阵、对比式、标准化和过滤

Results and uncertainty / 结果与不确定性
- Effect sizes, intervals or standard errors, p-values, FDR, diagnostic plots
- 效应量、区间或标准误、P 值、FDR 和诊断图

Enrichment / 富集分析
- Gene universe, database/version, method, correction, and interpretation limits
- 基因背景集、数据库/版本、方法、校正和解释边界

Reproducibility and limitations / 可复现性与局限性
- Files, code, environment, manual decisions, missing evidence, sensitivity analyses
- 文件、代码、环境、人工决定、缺失证据和敏感性分析
```

## Quality checks / 质量检查

- 每个样本是否能从元数据追溯到原始文件和计数矩阵列；
- 实验设计是否与分析单位、重复结构和设计矩阵一致；
- 参考基因组、注释、链特异性和 ID 版本是否明确且前后一致；
- QC 指标是否来自真实报告，处理决定是否有记录；
- 是否区分原始 counts、标准化表达量和可视化数据；
- 是否报告效应量、不确定性和多重检验，而不是只报告显著基因数量；
- 富集分析是否给出合理背景集、数据库版本和 ID 映射记录；
- 是否保留代码、参数、环境、日志和样本排除理由；
- 是否把统计关联写成通路激活、机制或因果结论；
- 是否明确数据缺失、模型假设、低统计效能和其他限制。

- Can every sample be traced from metadata to raw files and count-matrix columns?
- Does the design matrix represent the unit of analysis, replicate structure, and planned comparisons?
- Are the genome, annotation, strandedness, and identifier versions explicit and consistent?
- Do QC claims come from real reports, with decisions recorded?
- Are raw counts, normalized values, and visualization values distinguished?
- Are effect sizes, uncertainty, and multiplicity reported rather than only a list of significant genes?
- Does enrichment specify an appropriate universe, database version, and ID mapping?
- Are code, parameters, environments, logs, and exclusion reasons preserved?
- Are statistical associations kept separate from claims of activation, mechanism, or causality?
- Are missing data, model assumptions, low power, and other limitations explicit?

## Common failure modes / 常见错误

- 用 TPM 或 FPKM 直接替代适用于 counts 的差异模型输入；
- 把技术重复扩充成独立生物学重复，造成伪重复；
- 先看显著结果，再反复改变过滤或对比式；
- 用全基因组作为默认富集背景，忽略可检测特征和表达过滤；
- 只凭 PCA 或聚类图删除离群样本；
- 把批次校正后的展示矩阵拿去替代原始 counts 做差异分析；
- 只报告 P 值或显著基因数，不报告效应量和不确定性；
- 把数据库富集结果写成已证实的机制；
- 在没有原始文件、元数据或日志时声称流程“已经完成”。

- Feeding TPM or FPKM directly into a count-based differential model;
- Treating technical replicates as independent biological replicates;
- Changing filters or contrasts repeatedly after looking at significance;
- Using the whole genome as the default enrichment background;
- Removing samples from PCA or clustering alone;
- Replacing raw counts with a batch-corrected display matrix for differential testing;
- Reporting only p-values or significant-gene counts without effect sizes and uncertainty;
- Presenting database enrichment as a confirmed mechanism;
- Claiming completion when raw files, metadata, or logs are unavailable.

## Limitations / 限制

这个 Skill 只能帮助规划和审查 bulk RNA-seq 分析，不能确认样本质量、实验有效性或生物学机制。它不能替代原始数据检查、统计学判断、领域专家审阅或实验验证。低样本量、严重批次混杂、缺失元数据、参考注释不匹配和低质量文库都会限制结论，即使软件成功运行也不能消除这些限制。

This Skill can plan and audit bulk RNA-seq analyses, but it cannot certify sample quality, experimental validity, or biological mechanism. It does not replace raw-data inspection, statistical judgment, domain review, or experimental validation. Small sample sizes, severe batch confounding, missing metadata, mismatched annotations, and poor libraries limit inference even when the software completes successfully.

## Example / 示例

**Input / 输入:** 一份样本元数据表、FASTQ 文件清单、参考基因组版本和预设组间比较，要求制定差异表达和富集分析计划。

**Expected output / 预期输出:** 先核对样本映射、重复结构、批次和建库方向，再列出 QC、定量、标准化、模型、FDR 和富集背景集的计划。所有无法从真实文件确认的字段都标记为“待补充”，不生成任何差异基因、P 值或通路结果。

**Input / English:** A sample metadata table, FASTQ manifest, reference-genome version, and prespecified group contrast are supplied for a differential-expression and enrichment plan.

**Expected output / English:** First audit sample mapping, replicate structure, batches, and library strandedness. Then specify QC, quantification, normalization, model, FDR, and enrichment universe. Mark every field that cannot be verified from real files as “to be provided”; generate no genes, p-values, or pathway results.

**Source / 来源:** 来源于网络，自行整理汇总。
