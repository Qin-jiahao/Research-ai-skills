# Five-perspective Research Review / 五视角科研审查

## 中文

### 使用场景

在研究问题、分析计划、论文草稿或科研软件方案需要多角度审查时使用。五个角色用于暴露不同风险，不代表五个独立实验或五个独立证据来源。

### 输入要求

请提供待审材料、研究目标、已有证据、约束、决策标准和允许的修改范围。没有材料时，只能给出审查框架。

### 输出要求

分别让以下角色给出基于材料的意见：

1. 反对者：寻找最强反例、混杂和不可支持的主张；
2. 本质思考者：检查问题定义、必要条件和逻辑链；
3. 机会挖掘者：指出可检验的替代解释或改进方向；
4. 局外人：检查读者是否能理解术语、范围和限制；
5. 执行者：把已确认的改动转成可验收步骤。

最后输出证据矩阵、角色间分歧、优先级、条件化决定和下一步。每条意见都要标注材料中的位置或说明“没有直接证据”。

### 禁止编造的内容

角色不能互相制造证据，不能把多数意见写成事实，不能补写数据、文献、运行结果或用户批准。不同角色的相同猜测仍然只是猜测。

### 信息不足时的处理方式

先列出无法审查的部分和需要补充的材料。执行者不得在证据矩阵为空时提出“已完成”的结论。

### 双语示例

#### 中文输入

请审查一个关于三组细胞处理实验的分析计划。计划没有给出随机化、批次和主要结局。

#### 中文输出要点

反对者会标记批次混杂风险，本质思考者会要求明确分析单位和主要结局，机会挖掘者会提出分层或敏感性分析，局外人会指出术语缺少定义，执行者会把这些缺口转成补充字段和验收步骤。最终决定应保持条件化。

#### English input

Review an analysis plan for a three-group cell-treatment experiment. Randomization, batch information, and the primary outcome are missing.

#### English output points

The critic should flag batch confounding; the first-principles reviewer should request the analysis unit and primary outcome; the opportunity reviewer can suggest stratification or sensitivity analysis; the outsider should identify undefined terms; and the executor should convert the gaps into fields and acceptance checks. The decision must remain conditional.

### 来源说明

本 Prompt 独立改写了截图中“五个不同角度的顾问互相讨论”的主题，并加入科研证据和责任边界。截图来源不明，未复制原文。

## English

### Use case

Use this Prompt when a research question, analysis plan, manuscript draft, or scientific-software proposal needs independent perspectives. The roles expose different risks; they are not independent experiments or independent evidence sources.

### Required inputs

Provide the material, research goal, available evidence, constraints, decision criteria, and allowed scope of change. Without the material, return only the review framework.

### Expected output

Ask a critic, first-principles reviewer, opportunity reviewer, outsider, and executor to review the same material. Then return an evidence matrix, disagreements, priorities, conditional decision, and next steps. Each comment must cite a location or state that direct evidence is absent.

### Fabrication ban

Roles must not create evidence for one another. Agreement is not a fact, and no data, references, execution results, or approvals may be invented.

### Missing information

List unreviewable parts and required material first. The executor must not report completion when the evidence matrix is empty.

### Bilingual example

The example above is bilingual and must preserve the same missing fields and conditional decision in both languages.

### Source note

This Prompt is an independent rewrite of the five-advisor discussion theme shown in the screenshots, with added research evidence and responsibility boundaries.
