# Agent in Sandbox

[返回 Sandbox 总索引](../README.md) · [返回论文库](../../README.md)

本目录按**完整 Agent 任务环境**归类，重点关注为 RL rollout、评测或完整交互任务提供环境的工作。这里优先看任务承载、环境生命周期和轨迹状态，不以论文是否明确写出 Harness 进程位置作为入目录的必要条件。

| 论文 | 主要用途 | 为什么归这里 |
| --- | --- | --- |
| [Kimi K3](KIMI%20K3%20OPEN%20FRONTIER%20INTELLIGENCE.pdf) | **Agentic RL 后训练与评测** | §5.3.2 的 AgentENV 为完整任务提供环境，支持 pause/resume、fork、snapshot 与高密度运行；先读 PDF 第 22 页。 |
| [TClone](2026_TClone_2605.17320.pdf) | **在线 computer-use / 测试时搜索** | 管理包含 GUI、应用进程与文件的完整工作区，按轨迹分支 fork、rollback 和 commit；先读 PDF 第 4–5 页 §3/图 3。并非以 RL 训练为主要评估场景。 |

两篇的 Harness **物理进程位置仍未由现有正文明确确认**，这与按服务定位归入本目录不冲突。用于 RL 的环境也可能由外部 Harness 驱动；目录名称采用本库约定的较宽口径。

下面两篇覆盖两类，PDF 保留上层：

| 论文 | 相关设计 |
| --- | --- |
| [Crab](../2026_Crab_2604.28138.pdf) | §6 区分两种部署，包含 sandbox 内 Claude-code/iFlow-cli 评估；适合学习完整 Agent 的恢复。 |
| [DeltaBox](../DeltaBox.pdf) | 保护 agent worker/受管进程树，支持搜索 rollback 和 RL fan-out，也有宿主侧编排集成。 |

若重点研究 RL rollout 环境，可按 Kimi K3 → DeltaBox → Crab 阅读，再用 TClone 对照完整桌面任务的状态管理。正式发表状态、代码和详细证据集中维护在 [Sandbox 总索引](../README.md)。
