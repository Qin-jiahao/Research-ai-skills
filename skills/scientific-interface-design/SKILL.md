---
name: scientific-interface-design
description: Plan research-software interfaces around scientific tasks, data provenance, accessibility, and inspectable outputs; 面向科研软件设计任务、数据来源和可检查输出规划界面。
---
# Scientific Interface Design / 科研软件界面设计

**Maturity / 成熟度:** draft

## Use / 适用场景

用于科研分析工具、数据浏览器、图表生成器和实验记录界面的需求拆解、原型规划与评审。

Use this Skill to scope, prototype, and review interfaces for research-analysis tools, data browsers, figure generators, and experiment records.

## Boundaries / 边界

不把 Apple 风格或视觉偏好当作科学质量。不改变原始数据来适应界面，不隐藏参数、失败状态、数据来源或不确定性。没有真实用户测试时，只能提出原型级建议。

Do not treat an Apple-like style or visual preference as scientific quality. Do not alter raw data to fit an interface or hide parameters, failures, provenance, or uncertainty. Without user testing, provide prototype-level suggestions only.

## Required inputs / 必需输入

用户任务、数据对象、输入输出、错误状态、权限、可访问性要求、目标平台、可编辑或可导出格式、已知约束。缺失项写“待补充 / to be provided”。

Provide user tasks, data objects, inputs and outputs, error states, permissions, accessibility requirements, target platform, editable or export formats, and known constraints. Mark missing items as “待补充 / to be provided.”

## Workflow / 工作流程

1. 定义用户任务、分析单位和不可隐藏的证据。
2. 绘制任务流、状态图和异常路径。
3. 定义数据契约、控件、校验、权限和日志。
4. 设计空状态、失败状态、撤销和导出行为。
5. 输出页面结构、交互说明、数据来源、可访问性清单和待测试假设。

1. Define user tasks, analytical units, and evidence that must remain visible.
2. Map task flows, states, and failure paths.
3. Define data contracts, controls, validation, permissions, and logs.
4. Design empty states, failure states, undo behavior, and export behavior.
5. Return page structure, interaction notes, provenance, an accessibility checklist, and hypotheses to test.

## Output format / 输出格式

输出任务流、状态图、页面结构、数据契约、控件与校验、错误和空状态、来源展示、可访问性清单及待测试假设。

Return the task flow, state map, page structure, data contract, controls and validation, error and empty states, provenance display, accessibility checklist, and hypotheses to test.

## Quality checks / 质量检查

- 用户能否看出数据来源、版本、单位和处理状态；
- 错误、缺失数据和权限不足是否可理解并可恢复；
- 图表和表格是否保留可编辑输出、单位和不确定性；
- 键盘操作、颜色对比、文字替代和目标观看距离是否有检查；
- 界面是否把建议、计算结果和已核验事实分开。

- Can users see data provenance, version, units, and processing state?
- Are errors, missing data, and permission failures understandable and recoverable?
- Do figures and tables preserve editable output, units, and uncertainty?
- Were keyboard access, color contrast, text alternatives, and viewing distance checked?
- Does the interface separate suggestions, computed results, and verified facts?

## Limitations / 局限性

界面规划不能证明分析方法正确、数据质量合格或用户一定能理解结果。视觉风格不能替代可用性测试、领域审查、隐私评估和安全审计。

Interface planning cannot establish that an analysis method is correct, data quality is adequate, or users will understand results. Visual style cannot replace usability testing, domain review, privacy assessment, or security audit.

## Complete-input example / 完整输入示例

输入包含一个 RNA-seq 结果浏览器的用户任务、数据字段、权限角色、失败状态、目标屏幕和导出格式。输出应给出状态图、字段到界面元素的映射、错误提示和可访问性检查项。

The input contains user tasks for an RNA-seq results browser, data fields, permission roles, failure states, target screens, and export formats. The output should include a state map, field-to-interface mapping, error messages, and accessibility checks.

## Incomplete-input example / 信息不足示例

输入只有一张“更好看”的界面截图。输出应说明无法判断数据、用户任务、权限、错误状态和验收标准，只提出待补充问题，不宣称界面已经可用。

If the only input is a screenshot described as “make it look better,” state that data, user tasks, permissions, error states, and acceptance criteria cannot be judged. Ask for those fields and do not claim usability.

## Source / 来源

根据用户提供的 Anatomy、界面设计和科研绘图截图独立整理；具体项目和设计作者按 [`docs/external-projects.md`](../../docs/external-projects.md) 单独核验。

This Skill was independently organized from the supplied Anatomy, interface-design, and research-figure screenshots. Specific projects and authors are tracked separately in [`docs/external-projects.md`](../../docs/external-projects.md).
