# Requirements Before Implementation / 编码或分析前的需求文档

## 中文

### 使用场景

在开始科研软件开发、分析流程整理或较大范围的仓库修改前使用。这个 Prompt 先把目标、范围、输入输出、阶段和验收标准写清楚，再决定是否执行。

### 输入要求

请提供任务目标、目标用户、已有仓库或脚本、数据和文件位置、运行环境、时间限制、不可改变的约束、允许的外部依赖，以及谁负责最终确认。若某项未知，请明确写“待补充”。

### 输出要求

请按以下顺序输出：

1. 已提供事实、工作假设和信息缺口；
2. 问题定义和不在范围内的内容；
3. 输入输出契约和目录或文件边界；
4. 分阶段路线图，每阶段包含目标、前置条件、产物和验收标准；
5. 风险、回滚点、需要用户确认的决策；
6. 第一阶段可以执行的最小任务。

### 禁止编造的内容

不要编造样本量、数据质量、完成状态、测试结果、性能提升、文献、许可证或用户已经同意的事项。计划中的动词不能写成已经完成的结果。

### 信息不足时的处理方式

先列出缺失字段和它们对方案的影响。缺少会改变技术路线或研究结论的字段时，暂停相关执行步骤，只给出条件化方案。

### 双语示例

#### 中文输入

我想把一个用于 bulk RNA-seq 结果整理的脚本改成可复用项目，但还没有确定输入文件格式，也没有运行记录。

#### 中文输出要点

已知事实是目标为复用脚本。输入格式和运行记录待补充。第一阶段只定义样本元数据、计数矩阵、设计矩阵和输出报告的字段，不声称流程已经可复现。验收标准包括一个最小公开数据示例、环境记录和一次有日志的完整运行。

#### English input

I want to turn a bulk RNA-seq reporting script into a reusable project, but the input format and execution record are not defined yet.

#### English output points

The goal is known, while the input contract and execution evidence are missing. The first phase should define the metadata, count-matrix, design-matrix, and report fields. It must not claim reproducibility until a public test dataset, environment record, and logged run are available.

### 来源说明

本 Prompt 是根据用户截图中“先写 PRD、路线图和验收标准”的主题独立改写而成。截图来源不明，未复制原文。来源说明：`来源于网络，自行整理汇总`。

## English

### Use case

Use this Prompt before starting research-software development, reorganizing an analysis workflow, or making a broad repository change. It defines the goal, scope, inputs, stages, and acceptance checks before execution.

### Required inputs

Provide the goal, intended users, existing repository or scripts, data and file locations, runtime environment, time limits, immutable constraints, allowed external dependencies, and the person responsible for final confirmation. Mark unknown fields as “to be supplied.”

### Expected output

Return supplied facts, working assumptions, information gaps, scope boundaries, input/output contracts, a staged roadmap, risks, rollback points, confirmation gates, and the smallest executable first task.

### Fabrication ban

Do not invent sample sizes, data quality, completion status, test results, performance gains, references, licenses, or approvals. Planned actions must not be reported as completed results.

### Missing information

List each missing field and its impact first. Pause execution steps that depend on a missing field that could change the technical route or research conclusion.

### Bilingual example

The Chinese and English example above must lead to the same conditional plan and the same evidence boundary.

### Source note

This Prompt is an independent rewrite of the “write a PRD, roadmap, and acceptance checks before coding” theme found in the supplied screenshots. The screenshot source is unclear, so it is marked as independently organized online material.
