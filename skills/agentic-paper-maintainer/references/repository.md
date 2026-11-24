# 仓库格式与分类

以下描述初始发布时的结构；编辑前读取实际文件，后续仓库实现优先。

## 来源文件

| 内容 | 路径 |
| --- | --- |
| 论文元数据 | `papers.json`，根对象含 `checked_on` 和 `papers` 数组 |
| 离线 PDF / 索引 | `Offline Agentic RL Rollout Serving/` |
| 在线 PDF / 索引 | `Online Agentic AI Serving/` |
| 沙箱 PDF / 索引 | `Sandbox/` 及两类子目录 |
| 结构化导读 | `content/offline-reviews.json`、`online-reviews.json`、`sandbox-reviews.json`，每个文件为数组 |
| 首页与阅读页生成器 | `scripts/build_site.py` |
| 前端交互及样式 | `web/assets/site.js`、`site.css` |
| 校验器 / 发布工作流 | `scripts/validate_site.py`、`.github/workflows/pages.yml` |
| 版本说明 / 使用说明 | `CHANGELOG.md`、`README.md`、`docs/DEPLOYMENT.md` |

`_site/` 为忽略的可重建产物，不直接维护或提交。页面 PDF 是构建时复制的文件，来源目录每篇仅保留一份。

## 元数据契约

保留现有字段，参考相邻记录填写，不批量重新编号：

- 身份：`id`（稳定且可作文件名的 ID）、`version`、`title`、`short_name`、`authors`。
- 来源：`source_url`、固定版本的 `pdf_url`、`additional_sources`（URL 数组）。
- 分类：`category` 为 `offline` / `online` / `sandbox`，`priority` 为 P0 / P1 / P2，`classification_reason` 包含主要归类依据与交叉主题。
- 判断：`status`、`quality_evidence`、`code_status`、`reading_focus`、`small_scale_entry`。
- 时间：`first_submission_date`、`version_date`、逐篇 `checked_on`；只更新实际核查过的记录。库级日期表示本轮维护日期，不暗示所有旧论文当天重审。
- 文件：相对仓库路径 `local_path`、物理页数 `pages`、`bytes`、`sha256`、`existing_file_preserved`。

下载后验证确为可解析 PDF，防止将 HTML 错误页当论文；计算实际文件哈希和大小，页数用 PDF 工具读取。不要根据 URL 猜页数或用远端长度替代本地字节数。

## Sandbox 两条独立分类轴

| 用途分类 | `sandbox_workload_category` | 存放路径 |
| --- | --- | --- |
| 代码、命令、工具调用、环境准备服务 | `tool` | `Sandbox/Sandbox as a Tool/` |
| 完整 Agent 任务、rollout 或评测执行环境 | `agent` | `Sandbox/Agent in Sandbox/` |
| 论文有证据覆盖两类的通用机制 | `both` | `Sandbox/` 根目录 |

同时填 `sandbox_workload_label`、`sandbox_workload_evidence`（含章节/页码）、`sandbox_classification_basis`。用途不清时继续查正文，必要时保留候选，不把 `both` 当未知类别。

物理部署单独填 `sandbox_harness_category`（`tool` / `agent` / `both` / `unspecified`）、`sandbox_harness_label`、`sandbox_harness_evidence`、`sandbox_harness_checked_on`。论文没证明 Harness 在哪就写 `unspecified` / 待确认，不根据用途分类反填。

Kimi K3 的 AgentENV 与 TClone 按完整任务环境归 `agent`，不等于已确认 Harness 物理位置；Crab、DeltaBox 的双用途分类应保持证据链。新证据可更正判断，并说明原因。类别计数只反映本库筛选样本，不能推出全领域热度。

## 导读契约

每个元数据 ID 在对应 `content/*-reviews.json` 中恰有一条记录，字段：

```json
{
  "id": "stable-paper-id",
  "overview": "一段概述",
  "scenario": "面向场景",
  "motivation": "论文动机与已有方法的不足",
  "mechanism": "核心机制与贡献",
  "evaluation": "实验配置、对照对象与结果",
  "limitations": "适用边界与未验证内容",
  "evidence": [
    {"section": "§3 System Design", "pages": [4, 5], "note": "说明所支撑的机制"}
  ]
}
```

此示例仅展示结构，不能将示例文字/页码作为实际论文内容。`pages` 必须是非空整数数组，范围为 1 到该文件物理页数。主要导读字段当前为字符串，不擅自改成数组；需要格式扩展时一并更新生成器和验证器。

## 联动更新

更新根 README、所属主题 README、Sandbox 子目录 README 的链接、计数、阅读顺序、状态和分类依据。保留现有有价值的证据与阅读提示，不将逐篇索引覆盖为仅列标题的清单。

初始生成器含固定数量、`Release 1.0`、年份、`VERSION` / `DATE` 与 `release()` 文案；验证器含 `len(papers)==35` 及固定输出文字，`status()` 还枚举了部分会议名称。新增论文、新年份或新会议状态时检查这些位置，不能只改 JSON。

优先在需要时将数量和标签由数据生成，减少以后同步点；如暂时保留固定值，按实际库内容逐处一致更新。不要为通过验证而删除完整性检查，也不要全局替换所有“35”或年份，以免改动论文自身的数字、历史版本记录或 URL。

构建与基本校验：

```sh
python3 scripts/build_site.py
python3 scripts/validate_site.py
git diff --check
```

发布构建不使用 `--allow-incomplete`。现有校验器覆盖导读、PDF 哈希、页码范围和站内链接，但不证明学术结论、外链或元数据事实正确。对本次改动补充核对 ID 唯一性、分类计数、实际页数和来源；无需每次重做所有旧文献研究。
