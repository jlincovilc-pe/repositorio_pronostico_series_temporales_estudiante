from pathlib import Path
import json, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from _common import OPTIONAL_LARGE_DATASETS
REG=yaml.safe_load((ROOT/"registry.yaml").read_text())
def products(): return [ROOT/f for d in REG["datasets"] for f in d["files"]]
def present_products(): return [p for p in products() if p.exists()]
def test_inventory():
    assert len(REG["datasets"])==8
    assert len(products())==9
    missing=[p for p in products() if not p.exists()]
    assert all(p.relative_to(ROOT).as_posix() in OPTIONAL_LARGE_DATASETS for p in missing), missing
    assert all(p.stat().st_size>0 for p in present_products())
def test_receipts_and_source_limits():
    for p in present_products():
        r=json.loads(p.with_suffix(p.suffix+".receipt.json").read_text())
        assert r["output"]["bytes"]==p.stat().st_size
        assert r["source"]["downloaded_bytes"]<=500*1024*1024
def test_large_panel_contracts():
    e=json.loads((ROOT/"data/05_electricity/electricity_long.csv.receipt.json").read_text())["details"]
    p=json.loads((ROOT/"data/07_traffic_pems/traffic_pems.csv.receipt.json").read_text())["details"]
    assert e["rows"]==370*26304 and e["duplicate_keys"]==0
    assert p["rows"]==440*144 and p["series"]==963
def test_no_kaggle_or_credentials():
    token="ka"+"ggle"
    source="\n".join(p.read_text(errors="ignore") for p in (ROOT/"scripts").rglob("*.py"))
    assert token not in source.lower()
    assert not list(ROOT.rglob(token+".json"))
