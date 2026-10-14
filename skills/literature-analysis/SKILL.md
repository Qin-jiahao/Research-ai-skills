# Literature Analysis / 文献分析

**Status / 状态:** v0.1.0 draft

## Purpose / 用途

支持文献检索、筛选、证据提取和研究空白分析。没有可核验的检索结果或全文时，不能声称某篇文献存在或支持某个结论。

This Skill supports literature searching, screening, evidence extraction, and research-gap analysis. It must not claim that a paper exists or supports a conclusion without verifiable search results or full text.

## Required inputs / 所需输入

研究问题、关键词、同义词、时间范围、数据库、纳入与排除标准，以及需要提取的字段。用户应说明是否需要 DOI、PMID 或其他唯一标识符。

Provide the research question, keywords, synonyms, date range, databases, inclusion and exclusion criteria, extraction fields, and whether identifiers such as DOI or PMID are required.

## Workflow / 工作流程

1. 将研究问题拆分为核心概念，并扩展同义词和相关术语。
2. 设计检索式，记录数据库、检索日期和筛选标准。
3. 根据预设标准筛选文献，不把标题相似当作纳入依据。
4. 提取研究设计、样本、暴露或干预、结局、方法和主要发现。
5. 区分原文报告、跨研究比较和分析者推断。
6. 根据证据覆盖情况描述研究空白，不把“没有检索到”写成“没有研究”。

## Output format / 输出格式

输出应包括检索策略、筛选标准、文献表、证据矩阵和研究空白说明。文献表至少包含作者、年份、题目、期刊、唯一标识符、研究设计和主要发现。

Return the search strategy, screening criteria, literature table, evidence matrix, and a qualified gap statement. Include authors, year, title, journal, identifier, design, and main findings where available.

## Quality checks / 质量检查

- DOI、PMID 和题目是否对应；
- 引文是否真的支持所写主张；
- 是否区分原始研究、综述和预印本；
- 是否记录检索日期和数据库；
- 是否报告筛选标准和未纳入原因。

## Limitations / 限制

检索结果受数据库覆盖范围、关键词和访问权限影响。该 Skill 不能保证检索穷尽，也不能替代系统综述的正式注册和同行评审流程。

Search results depend on database coverage, query design, and access. This Skill cannot guarantee completeness or replace a registered systematic-review protocol and peer review.
