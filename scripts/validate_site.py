#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check source/PDF integrity, review coverage, evidence pages, and generated links."""
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from build_site import ROOT, load_reviews, SECTIONS

class Document(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set(); self.duplicates=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:self.duplicates.append(attrs['id'])
            self.ids.add(attrs['id'])
        for name in ['href','src']:
            if name in attrs:self.links.append(attrs[name])

def main():
    papers,reviews=load_reviews()
    assert len(papers)==35, 'Update expected release count when adding papers'
    hashes=set()
    for p in papers:
        source=ROOT/p['local_path'];raw=source.read_bytes()
        assert raw.startswith(b'%PDF-'), source
        digest=hashlib.sha256(raw).hexdigest()
        assert digest==p['sha256'] and len(raw)==p['bytes'], source
        assert digest not in hashes, 'Duplicate PDF'
        hashes.add(digest)
        for evidence in reviews[p['id']]['evidence']:
            assert evidence.get('section') and evidence.get('note'), (p['id'],evidence)
            pages=evidence['pages']; assert isinstance(pages,list) and pages,(p['id'],pages)
            assert all(isinstance(n,int) and 1<=n<=p['pages'] for n in pages),(p['id'],pages)
        deployed=ROOT/'_site/pdfs'/f'{p["id"]}.pdf'
        assert hashlib.sha256(deployed.read_bytes()).hexdigest()==digest, deployed
    docs={}
    for f in (ROOT/'_site').rglob('*.html'):
        doc=Document();doc.feed(f.read_text(encoding='utf-8'))
        assert not doc.duplicates,(f,doc.duplicates)
        docs[f.resolve()]=doc
    count=0
    for f,doc in docs.items():
        for link in doc.links:
            parsed=urlsplit(link)
            if parsed.scheme or parsed.netloc:continue
            target=(f.parent/unquote(parsed.path)).resolve() if parsed.path else f
            if target.is_dir():target=target/'index.html'
            assert target.exists(),(f,link)
            if parsed.fragment and target.suffix=='.html':
                assert unquote(parsed.fragment) in docs[target].ids,(f,link)
            count+=1
    for p in papers:
        doc=docs[(ROOT/'_site/papers'/f'{p["id"]}.html').resolve()]
        assert all(k in doc.ids for k,_,_ in SECTIONS),p['id']
    print(f'PASS: {len(papers)} reviews, 35 source/deployed PDF hashes, evidence pages, {len(docs)} HTML documents, {count} local links.')

if __name__=='__main__':main()
