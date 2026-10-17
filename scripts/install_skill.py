#!/usr/bin/env python3
"""Install one local Skill without overwriting an existing destination by default."""
from argparse import ArgumentParser
from pathlib import Path
import shutil
import sys

def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('skill_dir', type=Path, help='local Skill directory containing SKILL.md')
    parser.add_argument('--destination', type=Path, required=True, help='parent directory for the installed Skill')
    parser.add_argument('--force', action='store_true', help='replace an existing destination')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    source = args.skill_dir.resolve()
    destination = args.destination.resolve()
    target = destination / source.name
    if not (source/'SKILL.md').is_file():
        print(f'error: {source} does not contain SKILL.md', file=sys.stderr); return 2
    # Never remove the source itself or copy a source into one of its children.
    if target == source or source in target.parents or destination == source or source in destination.parents:
        print(f'error: destination would overwrite or contain source: {destination}', file=sys.stderr); return 4
    if target.exists() and not args.force:
        print(f'error: destination exists: {target} (use --force to replace)', file=sys.stderr); return 3
    if args.dry_run:
        print(f'would install {source} -> {target}'); return 0
    args.destination.mkdir(parents=True, exist_ok=True)
    if target.exists(): shutil.rmtree(target)
    shutil.copytree(source, target)
    print(f'installed {source.name} -> {target}')
    return 0

if __name__ == '__main__': raise SystemExit(main())
