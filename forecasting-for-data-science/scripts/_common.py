from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
MAX_BYTES=500*1024*1024
USER_AGENT="course-timeseries-benchmarks-pro/1.0"
# Datasets >100 MiB excluidos del repo GitHub (límite de tamaño de archivo);
# se regeneran con `make download && make clean`. El .receipt.json sí queda versionado.
OPTIONAL_LARGE_DATASETS={"data/05_electricity/electricity_long.csv","data/07_traffic_pems/traffic_pems.csv"}
def download(url: str, dest: Path, max_bytes: int=MAX_BYTES):
    dest.parent.mkdir(parents=True,exist_ok=True); tmp=dest.with_suffix(dest.suffix+".part")
    h=hashlib.sha256(); size=0
    req=Request(url,headers={"User-Agent":USER_AGENT})
    with urlopen(req,timeout=180) as r, tmp.open("wb") as f:
        declared=r.headers.get("Content-Length")
        if declared and int(declared)>max_bytes: raise RuntimeError(f"Source >500 MiB: {declared}")
        while True:
            chunk=r.read(1024*1024)
            if not chunk: break
            size+=len(chunk)
            if size>max_bytes: raise RuntimeError(f"Source >500 MiB while streaming: {url}")
            h.update(chunk); f.write(chunk)
    tmp.replace(dest)
    return {"url":url,"downloaded_bytes":size,"source_sha256":h.hexdigest()}
def sha256(path: Path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()
def write_receipt(output: Path, source: dict, details: dict):
    payload={"created_at_utc":datetime.now(timezone.utc).isoformat(),"source":source,
             "output":{"path":output.name,"bytes":output.stat().st_size,"sha256":sha256(output)},"details":details}
    output.with_suffix(output.suffix+".receipt.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False),encoding="utf-8")
