# Statistical Analysis / 统计分析

**Status / 状态:** v0.1.0 draft

## Purpose / 用途

根据研究设计和数据类型辅助选择统计方法，并检查结果解释。它不能仅凭一张结果表断定因果关系或统计有效性。

This Skill assists with method selection and result interpretation based on study design and data type. It cannot infer causality or validity from a result table alone.

## Required inputs / 所需输入

研究设计、分析单位、变量类型、样本量、分组和配对关系、缺失值、批次因素、预设假设、主要结局和分析目标。还应提供数据字典或示例数据结构。

Provide the study design, unit of analysis, variable types, sample size, grouping and pairing, missingness, batch factors, prespecified hypotheses, primary outcomes, goals, and a data dictionary or sample structure.

## Workflow / 工作流程

1. 检查数据结构、研究设计和分析单位是否匹配。
2. 明确估计目标、比较对象和统计假设。
3. 评估分布、独立性、方差结构、缺失机制和多重比较问题。
4. 比较可行方法及其前提条件，说明选择理由。
5. 规定诊断检查、效应量、置信区间和敏感性分析。
6. 输出可复现的分析计划，不直接替用户编造数值结果。

## Output format / 输出格式

输出包括：数据与设计检查、候选方法比较、推荐分析方案、假设诊断、效应量和不确定性报告要求，以及需要研究者确认的风险点。

Return the design-data check, candidate-method comparison, recommended analysis plan, assumption diagnostics, effect-size and uncertainty requirements, and unresolved risks.

## Quality checks / 质量检查

- 分析单位是否与研究设计一致；
- 样本量是否足以支持模型复杂度；
- 是否把统计显著性等同于实际重要性；
- 是否报告效应量和不确定性；
- 是否处理多重比较和缺失数据；
- 是否避免在观察性数据中直接使用因果表述。

## Limitations / 限制

统计建议依赖研究设计和数据质量。这个 Skill 不能替代统计专家、预注册分析计划或原始数据诊断。

Statistical recommendations depend on design and data quality. This Skill does not replace a statistician, a preregistered analysis plan, or diagnostics on the original data.
