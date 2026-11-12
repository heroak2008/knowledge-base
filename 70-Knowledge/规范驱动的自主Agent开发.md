---
type: concept
date: 2026-11-12
tags: [concept, agent架构, 测试策略]
---

# 规范驱动的自主Agent开发（Spec + Reference + Fidelity Tests）

## 是什么（自己的话，≤3 句）
让自主 AI agent 全权写代码的开发模式：机器可读的**规范**（如 Smithy/OpenAPI）当"考纲"，**参考实现**（真实系统）当"标准答案"，agent 先对参考实现验证测试再入库，另一批 agent 靠这些"保真度测试"找差距、修代码，人类只设计护栏（merge gate）不写不审代码。AWS Emulator 100% 由该模式产出（数百 agent 并发、日修数千 issue）。

## 为什么重要 / 什么时候用
- 信任问题被转化为"测试过不过"的客观判据，绕开人工 code review → 适合**有形式化契约 + 可调用参考实现 + 测试可幂等重放**的服务（如给自己微服务做本地模拟器/测试替身）；
- 三角色分离（写测试 / 找问题 / 修问题，各限边界）+ 合并门禁（编译+规范审查+安全+回归）是护栏核心，门禁速度决定 agent 迭代吞吐；
- 防幻觉命门：测试期望值必须先在参考实现上实跑验证，规范只做引导不做裁判；
- 盲区：覆盖率只到 agent 探索过的子集（错误码、幂等、并发边界最易漏），需独立的保真度度量；引导 agent"复用现有库"防重新造轮子（AWS 教训：agent 自造 Python 解释器）。

## 来源
- [How we built the agents that built AWS Emulator](https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator)（Matthew Goldberg, 2026-11-11）
- 开源产出：[aws/aws-emulator](https://github.com/aws/aws-emulator)（CC0）、[aws/aws-emulator-evaluation-suite](https://github.com/aws/aws-emulator-evaluation-suite)（保真度测试）
- 起源参照：Anthropic 自主构建 C 编译器实验

## 相关概念
- [[薄入口厚语料]]（同属 agent 工程架构）
- [[增量知识库]]
