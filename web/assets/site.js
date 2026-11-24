(() => {
  'use strict';
  const key = 'agenticpaper.saved.v1';
  let saved;
  try { saved = new Set(JSON.parse(localStorage.getItem(key) || '[]')); } catch { saved = new Set(); }
  const cards = [...document.querySelectorAll('.paper-card')];
  const list = document.querySelector('#paper-list');
  const params = new URLSearchParams(location.search);
  const state = {category: params.get('category') || 'all', sub: params.get('sub') || 'all', q: params.get('q') || '', priority: params.get('priority') || 'all', status: params.get('status') || 'all', saved: params.get('saved') === '1', sort: params.get('sort') || 'priority'};
  const toast = message => {
    let el = document.querySelector('.toast');
    if (!el) { el = document.createElement('div'); el.className = 'toast'; el.setAttribute('role', 'status'); document.body.append(el); }
    el.textContent = message; el.hidden = false;
    clearTimeout(window.toastTimeout); window.toastTimeout = setTimeout(() => { el.hidden = true; }, 2000);
  };
  const syncSaved = () => document.querySelectorAll('[data-save]').forEach(b => {
    const selected = saved.has(b.dataset.save);
    b.setAttribute('aria-pressed', String(selected));
    b.setAttribute('aria-label', (selected ? '取消收藏 ' : '收藏 ') + b.dataset.name);
    b.title = selected ? '取消收藏' : '收藏到本机';
  });
  document.querySelectorAll('[data-save]').forEach(b => b.addEventListener('click', () => {
    const id = b.dataset.save;
    saved.has(id) ? saved.delete(id) : saved.add(id);
    try { localStorage.setItem(key, JSON.stringify([...saved])); } catch { toast('浏览器未允许保存；本次会话仍可收藏'); }
    syncSaved(); if (list) render();
  }));
  syncSaved();
  document.querySelectorAll('[data-share]').forEach(b => b.addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(location.href); toast('阅读链接已复制'); }
    catch { toast('请复制浏览器地址栏中的阅读链接'); }
  }));
  document.querySelectorAll('[data-print]').forEach(b => b.addEventListener('click', () => window.print()));
  if (!list) return;
  const search = document.querySelector('#search');
  const priority = document.querySelector('#priority');
  const sort = document.querySelector('#sort');
  const categoryNames = {all:'全部论文',offline:'离线 Rollout Serving',online:'在线 Agent Serving',sandbox:'Sandbox 基础设施'};
  const valid = (value, values, fallback) => values.includes(value) ? value : fallback;
  state.category = valid(state.category,Object.keys(categoryNames),'all');
  state.priority = valid(state.priority,['all','P0','P1','P2'],'all');
  state.status = valid(state.status,['all','published','preprint'],'all');
  state.sub = valid(state.sub,['all','tool','agent','both'],'all');
  state.sort = valid(state.sort,['priority','newest','name'],'priority');
  function render(updateUrl = true) {
    search.value = state.q; priority.value = state.priority; sort.value = state.sort;
    document.querySelectorAll('[data-category]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.category === state.category)));
    document.querySelectorAll('[data-sub]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.sub === state.sub)));
    document.querySelectorAll('[data-status]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.status === state.status)));
    document.querySelector('#saved-only').setAttribute('aria-pressed',String(state.saved));
    document.querySelector('#sandbox-filters').hidden = state.category !== 'sandbox';
    document.querySelector('#category-title').textContent = categoryNames[state.category];
    const terms = state.q.toLowerCase().trim().split(/\s+/).filter(Boolean);
    cards.sort((a,b) => state.sort === 'newest' ? b.dataset.date.localeCompare(a.dataset.date) : state.sort === 'name' ? a.dataset.name.localeCompare(b.dataset.name) : a.dataset.priority.localeCompare(b.dataset.priority) || b.dataset.date.localeCompare(a.dataset.date));
    let count = 0;
    cards.forEach(card => {
      const d = card.dataset;
      const show = (state.category === 'all' || d.category === state.category) && (state.category !== 'sandbox' || state.sub === 'all' || d.sub === state.sub) && (state.priority === 'all' || state.priority === d.priority) && (state.status === 'all' || d.status === state.status) && (!state.saved || saved.has(d.id)) && terms.every(t => d.search.includes(t));
      card.hidden = !show; if (show) count++; list.append(card);
    });
    document.querySelector('#result-count').textContent = `${count} 篇 / 共 ${cards.length} 篇`;
    document.querySelector('#empty').hidden = count !== 0;
    if (updateUrl) {
      const next = new URLSearchParams();
      Object.entries(state).forEach(([k,v]) => {if (k === 'saved') {if(v) next.set(k,'1');} else if(v && v !== 'all' && !(k === 'sort' && v === 'priority')) next.set(k,v);});
      history.replaceState(null,'',location.pathname + (next.size ? '?' + next.toString() : '') + location.hash);
    }
  }
  document.querySelectorAll('[data-category]').forEach(b => b.addEventListener('click', () => {state.category=b.dataset.category; state.sub='all'; render();}));
  document.querySelectorAll('[data-sub]').forEach(b => b.addEventListener('click', () => {state.sub=b.dataset.sub; render();}));
  document.querySelectorAll('[data-status]').forEach(b => b.addEventListener('click', () => {state.status=b.dataset.status; render();}));
  document.querySelector('#saved-only').addEventListener('click', () => {state.saved=!state.saved; render();});
  search.addEventListener('input', () => {state.q=search.value;render();});
  priority.addEventListener('change', () => {state.priority=priority.value;render();});
  sort.addEventListener('change', () => {state.sort=sort.value;render();});
  document.querySelectorAll('[data-reset]').forEach(b => b.addEventListener('click', () => {Object.assign(state,{category:'all',sub:'all',q:'',priority:'all',status:'all',saved:false,sort:'priority'});render();}));
  window.addEventListener('keydown', e => {if(e.key==='/' && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)){e.preventDefault();search.focus();}});
  render(false);
})();
