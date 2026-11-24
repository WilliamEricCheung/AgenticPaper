# Online Agentic AI Serving

[返回总索引](../README.md) · 核验日期：2026-11-24

本目录 17 篇。P0 为优先精读，P1 为重要对照，P2 为扩展/方法参考；优先级不代表同行评审等级。

| 优先级 | 论文（本地 PDF） | 当前版本日期 | 发表状态 |
| --- | --- | --- | --- |
| P0 | [Agentix](2026_Agentix_Agentix.pdf) | 2026-05 | NSDI 2026，官方 proceedings 已核实 |
| P0 | [ThunderAgent](2026_ThunderAgent_2602.13692.pdf) | 2026-06-30 | ICML 2026，PMLR 官方条目已核实；本地为 arXiv v3 |
| P0 | [MARS](2026_MARS_2604.26963.pdf) | 2026-11-10 | 预印本，v3；未核实正式录用 |
| P0 | [Continuum](2026_Continuum_2511.02230.pdf) | 2026-09-08 | ICLR 2026 LLA Workshop（作者主页）；2025 首发、2026 v7 更新 |
| P0 | [TripleKV](2026_TripleKV_2611.25112.pdf) | 2026-11-21 | 预印本，2026-11-21 v2；未核实正式录用 |
| P0 | [Ask-the-Tool](2026_Ask-the-Tool_2609.18849.pdf) | 2026-09-16 | 预印本；未核实正式录用 |
| P0 | [AgentServe](2026_AgentServe_2603.10342.pdf) | 2026-11-05 | IEEE TC 录用（arXiv 作者声明及关联 DOI）；出版社页本次未能打开 |
| P1 | [AgentWeave](2026_AgentWeave_2610.14804.pdf) | 2026-11-10 | NeurIPS 2026 Main Track Poster（作者仓库与 EPFL 公告） |
| P1 | [EvolvingInfra](2026_EvolvingInfra_2611.12304.pdf) | 2026-11-12 | 预印本，v2；未核实正式录用 |
| P0 | [Production-Agent-Serving](2026_Production-Agent-Serving_2609.34432.pdf) | 2026-09-28 | 生产负载测量预印本；未核实正式录用 |
| P1 | [TAO](2026_TAO_2610.37230.pdf) | 2026-10-27 | 预印本；未核实正式录用 |
| P1 | [Duru](2026_Duru_2611.23558.pdf) | 2026-11-17 | 预印本，2026-11；未核实正式录用 |
| P1 | [KAIROS](2026_KAIROS_2604.16682.pdf) | 2026-11-10 | ASPLOS 2027 录用（作者主页及 PDF）；2026 年公开版本 |
| P1 | [Nalar](2026_Nalar_2601.05109.pdf) | 2026-09-30 | 预印本，v2；未核实正式录用 |
| P2 | [AgentServeSim](2026_AgentServeSim_2606.09613.pdf) | 2026-09-05 | 预印本，v3；未核实正式录用 |
| P2 | [AgentOpt](2026_AgentOpt_2604.06296.pdf) | 2026-04-15 | 技术报告；未核实正式录用 |
| P2 | [Software-Defined-Agentic-Serving](2026_Software-Defined-Agentic-Serving_2601.03197.pdf) | 2026-01-06 | 架构立场/短文预印本；未核实正式录用 |

## 逐篇阅读索引

### Agentix — P0

**Agentix: An Efficient Serving Engine for LLM Agents as General Programs**

[本地 PDF](2026_Agentix_Agentix.pdf) · [原始论文页](https://www.usenix.org/conference/nsdi26/presentation/luo) · 2026 proceedings · 18 页

- **时间与发表状态**：NSDI 2026，官方 proceedings 已核实。当前文件版本日期：2026-05；首发日期：见正式会议条目。
- **纳入依据**：UC Berkeley、Google DeepMind、上海交大；Joseph Gonzalez、Ion Stoica 等；正式系统论文。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：以程序/动态 DAG 为对象的 PLAS、ATLAS 调度及跨引擎局部性路由；对照 request-level FCFS。
- **小规模切入（分析建议，未经本地实验）**：先单引擎比较 program JCT、尾延迟和饥饿，再扩展多引擎。
- **归类理由与边界**：主目标为 Agent 程序端到端在线延迟；早期名称 Autellix，不重复收录旧名。

### ThunderAgent — P0

**ThunderAgent: A Simple, Fast and Program-Aware Agentic Inference System**

[本地 PDF](2026_ThunderAgent_2602.13692.pdf) · [原始论文页](https://arxiv.org/abs/2602.13692) · 2602.13692v3 · 34 页

- **时间与发表状态**：ICML 2026，PMLR 官方条目已核实；本地为 arXiv v3。当前文件版本日期：2026-06-30；首发日期：2026-02-14。
- **纳入依据**：Georgia Tech、UIUC、CMU、Together AI 等；正式会议论文和公开系统实现。
- **代码/工件**：[公开实现及 MIT 许可证已核实](https://github.com/ThunderAgent-org/ThunderAgent)。
- **重点读什么**：LLM Program 统一 KV、工具环境及外部资产；program-aware admission、KV 工作集和异步环境准备。
- **小规模切入（分析建议，未经本地实验）**：优先读环境准备/工作集管理；作为 Serving–Rollout–Sandbox 跨层联合优化基线。
- **归类理由与边界**：三类均覆盖，按通用 agentic inference 调度抽象归在线；离线和 Sandbox 均应交叉阅读。
- **补充核验来源**：[来源 1](https://proceedings.mlr.press/v306/kang26j.html)。

### MARS — P0

**MARS: Towards High Goodput and Low KV Thrashing in Agent Serving under GPU Memory Constraints**

[本地 PDF](2026_MARS_2604.26963.pdf) · [原始论文页](https://arxiv.org/abs/2604.26963) · 2604.26963v3 · 13 页

- **时间与发表状态**：预印本，v3；未核实正式录用。当前文件版本日期：2026-11-10；首发日期：2026-04-14。
- **纳入依据**：Duke University；Danyang Zhuo、Yiran Chen、Hai Li 等；有公开 preview 实现。
- **代码/工件**：[公开 preview 代码已核实](https://github.com/Afterglow231/MARS_preview)；仓库明确部分 benchmark 输入未随预览版提供。
- **重点读什么**：GPU 内存受限时，联合 workflow admission 和引擎内调度，避免 KV thrashing。
- **小规模切入（分析建议，未经本地实验）**：很适合从单卡/有限显存环境研究工作流 goodput；需区分请求吞吐与完整任务成功完成率。
- **归类理由与边界**：面向在线多轮工作流和内存压力，归在线。

### Continuum — P0

**Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live**

[本地 PDF](2026_Continuum_2511.02230.pdf) · [原始论文页](https://arxiv.org/abs/2511.02230) · 2511.02230v7 · 14 页

- **时间与发表状态**：ICLR 2026 LLA Workshop（作者主页）；2025 首发、2026 v7 更新。当前文件版本日期：2026-09-08；首发日期：2025-11-04。
- **纳入依据**：UC Berkeley、Stanford、清华；有 preview 代码；Workshop 不标成 ICLR 主会。
- **代码/工件**：[公开 preview 仓库已核实](https://github.com/Hanchenli/vllm-continuum)。
- **重点读什么**：工具等待期的 KV TTL 保留，与 program-level FCFS 的组合；可作为简单而强的状态保留基线。
- **小规模切入（分析建议，未经本地实验）**：单引擎即可研究 TTL 与队列顺序，仍需真实 KV 内存压力验证。
- **归类理由与边界**：跨工具调用的推理状态管理，归在线；明确保留 2025 首发信息。
- **补充核验来源**：[来源 1](https://runyuanhe.github.io/publications/)。

### TripleKV — P0

**TripleKV: Predict, Prefetch, Protect - KV Cache Management for AI Agents**

[本地 PDF](2026_TripleKV_2611.25112.pdf) · [原始论文页](https://arxiv.org/abs/2611.25112) · 2611.25112v2 · 13 页

- **时间与发表状态**：预印本，2026-11-21 v2；未核实正式录用。当前文件版本日期：2026-11-21；首发日期：2026-11-18。
- **纳入依据**：UIUC、NTUA、IBM Research；Fan Lai、Tianyin Xu、Josep Torrellas 等参与。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：工具结束时机预测；SSD→DRAM 预取、GPU/DRAM 去重与 victim cache；与直接预留 GPU 的区别。
- **小规模切入（分析建议，未经本地实验）**：需要可控制 KV 层级的推理引擎及 SSD；可从单卡加主机内存/SSD 的微基准开始。
- **归类理由与边界**：核心是多轮在线推理 KV 层级管理，归在线；工具等待信号可借鉴到离线。

### Ask-the-Tool — P0

**Ask the Tool, Don't Guess: Agent Tool Calls Hold Their Progress, and the Serving System Should Read It**

[本地 PDF](2026_Ask-the-Tool_2609.18849.pdf) · [原始论文页](https://arxiv.org/abs/2609.18849) · 2609.18849v1 · 23 页

- **时间与发表状态**：预印本；未核实正式录用。当前文件版本日期：2026-09-16；首发日期：2026-09-16。
- **纳入依据**：清华、浙大、阿里云；Huanchen Zhang、Feifei Li 等；包含真实工具进度信号分析。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：从正在执行的工具获取进度，而不是只按工具名预测时长；用信号决定 KV 保留、迁出和迁回。
- **小规模切入（分析建议，未经本地实验）**：先给少数工具加只读进度观测，并固定语义与输出；模型 API 可做信号研究，KV 收益需可控引擎。
- **归类理由与边界**：贡献落在工具信号驱动的 serving 状态管理，归在线、交叉 Sandbox。

### AgentServe — P0

**AgentServe: Algorithm-System Co-Design for Efficient Agentic AI Serving on a Consumer-Grade GPU**

[本地 PDF](2026_AgentServe_2603.10342.pdf) · [原始论文页](https://arxiv.org/abs/2603.10342) · 2603.10342v2 · 14 页

- **时间与发表状态**：IEEE TC 录用（arXiv 作者声明及关联 DOI）；出版社页本次未能打开。当前文件版本日期：2026-11-05；首发日期：2026-03-11。
- **纳入依据**：悉尼大学、西悉尼大学、南昆士兰大学等；单张消费级 GPU 的系统研究。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：区分 cold prefill、resume prefill 与短 decode；用预算和 CUDA Green Context 控制干扰。
- **小规模切入（分析建议，未经本地实验）**：直接贴合有限 GPU；复现前检查 GPU 和 CUDA 对 Green Context 的支持。
- **归类理由与边界**：明确面向单 GPU 在线 Agent serving；不要与 AgServe 同名近似工作混淆。
- **补充核验来源**：[来源 1](https://doi.org/10.1109/TC.2026.3745924)。

### AgentWeave — P1

**AgentWeave: Efficient Distributed Agent Serving via Flow Decomposition**

[本地 PDF](2026_AgentWeave_2610.14804.pdf) · [原始论文页](https://arxiv.org/abs/2610.14804) · 2610.14804v2 · 21 页

- **时间与发表状态**：NeurIPS 2026 Main Track Poster（作者仓库与 EPFL 公告）。当前文件版本日期：2026-11-10；首发日期：2026-10-10。
- **纳入依据**：中山大学与 EPFL；Rachid Guerraoui、Anne-Marie Kermarrec 等；公开代码。
- **代码/工件**：[已看到 src/agentweave 和实验脚本](https://github.com/Guodanding/agentweave)。
- **重点读什么**：聚合部署的 flow decomposition，减少长请求阻塞和 workflow 批处理气泡。
- **小规模切入（分析建议，未经本地实验）**：可先在小型工作流上验证细粒度切分；多模块模型共部署可能仍需多 GPU。
- **归类理由与边界**：主目标为在线分布式工作流 latency/throughput，归在线。
- **补充核验来源**：[来源 1](https://actu.epfl.ch/news/epflneurips-2026/)。

### EvolvingInfra — P1

**Evolving Infra: Agent-Adaptive LLM Serving at Scale**

[本地 PDF](2026_EvolvingInfra_2611.12304.pdf) · [原始论文页](https://arxiv.org/abs/2611.12304) · 2611.12304v2 · 40 页

- **时间与发表状态**：预印本，v2；未核实正式录用。当前文件版本日期：2026-11-12；首发日期：2026-11-09。
- **纳入依据**：Georgia Tech、UIUC、UC Berkeley、MIT、NVIDIA、OpenAI 等；公开系统实现。
- **代码/工件**：[公开实现已核实](https://github.com/mit-han-lab/EvolvingInfra)。
- **重点读什么**：将 P/D 计算角色调整与 KV 状态管理解耦，用 agent context 信号控制分布式 KV。
- **小规模切入（分析建议，未经本地实验）**：论文包含最多 256 GB300 的实验；小资源先读接口与信号设计，不把完整集群复现列为近期目标。
- **归类理由与边界**：分布式在线推理架构；交叉离线但非 RL trainer 优化。

### Production-Agent-Serving — P0

**Semantics, Workflows, and Infrastructure: Understanding Agent Serving at Production Scale**

[本地 PDF](2026_Production-Agent-Serving_2609.34432.pdf) · [原始论文页](https://arxiv.org/abs/2609.34432) · 2609.34432v1 · 13 页

- **时间与发表状态**：生产负载测量预印本；未核实正式录用。当前文件版本日期：2026-09-28；首发日期：2026-09-28。
- **纳入依据**：香港中文大学（深圳）与 Ant Group；两周、1170 万请求的生产 trace 分析。
- **代码/工件**：论文写计划发布脱敏 traces；本次未核实公开下载，不把计划当已发布。
- **重点读什么**：task semantics、workflow dependencies、跨任务 context reuse；用来约束研究假设，而非照搬请求级负载。
- **小规模切入（分析建议，未经本地实验）**：阅读与统计方法不需 GPU；若 traces 不可得，需自采或明确标注合成数据。
- **归类理由与边界**：测量对象是生产 Agent serving，归在线；可指导离线 trace 设计。

### TAO — P1

**TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving**

[本地 PDF](2026_TAO_2610.37230.pdf) · [原始论文页](https://arxiv.org/abs/2610.37230) · 2610.37230v1 · 26 页

- **时间与发表状态**：预印本；未核实正式录用。当前文件版本日期：2026-10-27；首发日期：2026-10-27。
- **纳入依据**：上海交大与 Stanford；Yinyu Ye、Dongdong Ge 等；有明确容量约束及联合选择/放置设计。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：工具就绪度、节点 KV 局部性和 token footprint 联合进入 admission/placement。
- **小规模切入（分析建议，未经本地实验）**：先比较简单 FIFO、局部性贪心和工具就绪启发式；动态规划的收益与开销都需测量。
- **归类理由与边界**：推理和 CPU 工具协同，但优化在线服务指标，归在线。

### Duru — P1

**Towards Fair Resource Sharing in Agentic LLM Serving**

[本地 PDF](2026_Duru_2611.23558.pdf) · [原始论文页](https://arxiv.org/abs/2611.23558) · 2611.23558v1 · 15 页

- **时间与发表状态**：预印本，2026-11；未核实正式录用。当前文件版本日期：2026-11-17；首发日期：2026-11-17。
- **纳入依据**：UIUC 与 Gimlet Labs；作者研究组项目页可核实，研究 agent-level slowdown 公平性。
- **代码/工件**：有[官方项目页](https://shepherdgroup.web.illinois.edu/duru/)；本次未核实系统代码发布。
- **重点读什么**：跨 router/runtime 的 slowdown 观测、准入例外和调度；避免只优化平均时延而掩盖饥饿。
- **小规模切入（分析建议，未经本地实验）**：小规模多租户负载即可研究相对独占执行的 slowdown；自动扩容部分需额外资源。
- **归类理由与边界**：在线多租户公平共享，归在线。

### KAIROS — P1

**KAIROS: Stateful, Context-Aware Power-Efficient Agentic Inference Serving**

[本地 PDF](2026_KAIROS_2604.16682.pdf) · [原始论文页](https://arxiv.org/abs/2604.16682) · 2604.16682v2 · 21 页

- **时间与发表状态**：ASPLOS 2027 录用（作者主页及 PDF）；2026 年公开版本。当前文件版本日期：2026-11-10；首发日期：2026-04-17。
- **纳入依据**：UIUC 与 University of Michigan；Mosharaf Chowdhury、Nishil Talati；录用年份已纠正。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：联合 GPU 频率、并发度和 agent placement；分析降频为何可能加剧 context thrashing。
- **小规模切入（分析建议，未经本地实验）**：可从单卡功耗/频率实验开始，但需要 GPU 管理权限及可靠功耗测量。
- **归类理由与边界**：Agent 在线推理能效；按预印本公开年份进入 2026 文献库。
- **补充核验来源**：[来源 1](https://sites.google.com/site/nishiltalatipersonal/)。

### Nalar — P1

**Nalar: Workflow-Aware Management of Agentic Applications**

[本地 PDF](2026_Nalar_2601.05109.pdf) · [原始论文页](https://arxiv.org/abs/2601.05109) · 2601.05109v2 · 19 页

- **时间与发表状态**：预印本，v2；未核实正式录用。当前文件版本日期：2026-09-30；首发日期：2026-01-08。
- **纳入依据**：UT Austin 与 Cisco Research；Aditya Akella 团队；系统接口与工作流实验较完整。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：Python futures 暴露动态依赖；全局策略与本地执行分层，跨工具/模型管理上下文。
- **小规模切入（分析建议，未经本地实验）**：可用小型异构工作流和 API 开始研究调度接口；KV 层需自托管推理。
- **归类理由与边界**：通用 Agent workflow serving runtime，归在线。

### AgentServeSim — P2

**AgentServeSim: Serving-System Simulation and Policy Search for LLM Agent Programs**

[本地 PDF](2026_AgentServeSim_2606.09613.pdf) · [原始论文页](https://arxiv.org/abs/2606.09613) · 2606.09613v3 · 13 页

- **时间与发表状态**：预印本，v3；未核实正式录用。当前文件版本日期：2026-09-05；首发日期：2026-06-08。
- **纳入依据**：University of Central Florida，Qian Lou 团队；报告真实引擎对照的模拟误差，作为方法参考。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：Program Control Block、因果释放下一轮、KV retention 与 dispatch 分离；有助于低成本筛选调度策略。
- **小规模切入（分析建议，未经本地实验）**：模拟器设计可在 CPU 上研究；本次未核实代码，且仿真不能替代目标硬件测量。
- **归类理由与边界**：模拟的是多轮 Agent serving；可用于离线 rollout 调度预筛，但此处归在线方法参考。

### AgentOpt — P2

**AgentOpt v0.1 Technical Report: Client-Side Optimization for LLM-Based Agent**

[本地 PDF](2026_AgentOpt_2604.06296.pdf) · [原始论文页](https://arxiv.org/abs/2604.06296) · 2604.06296v2 · 24 页

- **时间与发表状态**：技术报告；未核实正式录用。当前文件版本日期：2026-04-15；首发日期：2026-04-07。
- **纳入依据**：Microsoft Research、Cornell、Columbia；有公开 Python 包实现与 benchmark。
- **代码/工件**：[公开代码已核实](https://github.com/AgentOptimizer/agentopt)。
- **重点读什么**：客户端多阶段模型选择、API 成本/质量/延迟权衡；与底层资源调度分开阅读。
- **小规模切入（分析建议，未经本地实验）**：API 预算即可做小实验；偏应用配置优化，不是 Sandbox/引擎系统主线。
- **归类理由与边界**：Serving 客户端优化，作为 P2 扩展。

### Software-Defined-Agentic-Serving — P2

**Software-Defined Agentic Serving**

[本地 PDF](2026_Software-Defined-Agentic-Serving_2601.03197.pdf) · [原始论文页](https://arxiv.org/abs/2601.03197) · 2601.03197v1 · 7 页

- **时间与发表状态**：架构立场/短文预印本；未核实正式录用。当前文件版本日期：2026-01-06；首发日期：2026-01-06。
- **纳入依据**：UT Austin 与 Cisco Research；Aditya Akella 团队；与 Nalar 对照理解接口设计。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：借鉴 SDN 控制思想，讨论运行时可编程 Agent 通信与 serving 协同。
- **小规模切入（分析建议，未经本地实验）**：主要用于问题定义与架构讨论；不按完整高性能系统或可复现实现评价。
- **归类理由与边界**：在线 serving 架构观点；与 Nalar 是相关但题名与论文不同的两篇。
