# Statistical Method Comparison / 统计方法比较

## 中文

根据给出的研究设计和数据结构，比较可行的统计方法。请按表格输出：方法、适用条件、关键假设、优点、风险、需要的诊断和结果报告要求。

请先指出输入中缺失的关键信息，再给出条件化建议。不要在没有原始数据和完整设计的情况下生成 P 值、效应量或显著性结论，也不要把相关性表述为因果关系。

## English

Compare plausible statistical methods for the study design and data structure provided below. Use a table with method, applicability, key assumptions, strengths, risks, diagnostics, and reporting requirements.

Identify missing critical information before making conditional recommendations. Do not generate p-values, effect sizes, or significance claims without the original data and complete design. Do not describe association as causation.

## Prompt contract / 提示词契约

### 中文

- **使用场景：** 根据研究设计和数据结构比较可行的统计方法。
- **输入要求：** 研究问题、分析单位、结局类型、组别或协变量、重复结构、样本量、缺失值和测量时间点。
- **输出要求：** 方法比较表、关键假设、诊断、风险、报告要求和条件化选择理由。
- **禁止编造：** 不得生成 P 值、效应量、显著性或因果结论，不得把相关性写成因果关系。
- **信息不足：** 先列出影响模型选择的缺失字段，暂停确定性推荐。
- **双语示例：** 完整输入含配对结构和结局分布，输出候选模型和诊断；信息不足时只有“两组比较”，输出待补充设计字段。

### English

- **Use case:** Compare plausible statistical methods from a supplied design and data structure.
- **Required inputs:** Question, unit of analysis, outcome type, groups or covariates, replicate structure, sample size, missingness, and time points.
- **Expected output:** A method table, assumptions, diagnostics, risks, reporting requirements, and conditional rationale.
- **Fabrication ban:** Do not generate p-values, effect sizes, significance, or causal claims, and do not turn association into causation.
- **Missing information:** List design fields that affect model choice before giving any definitive recommendation.
- **Bilingual example:** With paired structure and outcome distribution, return candidate models and diagnostics; with only “compare two groups,” return missing design fields.

## Source / 来源

来源于网络和用户提供的统计分析材料，自行整理汇总；不代表已经对真实数据运行模型。

Source: online materials and user-provided statistical-analysis material, independently organized. It does not indicate that a model was run on real data.
