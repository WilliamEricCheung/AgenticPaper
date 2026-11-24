# Offline Agentic RL Rollout Serving

[返回总索引](../README.md) · 核验日期：2026-11-24

本目录 9 篇。P0 为优先精读，P1 为重要对照，P2 为扩展/方法参考；优先级不代表同行评审等级。

| 优先级 | 论文（本地 PDF） | 当前版本日期 | 发表状态 |
| --- | --- | --- | --- |
| P0 | [CAAS](2026_CAAS_2611.16661.pdf) | 2026-11-12 | 技术报告，2026-11；未核实正式录用 |
| P0 | [Heddle](2026_Heddle_2603.28101.pdf) | 2026-03-30 | 预印本；未核实正式录用 |
| P0 | [VenusRL](2026_VenusRL_2610.03286.pdf) | 2026-10-02 | 预印本；未核实正式录用 |
| P0 | [RollArt](2026_RollArt_RollArt.pdf) | 2026-07 | OSDI 2026，官方 proceedings 已核实 |
| P0 | [AgentLightning-v1](2026_AgentLightning-v1_2608.17528.pdf) | 2026-08-18 | 技术论文/预印本；未核实该 v1.0 论文正式录用 |
| P1 | [Libra](2026_Libra_2606.03077.pdf) | 2026-09-16 | 预印本，v3；未核实正式录用 |
| P1 | [RollPacker](2026_RollPacker_RollPacker.pdf) | 2026-05 | NSDI 2026，官方 proceedings 已核实 |
| P1 | [DynaRL](2026_DynaRL_DynaRL.pdf) | 2026-07 | OSDI 2026，官方 proceedings 已核实 |
| P2 | [EnvSched](2026_EnvSched_2610.37609.pdf) | 2026-10-27 | 预印本；未核实正式录用 |

## 逐篇阅读索引

### CAAS — P0

**Reducing Batch Makespan for LLM Agent Workloads through Inference-Environment Coordination**

[本地 PDF](2026_CAAS_2611.16661.pdf) · [原始论文页](https://arxiv.org/abs/2611.16661) · 2611.16661v1 · 26 页

- **时间与发表状态**：技术报告，2026-11；未核实正式录用。当前文件版本日期：2026-11-12；首发日期：2026-11-12。
- **纳入依据**：Ant Group Ling Team；论文报告实际模型训练/评测工作流和受控重放消融。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：有限环境容量下，将样本准入与环境执行解耦；以链进度调度工具动作，缩短整批 makespan。重点读 CAAS 和 controlled replay。
- **小规模切入（分析建议，未经本地实验）**：可先在 CPU 环境池上重放动作链与工具时延；真实推理子集验证因果时序，再评估整批完成时间。
- **归类理由与边界**：主目标是批量评测、数据生成和 RL rollout 的完成时间，因此归离线；交叉主题：Sandbox。

### Heddle — P0

**Heddle: A Distributed Orchestration System for Agentic RL Rollout**

[本地 PDF](2026_Heddle_2603.28101.pdf) · [原始论文页](https://arxiv.org/abs/2603.28101) · 2603.28101v1 · 14 页

- **时间与发表状态**：预印本；未核实正式录用。当前文件版本日期：2026-03-30；首发日期：2026-03-30。
- **纳入依据**：北京大学 Xin Jin 团队；作者及机构见 PDF 首页，作者主页也列出该论文。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：trajectory-level 调度、放置、工具等待窗口中的迁移，以及长尾轨迹的并行度调整。
- **小规模切入（分析建议，未经本地实验）**：先研究轨迹级排队与放置；动态模型并行需要多卡，不能用纯 CPU 重放声称复现全系统收益。
- **归类理由与边界**：以训练 rollout 吞吐和长尾为目标，归离线。
- **补充核验来源**：[来源 1](https://bingyangwu.github.io/publication/heddle/)。

### VenusRL — P0

**VenusRL: A Fully Disaggregated Agentic RL System with Priority Scheduling and Scalable Interaction**

[本地 PDF](2026_VenusRL_2610.03286.pdf) · [原始论文页](https://arxiv.org/abs/2610.03286) · 2610.03286v1 · 18 页

- **时间与发表状态**：预印本；未核实正式录用。当前文件版本日期：2026-10-02；首发日期：2026-10-02。
- **纳入依据**：中科院计算所、北航、Infrawaves、上海创智学院等；同时给出组完成调度与环境资源管理设计。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：优先完成能解除训练阻塞的 sample groups；重点比较 admission、KV residency 与 template-keyed sandbox page sharing。
- **小规模切入（分析建议，未经本地实验）**：环境准入和同模板沙箱内存共享可独立研究；PTE/COW 路径需要相应 Linux/虚拟化实现。
- **归类理由与边界**：虽然 Sandbox 部分很贴合，论文总体目标仍是 agentic RL 流水线，主归离线、交叉 Sandbox。

### RollArt — P0

**RollArt: Disaggregated Multi-Task Agentic RL Training at Scale**

[本地 PDF](2026_RollArt_RollArt.pdf) · [原始论文页](https://www.usenix.org/conference/osdi26/presentation/gao) · 2026 proceedings · 20 页

- **时间与发表状态**：OSDI 2026，官方 proceedings 已核实。当前文件版本日期：2026-07；首发日期：见正式会议条目。
- **纳入依据**：HKUST 与阿里巴巴/通义联合工作；USENIX 官方论文页及正式版 PDF。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：按轨迹解耦 generation、environment、reward；CPU 环境集群、无状态 reward 和有界陈旧权重同步的边界。
- **小规模切入（分析建议，未经本地实验）**：抽取环境队列与轨迹异步执行做小实验；完整训练与异构 GPU 分配属于高资源验证。
- **归类理由与边界**：多任务 RL rollout 执行底座；首发预印本为 2025-12，本次保存 2026 正式版。

### AgentLightning-v1 — P0

**Agent Lightning v1.0: Towards Harnessed Agentic RL**

[本地 PDF](2026_AgentLightning-v1_2608.17528.pdf) · [原始论文页](https://arxiv.org/abs/2608.17528) · 2608.17528v1 · 21 页

- **时间与发表状态**：技术论文/预印本；未核实该 v1.0 论文正式录用。当前文件版本日期：2026-08-18；首发日期：2026-08-18。
- **纳入依据**：Microsoft、复旦、浙大、爱丁堡；有公开框架和 coding-agent RL 工作流。
- **代码/工件**：[公开仓库](https://github.com/microsoft/agent-lightning)；本次核实入口，未运行训练。
- **重点读什么**：Harness 掌管环境交互，trainer 经 LLM API proxy 接入；重点看 Rollout API、controller、adapter 和轨迹交付。
- **小规模切入（分析建议，未经本地实验）**：可通过小模型/API 先研究 harness 托管、轨迹采集与故障恢复；训练质量结论仍需真实更新实验。
- **归类理由与边界**：重点是将现成 agent harness 接入 RL，而非在线服务请求调度，归离线。

### Libra — P1

**Libra: Efficient Resource Management for Agentic RL Post-Training**

[本地 PDF](2026_Libra_2606.03077.pdf) · [原始论文页](https://arxiv.org/abs/2606.03077) · 2606.03077v3 · 20 页

- **时间与发表状态**：预印本，v3；未核实正式录用。当前文件版本日期：2026-09-16；首发日期：2026-06-02。
- **纳入依据**：香港中文大学 Hong Xu 团队等；公开代码，论文报告 GPU 与 NPU 两类集群实验。
- **代码/工件**：[公开代码，已看到实现目录和 MIT 许可证](https://github.com/NetX-lab/Libra)。
- **重点读什么**：因果分桶调度缓解 rollout 长尾，跨 rollout/training 调整 worker；区分阶段内和阶段间收益。
- **小规模切入（分析建议，未经本地实验）**：先抽取阶段内调度；论文的 48 A800 / 160 Ascend 910B3 配置说明完整复现资源较高。
- **归类理由与边界**：资源管理覆盖完整 RL，但最相关部分是 rollout 长尾，归离线。

### RollPacker — P1

**RollPacker: Taming Long-Tail Rollouts for RL Post-Training with Tail Batching**

[本地 PDF](2026_RollPacker_RollPacker.pdf) · [原始论文页](https://www.usenix.org/conference/nsdi26/presentation/gao-wei) · 2026 proceedings · 19 页

- **时间与发表状态**：NSDI 2026，官方 proceedings 已核实。当前文件版本日期：2026-05；首发日期：见正式会议条目。
- **纳入依据**：HKUST 与阿里巴巴；正式论文和官方页提供代码链接。
- **代码/工件**：[作者代码入口](https://github.com/Farrrrland/RollPacker)由 USENIX 官方页提供；未运行。
- **重点读什么**：Tail batching 把长尾样本聚到部分轮次；作为同步 rollout 调度强基线，注意它不专门解决 Sandbox。
- **小规模切入（分析建议，未经本地实验）**：可先对长度分布和批次重排做重放；完整评估最多使用 128 H800，不作为低卡起点。
- **归类理由与边界**：属于较通用的 RL rollout 系统，对多轮 Agent 是相邻基线，故 P1。

### DynaRL — P1

**DynaRL: Flexible and Dynamic Scheduling of Large-Scale Reinforcement Learning Training**

[本地 PDF](2026_DynaRL_DynaRL.pdf) · [原始论文页](https://www.usenix.org/conference/osdi26/presentation/wang-yuanqing) · 2026 proceedings · 17 页

- **时间与发表状态**：OSDI 2026，官方 proceedings 已核实。当前文件版本日期：2026-07；首发日期：见正式会议条目。
- **纳入依据**：北大、清华、中科院计算所、北航、上海交大与 Infinigence 等；正式系统论文。
- **代码/工件**：论文写计划发布完整代码；[RLinf 官方更新](https://rlinf.readthedocs.io/en/latest/rst_source/resources/release_v0.3.html)列出动态调度功能，未核验论文实现完整对应关系。
- **重点读什么**：动态超图、资源迁移和多轮 context-aware routing；看工具返回如何触发瓶颈转移。
- **小规模切入（分析建议，未经本地实验）**：可单独分析 routing 与阶段瓶颈；全流水线动态 GPU 迁移是高资源工作。
- **归类理由与边界**：覆盖完整训练，按 rollout 调度参考纳入离线，优先级低于 Heddle/CAAS。

### EnvSched — P2

**EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning**

[本地 PDF](2026_EnvSched_2610.37609.pdf) · [原始论文页](https://arxiv.org/abs/2610.37609) · 2610.37609v1 · 27 页

- **时间与发表状态**：预印本；未核实正式录用。当前文件版本日期：2026-10-27；首发日期：2026-10-27。
- **纳入依据**：北大、西安交大、清华、三星研究、中科院自动化所、港中文；论文提供代码。
- **代码/工件**：[公开仓库入口已核实](https://github.com/Hhankyangg/envsched)。
- **重点读什么**：环境—任务图及历史 reward variance 驱动采样；这里的 scheduling 主要是训练数据/任务选择。
- **小规模切入（分析建议，未经本地实验）**：能研究有限 rollout budget 的任务选择，但收益验证依赖训练质量，不等同于服务调度优化。
- **归类理由与边界**：相关但偏算法与样本效率，作为 P2 扩展阅读，不作为系统主线。
