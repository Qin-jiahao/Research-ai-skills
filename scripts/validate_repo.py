#!/usr/bin/env python3
"""Small dependency-free static checks for this repository."""
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
errors=[]
seen=set()
for path in sorted((root/'skills').glob('*/SKILL.md')):
    text=path.read_text(encoding='utf-8')
    if not text.startswith('---\n') or '\n---\n' not in text[4:]: errors.append(f'{path}: missing frontmatter') ; continue
    block=text.split('---\n',2)[1]
    name=re.search(r'^name:\s*([a-z0-9-]+)\s*$',block,re.M)
    desc=re.search(r'^description:\s*(.+)$',block,re.M)
    if not name: errors.append(f'{path}: invalid name')
    else:
        if name.group(1) in seen: errors.append(f'{path}: duplicate name')
        seen.add(name.group(1))
    if not desc: errors.append(f'{path}: missing description')
    for required in ('## ','Source'):
        if required not in text: errors.append(f'{path}: missing {required}')
for path in sorted((root/'prompts').glob('*/*.md')):
    text=path.read_text(encoding='utf-8')
    if '中文' not in text or 'English' not in text: errors.append(f'{path}: bilingual sections missing')
for readme, directory in [('skills/README.md','skills'),('prompts/README.md','prompts')]:
    if not (root/readme).exists(): errors.append(f'{readme}: missing')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'validated {len(seen)} Skills and bilingual Prompt files')
