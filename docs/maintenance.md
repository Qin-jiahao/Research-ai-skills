# Maintenance Rules / 维护规则

## 中文

仓库把资源分为四类：

- `skills/`：可被 Agent 发现和调用的多步骤科研工作流；
- `prompts/`：可直接复制的单任务提示词；
- `tools/`：独立科研软件、开源项目和服务的说明入口；
- `catalog/`：来源、状态或测试尚未完整的候选资源记录。

资源状态只能根据实际证据更新：`collected` 表示已收集，`reviewed` 表示完成结构和来源审查，`tested` 表示完成记录化测试，`released` 表示进入版本发布范围。社交媒体截图只能支持 `collected`，不能单独支持 `tested` 或 `released`。

新增资源时应先检查是否与现有 Skill 重复，再补充原始链接、作者、许可证、核验日期、兼容环境和限制。更新外部资源记录时不要把当前页面状态追溯性地写成历史事实。

## English

The repository separates `skills/`, `prompts/`, `tools/`, and `catalog/`. Status changes require evidence: `collected`, `reviewed`, `tested`, and `released` describe increasing levels of verification. A social-media screenshot can support collection, but not testing or release.

Before adding a resource, check for overlap with existing Skills and record the original URL, author, license, verification date, compatibility, and limitations. Do not rewrite a current external page state as historical fact.
