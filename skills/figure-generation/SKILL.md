---
name: figure-generation
description: Specify reproducible research figures when real data and statistical results are supplied; 在已有真实数据和统计结果、需要制定科研图表规范时使用。
---

# Figure Generation / 科研绘图

**Status / 状态:** v0.1.0 draft

## Purpose / 用途

支持科研图表需求分析、图形规范制定和可编辑图形生成流程设计。它不能替代对原始数据、统计结果和图注的核对。

This Skill supports figure requirements, graphical specifications, and editable-figure workflows. It does not replace verification of raw data, statistical results, or captions.

## When to use / 适用场景

在已有真实数据字段、统计摘要和图形目标时使用。它适合制定可编辑图形规范、核对图注和规划导出检查，不适合凭空生成研究结果。

Use it when real data fields, statistical summaries, and a figure goal are available. It is suitable for editable-figure specifications, caption checks, and export planning, not for inventing results.

## Required inputs / 所需输入

请提供数据字段、统计结果、图形目的、目标读者、坐标单位、分组方式、误差定义、显著性标记和输出格式，例如 SVG、PDF、PNG 或 TIFF。

Provide the data fields, summaries, figure purpose, audience, units, grouping, error definition, significance notation, and output format such as SVG, PDF, PNG, or TIFF.

## Workflow / 工作流程

1. 明确图形要表达的比较、趋势或关系。
2. 检查数据字段、单位、样本量和统计摘要。
3. 选择与数据类型和研究问题匹配的图形类型。
4. 规定颜色、图例、坐标、误差线、显著性和图注。
5. 优先输出可编辑的图形方案或代码。
6. 列出数据核验、视觉核验和导出核验项目。

## Output format / 输出格式

输出包括图形目的、推荐图形类型、字段映射、视觉编码、统计标注、图注草稿、导出规格和核验清单。模型不能把示例数据冒充为真实结果。

Return the figure purpose, chart type, field mapping, visual encoding, statistical annotations, caption draft, export specification, and verification checklist. Example data must never be presented as real results.

## Quality checks / 质量检查

- 坐标轴是否包含名称和单位；
- 图例和颜色是否能区分分组；
- 误差线含义是否明确；
- 样本量和统计方法是否可追溯；
- 是否存在截断坐标或视觉编码误导；
- 导出后文字、分辨率和字体是否符合投稿要求。

## Limitations / 限制

生成的图形需要由研究者核对数据、统计结果和图注。模型不能保证图形符合所有期刊的版式要求。

Generated figures must be checked against the data, statistics, and captions. The Skill cannot guarantee compliance with every journal’s layout requirements.

## Examples / 示例

### Complete input / 完整输入

**Input / 输入:** 提供一个真实数据表的字段说明、分组变量、单位、已核对的统计摘要、误差定义、目标期刊图幅要求和输出格式。

**Expected handling / 预期处理:** 输出字段映射、图形类型、坐标与颜色规范、误差和统计标记定义、双语图注草稿，以及数据、视觉和导出核验清单。未提供的内容标记为“待补充 / to be provided”。

**Input / English:** A real data dictionary, grouping variable, units, checked statistical summaries, error definition, journal figure requirements, and output format are supplied.

**Expected handling / Expected output:** Return field mappings, chart type, axis and color rules, definitions for error bars and statistical annotations, a bilingual caption draft, and data, visual, and export checks. Mark missing items as “待补充 / to be provided.”

### Incomplete input / 信息不足

**Input / 输入:** 只有一张未标明单位和分组的截图，没有原始数据、误差定义或统计方法。

**Expected handling / 预期处理:** 不推断坐标含义、样本量或显著性。列出必须补充的字段、单位、分组、误差定义和统计来源，并把图形建议限定为待核查的结构方案。

**Input / English:** Only an image with no units or group labels is supplied; raw data, error definitions, and statistical methods are absent.

**Expected handling / Expected output:** Do not infer axes, sample size, or significance. List the required fields, units, groups, error definition, and statistical source, and limit the recommendation to a structure pending verification.

## Source / 来源

来源状态：来源于网络，自行整理汇总；当前未完成逐项作者、URL、许可证和版本核验。

Source status: collected from public online materials and independently reorganized; author, URL, license, and version have not yet been verified item by item.
