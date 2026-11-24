# Sandbox

[返回总索引](../README.md) · 核验日期：2026-11-24

本目录 9 篇。P0 为优先精读，P1 为重要对照，P2 为扩展/方法参考；优先级不代表同行评审等级。

| 优先级 | 论文（本地 PDF） | 当前版本日期 | 发表状态 |
| --- | --- | --- | --- |
| P0 | [Kimi-K3](Agent%20in%20Sandbox/KIMI%20K3%20OPEN%20FRONTIER%20INTELLIGENCE.pdf) | 2026-08-07 | Kimi Team 技术报告；保留用户已有 PDF |
| P0 | [DeltaBox](DeltaBox.pdf) | 2026-11-13 | SIGOPS ATC 2026，会议官方日程及本地正式版已核实 |
| P0 | [Crab](2026_Crab_2604.28138.pdf) | 2026-04-30 | 预印本；未核实正式录用 |
| P0 | [Readie](Sandbox%20as%20a%20Tool/2026_Readie_2611.22171.pdf) | 2026-11-17 | 预印本，2026-11-17；未核实正式录用 |
| P1 | [Planarian](Sandbox%20as%20a%20Tool/2026_Planarian_2609.35366.pdf) | 2026-09-28 | 预印本；未核实正式录用 |
| P1 | [TClone](Agent%20in%20Sandbox/2026_TClone_2605.17320.pdf) | 2026-05-17 | 预印本；未核实正式录用 |
| P1 | [HerAgent](Sandbox%20as%20a%20Tool/2026_HerAgent_2611.18443.pdf) | 2026-11-13 | 预印本，2026-11-13；未核实 TSE 或其他正式录用 |
| P1 | [Sandlock](Sandbox%20as%20a%20Tool/2026_Sandlock_2605.26298.pdf) | 2026-05-25 | 预印本；未核实正式录用 |
| P2 | [SpecBox](Sandbox%20as%20a%20Tool/2026_SpecBox_2607.23933.pdf) | 2026-08-05 | 预印本，v2；未核实该题名的正式录用 |

## 按服务用途与执行粒度分类

按当前研究关注点，将 **主要承载完整 Agent 任务、RL rollout 或评测环境**的工作归为 **Agent in Sandbox**；将**主要提供代码、命令、工具执行或环境准备能力**的工作归为 **Sandbox as a Tool**。明确覆盖两类的通用机制保留根目录。

这是本论文库采用的阅读分类口径：优先看沙箱为谁服务、管理什么执行单元，不要求论文必须写明 Harness 进程位于沙箱内才能归入 Agent in Sandbox。严格的 Harness 物理部署位置作为独立字段记录；“用于 RL”本身不构成“进程必在沙箱内”的证明。长期保留状态、支持 fork 或一次任务多次调用也不单独决定分类。

| 目录 | PDF 数 | 论文 |
| --- | ---: | --- |
| [Sandbox as a Tool](Sandbox%20as%20a%20Tool/README.md) | 5 | Readie、Planarian、HerAgent、Sandlock、SpecBox |
| [Agent in Sandbox](Agent%20in%20Sandbox/README.md) | 2 | Kimi K3、TClone |
| 根目录：两类通用 | 2 | Crab、DeltaBox |

**如何看当前关注分布**：本库主要归类为工具式的有 5 篇、完整任务环境的有 2 篇，另有 2 篇通用机制。计入通用论文，两条阅读线分别覆盖 7 篇和 4 篇（有重叠）。这是 9 篇精选样本的分布，不是全领域的热度统计。Agent in Sandbox 中，Kimi K3 直接面向 RL/评测；TClone 面向在线 CUA/测试时搜索，因此不能把两篇都计作 RL 系统。

### 逐篇分类依据

| 论文 | 本库归类 | 服务用途依据 |
| --- | --- | --- |
| [Kimi-K3](Agent%20in%20Sandbox/KIMI%20K3%20OPEN%20FRONTIER%20INTELLIGENCE.pdf) | Agent in Sandbox | 主要面向 Kimi K3 后训练与评测，AgentENV 为完整任务/rollout 提供高保真执行环境，并管理 pause/resume、fork、snapshot 与高密度环境生命周期。按 RL 任务环境的服务定位归入本目录。依据：PDF 第 22 页 §5.3.2。 |
| [DeltaBox](DeltaBox.pdf) | 两类通用 | 同时服务完整 Agent 执行状态恢复、RL fan-out，以及宿主侧编排的工具环境；保留根目录。依据：PDF 第 6 页图 3、第 10 页 §5 Integrations。 |
| [Crab](2026_Crab_2604.28138.pdf) | 两类通用 | 面向 Agent sandbox 的通用 checkpoint/restore，明确覆盖 Agent 内置运行和外部调用沙箱两种形态，并包含相应评估；保留根目录。依据：PDF 第 8 页 §6、第 9 页评估表。 |
| [Readie](Sandbox%20as%20a%20Tool/2026_Readie_2611.22171.pdf) | Sandbox as a Tool | 主要优化 Agent 生成代码的执行环境启动与快照准备，沙箱作为代码执行工具服务。依据：PDF 第 1 页摘要。 |
| [Planarian](Sandbox%20as%20a%20Tool/2026_Planarian_2609.35366.pdf) | Sandbox as a Tool | 主要通过工具路由管理本地执行副作用和远端 MCP 状态，恢复后将状态信息交回 Harness。虽支持长期状态与分支，本库按其工具执行/状态管理接口归类。依据：PDF 第 2 页说明、第 4 页图 2。 |
| [TClone](Agent%20in%20Sandbox/2026_TClone_2605.17320.pdf) | Agent in Sandbox | 管理完整 computer-use 任务的 GUI workspace，按轨迹分支进行 fork、探索、rollback 和 commit，而不是只准备一次代码执行。按完整 Agent 任务环境归入本目录；论文主要研究在线 CUA/测试时搜索，并非 RL 训练系统。依据：PDF 第 4–5 页 §3、图 3。 |
| [HerAgent](Sandbox%20as%20a%20Tool/2026_HerAgent_2611.18443.pdf) | Sandbox as a Tool | 主要由环境构建 Agent 调用 Docker 执行、验证和回退安装 block，产出可重放环境；本库按被调用的环境准备工具归类，不将其视为承载 RL rollout 的托管平台。依据：PDF 第 3–4 页 §III 及作者仓库 Core Loop。 |
| [Sandlock](Sandbox%20as%20a%20Tool/2026_Sandlock_2605.26298.pdf) | Sandbox as a Tool | 主要隔离 Agent 调用的命令、脚本、插件及子进程，关注工具调用的权限与启动成本。依据：PDF 第 1–2 页 §1/§2.1。 |
| [SpecBox](Sandbox%20as%20a%20Tool/2026_SpecBox_2607.23933.pdf) | Sandbox as a Tool | 主要根据流式生成中的工具意图预热外部工具沙箱，优化工具服务的资源开销和尾延迟。依据：PDF 第 1 页摘要、第 3–4 页运行时与图 3。 |

页码均为本地 PDF 的物理页码。具体 Harness 部署证据与未确认项见下方逐篇索引。

## 逐篇阅读索引

### Kimi-K3 — P0

- **服务用途归类**：Agent in Sandbox。主要面向 Kimi K3 后训练与评测，AgentENV 为完整任务/rollout 提供高保真执行环境，并管理 pause/resume、fork、snapshot 与高密度环境生命周期。按 RL 任务环境的服务定位归入本目录。依据：PDF 第 22 页 §5.3.2。

- **Harness 物理部署（独立记录）**：待确认。PDF 第 22 页 §5.3.2 描述 AgentENV 的 microVM、pause/resume、fork 和 snapshot，但没有明确给出 Harness 进程的位置。暂停环境等待推理本身不能区分两类。当前公开仓库的外部 API 是工具式接入证据，不足以反推报告中所有训练任务的部署方式。

**Kimi K3: Open Frontier Intelligence**

[本地 PDF](Agent%20in%20Sandbox/KIMI%20K3%20OPEN%20FRONTIER%20INTELLIGENCE.pdf) · [原始论文页](https://arxiv.org/abs/2607.24653) · 2607.24653v2 · 47 页

- **时间与发表状态**：Kimi Team 技术报告；保留用户已有 PDF。当前文件版本日期：2026-08-07；首发日期：2026-07-27。
- **纳入依据**：Moonshot/Kimi 一方技术报告；本地核实 arXiv v2，包含 AgentENV 生产规模与生命周期设计。
- **代码/工件**：报告第 22 页脚注 4 明确给出 [AgentENV 开源仓库](https://github.com/kvcache-ai/AgentENV)，本次已核实公开实现及文档；此前索引遗漏该脚注，现更正。未复现报告中的生产规模与性能；当前仓库能力不直接代表报告版本的全部能力。
- **重点读什么**：重点读 §5.3.2 Sandbox Infrastructure（PDF 第 22 页）及 §5.3.1（第 21 页）：pause/resume、fork、snapshot 和状态保留。
- **小规模切入（分析建议，未经本地实验）**：优先抽取 Linux/microVM 生命周期与高密度机制；不需要复现巨型模型训练。
- **归类理由与边界**：遵循用户指定，以最值得借鉴的 Sandbox 基础设施为主归类；交叉 RL rollout。

### DeltaBox — P0

- **服务用途归类**：两类通用。同时服务完整 Agent 执行状态恢复、RL fan-out，以及宿主侧编排的工具环境；保留根目录。依据：PDF 第 6 页图 3、第 10 页 §5 Integrations。

- **Harness 物理部署（独立记录）**：两种形态。PDF 第 6 页图 3 明确 agent worker 在 sandbox 内；第 10 页 §5 Integrations 同时说明 sandbox-resident workers、host-side LangGraph orchestration，以及 Codex 受管进程树和 exec-server 转发接入。按已说明的集成能力归为两者，不等于每种集成均有同等完整评估。

**DeltaBox: Millisecond-Scale Sandbox Checkpoint and Rollback for Stateful AI Agents**

[本地 PDF](DeltaBox.pdf) · [原始论文页](https://arxiv.org/abs/2605.22781) · 2605.22781v3 · 16 页

- **时间与发表状态**：SIGOPS ATC 2026，会议官方日程及本地正式版已核实。当前文件版本日期：2026-11-13；首发日期：见正式会议条目。
- **纳入依据**：上海交大 IPADS 与华为；Yubin Xia、Haibo Chen 等；本地为 2026-11-13 v3，保留原文件。
- **代码/工件**：[作者开源组织入口已核实](https://github.com/delta-box)。
- **重点读什么**：DeltaFS 与 DeltaCR 将文件和进程状态成对 checkpoint/rollback；关注一致性边界及 fork 扇出。
- **小规模切入（分析建议，未经本地实验）**：Linux 上可独立测 C/R、分叉和内存占用；不需本地大模型，但需匹配内核/CRIU 条件。
- **归类理由与边界**：主贡献是 Sandbox 状态机制；支持外部 harness 调用及受管 agent 进程树，不能只按训练/在线二分。
- **补充核验来源**：[来源 1](https://atc.sigops.org/2026/schedule.html)。

### Crab — P0

- **服务用途归类**：两类通用。面向 Agent sandbox 的通用 checkpoint/restore，明确覆盖 Agent 内置运行和外部调用沙箱两种形态，并包含相应评估；保留根目录。依据：PDF 第 8 页 §6、第 9 页评估表。

- **Harness 物理部署（独立记录）**：两种形态。PDF 第 8 页 §6 Deployment Refinement 明确支持 agent-with-a-sandbox 和 agent-in-a-sandbox；第 9 页评估表包含 sandbox 内 Claude-code/iFlow-cli 与外部 SWE-agent。

**Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes**

[本地 PDF](2026_Crab_2604.28138.pdf) · [原始论文页](https://arxiv.org/abs/2604.28138) · 2604.28138v1 · 15 页

- **时间与发表状态**：预印本；未核实正式录用。当前文件版本日期：2026-04-30；首发日期：2026-04-30。
- **纳入依据**：HKUST Wei Wang 团队；有公开 runtime、安装说明和不需模型 API key 的 smoke demo。
- **代码/工件**：[公开实现已核实](https://github.com/open-agent-infra/crab)；v0 使用 runc、CRIU、ZFS、eBPF。
- **重点读什么**：Agent turn 与 OS effects 联合决定是否 checkpoint、保存哪些状态，并与模型等待重叠。
- **小规模切入（分析建议，未经本地实验）**：Linux 主机可先做 checkpoint 策略和共置干扰实验；需要相应权限与文件系统。
- **归类理由与边界**：主机侧 Sandbox C/R 控制层；与 DeltaBox 的底层状态机制应分层比较。

### Readie — P0

- **服务用途归类**：Sandbox as a Tool。主要优化 Agent 生成代码的执行环境启动与快照准备，沙箱作为代码执行工具服务。依据：PDF 第 1 页摘要。

- **Harness 物理部署（独立记录）**：Sandbox as a Tool。PDF 第 1 页摘要明确将 agent harness 与 code execution 解耦，代码执行卸载到专用 code sandbox；主贡献是工具执行环境的启动快照。

**Readie: Low-Latency Code Sandboxes for AI Agents**

[本地 PDF](Sandbox%20as%20a%20Tool/2026_Readie_2611.22171.pdf) · [原始论文页](https://arxiv.org/abs/2611.22171) · 2611.22171v1 · 14 页

- **时间与发表状态**：预印本，2026-11-17；未核实正式录用。当前文件版本日期：2026-11-17；首发日期：2026-11-17。
- **纳入依据**：UIUC、ByteDance、Columbia；Eugene Wu、Yongjoo Park；明确快照选择问题和启动实验。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：学习一组紧凑启动快照，权衡包/数据覆盖率、存储预算与冷启动成本；Sandbox as a Tool 的直接参考。
- **小规模切入（分析建议，未经本地实验）**：CPU 代码执行与启动快照微基准适合低 GPU 预算；重点比较 fat image、手工快照和固定 warm pool。
- **归类理由与边界**：论文明确 harness 与 code execution 解耦；归 Sandbox，而非模型推理调度。

### Planarian — P1

- **服务用途归类**：Sandbox as a Tool。主要通过工具路由管理本地执行副作用和远端 MCP 状态，恢复后将状态信息交回 Harness。虽支持长期状态与分支，本库按其工具执行/状态管理接口归类。依据：PDF 第 2 页说明、第 4 页图 2。

- **Harness 物理部署（独立记录）**：Sandbox as a Tool。PDF 第 2 页说明 Harness 保留 LLM 调用与 context 构造职责，通过 Planarian 路由工具调用；第 4 页图 2 将 Agent loop 与 local-state Sandbox 分开。快照覆盖本地工具进程与远端补偿状态，不意味着 Harness 进程也被纳入。

**Planarian: Managing Agent State with Statepoints**

[本地 PDF](Sandbox%20as%20a%20Tool/2026_Planarian_2609.35366.pdf) · [原始论文页](https://arxiv.org/abs/2609.35366) · 2609.35366v1 · 14 页

- **时间与发表状态**：预印本；未核实正式录用。当前文件版本日期：2026-09-28；首发日期：2026-09-28。
- **纳入依据**：Imperial College London、IISc/SPARC、Microsoft Security Response Center；Peter Pietzuch、Kapil Vaswani 等。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：Statepoint 将本地进程/文件状态与远端补偿动作结合，暴露 snapshot、rollback、fork。
- **小规模切入（分析建议，未经本地实验）**：CPU/API 工作流可研究状态恢复；远程副作用的可补偿性必须逐类验证。
- **归类理由与边界**：关注完整执行环境和外部状态，而非仅保存聊天历史；主归 Sandbox。

### TClone — P1

- **服务用途归类**：Agent in Sandbox。管理完整 computer-use 任务的 GUI workspace，按轨迹分支进行 fork、探索、rollback 和 commit，而不是只准备一次代码执行。按完整 Agent 任务环境归入本目录；论文主要研究在线 CUA/测试时搜索，并非 RL 训练系统。依据：PDF 第 4–5 页 §3、图 3。

- **Harness 物理部署（独立记录）**：待确认。PDF 第 4–5 页 §3/图 3 明确克隆 GUI workspace、应用进程和文件，描述在分支中运行轨迹，但未明确标出 Harness 进程边界；第 8 页说明 GUI stack 在容器内，也不能据此认定 Agent loop 在内。本库按完整任务环境归类；该分类不等于已核实 Harness 进程位置。

**TClone: Low-Latency Forking of Live GUI Environments for Computer-Use Agents**

[本地 PDF](Agent%20in%20Sandbox/2026_TClone_2605.17320.pdf) · [原始论文页](https://arxiv.org/abs/2605.17320) · 2605.17320v1 · 14 页

- **时间与发表状态**：预印本；未核实正式录用。当前文件版本日期：2026-05-17；首发日期：2026-05-17。
- **纳入依据**：UC San Diego，Yiying Zhang 团队；面向 live GUI workspace 的 fork/COW 系统设计。
- **代码/工件**：论文写接受后将公开 TClone；本次未核实代码已发布。
- **重点读什么**：将快速分支与持久化 checkpoint 解耦；GUI、内存、文件、认证会话的工作区克隆。
- **小规模切入（分析建议，未经本地实验）**：CPU/虚拟化环境可做分支微基准；GUI 与外部服务状态使一致性验证比纯 shell 更复杂。
- **归类理由与边界**：完整 GUI 工作区 Sandbox；不自动等同于 harness 也在其中。

### HerAgent — P1

- **服务用途归类**：Sandbox as a Tool。主要由环境构建 Agent 调用 Docker 执行、验证和回退安装 block，产出可重放环境；本库按被调用的环境准备工具归类，不将其视为承载 RL rollout 的托管平台。依据：PDF 第 3–4 页 §III 及作者仓库 Core Loop。

- **Harness 物理部署（独立记录）**：Sandbox as a Tool。PDF 第 3–4 页 §III 描述控制器生成/修复 block，再在 Docker 环境执行，并使用 docker commit/run 保存与恢复环境；作者仓库 Core Loop 和 CLI 用法进一步显示宿主侧 builder 驱动容器。按所述实现归类，未声称只能支持此形态。

**HerAgent: A Block-Level Checkpointing Harness for Coding-Agent Environment Setup**

[本地 PDF](Sandbox%20as%20a%20Tool/2026_HerAgent_2611.18443.pdf) · [原始论文页](https://arxiv.org/abs/2611.18443) · 2611.18443v1 · 12 页

- **时间与发表状态**：预印本，2026-11-13；未核实 TSE 或其他正式录用。当前文件版本日期：2026-11-13；首发日期：2026-11-13。
- **纳入依据**：UCL、Uppsala、CMU；Federica Sarro、Claire Le Goues、He Ye；研究可重放环境准备。
- **代码/工件**：[作者公开仓库](https://github.com/BeeuniLab/pheragent) 本次已成功访问，包含 src/pheragent、tests 与 Docker builder 使用说明；更新此前“网页抓取失败”的记录，未运行代码。
- **重点读什么**：把环境安装组织成语义 block，逐块验证、checkpoint 和回退；对应 image readiness / setup 阶段。
- **小规模切入（分析建议，未经本地实验）**：CPU 容器加模型 API 可开始；需固定软件仓库版本、依赖源和 replay 验证。
- **归类理由与边界**：环境准备与恢复属于 Sandbox 支撑层；PDF 的 IEEE 模板页眉不能证明期刊录用。

### Sandlock — P1

- **服务用途归类**：Sandbox as a Tool。主要隔离 Agent 调用的命令、脚本、插件及子进程，关注工具调用的权限与启动成本。依据：PDF 第 1–2 页 §1/§2.1。

- **Harness 物理部署（独立记录）**：Sandbox as a Tool。PDF 第 1–2 页 §1/§2.1 将短时命令、脚本和工具插件作为受限执行对象，将 embedding agent runtime 与 supervisor 列为可信侧。按论文目标与示例归工具/子进程隔离，不凭可运行任意程序推定双形态已验证。

**Sandlock: Confining AI Agent Code with Unprivileged Linux Primitives**

[本地 PDF](Sandbox%20as%20a%20Tool/2026_Sandlock_2605.26298.pdf) · [原始论文页](https://arxiv.org/abs/2605.26298) · 2605.26298v1 · 9 页

- **时间与发表状态**：预印本；未核实正式录用。当前文件版本日期：2026-05-25；首发日期：2026-05-25。
- **纳入依据**：Multikernel Technologies 与 UC Santa Cruz；可核实公开实现，作为轻量隔离工程参考。
- **代码/工件**：[公开代码已核实](https://github.com/multikernel/sandlock)。
- **重点读什么**：无 root 的 Linux 进程隔离：静态内核策略与动态 supervisor 分工；比较启动成本与隔离语义。
- **小规模切入（分析建议，未经本地实验）**：CPU Linux 可研究；不要把不同隔离边界的性能直接当同等安全性下的优劣。
- **归类理由与边界**：工具/进程执行沙箱机制，主归 Sandbox；开源是纳入依据，非声称已完成安全审计。

### SpecBox — P2

- **服务用途归类**：Sandbox as a Tool。主要根据流式生成中的工具意图预热外部工具沙箱，优化工具服务的资源开销和尾延迟。依据：PDF 第 1 页摘要、第 3–4 页运行时与图 3。

- **Harness 物理部署（独立记录）**：Sandbox as a Tool。PDF 第 1 页摘要及第 3–4 页运行时/图 3：Agent 经 MCP 调用外部分离的工具 sandbox，流式生成期间预测工具意图并预热对应环境。

**SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving**

[本地 PDF](Sandbox%20as%20a%20Tool/2026_SpecBox_2607.23933.pdf) · [原始论文页](https://arxiv.org/abs/2607.23933) · 2607.23933v2 · 13 页

- **时间与发表状态**：预印本，v2；未核实该题名的正式录用。当前文件版本日期：2026-08-05；首发日期：2026-07-27。
- **纳入依据**：北航、Leeds、Sydney；作者 Yihui Zhang、Tianyu Wo、Renyu Yang 等；作为已有研究方向的公开对照。
- **代码/工件**：本次未核实到该系统的公开代码；不能据此断言未开源。
- **重点读什么**：流式 token 意图预测驱动独立工具环境预热；重点检查准备目标、提前信号与可重叠窗口。
- **小规模切入（分析建议，未经本地实验）**：CPU 工具环境加流式模型 API 即可研究预热；需要固定池、TTL、manifest/FIFO 等简单基线。
- **归类理由与边界**：Sandbox as a Tool；不能直接推断其预热机制适用于任务启动前就已确定的 Agent-in-Sandbox 环境。
