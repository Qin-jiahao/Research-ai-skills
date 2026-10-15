---
name: paper-review
description: Review manuscript structure, methods, evidence, and wording when manuscript material is supplied; 在已有论文或章节材料、需要检查结构、方法、证据链和表述时使用。
---

# Paper Review / 论文审查

**Status / 状态:** v0.1.0 draft

## Purpose / 用途

检查论文的研究问题、方法、证据链、逻辑结构和表达问题。这个 Skill 用于提交前自查，不替代同行评审。

This Skill checks research questions, methods, evidence alignment, logical structure, and academic expression. It supports pre-submission review and does not replace peer review.

## Required inputs / 所需输入

全文或待审章节、研究问题、研究设计、统计方法、主要图表和目标期刊要求。没有全文时，应明确审查范围有限。

Provide the manuscript or target sections, research question, design, statistical methods, key figures, and journal requirements. If the full text is unavailable, state the limited review scope.

## When to use / 适用场景

在已有论文全文或明确章节、研究问题和审查目标时使用。它适合提交前检查证据链和表达，不替代数据复核或同行评审。

Use it when a manuscript or defined section, research question, and review target are available. It is suitable for pre-submission evidence and wording checks, not for data verification or peer review replacement.

## Review dimensions / 审查维度

1. 研究问题是否明确，假设是否可检验；
2. 方法是否能够回答研究问题；
3. 结果是否支持主张和结论；
4. 统计报告是否包含必要的效应量、不确定性和样本信息；
5. 图表、正文和补充材料是否一致；
6. 语言、结构和术语是否影响理解。

## Workflow / 工作流程

1. 提取研究问题、假设、方法、结果和结论。
2. 建立“主张—证据—结论”对应关系。
3. 标出证据不足、逻辑跳跃、过度解释和内部矛盾。
4. 按严重程度排序：Major、Moderate、Minor。
5. 为每个问题提供原文位置、理由和可执行修改建议。

## Output format / 输出格式

| Level / 程度 | Location / 位置 | Issue / 问题 | Evidence / 依据 | Action / 建议 |
|---|---|---|---|---|
| Major | Section or line |  |  |  |

最后输出总体判断：研究问题、方法、证据链和表达是否需要进一步修改，并列出作者必须补充的信息。

The overall assessment must state whether the research question, methods, evidence chain, or wording require further revision and list information the author must provide.

## Quality checks / 质量检查

- 每条 Major 或 Moderate 问题是否有可定位的原文位置和证据依据；
- 是否区分已检查、待补充和无法判断的内容；
- 是否把统计关联、探索性结果和因果结论分开；
- 是否检查样本量、效应量、不确定性、分母和多重检验报告；
- 是否避免把审查意见写成数据真实性或实验重复性的证明。

- Does each Major or Moderate issue have a locatable passage and evidence basis?
- Are checked, missing, and undetermined items separated?
- Are statistical associations, exploratory findings, and causal claims distinguished?
- Are sample size, effect size, uncertainty, denominators, and multiplicity reporting checked?
- Does the review avoid presenting its comments as proof of data authenticity or experimental replication?

## Limitations / 限制

审查结果取决于输入材料的完整性。这个 Skill 不能确认数据真实性、重复实验结果或期刊最终决定。

The review depends on the supplied material. It cannot verify data authenticity, reproduce experiments, or predict an editor’s final decision.

## Examples / 示例

### Complete input / 完整输入

**Input / 输入:** 提供全文、研究问题、研究设计、统计方法、主要图表和目标期刊要求，并指定需要重点检查主张与证据链。

**Expected handling / 预期处理:** 输出按 Major、Moderate、Minor 分级的问题表，逐条给出位置、证据、影响和修改建议，并单独列出待补充信息和总体判断。

**Input / English:** The full manuscript, research question, design, statistical methods, key figures, and journal requirements are supplied, with a focus on claim–evidence alignment.

**Expected handling / Expected output:** Return a Major/Moderate/Minor issue table with location, evidence, impact, and revision advice, followed by missing information and an overall assessment.

### Incomplete input / 信息不足

**Input / 输入:** 只有摘要和一张结果图，没有方法、原始统计信息或图表分母。

**Expected handling / 预期处理:** 将审查范围限定为摘要和图表表面一致性，不判断方法有效性或数据真实性；列出需要补充的设计、样本、统计和图注信息。

**Input / English:** Only an abstract and one result figure are supplied; methods, raw statistical details, and denominators are absent.

**Expected handling / Expected output:** Limit the review to surface consistency in the abstract and figure. Do not judge method validity or data authenticity; list the missing design, sample, statistical, and caption information.

## Source / 来源

来源状态：来源于网络，自行整理汇总；当前未完成逐项作者、URL、许可证和版本核验。

Source status: collected from public online materials and independently reorganized; author, URL, license, and version have not yet been verified item by item.
