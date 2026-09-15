from __future__ import annotations
import shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
raw=ROOT/"raw"
if raw.exists():
    size=sum(p.stat().st_size for p in raw.rglob("*") if p.is_file())
    shutil.rmtree(raw)
    print(f"Removed raw/ ({size/2**20:.1f} MiB)")
else:
    print("raw/ does not exist; nothing to remove")
