---
type: doc
date: 2026-11-23
doc-kind: report
status: draft
---

# AI for 研发能力建设范围：外部依据对照表

> 目标读者：写"独立软件 AI for 研发能力建设范围"材料的作者
> 交付形式：先看"正向推导"一节的来源 × 方向矩阵（方向怎么从报告推出来，一页 PPT 版见 [[AIFor研发能力建设范围-正向推导一页纸.html]]）；再按方向查原文表，每条含原文、来源、链接（方向 → 原文的一页 PPT 版见 [[AIFor研发能力建设范围-外部依据一页纸.html]]，16:9，七个方向 × ≤3 条，同一来源在一个方向内只出现一次，关键字加粗）
> 用途：七个方向（知识工程 / Harness 工程 / 质量防护 / 配套的组织建设 / 研发流程 / AI 工具和算力保障 / 成效度量）各自能引哪句原文

## 来源清单

| 代号 | 来源 | 日期 | 链接 | 说明 |
|---|---|---|---|---|
| G1 | Gartner 新闻稿 Top Strategic Technology Trends in Software Engineering for 2026 and Beyond（六趋势） | 2026-11-18 | [原站](https://www.gartner.com/en/newsroom/press-releases/2026-11-18-gartner-identifies-the-top-strategic-technology-trends-in-software-engineering-for-2026-and-beyond) · [Express Computer 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) | 原站反爬，英文原文取自转载页；数字与德文转述一致 |
| G2 | Gartner 2026 Planning Guide for Software Engineering（G00837698） | 2025-10 | [公开摘录 PDF](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/2026-planning-guide-for-software-engineering.pdf) | 公开 16 页摘录，全文 38 页付费 |
| G3 | Gartner 2025 Planning Guide for Software Engineering（G00810365） | 2024-10 | [公开摘录 PDF](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/reskin-2025-planning-guide-for-software-engineering-v2.pdf) | 公开 16 页摘录，全文 37 页付费 |
| G4 | Gartner 新闻稿 Top Strategic Trends in Software Engineering for 2025 and Beyond（六趋势） | 2025-07-01 | [原站](https://www.gartner.com/en/newsroom/press-releases/2025-07-01-gartner-identifies-the-top-strategic-trends-in-software-engineering-for-2025-and-beyond) · [ABES 转载](https://abes.org.br/en/gartner-identifica-as-principais-tendencias-estrategicas-em-engenharia-de-software-para-2025-e-alem/) | 原站反爬，英文原文取自转载页 |
| G5 | Gartner Top 10 Strategic Technology Trends for 2026 | 2025-10 | [英文 PDF](https://emt.gartnerweb.com/ngw/globalassets/en/chief-information-officer/documents/2026-top-tech-trends.pdf) | 面向 CIO 的十条趋势 |
| C1 | 中国信通院《AI4SE 行业现状调查报告（2026 年）》 | 2026-03 | [PDF](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) | 现状调查，页码为报告印刷页码 |
| A | Anthropic "Effective harnesses for long-running agents" | 2025-11-26 | [链接](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | 工程实践文章 |
| N | NVIDIA "Practical Security Guidance for Sandboxing Agentic Workflows" | 2026-01-30 | [链接](https://developer.nvidia.com/blog/practical-security-guidance-for-sandboxing-agentic-workflows-and-managing-execution-risk/) | 沙箱控制清单 |

## 正向推导：从报告到方向（一页 PPT 版见 [[AIFor研发能力建设范围-正向推导一页纸.html]]，三步式：每份报告覆盖了哪些方向 → 多份报告在同一方向上相互印证 → 整合出最终洞察）

> 这张表回答"方向是怎么来的"：先看报告说了什么，再归并成能力项，最后和内部共识对照。后面各节的方向 → 原文表是它的反向引用。

**推导方法**
1. 选报告：权威机构、近 12 个月、直接谈软件工程或 AI 研发。Gartner 5 份（G1–G5），Anthropic、NVIDIA、信通院各 1 份（A、N、C1）。
2. 拆条目：把趋势、预测、规划要点拆成"组织要具备什么"，8 份共 50 处（直接建议 41、间接提及 9），每处标一个候选方向 D1–D13。
3. 归并：候选方向按报告印证数排序，至少 2 份报告直接指向、且落在"AI 用于研发"范围内的，进入最终范围；同一最终方向下的候选合并。
4. 对照：与内部共识的 6 个方向比对，查缺，也查多。

**候选方向（13 个）与筛选结果**

| 候选 | 包含什么 | 直接 ● / 间接 ○ | 来源 | 去向 |
|---|---|---|---|---|
| D1 知识与规约 | 组织知识、数据集、Agent 可读工件、规约编程 | 1 / 3 | C1；G1 G2 A | → 知识工程 |
| D2 Harness 工程 | 上下文、规则、工具、反馈循环 | 2 / 1 | G1 A；C1 | → Harness 工程 |
| D3 安全与隔离 | Agent 沙箱、secure-by-design、禁止删改测试、强制控制 | 6 / 0 | G1 G2 G3 A N C1 | → 质量防护 |
| D4 评测与质量判定 | eval-driven、AI testing、逐项验证 | 3 / 0 | G1 G3 A | → 质量防护（与 D3 合并） |
| D5 角色与技能 | 实现转向编排、FDE、rightskilling、人才密度、tiny teams | 5 / 1 | G1 G2 G3 G4 C1；G5 | → 组织建设 |
| D13 多 Agent 协同组织 | OPC 组织形态 | 1 / 0 | C1 | → 组织建设（并入 D5） |
| D7 研发流程与工作方式 | 产品制、黄金路径、AI 进每个 SDLC 阶段、小批次 | 5 / 1 | G2 G3 G4 A C1；G1 | → 研发流程 |
| D8 开发者平台与 IDP | 平台工程、平台准入策略、AI 原生开发平台 | 5 / 0 | G1 G2 G3 G4 G5 | → 工具与算力保障 |
| D9 模型与算力供给 | Local AI、混合计算、算力回迁、开放模型、云与模型集中度 | 4 / 1 | G1 G4 G5 C1；N | → 工具与算力保障（与 D8 合并） |
| D10 成效度量 | 生产力定义与基线、仪表盘、效能指标 | 3 / 0 | G2 G3 C1 | → 成效度量（新增） |
| D6 人机分工与审批 | 人工介入点、审批习惯化、自动化与监督平衡 | 3 / 0 | G1 G4 N | 未单列：议题分散在 Harness、质量、组织三处，建议作为跨方向原则 |
| D11 给产品加 AI 能力 | "SDLC for AI"、LLM 应用与智能体、AI 安全平台 | 2 / 2 | G3 G4；G1 G5 | 范围外：属于产品和解决方案，不是 "AI for 研发"，另立项 |
| D12 绿色软件工程 | 能耗与碳排放 | 1 / 0 | G4 | 议题不足：只有 1 份，关联弱 |

**来源 × 方向矩阵**（按最终 7 个方向归并后）（● 直接建议或预测；○ 间接提及或作为输入；— 未涉及）

| 来源 | 知识工程 | Harness 工程 | 质量防护 | 组织建设 | 研发流程 | 工具与算力保障 | 成效度量 |
|---|---|---|---|---|---|---|---|
| G1 Gartner 六大趋势 2026+ | ○ harness 接入 **organisational knowledge**、编码标准 | ● **Harness Engineering** 列为趋势；缺陷 **少 60%**（2028） | ● **Agent 沙箱** 70%（2030）；**Eval-driven** 70%（2028） | ● **FDE** 70%（2028）；AI 开发、治理、运营模式培训 | ○ harness 接入 **development workflows**；AI-first + 平台治理 | ● **平台策略**限定允许的 AI 原生开发平台；**Local AI** 数据主权、推理成本、时延 | ○ eval 从 **约 100 用例 + 3–5 指标**起步，放进 CI |
| G2 Gartner 2026 规划指南 | ○ 平台工程 "**enhance developer knowledge**" | — | ● **安全成为应用交付硬要求**；**security champion** | ● **AI 将根本改变工程师角色** | ● **产品制运作**；**黄金路径** | ● **平台工程**：IDP，把开发者当客户 | ● **生产力无定义无基线**；AI 助手 **+10%–20%**；避免**虚荣指标** |
| G3 Gartner 2025 规划指南 | — | — | ● **secure-by-design**；**AI testing and testing AI** | ● **rightskilling**、个人学习计划 | ● AI **沿价值链全面采用**；产品制 + IDP | ● **平台工程规模化**；IDP 目录、记分卡、脚手架 | ● **生产力驱动现代化**；实时仪表盘、团队级指标 |
| G4 Gartner 六大趋势 2025+ | — | — | — | ● 角色**从实现转向编排**（90% 用 AI 助手）；**最大化人才密度** | ● AI 进**每个 SDLC 阶段**；自动化与人工监督平衡 | ● **GenAI 平台工程** 70%（2027）；**开放模型** 30%（2028）；绿色软件工程 | — |
| G5 Gartner 十大技术趋势 2026 | — | — | ○ **AI 安全平台** 80%（2028），面向 AI 应用 | ○ AI 原生开发平台 → **tiny teams** | — | ● **AI 超算平台**；**混合计算架构** 40%（2028）；**Geopatriation** 75%（2030） | — |
| A Anthropic 长任务 agent harness | ○ **feature-list、进度文件**作为 Agent 可读工件 | ● **initializer agent + coding agent**，跨上下文窗口推进 | ● **禁止删改测试**；**浏览器自动化做端到端验证** | — | ● **一次一个 feature**、增量 **git 提交**、留进度文件 | — | ○ feature-list 的 **passes 字段**逐项验证 |
| N NVIDIA Agent 沙箱安全指引 | — | — | ● OS 级**强制控制三项**；**审批不缓存**；**密钥注入**；沙箱**生命周期管理** | ○ **审批疲劳 / 习惯化**，人工介入点要设计 | — | ○ **沙箱 / 虚拟化**运行环境 | — |
| C1 信通院 AI4SE 现状调查 | ● **高质量数据集缺乏**；**RAG 私有知识库 40.35%**；流程产物 **AI 友好型**；**规约编程** | ○ 规约编程：智能体在**约束框架内**实现与验证 | ● **安全 / 兼容性测试**落地少 | ● **人才短缺 34.02%**；人人都是开发者；**OPC 多 Agent 组织** | ● AI **融合需求 / 编码 / 测试 / 部署**；重心转向**规模化落地** | ● **公有云 31.8%**；模型 **94% 集中八个系列** | ● **应用成效度量难**；要明确**可量化的效能度量指标** |
| **直接 ● / 间接 ○** | 1 / 3 | 2 / 1 | 6 / 1 | 5 / 2 | 5 / 1 | 6 / 1 | 3 / 2 |
| **与内部共识对照** | 原有 | 原有 | 原有 | 原有 | 原有 | 原有 | **建议新增** |

**结论**
1. 50 处趋势与建议归并成 13 个候选方向，其中 10 个收进最终 7 个方向（质量防护、组织建设、工具与算力保障各由 2 个候选合并而成），3 个因关联度或议题数量没有进入（见上表）。
2. 七个方向都有至少 2 份来源直接支撑。质量防护和工具与算力保障各 6 份，组织建设、研发流程各 5 份，是公认度最高的几块。
3. 成效度量在共识里缺失：Gartner 两版规划指南（生产力无定义无基线、避免虚荣指标）和信通院（成效度量难）3 份直接指向，eval-driven 趋势间接支撑，建议补为第七个方向。
4. 知识工程单列的理由主要来自信通院和独立软件的场景：Gartner 把知识当作 harness 的输入而不是独立趋势；信通院把它列为一等缺口（数据集缺乏、RAG 40.35%、流程产物 AI 友好型）。私有化交付和存量知识多的产品形态支持单列。

**边界**（报告提到、但不在这七个方向里的）：Gartner 划出的另一半领域 "SDLC for AI"（给产品加 LLM 功能，G4 趋势②）、面向 AI 应用的 AI 安全平台（G5，2028 年 80%）、开放模型与绿色软件工程（G4 趋势⑤⑥）。这些属于产品路线或算力策略，建议另立项。

## 总判断（放材料开头）

| 方向 | 素材原文 | 来源 | 链接 |
|---|---|---|---|
| 总判断 | "The rapid advancement of AI is reshaping the software development life cycle (SDLC), forcing software engineering leaders to balance immediate productivity gains with longer-term investments in operating models, skills and governance." — Manjunath Bhat, Distinguished VP Analyst | G1 | [G1 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) |
| 总判断 | "AI tools offer useful, though not world-changing, benefits to software engineers. However, many organizations hit barriers to adoption or fail to realize the full benefits of these tools due to unrealistic management expectations and a misunderstanding of what the job of the software engineer entails." | G2 Key Findings | [G2](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/2026-planning-guide-for-software-engineering.pdf) |
| 总判断 | "此前，企业对智能化研发的投入主要集中于工具引入与平台搭建，而随着工具能力的持续跃升，未来企业智能化研发的建设重心将从'能力建设'转变为'规模化落地'……战略治理层面，明确智能化研发的落地目标与可量化的效能度量指标；研发流程层面，推动 AI 能力深度融合需求分析、代码生成、测试验证与部署运维等核心环节；组织保障层面，建立支撑智能研发持续运转的人才培养、协作规范与知识沉淀机制，构建新型组织架构以适应软件研发智能化的落地。" | C1 第七章第 5 条，第 28 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |

## 1. Harness 工程

| 素材原文 | 来源 | 链接 |
|---|---|---|
| "Harness engineering involves providing AI coding agents with the context, instructions, tools and guardrails needed to perform software engineering tasks reliably. These controls can include access to organisational knowledge, coding standards, development workflows and governance requirements." | G1 趋势② Harness Engineering | [G1 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) |
| "Gartner predicts that organisations with AI coding harness infrastructure will experience 60% fewer post-deployment defects by 2028 than those without it." | G1 趋势② | [G1 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) |
| "As AI-generated code becomes more common, organisations will also need mechanisms to ensure that the output follows internal standards and engineering practices." | G1 趋势② | [G1 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) |
| "受访企业在软件开发领域应用智能体（Agent）的核心聚焦于提升解决复杂问题的能力，企业占比达到 44.44%，其次聚焦于理解长上下文和辅助研发全流程打通，占比分别为 27.78% 和 18.65%。" | C1 第四章第 7 条，第 19 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |

## 2. 知识工程

Gartner 没有把知识单列为趋势，它出现在 harness 的"organisational knowledge"和平台工程的"enhance developer knowledge"里；信通院的"规约编程"和"AI 友好型流程产物"是最接近的国内表述。

| 素材原文 | 来源 | 链接 |
|---|---|---|
| "These controls can include access to organisational knowledge, coding standards, development workflows and governance requirements."（同上条，知识是 harness 的输入） | G1 趋势② | [G1 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) |
| "Reduce developer overload by using platform engineering to simplify nondifferentiating work and enhance developer knowledge." / "Define golden paths to simplify nondifferentiating work." | G2 Recommendations / Planning Considerations | [G2](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/2026-planning-guide-for-software-engineering.pdf) |
| "私有化部署方式中，通过 RAG（检索增强生成）嵌入私有知识库的方式最多，占比 40.35%。而全栈自研或微调方式占比不足 20%，可见企业现阶段更倾向依托成熟的通用大模型生态，以降低技术落地的成本与风险。" | C1 第二章第 5 条，第 6 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |
| "实践表明，智能化软件工程（AI for Software Engineering，AI4SE）为企业降本增效、提升生产力开辟了可行路径，但仍面临专业人才紧缺、应用成效度量难、高质量数据集缺乏等挑战，亟需行业提供指引。" | C1 前言 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |
| "Agentic Coding 驱动的研发体系中流程产物需被重新设计为'AI 友好型'，能够被下游 Agent 直接读取并驱动下一阶段的自动化执行，产物的第一读者正在从'人'转变为'Agent'，产物设计标准从'人类可理解'升级为'Agent 可消费'。" | C1 第七章第 1 条，第 26 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |
| "专业开发者负责将模糊的业务需求转化为精确、无歧义的规约描述，明确系统的输入输出契约、边界条件与验收标准；智能体则在约束框架内自主规划实现路径、生成代码、编写测试并持续验证。" | C1 第七章第 2 条"规约编程"，第 27 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |
| "组织保障层面，建立支撑智能研发持续运转的人才培养、协作规范与知识沉淀机制，构建新型组织架构以适应软件研发智能化的落地。" | C1 第七章第 5 条，第 28 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |

## 3. 质量防护

| 素材原文 | 来源 | 链接 |
|---|---|---|
| "Agent sandboxing involves running AI agents in isolated execution environments, limiting the extent to which they can interact with production systems, sensitive information or other critical resources." | G1 趋势③ Agent Sandboxing | [G1 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) |
| "Gartner predicts that 70% of enterprises will sandbox agentic development workflows in pre-production environments by 2030, up from 10% in 2026." | G1 趋势③ | [G1 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) |
| "Another emerging practice is eval-driven development, which involves evaluating AI applications against predefined criteria throughout the development process." / "Gartner predicts that 70% of software engineering teams will adopt eval-driven development by 2028, compared with fewer than 20% in 2026." | G1 趋势⑤ Eval-Driven Development | [G1 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) |
| "Both the frequency and impact of security incidents continue to increase, yet many organizations still perform security theatre without achieving real-world improvements." / "Security will become an imperative for application delivery." | G2 Key Findings / Trends | [G2](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/2026-planning-guide-for-software-engineering.pdf) |
| "Break the cycle of software engineers and security professionals seeing each other as the problem by adopting the role of security champion, proactively reaching out and building bridges with software security teams." | G2 Recommendations | [G2](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/2026-planning-guide-for-software-engineering.pdf) |
| "Improve proficiency in both AI testing and testing AI." / "Adopt AI throughout the software development value chain." | G3 趋势② 规划要点 | [G3](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/reskin-2025-planning-guide-for-software-engineering-v2.pdf) |
| "In Gartner's Software Engineering Survey for 2024, 75% of responding software engineering leaders recognized application security as a highly important skill to deliver software that meets the business needs in their organizations." | G3 Secure-by-Design 节 | [G3](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/reskin-2025-planning-guide-for-software-engineering-v2.pdf) |
| "AI security platforms (AISPs) consolidate controls to secure both third-party AI services and custom-built AI applications. They address AI-native risks like prompt injection, rogue agent actions and data leakage." / "80% of enterprises will adopt AISPs by 2028." | G5 趋势 9 | [G5](https://emt.gartnerweb.com/ngw/globalassets/en/chief-information-officer/documents/2026-top-tech-trends.pdf) |
| "受访企业应用智能测试工具主要集中于功能与接口测试环节，总占比超 50%，安全与兼容性测试等方面占比较低。……然而 AI 赋能安全性测试和兼容性测试的企业落地仍然较少。" | C1 第五章第 1 条，第 20 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |

## 4. 配套的组织建设

| 素材原文 | 来源 | 链接 |
|---|---|---|
| "These professionals work directly with business and technology teams to adapt and deploy AI solutions in real-world operating environments." / "Gartner predicts that more than 70% of AI technology and service providers will use FDEs by 2028, compared with 10% today." | G1 趋势⑥ Forward-Deployed Engineers | [G1 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) |
| "Gartner predicts that by 2028, 90% of enterprise software engineers will use AI code assistants, compared to less than 14% in early 2024. The role of developers will shift from implementation to orchestration, focusing on troubleshooting and system design, and ensuring that AI tools deliver high-quality results." | G4 趋势① AI-Native Software Engineering | [G4 转载](https://abes.org.br/en/gartner-identifica-as-principais-tendencias-estrategicas-em-engenharia-de-software-para-2025-e-alem/) |
| "Leaders must cultivate a culture of continuous learning and collaboration to attract and retain qualified professionals who can adapt and grow with evolving business needs." | G4 趋势④ Maximizing Talent Density | [G4 转载](https://abes.org.br/en/gartner-identifica-as-principais-tendencias-estrategicas-em-engenharia-de-software-para-2025-e-alem/) |
| "AI will fundamentally change the role of software engineers." / "Capitalize on the value of AI tools by building on developers' natural curiosity and desire to learn. Use AI for tasks across the software development life cycle (SDLC) where the work does not require a strong understanding of your organization and its goals." | G2 Trends / Recommendations | [G2](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/2026-planning-guide-for-software-engineering.pdf) |
| "Accelerated technology disruption will drive the urgency for rightskilling." / "Increase your impact and advance your career by creating a personal learning plan to identify development opportunities, integrate learning into your daily work and address critical skills gaps." | G3 趋势④ | [G3](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/reskin-2025-planning-guide-for-software-engineering-v2.pdf) |
| "AI-native development platforms empower 'tiny teams' to build more applications with the same resources — enabling, for example, five teams of two to deliver five applications at once." | G5 趋势 1 AI-Native Development Platforms | [G5](https://emt.gartnerweb.com/ngw/globalassets/en/chief-information-officer/documents/2026-top-tech-trends.pdf) |
| "近两年，受访企业开展软件研发智能化转型呈现两大核心挑战，一是专业人才短缺仍居首位，2025 年占比达 34.02%；二是投入成本高，短期投入产出比不明确，关注度升至 26.85%。" | C1 第二章第 2 条，第 4 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |
| "多 Agent 协同正在催生一种全新的软件行业竞争形态，组织规模不再是软件产出能力的决定性因素，一人携多 Agent 的 OPC（One Person Company）组织也可构成一支具备完整研发能力的工程团队。Agent 从处理数分钟的单次任务进化为可自主运行数天乃至数周的长时任务，仅在关键节点需要人类监督。" | C1 第七章第 4 条，第 27–28 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |

## 5. 研发流程

| 素材原文 | 来源 | 链接 |
|---|---|---|
| "Improve developer productivity by focusing on software engineering basics, such as product-centric delivery, so that when you introduce AI tools and emerging approaches, you maximize their benefits." / "Adopt product-centric approaches when operating in an unclear environment." | G2 Recommendations / Planning Considerations | [G2](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/2026-planning-guide-for-software-engineering.pdf) |
| "Transition to a product operating model powered by internal developer platforms." / "The integration of generative AI (GenAI) throughout the software development life cycle (SDLC) is shifting from pilot validation to value realization." | G3 趋势① / Key Findings | [G3](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/reskin-2025-planning-guide-for-software-engineering-v2.pdf) |
| "AI-native software engineering is transforming the lifecycle of software development by incorporating AI into every phase, from design to implementation." / "To be successful, teams must balance automation with human oversight, considering business criticality, risk, and workflow complexity." | G4 趋势① | [G4 转载](https://abes.org.br/en/gartner-identifica-as-principais-tendencias-estrategicas-em-engenharia-de-software-para-2025-e-alem/) |
| "Agentic Coding 驱动研发全生命周期智能化，Agent 不再局限于单一编码任务的辅助执行，而是作为具备自主规划、工具调用与闭环执行能力的开发主体，系统性接管完整研发链路，人类工程师的核心职能从'亲自执行'转向'编排决策'。" | C1 第七章第 1 条，第 26 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |
| "研发流程层面，推动 AI 能力深度融合需求分析、代码生成、测试验证与部署运维等核心环节。" | C1 第七章第 5 条，第 28 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |

## 6. AI 工具和算力保障

| 素材原文 | 来源 | 链接 |
|---|---|---|
| "Gartner predicts that by 2030, 40% of enterprise application portfolios will consist of custom applications built using AI-native development platforms, compared with 2% in 2025." | G1 趋势① AI-Native Development Platforms | [G1 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) |
| "Local deployment can help organisations address data sovereignty requirements, manage inference costs and support applications where low latency is important." / "Gartner predicts that by 2028, 60% of regulated enterprises will migrate AI workloads to local infrastructure after discovering that a provider's headquarters location, rather than the location of data storage, determines government access." | G1 趋势④ Local AI | [G1 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) |
| "GenAI Platform Engineering leverages established platform engineering approaches to help developers discover, integrate, and safely use GenAI resources in their applications. Gartner predicts that by 2027, 70% of companies with platform teams will include GenAI capabilities in their internal developer platforms." | G4 趋势③ | [G4 转载](https://abes.org.br/en/gartner-identifica-as-principais-tendencias-estrategicas-em-engenharia-de-software-para-2025-e-alem/) |
| "Gartner predicts that by 2028, 30% of total global enterprise spending on GenAI technologies will be on open GenAI models tailored to use cases." | G4 趋势⑤ Growth of GenAI Open Models and Ecosystem | [G4 转载](https://abes.org.br/en/gartner-identifica-as-principais-tendencias-estrategicas-em-engenharia-de-software-para-2025-e-alem/) |
| "AI supercomputing platforms deliver the massive processing power needed to train and run advanced AI models. These systems combine high-performance computing (HPC), specialized processors and scalable architectures to handle data-intensive workloads." / "40% of enterprises will adopt hybrid computing architectures by 2028 (up from 8%)." | G5 趋势 2 AI Supercomputing Platforms | [G5](https://emt.gartnerweb.com/ngw/globalassets/en/chief-information-officer/documents/2026-top-tech-trends.pdf) |
| "Geopatriation is the relocation of workloads from global hyperscale clouds to sovereign or local environments to reduce geopolitical risk." / "75% of enterprises will geopatriate workloads by 2030." | G5 趋势 10 Geopatriation | [G5](https://emt.gartnerweb.com/ngw/globalassets/en/chief-information-officer/documents/2026-top-tech-trends.pdf) |
| "受访企业在软件研发中对大模型的应用普遍选择低成本落地方式，公有云方式占比 31.8%……全栈自研或微调方式占比不足 20%。" / "94%集中于八个系列模型，包括深度求索 DeepSeek 系列、阿里通义千问系列、字节豆包系列、百度文心系列、月之暗面 Kimi 系列、智谱清言 GLM 系列、腾讯混元系列、科大讯飞星火系列。" | C1 第二章第 5、6 条，第 6–7 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |

## 7. Gartner 点名、六方向里没有显式出现的（建议补）

| 项 | 素材原文 | 来源 | 链接 |
|---|---|---|---|
| 成效度量 | "Organizations are shifting focus away from developer experience and toward developer productivity. However, most organizations do not have a clear definition of developer productivity or an established baseline for it." | G2 Key Findings | [G2](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/2026-planning-guide-for-software-engineering.pdf) |
| 成效度量 | "AI code assistants typically drive a 10% to 20% increase in developer productivity. Most of the gains come from enhanced velocity and faster code understanding." / "Avoid chasing vanity metrics and focus on business outcomes and customer experience." | G2 | [G2](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/2026-planning-guide-for-software-engineering.pdf) |
| 成效度量 | "投入成本高，短期投入产出比不明确，关注度升至 26.85%" / "明确智能化研发的落地目标与可量化的效能度量指标" | C1 第 4 页、第 28 页 | [C1](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202604/P020260402599647343221.pdf) |
| 评测体系 | 见第 3 节 eval-driven development 两条；Gartner 单列为趋势并给出起步规格（约 100 个精选用例、3–5 个指标、放进 CI，该规格来自 Gartner 引用的 DeepEval，非 Gartner 原文） | G1 趋势⑤ | [G1 转载](https://www.expresscomputer.in/news/gartner-identifies-six-software-engineering-trends-shaping-enterprise-ai-development/141439/) |
| 平台工程 | "Platform engineering continues to be a focus for streamlining developer work, but building developer platforms without treating developers as customers will fail to deliver the benefits they anticipate." | G2 Key Findings | [G2](https://emt.gartnerweb.com/ngw/globalassets/en/technical-professionals/documents/2026-planning-guide-for-software-engineering.pdf) |
| 绿色软件工程 | "Building intelligent applications with GenAI consumes a lot of energy, making green software engineering practices essential." | G4 趋势⑥ Green Software Engineering | [G4 转载](https://abes.org.br/en/gartner-identifica-as-principais-tendencias-estrategicas-em-engenharia-de-software-para-2025-e-alem/) |

## 证据边界

- G1、G4 的 gartner.com 原站返回 403，英文原文取自媒体转载页，G1 的数字另与德文转述（ap-verlag）核对一致。
- G2、G3 为公开摘录，部分规划要点在摘录里只有标题没有正文。
- Gartner 文中的百分比均为预测值，不是实测数据。C1 的百分比为问卷结果（2443 份问卷、2109 份有效）。
- 信通院报告依据《智能化软件工程技术和应用要求》《面向软件工程的智能体技术和应用要求》两份标准编写，标准原文未读。

## 待办

- [x] 材料定稿时确认是否补"成效度量"为第七个方向
- [x] 如需国内框架性文件，补读信通院两份标准
