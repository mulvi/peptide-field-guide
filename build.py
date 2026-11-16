#!/usr/bin/env python3
"""Rebuild index.html (the live site) from src/app.html (the app source)."""
import pathlib
root = pathlib.Path(__file__).parent
HEAD = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="description" content="Free peptide reconstitution and dose calculator, with an evidence-graded library. Nothing for sale.">'
        '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style></head><body>\n')
src = (root / 'src' / 'app.html').read_text(encoding='utf-8').rstrip('\n')
(root / 'index.html').write_text(HEAD + src + '\n</body></html>\n', encoding='utf-8')
print('index.html rebuilt,', len(src), 'chars')
