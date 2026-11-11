---
type: concept
date: 2026-11-11
tags: [concept, cli, 知识库架构]
---

# CLI 中介层

## 是什么（自己的话，≤3 句）
Agent 消费外挂知识库时不直接读文件，而是经由一个 npm CLI（`search`/`retrieve` 子命令）中介：包内预构建离线索引 + 内嵌语料 + embedding 模型（~16.5MB），零依赖、零 API key、完全本地检索，网络只在 `npx @latest` 拉包时使用。

## 为什么重要 / 什么时候用
- 语义检索（embedding+BM25）远超 grep/文件遍历，索引必须预构建随包分发；
- CLI 平台无关——任何能跑 shell 的 Agent 都能用，这是「一份内容接十余家平台」的底层原因；`@latest` 保证内容保鲜，`--skill-version` 锁定协议与语料版本对齐。

## 来源
- [[10-Papers/2026-11-11-modern-web-guidance机制解析|modern-web-guidance机制解析]]（§3.10）

## 相关概念
- [[薄入口厚语料]]
- [[增量知识库]]
- 我的 local-rag 即同构实现（Qdrant 离线索引 + OpenAI 兼容 API 中介）：[[../40-Prototype/local-rag/README|local-rag]]
