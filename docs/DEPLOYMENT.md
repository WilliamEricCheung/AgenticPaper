# 网站构建与 GitHub Pages

网站使用 Python 标准库生成静态 HTML，前端为原生 CSS/JavaScript；不需要 npm、数据库或 API key。

```sh
python3 scripts/build_site.py
python3 scripts/validate_site.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory _site
```

本地打开 `http://127.0.0.1:8765/`。`_site/` 是忽略的构建产物，包含独立阅读页和从原目录复制的 PDF；源目录中的每篇 PDF 仍只保留一份。

## 发布

仓库 Settings → Pages → Source 选择 **GitHub Actions**。推送 `main` 后，`.github/workflows/pages.yml` 构建并检查内容，然后上传 Pages artifact 并部署。PR 只构建检查，不部署。

- 项目：<https://github.com/WilliamEricCheung/AgenticPaper>
- 网站：<https://willienericcheung.github.io/AgenticPaper/>
- 更换账号或仓库名：同步修改 `scripts/build_site.py` 的 `REPO` 与 `SITE`。
- 创建后续版本：修改生成器的 `VERSION`、`DATE` 和 release 文案，更新 CHANGELOG，提交后创建同名 Git tag / GitHub Release。

## 内容维护

1. PDF 放入三个主题目录中最合适的一处；Sandbox 按约定的用途子分类组织。
2. 更新 `papers.json`：来源、准确版本、发表/代码状态、本地路径、页数、字节数与 SHA-256。
3. 在 `content/*-reviews.json` 中维护同 ID 的导读：`overview`、`scenario`、`motivation`、`mechanism`、`evaluation`、`limitations`、`evidence`。`evidence.pages` 必须为 PDF 物理页码整数数组。
4. 任何新硬件、模型、基线或数值都要核对对应原文；区分实测、重放、仿真和生产报告。读不到的配置写“未明确披露”。
5. 新增论文时同步修改生成器首页计数和验证器 release 数量，再构建、检查、推送。

公开页面只包含本库收录材料与论文导读。收藏使用浏览器 localStorage，不发送到服务器。导读未经过实验复现，不应替代原文引用。

GitHub 官方文档：[自定义工作流发布 Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。
