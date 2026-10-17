# Contributing

## 中文

提交新的 Skill 或 Prompt 时，请说明适用场景、所需输入、预期输出、质量检查、已知限制、来源和一个完整案例与信息不足案例。中英文内容需要表达同一要求。不要提交未经授权的第三方原文、个人信息、未公开研究数据或凭空生成的文献和结果。

提交前运行：

```bash
python3 scripts/validate_repo.py
git diff --check
```

新增外部项目时，记录原始链接、作者或维护者、许可证、核验日期、兼容性和限制。无法确认的字段写明“待核验”，不要用截图、Star 数或宣传语代替证据。

建议从独立分支提交改动，并在 Pull Request 中说明文件、行为变化、验证命令和未执行的检查。本仓库原创内容按根目录 MIT 许可证发布；改写第三方材料时必须保留归因、原始链接和许可证边界。

## English

When contributing a Skill or Prompt, document its use case, required inputs, expected outputs, quality checks, limitations, provenance, and both complete and incomplete examples. The Chinese and English sections must express the same requirements. Do not submit unauthorized third-party text, personal information, unpublished research data, fabricated references, or fabricated results.

Before submitting, run `python3 scripts/validate_repo.py` and `git diff --check`. For external projects, record the original URL, author or maintainer, license, verification date, compatibility, and limitations. Mark unknown fields as “to be verified”; screenshots, star counts, and promotional claims are not substitutes for evidence.

Use a separate branch for changes and describe the files, behavior changes, validation commands, and unrun checks in the pull request. Original content in this repository is released under the root MIT license. Adapted third-party material must retain attribution, the original link, and the license boundary.
