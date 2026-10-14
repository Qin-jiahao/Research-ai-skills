# Research AI Skills

## 中文

`Research-ai-skills` 是一个面向科研工作的 AI Skills 与 Prompt 集合，重点覆盖论文写作、文献分析、科研数据处理、科研绘图和科研编程。

项目地址：[github.com/Qin-jiahao/Research-ai-skills](https://github.com/Qin-jiahao/Research-ai-skills)

本项目的内容会经过重新整理、改写和测试。网络截图和其他公开材料只作为参考来源，不直接作为最终内容发布。

### 项目结构

```text
Research-ai-skills/
├── skills/       # 复杂的、多步骤科研工作流
├── prompts/      # 单个任务或短流程提示词
├── docs/         # 设计原则、兼容性和限制说明
└── tests/        # Skill 和 Prompt 的检查清单
```

Skills 索引见 [`skills/README.md`](skills/README.md)，Prompts 索引见 [`prompts/README.md`](prompts/README.md)。兼容性说明见 [`docs/compatibility.md`](docs/compatibility.md)。

### 当前规划

第一阶段计划建设以下 Skills：

- `academic-writing`：论文段落和章节写作
- `paper-review`：论文结构、方法和论证检查
- `literature-analysis`：文献检索、筛选和证据整理
- `statistical-analysis`：统计方法选择和结果解释
- `figure-generation`：科研图表设计和生成规范

后续会根据测试结果加入 RNA-seq 分析、科研编程和研究汇报等内容。

### 使用原则

- 使用前应提供足够的研究背景、数据说明和任务目标。
- 模型不得凭空生成数据、文献、统计结果或实验结论。
- 输入信息不足时，Skill 应先指出缺失信息和可能影响。
- 科研分析结果需要由研究者结合原始数据和方法学判断进行核验。
- 每个 Skill 都应说明适用场景、输入要求、输出格式和限制。

### 许可证与来源

本仓库中的原创内容将使用仓库根目录声明的许可证。已知来源的材料会保留原作者、原项目和许可证信息。来源不明确的材料只作为参考，并标注“来源于网络，自行整理汇总”，不会直接复制原文。

## English

`Research-ai-skills` is a collection of AI Skills and Prompts for research work. It focuses on academic writing, literature analysis, scientific data processing, research visualization, and research coding.

Project repository: [github.com/Qin-jiahao/Research-ai-skills](https://github.com/Qin-jiahao/Research-ai-skills)

The materials in this repository are reorganized, rewritten, and tested before publication. Screenshots and other public materials are treated as references only and are not copied directly as final content.

### Repository structure

```text
Research-ai-skills/
├── skills/       # Complex, multi-step research workflows
├── prompts/      # Prompts for single tasks or short workflows
├── docs/         # Design principles, compatibility, and limitations
└── tests/        # Checklists for evaluating Skills and Prompts
```

See [`skills/README.md`](skills/README.md) for the Skill index, [`prompts/README.md`](prompts/README.md) for the Prompt index, and [`docs/compatibility.md`](docs/compatibility.md) for platform notes.

### Current roadmap

The first phase will focus on:

- `academic-writing`: writing research paragraphs and sections
- `paper-review`: checking structure, methods, and reasoning
- `literature-analysis`: searching, screening, and organizing evidence
- `statistical-analysis`: choosing methods and interpreting results
- `figure-generation`: specifications for research figures and charts

RNA-seq analysis, research coding, and research presentation workflows may be added after further testing.

### Usage principles

- Provide sufficient research context, data description, and task objectives.
- Do not fabricate data, references, statistical results, or experimental conclusions.
- When required information is missing, identify the missing information and its possible impact first.
- Researchers must verify analytical results against the original data and methods.
- Every Skill should document its use cases, required inputs, output format, and limitations.

### License and attribution

Original content in this repository will be released under the license declared at the repository root. Materials with known sources will retain the original author, project, and license information. Materials with unclear provenance will be marked as “Source: online materials, independently organized and summarized” and will not be copied verbatim.
