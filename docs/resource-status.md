# Resource Status / 资源状态

## 中文

资源目录使用以下状态词语：

- **Collected**：已记录来源或主题，但尚未完成本仓库行为测试。
- **Reviewed**：已核对记录的公开来源、用途和许可证信息。
- **Tested**：已按记录的案例或本地检查完成验证；不等于科研结论正确。
- **Released**：已作为本仓库内容发布；不表示已经完成真实数据验证。

仓库同时使用两种状态维度。Skill 文件中的 `draft` 表示内容成熟度和行为测试仍有限；`catalog/resources.json` 中的 `released` 表示内容已进入仓库版本。外部项目通常标为 `collected`，不属于本仓库可安装包。任何状态都不能代替真实数据测试、可复现运行、许可证审查或科研判断。

## English

The catalog uses **Collected**, **Reviewed**, **Tested**, and **Released**. **Collected** means that a source or topic has been recorded, but repository behavior testing is incomplete. **Reviewed** means that the recorded public source, purpose, and license information have been checked. **Tested** means that static or local testing has been completed in this repository. The `draft` label inside a Skill describes content maturity, while catalog `released` means that the item has been published as repository content. None of these labels certifies a research result. External projects are references, not installable contents of this repository, unless a separate record says otherwise.
