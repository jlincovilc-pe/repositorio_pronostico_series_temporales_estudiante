from __future__ import annotations
import hashlib
from pathlib import Path
from _common import OPTIONAL_LARGE_DATASETS
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"MANIFEST.sha256"
def sha256(path: Path) -> str:
    digest=hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda:stream.read(8*1024*1024),b""): digest.update(chunk)
    return digest.hexdigest()
def main() -> None:
    EXCLUDED_DIRS={".git",".venv",".pytest_cache","__pycache__",".benchmarks",".ipynb_checkpoints"}
    files=sorted(p for p in ROOT.rglob("*") if p.is_file() and p!=MANIFEST and EXCLUDED_DIRS.isdisjoint(p.parts) and p.relative_to(ROOT).as_posix() not in OPTIONAL_LARGE_DATASETS)
    MANIFEST.write_text("\n".join(f"{sha256(p)}  {p.relative_to(ROOT).as_posix()}" for p in files)+"\n",encoding="utf-8")
    print(f"Wrote {MANIFEST.name}: {len(files)} files")
if __name__=="__main__": main()
