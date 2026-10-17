---
name: multi-agent-review
description: Coordinate role-based research review while preserving independent evidence checks and responsibility boundaries; 协调多角色科研审查并保留独立证据核验。
---
# Multi-agent Research Review / 多角色科研审查

**Maturity / 成熟度:** draft

## Use / 适用场景

适用于研究设计、分析计划、论文草稿和科研软件方案需要多个角度审查的情况。可使用研究设计、统计、代码、图表和写作等角色。

Use this Skill when a study design, analysis plan, manuscript, or research-software proposal needs several review perspectives. Possible roles include study design, statistics, code, figures, and writing.

## Boundaries / 边界

多个 Agent 的一致意见不等于事实，也不等于独立证据。角色不能共享未经核验的假设，汇总器不能替角色补写证据。最终判断必须回到原始数据、代码、文献和研究设计。

Agreement among agents is not a fact or independent evidence. Roles must not share unverified assumptions, and the synthesizer must not invent support for a role. Final judgments must return to raw data, code, literature, and study design.

## Required inputs / 必需输入

任务范围、已有材料、角色定义、每个角色的独立输入、输出格式、冲突处理规则和人工确认节点。缺失项写“待补充 / to be provided”。

Provide the scope, supplied materials, role definitions, independent inputs for each role, output format, conflict rules, and human confirmation points. Mark missing items as “待补充 / to be provided.”

## Workflow / 工作流程

1. 定义问题、证据边界和审查标准。
2. 为每个角色分配明确且不重复的任务。
3. 让角色独立记录证据、风险、不确定性和未执行检查。
4. 汇总共同意见，同时保留冲突和不同证据等级。
5. 检查角色是否越权、是否重复推测、是否出现虚构共识。
6. 由研究者确认行动清单，不把建议写成已完成。

1. Define the question, evidence boundary, and review criteria.
2. Assign explicit, non-overlapping tasks to each role.
3. Have each role record evidence, risks, uncertainty, and unexecuted checks independently.
4. Synthesize shared points while preserving conflicts and different evidence levels.
5. Check for role overreach, repeated speculation, and fabricated consensus.
6. Have the researcher confirm the action list; do not present suggestions as completed work.

## Output format / 输出格式

输出角色意见表、共同结论、分歧、证据链接、待核验事项、行动清单和人工确认记录。每条意见注明角色、证据、判断强度和是否执行过检查。

Return a role-opinion table, shared findings, disagreements, evidence links, items to verify, an action list, and human-confirmation notes. Label each opinion with its role, evidence, confidence, and execution status.

## Quality checks / 质量检查

- 角色是否使用了各自独立的材料和问题定义；
- 每条结论是否有证据或明确标为推测；
- 是否把一致意见误写成独立重复证据；
- 分歧是否保留，是否说明需要什么信息才能解决；
- 是否区分已检查、待核验和未执行步骤。

- Did each role use its assigned materials and question definition independently?
- Does each conclusion have evidence or an explicit speculation label?
- Was agreement incorrectly treated as replicated independent evidence?
- Are disagreements retained with the information needed to resolve them?
- Are checked, to-be-verified, and unexecuted steps separated?

## Limitations / 局限性

多角色审查不能替代真实数据分析、同行评议、伦理审查或领域专家判断。角色数量增加也不会自动提高证据质量，输入材料相同会产生相关而非独立的意见。

Multi-role review does not replace real-data analysis, peer review, ethics review, or domain expertise. More roles do not automatically improve evidence quality; shared inputs can produce correlated rather than independent opinions.

## Complete-input example / 完整输入示例

输入包含研究问题、分析计划、数据字典、代码审查范围、目标期刊要求和五个角色的独立任务。输出应逐条关联证据，并保留统计角色与写作角色之间的分歧。

The input contains the research question, analysis plan, data dictionary, code-review scope, journal requirements, and independent tasks for five roles. The output should link each finding to evidence and retain disagreements between, for example, statistics and writing roles.

## Incomplete-input example / 信息不足示例

输入只有一句“请让五个 Agent 判断这个方案是否可靠”。输出应先列出缺少的研究设计、数据、评价标准和角色边界，不能生成“多数 Agent 认为可靠”的结论。

If the only input is “ask five agents whether this plan is reliable,” list the missing design, data, evaluation criteria, and role boundaries first. Do not produce a conclusion that most agents found it reliable.

## Source / 来源

根据用户提供的多角色讨论截图和证据审查要求独立整理，未直接复制第三方宣传性表述。

This Skill was independently organized from the supplied multi-role discussion screenshots and evidence-review requirements. No third-party promotional wording was copied.
