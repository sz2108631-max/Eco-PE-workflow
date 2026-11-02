#!/usr/bin/env python3
"""Create an empty, non-destructive empirical research project."""
import argparse
import shutil
from pathlib import Path

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('destination', type=Path)
    args = ap.parse_args()
    root = args.destination.resolve()
    if root.exists():
        ap.error('Destination exists; choose a new directory. Nothing overwritten.')
    root.mkdir(parents=True)
    for folder in ['code','data/raw','data/intermediate','data/analysis','outputs/tables','outputs/figures','logs','audit']:
        (root / folder).mkdir(parents=True, exist_ok=True)
    templates = Path(__file__).resolve().parents[1] / 'templates'
    for name in ['profile.json','research-spec.json']:
        shutil.copyfile(templates / name, root / name)
    (root / 'audit/run_report.md').write_text('# Run report\n\nStatus: initialized, analysis not executed.\n', encoding='utf-8')
    (root / 'README.md').write_text('# Empirical project\n\nComplete research-spec.json, audit data, then implement the selected engine master entrypoint. No estimates have been generated.\n', encoding='utf-8')
    print(root)

if __name__ == '__main__':
    main()
