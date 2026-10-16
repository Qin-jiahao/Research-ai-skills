# Data-first Figure Workflow / 数据先行的科研绘图流程

## 中文

### 使用场景

在需要根据真实实验数据、统计输出和参考文献制作论文图、汇报图或机制图时使用。流程要求先理解数据，再决定图形和版式。

### 输入要求

请提供原始或处理后数据的位置、变量字典、统计单位、分组和样本量、分析代码或结果、研究问题、目标期刊或展示尺寸、引用文献，以及可编辑输出格式。截图不能替代数据文件。

### 输出要求

请按顺序输出：数据和分析输出摘要、每张图的主张与证据对应、字段到视觉元素的映射、图形类型和不确定性表示、图注草稿、可编辑输出方案、生成过程记录和核查清单。若生成代码或 SVG，必须同时给出可追溯的输入和版本信息。

### 禁止编造的内容

不要从截图猜测数值、样本量、P 值、效应量、显著性或因果关系。不要把生成的示意图写成实验结果，也不要把参考文献标题或期刊指标当作已核验事实。

### 信息不足时的处理方式

缺少数据、单位、误差定义或统计方法时，先输出待补充清单和条件化图形方案。不能直接生成看似真实的结果图。

### 双语示例

#### 中文输入

我有一个三组实验的均值和标准误，想做论文图，但没有提供每组样本量和统计检验方法。

#### 中文输出要点

可以先给出候选图形和字段映射，但样本量、误差定义和检验方法必须标为待补充。输出图注只能使用已提供的均值和标准误，不能添加显著性标记。

#### English input

I have means and standard errors for three experimental groups and want a manuscript figure, but the sample sizes and statistical test are missing.

#### English output points

A candidate figure and field mapping can be planned, but sample sizes, error definitions, and the test must remain unresolved. The caption may mention only the supplied means and standard errors and must not add significance marks.

### 来源说明

本 Prompt 综合了截图中“先理解数据和文献、再生成图、保留 SVG 和 Markdown 过程记录”的主题，并结合本仓库已有图表审查原则独立改写。来源说明：`来源于网络，自行整理汇总`。

## English

### Use case

Use this Prompt for manuscript figures, presentation figures, or mechanistic diagrams based on real data, statistical outputs, and reference sources. The workflow understands the data before choosing the visual form.

### Required inputs

Provide raw or processed data locations, a variable dictionary, statistical unit, groups and sample sizes, analysis code or outputs, research question, target journal or canvas size, cited sources, and an editable output format. A screenshot is not a data file.

### Expected output

Return a data and analysis summary, claim-to-evidence mapping for each figure, field-to-visual mapping, figure type and uncertainty plan, caption draft, editable-output plan, process record, and audit checklist. Generated code or SVG must retain traceable input and version information.

### Fabrication ban

Do not infer values, sample sizes, P values, effect sizes, significance, or causality from screenshots. Do not present a schematic as an experimental result.

### Missing information

When data, units, error definitions, or statistical methods are missing, return a missing-information list and a conditional figure plan. Do not produce a realistic-looking result figure.

### Bilingual example

The example above is bilingual and must lead to identical unresolved fields in both languages.

### Source note

This Prompt independently rewrites the screenshot themes of understanding data and literature first, generating editable figures, and keeping a Markdown process record. No screenshot values or wording were copied.
