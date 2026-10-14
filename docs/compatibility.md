# Compatibility / 兼容性说明

## 中文

本仓库使用 Markdown 编写，适合能够读取 Markdown 指令的通用大语言模型和本地代理工具。不同平台对 Skill、system prompt、项目指令和文件引用的加载方式并不相同，仓库中的文件不能保证在所有产品中自动注册为可调用 Skill。

使用前可以把对应的 `SKILL.md` 内容提供给模型，或者根据目标平台的文档放入它支持的技能目录。Prompt 文件可以直接复制后填写变量，也可以作为项目级指令的草稿。

本仓库没有绑定特定模型、API、插件或操作系统。涉及统计计算、绘图和文献检索时，模型需要使用实际工具或用户提供的数据，不能把示例输出当成真实结果。平台的上下文长度、工具权限和文件读取能力会影响实际效果。

## English

This repository is written in Markdown and is intended for general-purpose language models and local agent tools that can read Markdown instructions. Platforms differ in how they load Skills, system prompts, project instructions, and referenced files, so these files are not guaranteed to become automatically callable Skills in every product.

Before use, provide the relevant `SKILL.md` to the model or place it in a skill directory supported by the target platform. Prompt files can be copied and completed directly, or adapted as project-level instructions.

The repository is not tied to a specific model, API, plugin, or operating system. For statistical analysis, plotting, and literature search, the model must use real tools or user-provided data; example outputs must not be treated as research results. Context limits, tool permissions, and file access vary by platform and affect practical performance.
