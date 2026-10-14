# Figure Generation / 科研绘图

**Status / 状态:** v0.1.0 draft

## Purpose / 用途

支持科研图表需求分析、图形规范制定和可编辑图形生成流程设计。它不能替代对原始数据、统计结果和图注的核对。

This Skill supports figure requirements, graphical specifications, and editable-figure workflows. It does not replace verification of raw data, statistical results, or captions.

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
