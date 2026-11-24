---
name: agentic-paper-maintainer
description: 持续维护 AgenticPaper 论文库：增量检索 Agentic RL rollout、在线 Agent Serving 和 Sandbox 论文，核验版本与收录依据，撰写中文结构化导读，维护目录和网站，并按用户请求同步 GitHub、GitHub Pages 与 Release。适用于该项目的论文更新、分析总结、分类修正和发布维护。
---

# AgenticPaper 论文库维护

把新证据转成可追溯的论文索引和导读，延续用户以有限 GPU 资源研究 Agent 执行系统的主线。

## 定位与任务范围

- 优先使用当前 AgenticPaper checkout；否则检查 `/Users/zhangyihui/Projects/AgenticPaper`。通过 `papers.json`、`content/`、`scripts/build_site.py` 确认项目，读取适用的 `AGENTS.md` 和工作区改动。
- 公开仓库为 `WilliamEricCheung/AgenticPaper`；网站为 `https://williamericcheung.github.io/AgenticPaper/`。操作前以当前 remote、构建配置与用户指令核对，不能只相信这些默认值。
- “更新论文库并发布”涵盖本次公开论文、导读、索引、站点构建与发布；已有有效授权时不要重复询问。仅请求搜索、分析或本地更新时，完成对应工作即可，不自动推送或创建 Release。skill 的存在不构成未来发布或定时任务的授权。
- 增量检索默认从库中上次核验时间延续到当前日期，窗口适当重叠以补漏；同时检查相关已有论文的新版、录用和代码发布。跨年后继续跟随当前日期，不永久限定为 2026 年。尊重用户指定的时间、主题与数量。

## 核心研究口径

- **离线 Agentic RL：**重点是 rollout / 评测 / 数据生成的执行服务，关注轨迹吞吐、组完成、长尾、环境容量、推理与工具协同。这里“离线”是批量服务用途，不是 offline RL 算法，也不表示不与环境实时交互。完整训练、大规模 GPU 并行仅作必要背景。
- **在线 Agent Serving：**关注任务延迟、SLO goodput、调度公平性、跨轮 KV 状态、推理—工具协同和资源调度。
- **Sandbox：**关注启动、隔离、环境准备、checkpoint/restore、pause/resume、fork、生命周期和共置资源。跨主题论文只存一份 PDF，按最值得学习的主贡献归类，并标注交叉主题。
- Sandbox 的目录依据是**服务用途和执行粒度**；Harness 的实际进程位置另作证据记录。不能由“用于 RL”“有持久状态”推断 Harness 在沙箱内。Kimi K3 仍以 Sandbox 为主分类，除非用户另行调整。
- 每篇给出有限资源切入建议，说明 CPU、模型 API、少量 GPU 或轨迹重放能验证什么、不能验证什么；建议不写成已完成实验。

## 按任务使用工作流

1. **检索与选文：**读取 [research.md](references/research.md)。实时查证官方论文页、会议、作者项目和正文；先核对已有 ID，区分新工作、新版本、状态更新与不收录候选。
2. **导读与入库：**读取 [repository.md](references/repository.md)。读取对应 PDF 正文及图表，完成一段概述和场景、动机、机制贡献、实验设置与对比对象四部分，再补证据页码、结论边界和小规模切入建议。没有读到正文时不要发布仿完整导读。
3. **检查与发布：**本地更新后构建并校验。用户要求同步 GitHub / Pages / Release 时，再读取 [publishing.md](references/publishing.md) 完成外部发布及上线检查。区分网站 `release.html` 与 GitHub Release，不能只更新其中一个便声称两者已完成。

任务可以只执行其中一部分；已有资料足够时不必重新搜索全部论文。没有合格新增时如实报告，仍可更新有证据变化的版本/状态，不凑数、不制造空 Release。

## 交付

说明新增、版本更新、状态更正与未收录情况；列出值得优先阅读的变化及其系统研究价值。发布任务提供实际可用的网站、仓库和 Release 链接以及验证结果；只做本地工作时给出文件位置和待发布状态。记录具体未核实项，不把“未查到”写成不存在，也不把网页可访问写成实验复现。

## 典型调用

- `使用 $agentic-paper-maintainer 检索上次更新以来的新论文，更新导读并发布网站和新 Release。`
- `使用 $agentic-paper-maintainer 精读这篇论文并加入 Sandbox，只更新本地文件。`
- `使用 $agentic-paper-maintainer 核验已有论文的新版、录用和代码状态，修正后同步 GitHub 和 Pages。`

本项目 `skills/agentic-paper-maintainer/` 保存可维护源文件；本机技能目录可安装副本。修改技能时同步已安装副本，避免两者漂移。
