---
name: figure-evidence-audit
description: Plan and audit research figures from data, claims, methods, uncertainty, and editable outputs; 根据数据、主张、方法和不确定性审查科研图表。
---

# Figure Evidence Audit / 科研图表证据审查

**Maturity / 成熟度:** draft

## Purpose / 用途

帮助研究者在绘图前理解数据和研究问题，建立图表与主张、分析方法和来源之间的对应关系。Skill 不直接替用户制造结果，不把截图或草图当作分析输出。

This Skill links figures to data, claims, methods, uncertainty, and provenance. It must not fabricate results or treat screenshots and sketches as analytical outputs.

## Use and boundaries / 适用场景与边界

适用于论文图、汇报图、统计图、组学结果图和可编辑矢量图规划。它不能修正错误数据，不能替代统计分析，也不能仅凭图形外观判断因果关系或显著性。

## Required inputs / 必需输入

原始或已核验的数据表；变量定义、单位和分母；研究问题和目标主张；分析方法及其输出；样本量和不确定性；图形格式要求；引用和许可证信息。缺失信息必须标记。

## Workflow / 工作流程

1. 核对数据结构、变量、单位、分组和缺失值。
2. 明确每张图只服务于一个主要问题或主张。
3. 选择与数据类型和设计匹配的图形及统计摘要。
4. 记录变换、过滤、误差定义、统计标记和分母。
5. 输出可编辑格式和生成代码要求，保留分析过程记录。
6. 进行独立的数值、标签、图例、颜色和可读性审查。

## Output format / 输出格式

输出图表规格表：目的、数据、统计单位、分组、坐标轴和单位、误差或不确定性、统计方法、图注、来源、输出格式、待核验问题。另附主张—证据表和质量检查记录。

## Quality checks / 质量检查

不得把相关性写成因果关系；不得省略分母、样本量或不确定性；不得用批次校正展示矩阵替代正式模型输入；不得为了版式修改原始数据；检查图表是否可编辑、可读、可追溯。

## Limitations / 局限性

该 Skill 不能从截图、草图或图形外观恢复原始数据，也不能证明统计模型、测量质量或生物学机制正确。缺少数据和分析记录时，输出只能停留在核查计划和待补充字段。

This Skill cannot recover raw data from a screenshot, sketch, or visual appearance, and it cannot certify a statistical model, measurement quality, or biological mechanism. Without data and analysis records, limit the output to an audit plan and missing fields.

## Complete-input example / 完整输入示例

输入包含数据字典、已核验结果表、预设统计方法、样本量、误差定义和目标期刊格式。输出为图表规格、图注草稿和逐项核查清单。

## Incomplete-input example / 信息不足示例

输入只有一张截图和“请画得更好看”。输出应说明无法判断数据、单位、分组、样本量、统计方法和来源，只提出待补充清单，不生成新图或结论。

## Source / 来源

截图仅作为主题参考，来源、作者和许可证未能可靠核验；本文为仓库维护者独立整理。

## English

### Use and boundaries

Use this Skill for manuscript figures, presentation figures, statistical plots, omics figures, and editable vector figures. It cannot correct bad data, replace statistical analysis, or infer causality or significance from appearance.

### Required inputs and workflow

Provide raw or checked data, variable definitions, units and denominators, the research question and target claim, analytical methods and outputs, sample size and uncertainty, format requirements, citations, and license information. Check the data structure, define one main claim per figure, choose a compatible graphic, record transformations and annotations, specify editable output, and perform independent numerical and readability checks.

### Output and quality checks

Return a figure specification with purpose, data, statistical unit, groups, axes and units, uncertainty, method, caption, provenance, output format, open questions, a claim–evidence table, and a quality record. Do not turn association into causality, omit denominators or uncertainty, use a batch-corrected display matrix as model input, or alter raw data for layout.

### Complete-input example

Input: a data dictionary, checked result table, prespecified method, sample size, error definition, and journal format. Expected output: a figure specification, caption draft, claim–evidence links, and an itemized audit checklist.

### Incomplete-input example

Input: only a screenshot and “make it look better.” Expected handling: state that data, units, groups, sample size, method, and provenance cannot be determined; return missing fields and no new figure or conclusion.

### Source

The Skill was independently organized from the supplied screenshots. Authors, URLs, and licenses for the screenshot material were not reliably identifiable, and no screenshot text was copied.
