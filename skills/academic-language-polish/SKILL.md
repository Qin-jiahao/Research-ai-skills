---
name: academic-language-polish
description: Improve naturalness and clarity of academic prose while preserving claims, terminology, evidence, and authorship; 在保留主张、术语和证据的前提下润色学术语言。
---
# Academic Language Polish / 学术语言润色

**Maturity / 成熟度:** draft

## Use / 适用场景

用于降低机器翻译感、拆分长句、统一术语、改善段落逻辑和保留学术语气。适合处理作者已经提供的论文段落、摘要、图注或审稿回复。

Use this Skill to improve naturalness, sentence structure, terminology consistency, and academic tone in supplied paragraphs, abstracts, figure captions, or responses to reviewers.

## Boundaries / 边界

不新增事实、文献、数据、因果关系或作者观点。不把“像人写的”当成正确性证明，也不模仿特定作者来规避署名或版权问题。术语含义、统计结果和引用关系发生变化时，必须标记并要求作者核对。

Do not add facts, references, data, causal relationships, or authorial opinions. Naturalness is not evidence of correctness. Do not imitate a named author to evade attribution or copyright. Flag any possible change to terminology, statistics, or citation meaning.

## Required inputs / 必需输入

原文、研究领域、目标读者、目标语言、保留术语、目标期刊或格式要求、允许的修改范围。没有提供的字段写“待补充 / to be provided”。

Provide the source text, field, audience, target language, terms to preserve, journal or style requirements, and allowed scope of edits. Mark absent fields as “待补充 / to be provided.”

## Workflow / 工作流程

1. 区分事实、主张、解释和作者立场。
2. 检查术语、指代、时态、逻辑关系和证据边界。
3. 先做不改变含义的句法和用词调整，再处理段落衔接。
4. 对可能改变含义的句子提供替代版本，并保留作者确认项。
5. 将无法从原文判断的事实或引用单独列出。

1. Separate facts, claims, interpretations, and authorial positions.
2. Check terminology, references, tense, logical relations, and evidence boundaries.
3. Make meaning-preserving sentence and word-level edits before changing paragraph transitions.
4. Provide alternatives for wording that could change meaning and keep author-confirmation items.
5. List facts or citations that cannot be judged from the source text.

## Output format / 输出格式

返回修改稿、关键修改理由、术语变化表、主张变化警告、待作者确认项和未执行的核验步骤。保留原始数字、统计结果和引用标识。

Return the revised text, key reasons, a terminology-change table, claim-change warnings, author-confirmation items, and unexecuted checks. Preserve original numbers, statistical results, and citation markers.

## Quality checks / 质量检查

- 每个数字、单位、P 值、区间和引用是否与原文一致；
- 是否把相关性、预测或假设改成因果结论；
- 是否保留限定词、样本范围和不确定性；
- 中英文术语是否一一对应；
- 修改理由是否能回到原文位置；
- 未核验的事实是否明确标记。

- Are numbers, units, p-values, intervals, and citations unchanged?
- Has association, prediction, or hypothesis been turned into causality?
- Are qualifiers, sample scope, and uncertainty preserved?
- Do Chinese and English terms correspond consistently?
- Can every rationale be traced to a source location?
- Are unverified facts explicitly marked?

## Limitations / 局限性

该 Skill 不能判断实验是否真实、统计方法是否正确或引用是否完整。它只能在提供的文本和约束内修改表达。专业术语、语言变体和期刊要求仍需作者或领域专家复核。

This Skill cannot establish whether an experiment is real, a statistical method is correct, or citations are complete. It edits expression within supplied text and constraints. Authors or domain experts must review specialized terminology, language variants, and journal requirements.

## Complete-input example / 完整输入示例

输入包含一段英文结果描述、原始统计数值、目标期刊的语言要求、需保留的术语表和允许的改写范围。输出包含修改稿、逐项理由和一份确认清单，不改变数值或结论强度。

The input contains an English results paragraph, original statistics, journal style requirements, a terminology list, and an allowed edit scope. The output contains a revision, itemized reasons, and a confirmation checklist without changing numbers or claim strength.

## Incomplete-input example / 信息不足示例

输入只有一句“把这段写得更像人”。输出应先要求提供原文、目标语言、读者和不可改变的事实；在这些信息补齐前，只能给出通用检查项，不能重写成新的研究结论。

If the only input is “make this sound more human,” request the source text, target language, audience, and non-negotiable facts first. Until they are supplied, return only a general checklist and do not create a new research conclusion.

## Source / 来源

根据用户提供的 humanizer 类截图和科研写作约束独立整理，未复制第三方原文或宣传语。具体外部项目见 [`docs/external-projects.md`](../../docs/external-projects.md)。

This Skill was independently organized from the supplied humanizer-related screenshots and research-writing constraints. No third-party text or promotional copy was copied. External project leads are listed in [`docs/external-projects.md`](../../docs/external-projects.md).
