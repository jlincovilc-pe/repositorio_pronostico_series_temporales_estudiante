from __future__ import annotations
import argparse
from pathlib import Path
import nbformat
from nbclient import NotebookClient

ROOT=Path(__file__).resolve().parents[1]
NB_DIR=ROOT/"notebooks"

def execute(path: Path, timeout: int) -> None:
    nb=nbformat.read(path,as_version=4)
    NotebookClient(nb,timeout=timeout,kernel_name="python3",resources={"metadata":{"path":str(ROOT)}}).execute()
    nbformat.write(nb,path)
    print(f"Executed: {path.relative_to(ROOT)}")

def main() -> None:
    parser=argparse.ArgumentParser(description="Execute course notebooks from repository root")
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--notebook",help="Notebook number, e.g. 01 or 7")
    group.add_argument("--all",action="store_true",help="Execute all notebooks in order")
    parser.add_argument("--timeout",type=int,default=1800,help="Per-cell timeout in seconds")
    args=parser.parse_args()
    paths=sorted(NB_DIR.glob("0[1-8]_*.ipynb"))
    if not args.all:
        number=str(args.notebook).zfill(2)
        paths=[p for p in paths if p.name.startswith(number+"_")]
        if len(paths)!=1: raise SystemExit(f"Notebook not found or ambiguous: {args.notebook}")
    for path in paths: execute(path,args.timeout)
if __name__=="__main__": main()
