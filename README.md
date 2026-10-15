# Research AI Skills

## 中文

`Research-ai-skills` 是一个面向科研工作的 AI Skills 与 Prompt 集合，覆盖论文写作、文献分析、统计分析、科研绘图、转录组分析、科研代码和科研汇报。

项目地址：[github.com/Qin-jiahao/Research-ai-skills](https://github.com/Qin-jiahao/Research-ai-skills)

已发布内容会在发布前经过整理、改写和检查。当前未发布的工作区改动仍需完成来源核验和行为评估。网络截图和其他公开材料只作为参考来源，不直接作为最终内容发布。

### 项目结构

```text
Research-ai-skills/
├── skills/       # 复杂的、多步骤科研工作流
├── prompts/      # 单个任务或短流程提示词
├── docs/         # 设计原则、兼容性和限制说明
└── tests/        # Skill 和 Prompt 的检查清单
```

Skills 索引见 [`skills/README.md`](skills/README.md)，Prompts 索引见 [`prompts/README.md`](prompts/README.md)。兼容性说明见 [`docs/compatibility.md`](docs/compatibility.md)。

### 当前收录的 Skills

当前收录以下 Skills。各文件和变更日志中的状态用于区分已发布内容与未发布草稿。

- `academic-writing`：论文段落和章节写作
- `paper-review`：论文结构、方法和论证检查
- `literature-analysis`：文献检索、筛选和证据整理
- `statistical-analysis`：统计方法选择和结果解释
- `figure-generation`：科研图表设计和生成规范
- `rnaseq-analysis`：bulk RNA-seq 分析规划、质量控制和结果审查
- `research-coding`：科研代码整理、可复现性和代码审查
- `research-presentation`：科研汇报的故事线、逐页结构和证据核查
- `scientific-interface-design`：科研软件界面和交互设计
- `academic-language-polish`：保留科学含义的学术语言润色
- `agent-memory-handoff`：跨会话项目记忆和任务交接
- `multi-agent-review`：多角色科研审查和分歧记录

后续内容会根据实际测试和使用反馈继续扩展。

### 安装与使用

安装说明见 [`docs/installation.md`](docs/installation.md)。正式发布和草稿状态见 [`docs/resource-status.md`](docs/resource-status.md)。

### 使用原则

- 使用前应提供足够的研究背景、数据说明和任务目标。
- 模型不得凭空生成数据、文献、统计结果或实验结论。
- 输入信息不足时，Skill 应先指出缺失信息和可能影响。
- 科研分析结果需要由研究者结合原始数据和方法学判断进行核验。
- 每个 Skill 都应说明适用场景、输入要求、输出格式和限制。

### 许可证与来源

本仓库中的原创内容将使用仓库根目录声明的许可证。已知来源的材料会保留原作者、原项目和许可证信息。来源不明确的材料只作为参考，并标注“来源于网络，自行整理汇总”，不会直接复制原文。

## English

`Research-ai-skills` is a collection of AI Skills and Prompts for research work. It covers academic writing, literature analysis, statistics, research figures, transcriptomics, research code, and scientific presentations.

Project repository: [github.com/Qin-jiahao/Research-ai-skills](https://github.com/Qin-jiahao/Research-ai-skills)

Published materials are reorganized, rewritten, and checked before release. Unreleased working-tree changes still require provenance review and behavioral evaluation. Screenshots and other public materials are treated as references only and are not copied directly as final content.

### Repository structure

```text
Research-ai-skills/
├── skills/       # Complex, multi-step research workflows
├── prompts/      # Prompts for single tasks or short workflows
├── docs/         # Design principles, compatibility, and limitations
└── tests/        # Checklists for evaluating Skills and Prompts
```

See [`skills/README.md`](skills/README.md) for the Skill index, [`prompts/README.md`](prompts/README.md) for the Prompt index, and [`docs/compatibility.md`](docs/compatibility.md) for platform notes.

### Skills currently included

The repository currently includes the following Skills. Each file and the changelog records whether content is released or still under evaluation.

- `academic-writing`: writing research paragraphs and sections
- `paper-review`: checking structure, methods, and reasoning
- `literature-analysis`: searching, screening, and organizing evidence
- `statistical-analysis`: choosing methods and interpreting results
- `figure-generation`: specifications for research figures and charts
- `rnaseq-analysis`: planning, quality control, and auditing bulk RNA-seq workflows
- `research-coding`: organizing research code and checking reproducibility
- `research-presentation`: storylines, slide structures, and claim-evidence checks

Future additions will follow actual testing and usage feedback.

### Installation and use

See [`docs/installation.md`](docs/installation.md) for installation instructions and [`docs/resource-status.md`](docs/resource-status.md) for release status.

### Usage principles

- Provide sufficient research context, data description, and task objectives.
- Do not fabricate data, references, statistical results, or experimental conclusions.
- When required information is missing, identify the missing information and its possible impact first.
- Researchers must verify analytical results against the original data and methods.
- Every Skill should document its use cases, required inputs, output format, and limitations.

### License and attribution

Original content in this repository will be released under the license declared at the repository root. Materials with known sources will retain the original author, project, and license information. Materials with unclear provenance will be marked as “Source: online materials, independently organized and summarized” and will not be copied verbatim.

## Resource catalog

The complete bilingual R01–R31 inventory is in [`catalog/resources.json`](catalog/resources.json), with definitions in [`catalog/README.md`](catalog/README.md). Coverage and test boundaries are documented in [`tests/resource-coverage.md`](tests/resource-coverage.md).

The local installer is `scripts/install_skill.py`. It copies one local Skill to a user-selected destination and refuses to overwrite an existing directory unless `--force` is provided.
