# AgenticPaper

**2026 Agent 系统论文阅读库：离线 Rollout、在线 Serving 与 Sandbox。**

[在线阅读](https://williamericcheung.github.io/AgenticPaper/) · [Release 说明](https://williamericcheung.github.io/AgenticPaper/release.html) · [GitHub Releases](https://github.com/WilliamEricCheung/AgenticPaper/releases) · [构建与维护](docs/DEPLOYMENT.md)

35 篇论文均提供一段概述，以及**面向场景、论文动机、核心机制与贡献、实验设置与对比对象**四部分导读，附 PDF 物理页码依据、结论边界和有限资源切入建议。网站支持方向/用途/发表状态筛选、关键词搜索、独立分享链接、本机收藏和打印。

导读由 AI 辅助生成并对照正文整理，未进行论文实验复现。引用具体结论前请核对原文；发现问题可提交 Issue 并附来源章节。网站源代码和原创导读采用 [MIT License](LICENSE)，第三方论文 PDF 保持原有版权与许可。

## 2026 文献目录

检索与核验日期：**2026-11-24（北京时间）**。本次整理 **35 篇 PDF：新增 33 篇，保留原有 Kimi K3 与 DeltaBox 两篇**。这是围绕系统研究问题筛选的文献快照，不声称穷尽 2026 全部论文。最新收录版本更新至 **2026-11-21**。

## 研究范围与归类规则

关注点是**资源调度、执行优化与状态管理**。Agentic RL 目录以多轮 rollout、环境交互、评分和轨迹交付为核心；完整模型训练、RL 算法和大规模训练并行仅作为必要背景。

这里“离线”指训练/评测/数据生成用途的批量服务，不是 offline RL 算法，也不表示 rollout 不与环境实时交互。在线 Serving 更关注交互延迟、SLO 和公平性；离线 rollout 更关注整批 makespan、有效轨迹吞吐、环境成本，以及组采样、策略版本与训练同步约束。

| 目录 | 数量 | 主要研究对象 |
| --- | --- | --- |
| [Offline Agentic RL Rollout Serving](Offline%20Agentic%20RL%20Rollout%20Serving/README.md) | 9 | 轨迹/组调度、长尾、环境容量、推理—工具执行协同、Harness 接入 |
| [Online Agentic AI Serving](Online%20Agentic%20AI%20Serving/README.md) | 17 | Program/workflow 调度、准入、KV 生命周期、尾延迟、公平性与能效 |
| [Sandbox](Sandbox/README.md) | 9 | 环境启动与准备、池化、暂停恢复、分叉、快照、状态一致性和隔离 |

每篇只保存一份，按**最值得借鉴的主要系统贡献**归类，在分目录索引中标明交叉主题。Kimi K3 归入 Sandbox，重点读 §5.3.2。ThunderAgent 横跨三个方向，主归在线通用推理底座；VenusRL 主归离线，Sandbox 资源共享部分仍值得重点阅读。

### Sandbox as a Tool 与 Agent in Sandbox

本库以**服务用途与执行粒度**分类：

| 阅读分类 | 主要服务对象 | 更值得观察的状态 |
| --- | --- | --- |
| Sandbox as a Tool | Agent 调用的代码、命令、工具执行或环境准备服务 | 工具环境启动/预热、权限、调用间状态复用 |
| Agent in Sandbox | 完整 Agent 任务环境，尤其 RL rollout、评测，也包括完整桌面任务 | 任务级生命周期、进程/文件/GUI 状态、恢复、分叉、结果交付 |

此处 Agent in Sandbox 是按完整任务环境理解的阅读标签；严格意义上的 Harness 进程位置单独记录。用于 RL 不必然意味着 Harness 在沙箱内，模型推理也可以由外部服务提供。跨轮复用状态本身不决定分类。

子目录 [Sandbox as a Tool](Sandbox/Sandbox%20as%20a%20Tool/README.md) 收录 5 篇，[Agent in Sandbox](Sandbox/Agent%20in%20Sandbox/README.md) 收录 2 篇（Kimi K3、TClone）；根目录保留两类通用论文 2 篇（Crab、DeltaBox）。Kimi K3 直接面向 RL/评测，TClone 面向在线 CUA/测试时搜索。详见 [分类证据与样本统计](Sandbox/README.md)，不将当前精选库的数量直接解释为全领域热度。

## 筛选与证据标准

- **正式论文**：优先使用会议官方 proceedings、官方日程、出版社信息。作者主页或 arXiv 声明的录用会注明依据。主会、Workshop、技术报告、预印本分别标注。
- **预印本**：结合可核实的作者/机构、具体系统设计、实验与消融、公开实现或真实工作负载证据筛选。机构和学者背景是参考，不等于论文结论已验证；没有代码的强相关新论文也可以纳入，但明确缺口。
- **代码**：“公开实现已核实”只表示本次看到对应仓库及实现，不表示已复现实验；preview、计划开源、仅提供链接但访问失败分别标注。模型开放也不等于训练或 Sandbox 基础设施开源。
- **引用**：本次未取得统一、可靠、可比的引用量快照，因此不填写猜测的引用数，也不把 GitHub stars 当学术引用。论文已有正式发表或系统实现证据时，不强制要求新预印本已有大量引用。
- **年份**：以 2026 首发、2026 正式发表或 2026 重要更新为主。Continuum 明确标注“2025 首发、2026 更新/Workshop”；RollArt 保存 OSDI 2026 正式版；KAIROS 是 **ASPLOS 2027 录用、2026 公开**。
- **核验范围**：已检查论文来源页、PDF 题名/作者/相关正文、版本和文件结构；未完整审稿式复核所有实验，没有运行任何论文代码或模型训练。所有“小规模切入”都是研究建议。

**阅读优先级**：P0 最贴近当前问题，应先读；P1 用于机制对照或扩展；P2 为方法/背景或偏离系统主线的补充。P0 不表示比已录用 P1 论文更可靠。

## 建议先读的三条线

1. **环境和 Sandbox，优先投入 CPU/系统资源**：Kimi K3 §5.3.2 → DeltaBox → Crab → Readie。分别回答生产需求、怎样快速保存状态、何时值得保存状态、如何减少准备成本。
2. **离线 Agent Serving，先把整条执行链测清楚**：Agent Lightning v1.0 → CAAS → Heddle → VenusRL → RollArt。重点看 Harness/环境的边界、batch tail、组完成和环境容量，训练参数更新不是本轮主线。
3. **少量 GPU 的在线 Serving**：Agentix → ThunderAgent → Continuum → MARS / AgentServe → Ask the Tool / TripleKV。先比较程序级调度、简单 TTL、工作流准入，再讨论更复杂的预测和多层 KV 管理。

Production Agent Serving 测量论文可穿插先读，帮助避免不符合真实工作流的假设。Evolving Infra、Libra、DynaRL 的集群设计值得学习，但不应因论文规模大就把完整复现当成近期前提。

## 全部论文

以下短名直接链接本地 PDF；完整题名、机构、代码、阅读重点和归类理由见各目录 README。

### Offline Agentic RL Rollout Serving

| 优先级 | 论文（本地 PDF） | 当前版本日期 | 发表状态 |
| --- | --- | --- | --- |
| P0 | [CAAS](Offline%20Agentic%20RL%20Rollout%20Serving/2026_CAAS_2611.16661.pdf) | 2026-11-12 | 技术报告，2026-11；未核实正式录用 |
| P0 | [Heddle](Offline%20Agentic%20RL%20Rollout%20Serving/2026_Heddle_2603.28101.pdf) | 2026-03-30 | 预印本；未核实正式录用 |
| P0 | [VenusRL](Offline%20Agentic%20RL%20Rollout%20Serving/2026_VenusRL_2610.03286.pdf) | 2026-10-02 | 预印本；未核实正式录用 |
| P0 | [RollArt](Offline%20Agentic%20RL%20Rollout%20Serving/2026_RollArt_RollArt.pdf) | 2026-07 | OSDI 2026，官方 proceedings 已核实 |
| P0 | [AgentLightning-v1](Offline%20Agentic%20RL%20Rollout%20Serving/2026_AgentLightning-v1_2608.17528.pdf) | 2026-08-18 | 技术论文/预印本；未核实该 v1.0 论文正式录用 |
| P1 | [Libra](Offline%20Agentic%20RL%20Rollout%20Serving/2026_Libra_2606.03077.pdf) | 2026-09-16 | 预印本，v3；未核实正式录用 |
| P1 | [RollPacker](Offline%20Agentic%20RL%20Rollout%20Serving/2026_RollPacker_RollPacker.pdf) | 2026-05 | NSDI 2026，官方 proceedings 已核实 |
| P1 | [DynaRL](Offline%20Agentic%20RL%20Rollout%20Serving/2026_DynaRL_DynaRL.pdf) | 2026-07 | OSDI 2026，官方 proceedings 已核实 |
| P2 | [EnvSched](Offline%20Agentic%20RL%20Rollout%20Serving/2026_EnvSched_2610.37609.pdf) | 2026-10-27 | 预印本；未核实正式录用 |

### Online Agentic AI Serving

| 优先级 | 论文（本地 PDF） | 当前版本日期 | 发表状态 |
| --- | --- | --- | --- |
| P0 | [Agentix](Online%20Agentic%20AI%20Serving/2026_Agentix_Agentix.pdf) | 2026-05 | NSDI 2026，官方 proceedings 已核实 |
| P0 | [ThunderAgent](Online%20Agentic%20AI%20Serving/2026_ThunderAgent_2602.13692.pdf) | 2026-06-30 | ICML 2026，PMLR 官方条目已核实；本地为 arXiv v3 |
| P0 | [MARS](Online%20Agentic%20AI%20Serving/2026_MARS_2604.26963.pdf) | 2026-11-10 | 预印本，v3；未核实正式录用 |
| P0 | [Continuum](Online%20Agentic%20AI%20Serving/2026_Continuum_2511.02230.pdf) | 2026-09-08 | ICLR 2026 LLA Workshop（作者主页）；2025 首发、2026 v7 更新 |
| P0 | [TripleKV](Online%20Agentic%20AI%20Serving/2026_TripleKV_2611.25112.pdf) | 2026-11-21 | 预印本，2026-11-21 v2；未核实正式录用 |
| P0 | [Ask-the-Tool](Online%20Agentic%20AI%20Serving/2026_Ask-the-Tool_2609.18849.pdf) | 2026-09-16 | 预印本；未核实正式录用 |
| P0 | [AgentServe](Online%20Agentic%20AI%20Serving/2026_AgentServe_2603.10342.pdf) | 2026-11-05 | IEEE TC 录用（arXiv 作者声明及关联 DOI）；出版社页本次未能打开 |
| P1 | [AgentWeave](Online%20Agentic%20AI%20Serving/2026_AgentWeave_2610.14804.pdf) | 2026-11-10 | NeurIPS 2026 Main Track Poster（作者仓库与 EPFL 公告） |
| P1 | [EvolvingInfra](Online%20Agentic%20AI%20Serving/2026_EvolvingInfra_2611.12304.pdf) | 2026-11-12 | 预印本，v2；未核实正式录用 |
| P0 | [Production-Agent-Serving](Online%20Agentic%20AI%20Serving/2026_Production-Agent-Serving_2609.34432.pdf) | 2026-09-28 | 生产负载测量预印本；未核实正式录用 |
| P1 | [TAO](Online%20Agentic%20AI%20Serving/2026_TAO_2610.37230.pdf) | 2026-10-27 | 预印本；未核实正式录用 |
| P1 | [Duru](Online%20Agentic%20AI%20Serving/2026_Duru_2611.23558.pdf) | 2026-11-17 | 预印本，2026-11；未核实正式录用 |
| P1 | [KAIROS](Online%20Agentic%20AI%20Serving/2026_KAIROS_2604.16682.pdf) | 2026-11-10 | ASPLOS 2027 录用（作者主页及 PDF）；2026 年公开版本 |
| P1 | [Nalar](Online%20Agentic%20AI%20Serving/2026_Nalar_2601.05109.pdf) | 2026-09-30 | 预印本，v2；未核实正式录用 |
| P2 | [AgentServeSim](Online%20Agentic%20AI%20Serving/2026_AgentServeSim_2606.09613.pdf) | 2026-09-05 | 预印本，v3；未核实正式录用 |
| P2 | [AgentOpt](Online%20Agentic%20AI%20Serving/2026_AgentOpt_2604.06296.pdf) | 2026-04-15 | 技术报告；未核实正式录用 |
| P2 | [Software-Defined-Agentic-Serving](Online%20Agentic%20AI%20Serving/2026_Software-Defined-Agentic-Serving_2601.03197.pdf) | 2026-01-06 | 架构立场/短文预印本；未核实正式录用 |

### Sandbox

| 优先级 | 论文（本地 PDF） | 当前版本日期 | 发表状态 |
| --- | --- | --- | --- |
| P0 | [Kimi-K3](Sandbox/Agent%20in%20Sandbox/KIMI%20K3%20OPEN%20FRONTIER%20INTELLIGENCE.pdf) | 2026-08-07 | Kimi Team 技术报告；保留用户已有 PDF |
| P0 | [DeltaBox](Sandbox/DeltaBox.pdf) | 2026-11-13 | SIGOPS ATC 2026，会议官方日程及本地正式版已核实 |
| P0 | [Crab](Sandbox/2026_Crab_2604.28138.pdf) | 2026-04-30 | 预印本；未核实正式录用 |
| P0 | [Readie](Sandbox/Sandbox%20as%20a%20Tool/2026_Readie_2611.22171.pdf) | 2026-11-17 | 预印本，2026-11-17；未核实正式录用 |
| P1 | [Planarian](Sandbox/Sandbox%20as%20a%20Tool/2026_Planarian_2609.35366.pdf) | 2026-09-28 | 预印本；未核实正式录用 |
| P1 | [TClone](Sandbox/Agent%20in%20Sandbox/2026_TClone_2605.17320.pdf) | 2026-05-17 | 预印本；未核实正式录用 |
| P1 | [HerAgent](Sandbox/Sandbox%20as%20a%20Tool/2026_HerAgent_2611.18443.pdf) | 2026-11-13 | 预印本，2026-11-13；未核实 TSE 或其他正式录用 |
| P1 | [Sandlock](Sandbox/Sandbox%20as%20a%20Tool/2026_Sandlock_2605.26298.pdf) | 2026-05-25 | 预印本；未核实正式录用 |
| P2 | [SpecBox](Sandbox/Sandbox%20as%20a%20Tool/2026_SpecBox_2607.23933.pdf) | 2026-08-05 | 预印本，v2；未核实该题名的正式录用 |

## 暂不纳入精选 PDF 的候选与补充入口

| 候选 | 本次处理理由 |
| --- | --- |
| [WAR](https://arxiv.org/abs/2607.17299) | 主题相关，但本次 PDF/来源未核实足够的作者机构、正式录用或代码证据，暂留待核实；不据此否定论文质量。 |
| [SAGA: Workflow-Atomic Scheduling](https://arxiv.org/abs/2605.00528) | 发现部分版本/搜索结果标注 HPDC 2026，但[官方 program](https://hpdc.sci.utah.edu/2026/program.html)中可核对的 SAGA 是不同题名、不同作者的图分析论文。该 Agent Serving 论文的录用信息未得到一致确认，暂不以“HPDC 已录用”纳入。 |
| [InferCept](https://proceedings.mlr.press/v235/abhyankar24a.html) | 重要历史背景，但为 ICML 2024，未放入本次 2026 PDF 主库。 |
| [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)、[Kubernetes agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | 属于可参考的基础设施项目；本次不把项目文档包装成已发表论文。 |

## 适合有限 GPU 资源的验证方式

这些是从文献机制推导的实验入口，不是论文已证明在任意低资源配置均有效：

| 研究问题 | 可先做的低成本实验 | 后续必须补的证据 |
| --- | --- | --- |
| 冷启动/环境准备 | CPU 节点固定镜像集合；对比按需、预安装、固定池、TTL、元数据预取 | 同一任务集/隔离边界下的端到端时间、内存时间积分、误预热与清理成本 |
| Rollout 长尾与环境准入 | 保留前后依赖的闭环 trace replay；限制环境并发、注入时延与失败 | 小规模真实模型/工具执行；组完成、轨迹完整性、policy version 与质量约束 |
| C/R 与 fork | shell/文件/进程状态微基准和少量真实 Agent 任务 | 正确性、外部副作用、共置干扰、失败恢复与存储成本 |
| KV/工具协同 | 单卡或少量 GPU、自托管小模型；对比 FCFS、程序级调度、TTL、准入限制 | 真实 KV 压力下的 JCT/P95/P99、重算/搬运开销、成功率和公平性 |

测量时分别记录 queueing、环境准备、Harness startup、模型等待、tool execution、verifier、数据就绪、失败/取消、cleanup 和资源成本。固定到达时间的开环重放可能破坏 Agent 下一轮的因果关系；模拟结果应与小规模真实执行校准。

## 文件与维护

- `papers.json` 保存全部 35 篇的来源、版本、相对路径、归类、代码核验说明、PDF 页数/字节数/SHA-256，便于以后去重和更新；Sandbox 条目另外分别记录服务用途归类、Harness 物理部署、证据及核验日期。
- 新文件命名：`2026_<短名>_<arXiv ID 或会议短名>.pdf`；前缀表示本轮 2026 阅读集合，确切首发年份见索引。
- 原有 `Sandbox/DeltaBox.pdf` 与 `Sandbox/Agent in Sandbox/KIMI K3 OPEN FRONTIER INTELLIGENCE.pdf` 原名原内容保留（Kimi K3 已移入子目录）。PDF 不跨目录重复复制。
- 本项目分享公开论文、原创导读和网站源码，不包含私有实验数据或凭据。收录阶段未运行论文代码；后续更新应重新核实论文版本、录用与代码状态。

## 本地构建

```sh
python3 scripts/build_site.py
python3 scripts/validate_site.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory _site
```

打开 `http://127.0.0.1:8765/`。构建只使用 Python 标准库，无 npm 或服务端依赖。`content/` 保存可维护的逐篇导读，`web/assets/` 保存前端样式与交互，`scripts/` 生成静态网站；`_site/` 为忽略的构建产物。推送 main 后由 GitHub Actions 检查并部署到 Pages。详见 [部署说明](docs/DEPLOYMENT.md)。
