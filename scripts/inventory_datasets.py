#!/usr/bin/env python3
"""Build a read-only dataset catalog; never change source files."""
import csv
import hashlib
import json
import math
import os
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'datasets' / 'curation-v1'


def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def relative(path):
    return path.relative_to(ROOT).as_posix()


def csv_write(name, fields, rows):
    with (OUT / name).open('x', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def yolo_issues(path):
    issues = []
    for num, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        parts = line.split()
        if len(parts) != 5:
            issues.append(f'line {num}: expected five values')
            continue
        try:
            cls = int(parts[0])
            x, y, w, h = map(float, parts[1:])
        except ValueError:
            issues.append(f'line {num}: invalid numeric value')
            continue
        if cls != 0 or not all(map(math.isfinite, (x, y, w, h))) or w <= 0 or h <= 0 or x-w/2 < -1e-6 or x+w/2 > 1+1e-6 or y-h/2 < -1e-6 or y+h/2 > 1+1e-6:
            issues.append(f'line {num}: class or bounding box outside YOLO bounds')
    return '; '.join(issues)


def main():
    if OUT.exists():
        raise SystemExit(f'Refusing to overwrite existing output: {OUT}')
    for name in ('dataset_1', 'dataset_2', 'dataset_3'):
        if not (ROOT / name).is_dir():
            raise SystemExit(f'Missing source directory: {name}')
    OUT.mkdir(parents=True)
    files = []
    for name in ('dataset_1', 'dataset_2', 'dataset_3'):
        for p in sorted((ROOT / name).rglob('*')):
            if p.is_file():
                files.append({'dataset': name, 'path': relative(p), 'size_bytes': p.stat().st_size, 'sha256': sha256(p)})
    csv_write('files.csv', ['dataset', 'path', 'size_bytes', 'sha256'], files)
    hashes = defaultdict(list)
    image_ext = {'.jpg', '.jpeg', '.png', '.webp'}
    for item in files:
        if item['dataset'] == 'dataset_2' and Path(item['path']).parent.name == 'IMG' and Path(item['path']).suffix.lower() in image_ext:
            hashes[item['sha256']].append(item['path'])
    duplicates = [{'sha256': key, 'path': p, 'group_size': len(paths)} for key, paths in sorted(hashes.items()) if len(paths) > 1 for p in sorted(paths)]
    csv_write('dataset_2_duplicate_images.csv', ['sha256', 'path', 'group_size'], duplicates)
    rows = []
    for item in files:
        p = ROOT / item['path']
        if item['dataset'] == 'dataset_2' and p.parent.name == 'IMG' and p.suffix.lower() in image_ext:
            txt = ROOT / 'dataset_2' / 'TXT' / (p.stem + '.txt')
            xml = ROOT / 'dataset_2' / 'XML' / (p.stem + '.xml')
            issues = yolo_issues(txt) if txt.is_file() else 'missing YOLO annotation'
            if not xml.is_file():
                issues = '; '.join(filter(None, [issues, 'missing XML annotation']))
            rows.append({'image': item['path'], 'yolo': relative(txt) if txt.is_file() else '', 'xml': relative(xml) if xml.is_file() else '', 'image_sha256': item['sha256'], 'duplicate_group_size': len(hashes[item['sha256']]), 'issues': issues})
    csv_write('dataset_2_index.csv', ['image', 'yolo', 'xml', 'image_sha256', 'duplicate_group_size', 'issues'], rows)
    pairs = []
    for split in ('train', 'val', 'test'):
        root = ROOT / 'dataset_1' / 'pothole_video' / split
        rgb = {p.stem: p for p in (root / 'rgb').glob('*.mp4')}
        masks = {p.stem: p for p in (root / 'mask').glob('*.mp4')}
        for stem in sorted(rgb.keys() | masks.keys()):
            pairs.append({'split': split, 'id': stem, 'rgb': relative(rgb[stem]) if stem in rgb else '', 'mask': relative(masks[stem]) if stem in masks else ''})
    csv_write('dataset_1_video_pairs.csv', ['split', 'id', 'rgb', 'mask'], pairs)
    counts = Counter(x['dataset'] for x in files)
    summary = {'file_count': dict(counts), 'dataset_1_pairs': len(pairs), 'dataset_1_unpaired': sum(not x['rgb'] or not x['mask'] for x in pairs), 'dataset_2_images': len(rows), 'dataset_2_with_issues': sum(bool(x['issues']) for x in rows), 'dataset_2_duplicate_groups': sum(len(x) > 1 for x in hashes.values()), 'dataset_2_duplicate_extra_images': sum(max(len(x)-1, 0) for x in hashes.values()), 'dataset_3_note': 'Export has no annotation data; labels must not be treated as verified negatives.'}
    with (OUT / 'summary.json').open('x', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
        f.write('\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
