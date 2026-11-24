#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the dependency-free AgenticPaper site for GitHub Pages."""
import argparse
import html
import json
import re
import shutil
from collections import Counter
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/WilliamEricCheung/AgenticPaper'
SITE = 'https://willienericcheung.github.io/AgenticPaper'
VERSION = 'v1.0.0'
DATE = '2026-11-24'
LABELS = {'offline': '离线 Rollout', 'online': '在线 Serving', 'sandbox': 'Sandbox'}
SECTIONS = [('scenario', '面向场景', 'SCENARIO'), ('motivation', '论文动机', 'MOTIVATION'), ('mechanism', '核心机制与贡献', 'MECHANISM'), ('evaluation', '实验设置与对比对象', 'EVALUATION')]
BOOKMARK = '<svg viewBox="0 0 18 22" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 2h12v17l-6-4-6 4z"/></svg>'

def esc(value):
    return html.escape(str(value), quote=True)

def prose(value):
    """Escape all source content, allowing only explicit HTTP(S) Markdown links."""
    escaped = esc(value)
    return re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', escaped)

def status(p):
    s = p['status']
    for marker in ['OSDI 2026', 'NSDI 2026', 'ICML 2026', 'SIGOPS ATC 2026', 'ASPLOS 2027', 'NeurIPS 2026', 'IEEE TC']:
        if marker in s:
            return marker, 'published'
    if 'Workshop' in s:
        return 'ICLR 2026 Workshop', 'published'
    if '技术报告' in s:
        return '技术报告', 'preprint'
    return '预印本', 'preprint'

def nav(prefix=''):
    return f'''<a class="skip" href="#main">跳到主要内容</a><header class="topbar"><nav class="wrap nav" aria-label="主导航"><a class="brand" href="{prefix}index.html"><img src="{prefix}assets/icon.svg" alt="">AgenticPaper</a><div class="navlinks"><a class="nav-home" href="{prefix}index.html#library">论文库</a><a class="release" href="{prefix}release.html">{VERSION}</a><a href="{REPO}" target="_blank" rel="noopener noreferrer">GitHub</a></div></nav></header>'''

def footer(prefix=''):
    return f'''<footer class="footer"><div class="wrap"><span>AgenticPaper · Agent systems reading collection</span><span>资料核验 {DATE} · <a href="{prefix}release.html">版本与收录说明</a></span></div></footer>'''

def page(title, description, body, prefix='', canonical=''):
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} · AgenticPaper</title><meta name="description" content="{esc(description)}"><meta name="theme-color" content="#155de9"><meta property="og:title" content="{esc(title)} · AgenticPaper"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="article"><link rel="canonical" href="{SITE}/{canonical}"><link rel="icon" href="{prefix}assets/icon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/site.css"><script src="{prefix}assets/site.js" defer></script></head><body>{nav(prefix)}{body}{footer(prefix)}</body></html>'''

def save_button(p):
    return f'<button class="save" data-save="{esc(p["id"])}" data-name="{esc(p["short_name"])}" aria-label="收藏 {esc(p["short_name"])}" aria-pressed="false" title="收藏到本机">{BOOKMARK}</button>'

def badges(p):
    label, _ = status(p)
    return f'<div class="badges"><span class="badge {p["category"]}">{LABELS[p["category"]]}</span><span class="badge">{esc(label)}</span><span class="priority">{p["priority"]}</span></div>'

def load_reviews(allow_incomplete=False):
    result = {}
    for path in sorted((ROOT/'content').glob('*-reviews.json')):
        for review in json.loads(path.read_text()):
            if review['id'] in result:
                raise ValueError('Duplicate review: '+review['id'])
            result[review['id']] = review
    papers = json.loads((ROOT/'papers.json').read_text())['papers']
    for p in papers:
        if p['id'] not in result:
            if not allow_incomplete:
                raise ValueError('Missing review: '+p['id'])
            result[p['id']] = {'overview':p['reading_focus'], **{key:'此篇论文的结构化导读正在整理，稍后补齐。' for key,_,_ in SECTIONS}, 'limitations':'预览版本，摘要尚未完成。','evidence':[]}
        review = result[p['id']]
        for field in ['overview','scenario','motivation','mechanism','evaluation','limitations']:
            if not isinstance(review.get(field),str) or len(review[field])<10:
                raise ValueError(f'{p["id"]}: invalid {field}')
        if not allow_incomplete and not review.get('evidence'):
            raise ValueError('Missing evidence: '+p['id'])
    if set(result)-{p['id'] for p in papers}:
        raise ValueError('Unmatched review IDs')
    return papers, result

def index(papers, reviews):
    cards=[]
    for p in sorted(papers,key=lambda x:(x['priority'],x['category'])):
        r=reviews[p['id']]; _,pub=status(p)
        search=' '.join([p['short_name'],p['title'],p['quality_evidence'],p['status'],p.get('sandbox_workload_label','')]+[r[k] for k in ['overview','scenario','motivation','mechanism','evaluation']]).lower()
        cards.append(f'''<article class="paper-card" data-id="{p['id']}" data-name="{esc(p['short_name'])}" data-category="{p['category']}" data-priority="{p['priority']}" data-sub="{p.get('sandbox_workload_category','')}" data-status="{pub}" data-date="{p['version_date']}" data-search="{esc(search)}"><div class="card-top">{badges(p)}{save_button(p)}</div><h3><a href="papers/{p['id']}.html">{esc(p['short_name'])}</a></h3><p class="full-title">{esc(p['title'])}</p><p class="overview">{prose(r['overview'])}</p><div class="card-footer"><div class="links"><a class="primary-link" href="papers/{p['id']}.html">阅读导读</a><a href="pdfs/{p['id']}.pdf" target="_blank" rel="noopener">PDF</a><a href="{esc(p['source_url'])}" target="_blank" rel="noopener noreferrer">论文来源</a></div><span class="date">版本 {p['version_date']}</span></div></article>''')
    counts=Counter(p['category'] for p in papers)
    tabs=''.join(f'<button class="filter-tab" data-category="{cat}" aria-pressed="{str(cat=="all").lower()}">{name}<span>{len(papers) if cat=="all" else counts[cat]}</span></button>' for cat,name in [('all','全部论文'),('offline','离线 Rollout'),('online','在线 Serving'),('sandbox','Sandbox')])
    return page('2026 Agent 系统论文阅读库','围绕离线 Agentic RL rollout、在线 Agent Serving 与 Sandbox 的 35 篇精选论文，提供场景、动机、机制和实验导读。',f'''
<main id="main"><div class="wrap"><section class="hero"><div><div class="eyebrow">2026 Research Collection · Release 1.0</div><h1>读懂 Agent 系统，<br><em>从论文到机制。</em></h1><p>沿着 Rollout、在线 Serving 与 Sandbox 三条线，梳理系统问题、关键设计与实验证据。为快速阅读，也为下一步研究。</p><div class="hero-meta"><span>35 篇精选文献</span><span>四个维度，逐篇拆解</span><span>持续更新</span></div></div><div class="architecture" aria-label="研究范围：离线 Rollout 与在线 Serving 共享 Sandbox 执行环境"><div class="arch-title">THE AGENT SYSTEMS STACK</div><div class="arch-pair"><div class="arch-node"><span>训练 / 评测 / 数据生成</span><b>Offline Rollout</b><span>轨迹吞吐 · 组完成 · 长尾</span></div><div class="arch-node"><span>交互 / 生产推理服务</span><b>Online Serving</b><span>延迟 · KV 状态 · 公平性</span></div></div><div class="arch-base"><b>Sandbox</b> · 工具执行与完整任务环境</div><div class="arch-caption">一条执行链，三个系统研究视角</div></div></section><div class="stats"><div class="stat"><strong>35</strong><span>论文与技术报告</span></div><div class="stat"><strong>09</strong><span>离线 Rollout</span></div><div class="stat"><strong>17</strong><span>在线 Serving</span></div><div class="stat"><strong>09</strong><span>Sandbox</span></div></div>
<section class="library" id="library" aria-label="论文目录"><aside class="sidebar"><div class="side-label">Research areas</div><div class="filter-tabs" aria-label="方向筛选">{tabs}</div><button class="chip saved-filter" id="saved-only" aria-pressed="false">只看本机收藏</button><div class="side-note"><b>从哪开始读？</b><p>环境系统：Kimi K3、DeltaBox、Crab。<br>离线执行：CAAS、Heddle。<br>在线调度：Agentix、ThunderAgent。</p><a href="release.html#method">收录与分类口径</a></div></aside><div><div class="library-top"><h2 id="category-title">全部论文</h2><p>资料截至 {DATE}</p></div><noscript><p class="noscript">当前未启用 JavaScript。下方仍可阅读全部论文；筛选和本机收藏需要 JavaScript。</p></noscript><div class="toolbar"><div class="search"><label class="sr-only" for="search" hidden>搜索论文、机制、模型或基线</label><input id="search" type="search" aria-label="搜索论文、机制、模型或基线" placeholder="搜索论文、机制、模型或基线…" autocomplete="off"></div><select id="priority" class="select" aria-label="阅读优先级"><option value="all">全部优先级</option><option value="P0">P0 优先精读</option><option value="P1">P1 机制对照</option><option value="P2">P2 扩展参考</option></select><select id="sort" class="select" aria-label="排序方式"><option value="priority">按阅读优先级</option><option value="newest">按版本日期</option><option value="name">按论文名称</option></select></div><div class="subfilters" aria-label="发表状态"><button class="chip" data-status="all" aria-pressed="true">全部状态</button><button class="chip" data-status="published" aria-pressed="false">已发表 / 已录用 / Workshop</button><button class="chip" data-status="preprint" aria-pressed="false">预印本 / 技术报告</button></div><div class="subfilters" id="sandbox-filters" hidden aria-label="Sandbox 服务用途"><button class="chip" data-sub="all" aria-pressed="true">全部 Sandbox</button><button class="chip" data-sub="tool" aria-pressed="false">Sandbox as a Tool · 5</button><button class="chip" data-sub="agent" aria-pressed="false">Agent in Sandbox · 2</button><button class="chip" data-sub="both" aria-pressed="false">两类通用 · 2</button></div><div class="results"><span id="result-count" role="status" aria-live="polite">35 篇 / 共 35 篇</span><button class="reset" data-reset>重置筛选</button></div><div class="paper-list" id="paper-list">{''.join(cards)}</div><div id="empty" class="empty" hidden><h3>没有符合条件的论文</h3><p>试试更短的关键词，或放宽方向与优先级筛选。</p><button class="button secondary" data-reset>显示全部论文</button></div></div></section></div><section class="method"><div class="wrap method-grid"><div><h3>以执行系统为主线</h3><p>离线方向重点看 rollout 与环境交互。完整训练和大规模 GPU 并行作为背景，优先寻找可独立验证的系统问题。</p></div><div><h3>让判断有出处</h3><p>每篇导读提供来源与 PDF 页码。正式录用、Workshop、预印本分别记录；模拟、重放和真机实验明确区分。</p></div><div><h3>把论文变成阅读入口</h3><p>先读一段概述，再看场景、动机、机制和实验。P0–P2 表示本库阅读顺序，不代表论文质量排名。</p></div></div></section></main>''',canonical='')

def detail(p,r):
    pdf=f'../pdfs/{p["id"]}.pdf'
    sections=''.join(f'<section id="{key}"><div class="kicker">{en}</div><h2>{label}</h2><p>{prose(r[key])}</p></section>' for key,label,en in SECTIONS)
    evidence=[]
    for e in r.get('evidence',[]):
        pages=e.get('pages',[])
        if isinstance(pages,int):pages=[pages]
        if isinstance(pages,str):pages=[int(x) for x in re.findall(r'\d+',pages)]
        links='、'.join(f'<a href="{pdf}#page={n}" target="_blank" rel="noopener">{n}</a>' for n in pages)
        evidence.append(f'<li><b>{esc(e.get("section","正文"))}</b> · PDF 第 {links} 页<br>{prose(e.get("note",""))}</li>')
    sources=[p['source_url']]+p.get('additional_sources',[])
    source_links=' · '.join(f'<a href="{esc(url)}" target="_blank" rel="noopener noreferrer">{"论文来源" if i==0 else "补充来源 "+str(i)}</a>' for i,url in enumerate(dict.fromkeys(sources)))
    meta=[('发表状态',p['status']),('版本日期',p['version_date']),('纳入依据',p['quality_evidence']),('代码与工件',p['code_status'])]
    if p['category']=='sandbox':meta.extend([('本库用途分类',p.get('sandbox_workload_label','')),('Harness 物理部署',p.get('sandbox_harness_label','待确认'))])
    metadata=''.join(f'<div class="meta-item"><dt>{label}</dt><dd>{prose(value)}</dd></div>' for label,value in meta)
    toc=''.join(f'<a href="#{key}">{label}</a>' for key,label,_ in SECTIONS)
    return page(p['short_name']+'：论文导读',r['overview'],f'''<main id="main" class="wrap"><div class="breadcrumb"><a href="../index.html#library">论文库</a><span>/</span><a href="../index.html?category={p['category']}#library">{LABELS[p['category']]}</a><span>/</span><span>{esc(p['short_name'])}</span></div><header class="reader-header">{badges(p)}<h1>{esc(p['short_name'])}</h1><p class="full-title">{esc(p['title'])}</p><p class="lead">{prose(r['overview'])}</p><div class="actions"><a class="button" href="{pdf}" target="_blank" rel="noopener">阅读 PDF · {p['pages']} 页</a><a class="button secondary" href="{esc(p['source_url'])}" target="_blank" rel="noopener noreferrer">原始论文</a><button class="button secondary" data-share>复制阅读链接</button><button class="button secondary" data-print>打印导读</button>{save_button(p)}</div></header><div class="reader-grid"><article class="reading">{sections}<section id="limitations"><div class="kicker">READING NOTES</div><h2>结论边界与阅读提示</h2><p>{prose(r['limitations'])}</p><p><b>有限资源的切入建议：</b>{prose(p['small_scale_entry'])}</p><p class="notice">以上是基于论文正文的阅读整理，不代表已复现实验。低资源切入点为分析建议；性能数字只适用于论文报告的配置。</p></section><section id="evidence"><div class="kicker">SOURCES</div><h2>正文依据</h2><p class="notice">以下为本地 PDF 的物理页码，可直接跳转。与印刷页码可能不同。</p><ul class="evidence-list">{''.join(evidence)}</ul><p>{source_links}</p></section><div class="article-nav"><a href="../index.html?category={p['category']}#library">返回 {LABELS[p['category']]} 目录</a><a href="#main">回到页首</a></div></article><aside class="reader-aside"><div class="side-label">On this page</div><nav class="toc" aria-label="导读目录">{toc}<a href="#limitations">结论边界</a><a href="#evidence">正文依据</a></nav><details class="meta-details" open><summary>论文信息</summary><dl>{metadata}</dl></details></aside></div></main>''',prefix='../',canonical=f'papers/{p["id"]}.html')

def release():
    return page('Release 1.0 · 版本与收录说明','AgenticPaper v1.0.0：35 篇 Agent 系统论文的结构化阅读库。',f'''<main id="main" class="wrap"><div class="release-body"><div class="breadcrumb"><a href="index.html">论文库</a><span>/</span><span>Release</span></div><div class="eyebrow">Research library release</div><h1>从文献目录，<br>到可追溯的阅读库。</h1><p>AgenticPaper 围绕 Agent 系统的资源调度、执行优化与状态管理，连接论文、机制和实验证据。</p><div class="actions"><a class="button" href="index.html#library">浏览全部论文</a><a class="button secondary" href="{REPO}/releases">GitHub Releases</a></div><section class="release-block"><div class="eyebrow">{DATE} · {VERSION}</div><h2>首个结构化阅读版本</h2><ul><li>35 篇论文与技术报告：离线 Rollout 9 篇、在线 Serving 17 篇、Sandbox 9 篇。</li><li>每篇包含一段概述，以及面向场景、论文动机、核心机制与贡献、实验设置与对比对象四部分。</li><li>逐篇提供 PDF 页码、来源、代码状态、结论边界与有限资源实验建议。</li><li>支持全文关键词、方向、优先级、发表状态与 Sandbox 用途筛选。</li><li>独立分享链接、本机收藏、打印导读与 PDF 阅读入口。</li></ul></section><section class="release-block" id="method"><h2>收录口径</h2><p>覆盖 2026 首发、正式发表或重要更新的论文；少数 2025 首发但 2026 重要更新的工作保留，并记录准确版本。KAIROS 是 2026 公开、ASPLOS 2027 录用。主会、Workshop、技术报告和预印本不混为同一等级。</p><p>预印本结合作者/机构、具体系统设计、实验、公开实现及真实负载证据筛选。没有统一可靠的引用量快照，因此不填猜测的引用数，也不以 stars 替代引用。</p><p>P0 最贴近当前研究问题，P1 用于机制对照，P2 用于扩展与背景。阅读优先级不代表质量排名。</p></section><section class="release-block"><h2>Sandbox 的两种阅读视角</h2><p><b>Sandbox as a Tool：</b>代码、命令、工具执行及环境准备服务，共 5 篇。<b>Agent in Sandbox：</b>承载完整任务/rollout 的环境，共 2 篇。Crab、DeltaBox 覆盖两类，单独列为通用机制。</p><p>该分类按服务用途和执行粒度组织。Harness 的实际物理部署单独记录；RL 用途不等于已经证明 Harness 位于沙箱内。Kimi K3 面向后训练和评测，TClone 面向在线 CUA 与测试时搜索。</p><p>当前数量反映精选样本的覆盖，不代表全领域研究热度。</p></section><section class="release-block"><h2>使用与维护</h2><p>本站为个人研究文献整理。导读由 AI 辅助生成并对照论文正文整理，仍可能存在理解偏差；引用论文结论前请核对原文。未运行论文代码或复现训练实验。</p><p>收藏只保存在当前浏览器，不上传服务器。站点不使用分析追踪或第三方字体。论文及图表版权归各自权利人，网站代码许可不适用于第三方 PDF。</p><p>发现错误、更新版本或希望推荐论文，可在 <a class="read-link" href="{REPO}/issues">GitHub Issues</a> 提交来源与对应章节。</p></section></div></main>''',canonical='release.html')

def build(allow_incomplete=False):
    papers,reviews=load_reviews(allow_incomplete)
    out=ROOT/'_site'
    if out.exists():shutil.rmtree(out)
    (out/'papers').mkdir(parents=True)
    (out/'pdfs').mkdir()
    shutil.copytree(ROOT/'web/assets',out/'assets')
    (out/'.nojekyll').touch()
    (out/'index.html').write_text(index(papers,reviews))
    (out/'release.html').write_text(release())
    for p in papers:
        (out/'papers'/f'{p["id"]}.html').write_text(detail(p,reviews[p['id']]))
        shutil.copy2(ROOT/p['local_path'],out/'pdfs'/f'{p["id"]}.pdf')
    (out/'404.html').write_text(page('页面未找到','返回论文库查找论文。','<main id="main" class="wrap release-body"><h1>页面未找到</h1><p>论文链接可能已更新。</p><a class="button" href="'+SITE+'/">返回论文库</a></main>'))
    (out/'catalog.json').write_text(json.dumps({'version':VERSION,'checked_on':DATE,'papers':[{**p,'review':reviews[p['id']]} for p in papers]},ensure_ascii=False,indent=2))
    urls=['', 'release.html']+[f'papers/{p["id"]}.html' for p in papers]
    (out/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}/{u}</loc><lastmod>{DATE}</lastmod></url>' for u in urls)+'</urlset>')
    print(f'Built {len(papers)} reading pages, home, release, and {len(papers)} PDFs in {out}')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--allow-incomplete',action='store_true');args=parser.parse_args()
    build(args.allow_incomplete)
