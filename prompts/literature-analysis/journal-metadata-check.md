# Journal and Paper Metadata Check / 期刊与论文元数据核验

## 中文

### 使用场景

在整理论文首页、期刊名称、作者、DOI、年份、机构、摘要或期刊指标时使用。这个 Prompt 只整理可核验的元数据，不把自动提取当作事实证明。

### 输入要求

请提供 DOI、文章链接、PDF、数据库记录或明确的检索范围，并说明指标名称、来源数据库和截止日期。影响因子、分区和排名必须带来源年份。

### 输出要求

输出字段、原始来源、访问日期、提取结果、核验状态和冲突记录。对文章标题可以同时给出原文和翻译，但翻译必须标为译文。对缺少来源的字段写“待核验”。

### 禁止编造的内容

不得编造 DOI、作者、机构、期刊指标、文章标题、摘要或引用次数。不同数据库的指标不能混写，也不能用截图中的数值代替正式来源。

### 信息不足时的处理方式

先列出缺少的识别信息。只有模糊标题时，可以给出检索式和候选记录，不能选定一条作为真实记录。

### 双语示例

#### 中文输入

我只有一张论文首页截图，想知道文章标题、期刊和影响因子。

#### 中文输出要点

截图可以帮助提取候选标题和期刊名，但 DOI、作者和影响因子仍待核验。下一步应使用 DOI、期刊官网或指定数据库检索，并记录访问日期和指标年份。

#### English input

I only have a screenshot of a paper's first page and want its title, journal, and impact factor.

#### English output points

The screenshot can provide candidate title and journal fields, but the DOI, authors, and impact factor remain unverified. Use the DOI, the journal website, or a named database and record the access date and metric year.

### 来源说明

本 Prompt 根据截图中“自动列出期刊名称、影响因子和中英文标题”的主题独立改写。动态指标必须回到官方期刊页面或明确的数据库来源，截图不构成来源证明。

## English

### Use case

Use this Prompt to organize paper-page metadata, journal names, authors, DOIs, dates, affiliations, abstracts, or journal metrics. Extraction is not treated as proof.

### Required inputs

Provide a DOI, article URL, PDF, database record, or explicit search scope. For metrics, provide the metric name, source database, and cutoff date. Impact factors, quartiles, and rankings must include the metric year.

### Expected output

Return fields, original sources, access dates, extracted values, verification states, and conflicts. A translated title must be labeled as a translation. Missing sources must be marked for verification.

### Fabrication ban

Do not invent DOIs, authors, affiliations, metrics, titles, abstracts, or citation counts. Do not use screenshot numbers as a substitute for a formal source.

### Missing information

List missing identifiers first. With only an ambiguous title, provide search queries and candidate records without selecting one as fact.

### Bilingual example

The example above is bilingual and must preserve the same uncertainty labels in both languages.

### Source note

This Prompt independently rewrites the screenshot theme of extracting journal metadata and bilingual titles. Dynamic metrics must be checked against an official journal page or a named database.
