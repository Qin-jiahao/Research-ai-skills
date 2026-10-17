# Contributing / 贡献指南

## 中文

本仓库接受可复用的科研 Skill、Prompt、文档、索引和来源记录。每项贡献都应便于其他研究者复查；无法确认的事实需要明确标注，不能用默认值补齐。

### 贡献什么

可以提交以下内容：

- 新的或经过实质改进的 Skill 和 Prompt；
- 安装、兼容性、维护和评估边界等文档；
- 资源目录、外部项目记录和来源归因信息；
- 能够复现的错误报告、缺失信息报告和改进建议。

### 内容要求

每个 Skill 至少应包含：适用场景、使用边界、必需输入、工作流程、输出格式、质量检查、局限性、完整输入示例、信息不足时的处理示例和来源说明。Skill 的 YAML frontmatter 必须包含实际用途的 `description`；`name` 只能使用小写字母、数字和连字符，并且必须与目录名一致。

每个 Prompt 至少应说明：使用场景、输入要求、输出要求、禁止编造的内容、信息不足时的处理方式、一个双语示例和来源。中英文需要表达相同的要求，不要求逐句直译，但不能遗漏使用边界或限制。

贡献内容不得凭空生成数据、文献、统计结果、P 值、FDR、实验结论或运行结果。输入不足时，请写出“待补充”“待核验”或“无法判断”的项目，并说明它们对结果的影响。

### 来源、版权与隐私

新增或改写外部材料时，请记录原始链接、作者或维护者、许可证、核验日期、版本或 commit、兼容性和限制。来源不明的内容应标注“来源于网络，自行整理汇总”，不能包装成原创，也不能复制第三方原文。截图可以帮助记录线索，但不能单独证明内容已经测试或获得复用授权。

请勿提交未授权的第三方原文、个人信息、API 密钥、未公开研究数据、受限数据或其他不应公开的材料。提交者需要自行确认拥有提交所需的权利，并在文件级说明中保留第三方归因和许可证要求。

根目录的 [MIT License](LICENSE) 适用于维护者创作，或贡献者明确按 MIT 提交且本仓库有权分发的原创内容。提交者需要确认自己有权按 MIT 分发所提交的内容。第三方文本、图片、代码、名称和外部项目仍受其原始许可证约束，详细范围见[许可证与署名说明](docs/license-and-attribution.md)。

### 提交前检查

在打开 Pull Request 前，请运行：

```bash
python3 scripts/validate_repo.py
git diff --check
```

还需要人工检查以下内容：

- Markdown 链接、YAML frontmatter、文件名和目录名是否正确；
- 中文和英文是否覆盖相同字段，是否存在机翻表达或明显歧义；
- 是否残留 `TODO`、`FIXME`、`待替换`、`未替换` 或其他占位符；
- 是否清楚区分已完成、已检查、待核验和未执行的内容；
- 来源、版权、许可证、隐私和未执行检查是否写明。

仓库校验脚本主要检查结构、链接和静态安全边界。它不等于真实数据分析、客户端行为、可复现运行或法律审查已经完成。未执行的检查需要在 Pull Request 中列出。

### 提交流程

1. 从 `main` 创建独立分支，或 Fork 仓库后创建分支。
2. 修改对应目录，并同步更新索引、来源记录或维护文档。
3. 运行上面的检查，记录失败项和仍待核验的内容。
4. 提交 Pull Request，说明改动文件、用户可见的行为变化、来源与许可证、已执行检查和未执行检查。

提交信息可以使用 `feat:`、`fix:` 或 `docs:` 前缀，但这不是硬性要求。请让提交标题能够说明改动的实际内容。

### 状态标签

Skill 文件中的 `draft` 表示内容成熟度和行为测试仍有限。资源目录中的 `collected`、`reviewed`、`tested` 和 `released` 只按记录的证据推进；`reviewed` 表示已核对记录的公开来源、用途和许可证信息，`tested` 表示已在本仓库的静态或本地测试中验证，`released` 表示已作为本仓库内容发布。这些状态不代表科学结论、法律审查或所有客户端行为已经验证。状态定义见[资源状态](docs/resource-status.md)。

## English

This repository accepts reusable research Skills, Prompts, documentation, indexes, and provenance records. Each contribution should be reviewable by other researchers. Facts that cannot be confirmed must be labeled instead of filled with assumptions.

### What to contribute

You may submit:

- new or substantially improved Skills and Prompts;
- documentation for installation, compatibility, maintenance, and evaluation boundaries;
- resource catalogs, external-project records, and attribution information;
- reproducible bug reports, missing-information reports, and focused improvement suggestions.

### Content requirements

Each Skill must document at least its use case, boundaries, required inputs, workflow, output format, quality checks, limitations, a complete input example, an insufficient-input example, and its sources. Skill YAML frontmatter must include a `description` that states the actual use. `name` may contain only lowercase letters, numbers, and hyphens, and must match the directory name.

Each Prompt must document its use case, input requirements, output requirements, prohibited fabrication, handling of missing information, one bilingual example, and its sources. The Chinese and English sections must express the same requirements. They do not need to be literal translations, but neither section may omit the boundaries or limitations.

Do not invent data, references, statistical results, P values, FDR values, experimental conclusions, or execution results. When information is missing, list items as “to be provided,” “to be verified,” or “cannot be determined,” and state how the gap may affect the result.

### Provenance, copyright, and privacy

For new or adapted external material, record the original URL, author or maintainer, license, verification date, version or commit, compatibility, and limitations. Mark unclear provenance as “Source: online materials, independently organized and summarized.” Do not present it as original work or copy third-party text. Screenshots can record leads, but they do not by themselves prove testing or reuse permission.

Do not submit unauthorized third-party text, personal information, API keys, unpublished research data, restricted data, or other material that should not be public. Contributors must confirm that they have the rights needed for the submission and retain third-party attribution and license requirements in file-level notes.

The root [MIT License](LICENSE) applies to original content created by the maintainers, or explicitly submitted under MIT by contributors when this repository has the right to distribute it. Contributors must confirm that they have the right to distribute their submission under MIT. Third-party text, images, code, names, and external projects remain subject to their original licenses. See the [license and attribution scope](docs/license-and-attribution.md) for details.

### Before opening a pull request

Run:

```bash
python3 scripts/validate_repo.py
git diff --check
```

Also check manually:

- Markdown links, YAML frontmatter, file names, and directory names;
- matching fields in Chinese and English, including natural wording and unambiguous terms;
- remaining `TODO`, `FIXME`, `待替换`, `未替换`, or other placeholders;
- a clear distinction between completed, checked, unverified, and unrun work;
- provenance, copyright, license, privacy, and unrun checks.

The repository validator mainly checks structure, links, and static safety boundaries. It does not establish real-data behavior, client compatibility, reproducible execution, or legal clearance. List unrun checks in the pull request.

### Contribution workflow

1. Create a branch from `main`, or fork the repository and create a branch.
2. Edit the relevant directory and update indexes, provenance records, or maintenance notes when needed.
3. Run the checks above and record failures or unresolved items.
4. Open a pull request describing changed files, user-visible behavior, provenance and licensing, checks that ran, and checks that did not run.

You may use `feat:`, `fix:`, or `docs:` prefixes in commit messages, but they are optional. Make the title describe the actual change.

### Status labels

The `draft` label inside a Skill describes limited content maturity and behavioral testing. The catalog labels `collected`, `reviewed`, `tested`, and `released` should advance only when the recorded evidence supports them. `reviewed` means that the recorded public source, purpose, and license information have been checked. `tested` means that static or local testing has been completed in this repository. `released` means that the item has been published as repository content. These labels do not certify scientific conclusions, legal review, or behavior in every client. See [resource status](docs/resource-status.md) for definitions.
