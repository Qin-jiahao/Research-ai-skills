# Resource coverage / 资源覆盖

The machine-readable matrix is [`catalog/resources.json`](../catalog/resources.json). It currently contains R01–R31. Each record includes status, local path or source URL, and the reason for inclusion or deferral. New IDs may be added when the schema and validation record are updated.

机器可读矩阵见 [`catalog/resources.json`](../catalog/resources.json)，当前包含 R01–R31。每条记录都写明状态、本地路径或来源链接，以及收录或暂缓的原因。后续可以增加新的 ID，但需要同步更新 schema 和验证记录。

Local `released` records are the repository's own rewritten material. External records remain catalog entries until their upstream license, version, and behavior have been checked.
