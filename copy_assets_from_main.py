#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import shutil
import sys

HERE = Path(__file__).resolve().parent
DEST = HERE / "assets"
DEST.mkdir(exist_ok=True)

if len(sys.argv) >= 2:
    main_repo = Path(sys.argv[1]).expanduser().resolve()
else:
    # GitHub Desktop 기본 관리 방식처럼 저장소들이 같은 상위 폴더에 있을 때 자동 탐색
    candidates = [
        HERE.parent / "minhosong-mse.github.io",
        HERE.parent.parent / "minhosong-mse.github.io",
    ]
    main_repo = next((p for p in candidates if p.is_dir()), None)

if not main_repo:
    print("ERROR: minhosong-mse.github.io local repository was not found.")
    print("Usage: py copy_assets_from_main.py \"C:\\path\\to\\minhosong-mse.github.io\"")
    raise SystemExit(1)

mapping = {
    "발표사진.png": "conference-presentation.png",
    "발표순서.png": "conference-program-order.png",
}

for src_name, dst_name in mapping.items():
    src = main_repo / src_name
    if not src.is_file():
        print(f"ERROR: Missing source file: {src}")
        raise SystemExit(1)
    shutil.copy2(src, DEST / dst_name)
    print(f"Copied: {src_name} -> assets/{dst_name}")

print("Done.")
print("Optional: change the README image URLs to local assets paths later if desired.")
