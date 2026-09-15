from __future__ import annotations
import ast, hashlib, json
from pathlib import Path
import pandas as pd
import yaml
from _common import OPTIONAL_LARGE_DATASETS
ROOT=Path(__file__).resolve().parents[1]
def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(4*1024*1024),b""): h.update(chunk)
    return h.hexdigest()
def csv_shape(path):
    receipt=json.loads(path.with_suffix(path.suffix+".receipt.json").read_text())
    return receipt["details"]["rows"],len(receipt["details"]["columns"])
def main():
    reg=yaml.safe_load((ROOT/"registry.yaml").read_text())
    assert reg["generated_data_included"] is True and len(reg["datasets"])==8
    files=[ROOT/f for d in reg["datasets"] for f in d["files"]]
    assert len(files)==9
    missing=[p for p in files if not p.is_file()]
    assert all(p.relative_to(ROOT).as_posix() in OPTIONAL_LARGE_DATASETS for p in missing), missing
    if missing:
        print("Nota: dataset(s) grande(s) no presentes localmente (regenerar con 'make download && make clean'): "
              +", ".join(p.relative_to(ROOT).as_posix() for p in missing))
    total=0
    for p in files:
        if p in missing: continue
        r=json.loads(p.with_suffix(p.suffix+".receipt.json").read_text())
        assert r["output"]["sha256"]==sha256(p),p
        assert r["output"]["bytes"]==p.stat().st_size
        assert r["source"]["downloaded_bytes"]<=500*1024*1024
        total+=p.stat().st_size
    e=json.loads((ROOT/"data/05_electricity/electricity_long.csv.receipt.json").read_text())["details"]
    assert (e["rows"],e["series"],e["timestamps"],e["duplicate_keys"])==(9732480,370,26304,0)
    p=json.loads((ROOT/"data/07_traffic_pems/traffic_pems.csv.receipt.json").read_text())["details"]
    assert (p["rows"],p["days"],p["series"])==(63360,440,963)
    for src_dir in (ROOT/"scripts",ROOT/"tests"):
        for py in src_dir.rglob("*.py"): ast.parse(py.read_text(),filename=str(py))
    print(f"Valid: 8 datasets, {len(files)-len(missing)}/9 CSVs present, {total} bytes, receipts/hashes/large-panel contracts verified.")
if __name__=="__main__": main()
