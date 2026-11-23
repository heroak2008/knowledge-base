---
type: doc
date: 2026-11-23
doc-kind: report
status: draft
---

# AI for 研发能力建设范围：外部依据对照表

> 目标读者：写"独立软件 AI for 研发能力建设范围"材料的作者
> 交付形式：Markdown 表格，每条含原文、来源、链接；一页 PPT 版见 [[AIFor研发能力建设范围-外部依据一页纸.html]]（16:9，七个方向 × ≤3 条，同一来源在一个方向内只出现一次，关键字加粗）
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
