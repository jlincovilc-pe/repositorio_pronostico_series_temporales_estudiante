from __future__ import annotations
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from _common import download
SOURCES={
"metro":("https://archive.ics.uci.edu/static/public/492/metro+interstate+traffic+volume.zip","metro.zip"),
"energy":("https://archive.ics.uci.edu/static/public/374/appliances+energy+prediction.zip","energy.zip"),
"beijing":("https://archive.ics.uci.edu/static/public/381/beijing+pm2+5+data.zip","beijing.zip"),
"bike":("https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip","bike.zip"),
"electricity":("https://archive.ics.uci.edu/static/public/321/electricityloaddiagrams20112014.zip","electricity.zip"),
"opsd":("https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv","opsd.csv"),
"pems":("https://archive.ics.uci.edu/static/public/204/pems+sf.zip","pems.zip"),
"m3":("https://zenodo.org/api/records/4656298/files/m3_monthly_dataset.zip/content","m3_monthly.zip")}
def main():
    raw=ROOT/"raw"; raw.mkdir(exist_ok=True)
    for name,(url,filename) in SOURCES.items():
        print(f"Downloading {name}...",flush=True)
        meta=download(url,raw/filename)
        print(name,meta["downloaded_bytes"],meta["source_sha256"],flush=True)
if __name__=="__main__": main()
