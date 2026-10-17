# Installation test / 安装测试

The installer is intentionally local and non-destructive. The following test was run with a temporary destination:

```sh
tmp_dir="$(mktemp -d)"
python3 scripts/install_skill.py skills/research-planning --destination "$tmp_dir"
test -f "$tmp_dir/research-planning/SKILL.md"
python3 scripts/install_skill.py skills/research-planning --destination skills --force
test "$?" -eq 4
test -f skills/research-planning/SKILL.md
rm -rf "$tmp_dir"
```

The test verifies copying and destination creation. It does not claim that every Codex client loads Skills from the same directory. Client-specific paths must be confirmed in the client documentation.

The installer also rejects a source-equals-destination case when `--force` is used. This prevents a forced install from deleting its own source directory.

安装器只处理本地复制，默认不会覆盖已有目录。测试验证了复制和目标目录创建，但没有声称所有 Codex 客户端都使用同一个加载路径。客户端路径需要按对应文档确认。

安装器还会拒绝“源目录等于目标目录”的 `--force` 情况，避免强制安装时先删除自身源目录。
