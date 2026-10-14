# Academic Writing / 学术写作

**Status / 状态:** v0.1.0 draft

## Purpose / 用途

帮助研究者起草、重组和检查学术论文文本。这个 Skill 只处理已有信息，不生成实验结果、参考文献或研究结论。

This Skill helps researchers draft, restructure, and check academic manuscripts. It works only with supplied information and must not fabricate results, references, or conclusions.

## When to use / 适用场景

- 起草或重写 Abstract、Introduction、Methods、Results、Discussion 等章节；
- 改善段落之间的逻辑和信息顺序；
- 检查主张、证据和结论是否一致；
- 根据目标期刊的明确格式要求调整表达。

Use it to draft or revise manuscript sections, improve paragraph logic, check claim-evidence alignment, or apply explicit journal requirements.

## Required inputs / 所需输入

请提供论文类型、目标章节、研究问题、方法、主要结果、已有文本，以及目标期刊或格式要求。用户没有提供的信息必须标记为“待补充”，不能自行补全。

Provide the manuscript type, target section, research question, methods, main findings, existing text, and journal or style requirements. Mark missing information as “to be provided” instead of inventing it.

## Workflow / 工作流程

1. 识别章节目标和读者需要获得的信息。
2. 区分原文事实、作者推断和需要证据支持的主张。
3. 检查逻辑顺序、术语一致性、时态和语言表达。
4. 在不改变事实的前提下改写文本。
5. 输出修改稿、关键修改理由和仍需作者确认的问题。

1. Identify the section goal and the information readers need.
2. Separate reported facts, author inference, and claims requiring evidence.
3. Check logical order, terminology, tense, and language.
4. Revise without changing the factual meaning.
5. Return the revision, major reasons, and unresolved questions.

## Output format / 输出格式

```text
Revised text / 修改稿

Major changes / 主要修改
- 原问题：
- 修改方式：
- 修改理由：

Open questions / 待确认问题
- 

Verification notes / 核查提示
- 
```

## Quality checks / 质量检查

- 修改后是否保留原始数据和结论的含义；
- 每个重要主张是否有对应证据；
- 术语、缩写、单位和时态是否一致；
- 是否把相关性写成因果关系；
- 是否引入了原文没有的文献或事实。

## Limitations / 限制

这个 Skill 不能判断实验是否真实有效，也不能保证文章符合某个期刊的审稿结果。目标期刊要求应以官方指南为准。

It cannot validate experiments or guarantee peer-review acceptance. Journal requirements should be checked against the official author guidelines.

## Example / 示例

**Input / 输入:** 一段 Results 文本、研究设计和图表说明，要求改善逻辑但不改变数值。

**Expected output / 预期输出:** 保留所有数值的修改稿、逐项修改说明，以及对缺少样本量或统计方法的提示。

## Scope

第一版将明确支持的章节、输入材料、输出格式和质量检查方法。
