---
type: doc
doc-kind: analysis
date: 2026-11-13
project: "[[../60-Projects/CoreALM-Next|CoreALM-Next]]"
status: draft
tags: [skill自进化, 知识工程, skillopt]
---

# SkillOpt 融合分析：CoreALM-Next 的知识自进化引擎

> 分析对象：微软 [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt)（MIT，NeurIPS 2026 Spotlight，[arXiv:2605.23904](https://arxiv.org/abs/2605.23904)）。
> 本地代码：`/Users/acoin/Code/SkillOpt`。
> 结论：**SkillOpt 不是第 19 个模块，而是 CoreALM-Next 已有 KE 治理流水线的"执行引擎"**——把"候选经验 → 审核回归 → 正式资产"从人工流程变成带验证门的自动训练循环。

## 1. SkillOpt 是什么

核心主张：**skill 文档就是 Agent 的"外部权重"**，权重可以用梯度下降训练，skill 文档也应该有一套系统化训练方法——训练的是文本，不是模型参数。

| 要素 | 机制 | 深度学习类比 |
|---|---|---|
| 可训练状态 | 单份 skill 文档（部署物 `best_skill.md`，300–2000 tokens） | 模型权重 |
| 前向传播 | 冻结的目标模型带着当前 skill 跑任务批（rollout）并打分 | epoch/batch |
| 反向传播 | optimizer 模型复盘轨迹：成功吸收经验、失败找规律 | 计算梯度 |
| 参数更新 | 对 skill 文档做**有界** add/delete/replace（约 4 处/轮） | 小学习率 |
| 验证门 | 改动必须在 **held-out 验证集**上严格提升才保留，否则回滚 | validation gate |
| 反震荡 | 被拒改动进失败档案（不重复试错）+ 周期性整份复盘（防漂移） | 负样本缓存 |
| 效果 | 6 benchmark × 7 模型 × 3 执行环境共 52 格全部 best/tied-best；GPT-5.5 平均 +19~25 pp，且 skill 可跨模型/跨 harness 迁移 | — |

关键工程事实：部署时**零额外推理调用**——最终就是一份普通 markdown；v0.2.0 新增 **SkillOpt-Sleep** 夜间离线自进化（harvest 复盘历史会话 → mine 挖掘模式 → replay 重放任务 → consolidate 固化，全程在 held-out 验证门之后），并提供 Claude Code / Codex / Copilot / Devin 集成壳。

## 2. 与 CoreALM-Next 的映射：补上"自进化"缺口

CoreALM-Next 知识工程的现状（[[AI原生研发作业知识工程实施方案|KE实施方案]] + [[CoreALM-Next知识目录与任务续作设计|目录与续作设计]]）有一条明确的治理流：*"从任务中提炼的经验先成为候选，经审核和回归后进入正式资产"*（续作设计 §11）——但**候选怎么变成资产、靠什么判断"更好"，目前只有制度没有引擎**。SkillOpt 恰好就是那个引擎：

| CoreALM-Next 现有概念 | SkillOpt 提供的机制 | 落点模块 |
|---|---|---|
| M11 事件/回执/验证证据 | rollout 轨迹与打分 = 治理流的原料采集 | M11 → 供给 |
| M8/M12 分析与评测试验 | rollout → reflect → aggregate → select → update → evaluate 六步训练循环 | M12 的参考实现 |
| KE 治理"审核 + 回归" | **held-out 验证门**：验证集不提升就回滚，版本可追溯 | 治理规则的可执行化 |
| M18 基线（不可变清单 + 派生） | skill 版本树 + 失败档案 + 周期性整份复盘 | M18 的一种 baseline 载体 |
| M5 知识装配（薄入口） | 部署物是 300–2000 token 的 `best_skill.md`——**训练结果天然符合"薄入口"** | M5 的产物源 |
| SkillOpt-Sleep（夜间离线） | harvest 复盘历史会话 ≈ 续作设计里"任务结束冻结现场、提炼候选经验"的自动化 | M12 + M4 现场 |

三层对接关系与库内既有概念完全同构：

```
M11事件/轨迹(原料) ──SkillOpt训练循环──► held-out验证门 ──► best_skill.md
                                                        │
                    M5装配（薄入口厚语料）◄──────────────┘
                                                        │
                    实验闭环与uplift指标：无skill/有skill A/B ≈ 验证门的对照逻辑
```

## 3. 融合方案（分三步，对齐续作设计的交付节奏）

**第一步：把 SkillOpt 当外部评测基建用（零改造）**
- 选 1–2 个 CoreALM-Next 的真实任务域（如"Task 关联与 resume 生成"），整理 30–50 个带黄金判据的任务集作为 held-out 验证集——这一步同时就是在补 M8/M12 一直缺的评测集资产；
- 用本地 `/Users/acoin/Code/SkillOpt` 跑通 `pip install -e .` + openai_compatible 后端对接现有模型（它支持自定义后端，接 Qwen/内部模型均可）；
- 产出：AGENTS.md/skill 文档的"训练版"，与手写版 A/B 对比（opportunity/uplift 口径）。

**第二步：接进治理流水线（制度对齐）**
- SkillOpt 的验证门 = KE 治理"审核 + 回归"的自动化执行器；被拒改动档案 = 候选经验的失败记录；
- `best_skill.md` 进入中心知识目录的对应位置（如 `domains/task-and-sop.md` 的可执行版），带 M18 基线引用与 M11 验证回执——满足"知识是经实证的补差集"。

**第三步：Sleep 模式做夜间自进化（平台化）**
- nightly harvest 全平台执行轨迹 → mine 共性失败 → replay → 验证门后 consolidate 进 skill 资产；
- 对应续作设计 §11"任务结束冻结现场、提炼候选经验"的自动化版本，依附 KE-04/06/07/08，仍**无需第 19 个模块**。

## 4. 风险与边界（保持批判）

1. **held-out 验证集是成败关键**：SkillOpt 论文的 benchmark 是公开数据；CoreALM 内部任务集小（几十个），验证门统计功效有限，需防过拟合到验证集本身——建议验证集滚动更新；
2. **优化目标单一**：SkillOpt 优化的是任务得分，KE 治理还关心安全/合规/可维护性——这些维度必须保留人工审核位，不能全交给自动验证门；
3. **skill 漂移风险**：周期性整份复盘（meta update）能缓解，但内部场景下建议 skill 变更走中心 `changes/` 流程留痕，与 ADR 关联；
4. **成本**：训练循环本身消耗大量推理（rollout 批 + 验证批），Sleep 模式放夜间低峰是对的，但要计入 M9 的 Token/Credit 口径。

## 5. 本库关联

- 项目台账：[[../../60-Projects/CoreALM-Next|CoreALM-Next]]
- 概念卡：[[../../70-Knowledge/技能自进化|技能自进化]]（本文沉淀）
- 同构参照：[[../../70-Knowledge/实验闭环与uplift指标|实验闭环与uplift指标]]（MWG 的 A/B 验证 ≈ SkillOpt 的验证门）、[[../../70-Knowledge/薄入口厚语料|薄入口厚语料]]（best_skill.md 是训练出来的薄入口）、[[../../70-Knowledge/增量知识库|增量知识库]]（有界编辑 + 剪枝 ≈ 只保留有效知识）
- 参考资料：
  - [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) · [项目页](https://microsoft.github.io/SkillOpt/) · [论文 arXiv:2605.23904](https://arxiv.org/abs/2605.23904)
  - [机器之心报道](https://m.163.com/dy/article/KU9D0E1H0511AQHO.html) · [Microsoft Research Blog](https://www.microsoft.com/en-us/research/blog/skillopt-agent-skills-as-trainable-parameters/)
