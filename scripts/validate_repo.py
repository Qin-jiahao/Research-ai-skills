#!/usr/bin/env python3
"""Small dependency-free static checks for this repository."""
from pathlib import Path
import json
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
    index = root/readme
    if not index.exists():
        errors.append(f'{readme}: missing')
        continue
    links = re.findall(r'\[[^]]+\]\(([^)]+)\)', index.read_text(encoding='utf-8'))
    for link in links:
        if link.startswith(('http://','https://','#')):
            continue
        target = (index.parent/link).resolve()
        if not target.exists():
            errors.append(f'{readme}: broken local link {link}')
    expected = sorted((root/directory).glob('*/SKILL.md' if directory=='skills' else '*/*.md'))
    if directory == 'skills':
        expected_links = {f'{p.parent.name}/SKILL.md' for p in expected}
    else:
        expected_links = {f'{p.parent.name}/{p.name}' for p in expected}
    indexed_links = {x for x in links if not x.startswith(('http://','https://','#'))}
    missing = expected_links - indexed_links
    for item in sorted(missing):
        errors.append(f'{readme}: missing index entry {item}')
catalog_path = root/'catalog/resources.json'
if not catalog_path.exists():
    errors.append('catalog/resources.json: missing')
else:
    try:
        catalog = json.loads(catalog_path.read_text(encoding='utf-8'))
        resources = catalog['resources']
        ids = [item.get('id') for item in resources]
        expected_ids = [f'R{i:02d}' for i in range(1, 32)]
        if ids != expected_ids:
            errors.append('catalog/resources.json: IDs must be exactly R01-R31 in order')
        allowed = {'collected','reviewed','tested','released'}
        required = {'id','name','type','category','status','path','source_url','reason'}
        for item in resources:
            missing = required - item.keys()
            if missing: errors.append(f"catalog/{item.get('id','?')}: missing fields {sorted(missing)}")
            if item.get('status') not in allowed: errors.append(f"catalog/{item.get('id','?')}: invalid status")
            if item.get('path') and not (root/item['path']).exists(): errors.append(f"catalog/{item.get('id','?')}: missing local path {item['path']}")
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        errors.append(f'catalog/resources.json: invalid catalog ({exc})')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'validated {len(seen)} Skills and bilingual Prompt files')
