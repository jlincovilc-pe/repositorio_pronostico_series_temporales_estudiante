from __future__ import annotations
import csv, gzip, json, shutil, sys, zipfile
from pathlib import Path
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from _common import sha256, write_receipt
RAW=ROOT/"raw"; DATA=ROOT/"data"
URLS={
"metro":"https://archive.ics.uci.edu/static/public/492/metro+interstate+traffic+volume.zip",
"energy":"https://archive.ics.uci.edu/static/public/374/appliances+energy+prediction.zip",
"beijing":"https://archive.ics.uci.edu/static/public/381/beijing+pm2+5+data.zip",
"bike":"https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip",
"electricity":"https://archive.ics.uci.edu/static/public/321/electricityloaddiagrams20112014.zip",
"opsd":"https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv",
"pems_requested":"https://archive.ics.uci.edu/static/public/204/pems-sf.zip",
"pems":"https://archive.ics.uci.edu/static/public/204/pems+sf.zip",
"m3":"https://zenodo.org/api/records/4656298/files/m3_monthly_dataset.zip/content"}
def source_meta(name,filename):
    p=RAW/filename
    out={"url":URLS[name],"downloaded_bytes":p.stat().st_size,"source_sha256":sha256(p)}
    if name=="pems": out["requested_url_404"]=URLS["pems_requested"]
    return out
def save(df,out,source,details,date_format=None):
    out.parent.mkdir(parents=True,exist_ok=True); df.to_csv(out,index=False,date_format=date_format)
    write_receipt(out,source,{**details,"rows":len(df),"columns":list(df.columns),"nulls":int(df.isna().sum().sum())})
def metro():
    with zipfile.ZipFile(RAW/"metro.zip") as z, z.open("Metro_Interstate_Traffic_Volume.csv.gz") as b, gzip.open(b,"rt") as f: df=pd.read_csv(f)
    df.columns=[c.strip().lower() for c in df.columns]; df=df.rename(columns={"date_time":"ds","traffic_volume":"y"}); df["ds"]=pd.to_datetime(df["ds"]); df["holiday"]=df["holiday"].fillna("None")
    save(df,DATA/"01_traffic_metro/traffic.csv",source_meta("metro","metro.zip"),{"target":"y","frequency":"hourly","cleaning":"decompressed nested gzip; standardized date_time->ds and traffic_volume->y"},"%Y-%m-%d %H:%M:%S")
def energy():
    with zipfile.ZipFile(RAW/"energy.zip") as z, z.open("energydata_complete.csv") as f: df=pd.read_csv(f)
    df.columns=[c.strip().lower().replace(" ","_") for c in df.columns]; df=df.rename(columns={"date":"ds","appliances":"y"}); df["ds"]=pd.to_datetime(df["ds"])
    save(df,DATA/"02_energy/energy.csv",source_meta("energy","energy.zip"),{"target":"y","frequency":"10min","cleaning":"trimmed/lowercased column names; date->ds, appliances->y"},"%Y-%m-%d %H:%M:%S")
def beijing():
    with zipfile.ZipFile(RAW/"beijing.zip") as z, z.open("PRSA_data_2010.1.1-2014.12.31.csv") as f: df=pd.read_csv(f)
    df=df.iloc[24:].copy(); df["ds"]=pd.to_datetime(df[["year","month","day","hour"]]); df=df[["ds"]+[c for c in df.columns if c!="ds"]]
    save(df,DATA/"03_beijing/beijing_pm25.csv",source_meta("beijing","beijing.zip"),{"target":"pm2.5","frequency":"hourly","cleaning":"removed first 24 rows as requested; created ds; interior PM2.5 gaps retained"},"%Y-%m-%d %H:%M:%S")
def bike():
    with zipfile.ZipFile(RAW/"bike.zip") as z:
        for member,name in [("hour.csv","bike_hour.csv"),("day.csv","bike_day.csv")]:
            with z.open(member) as f: df=pd.read_csv(f)
            df.columns=[c.strip().lower() for c in df.columns]; df["dteday"]=pd.to_datetime(df["dteday"])
            save(df,DATA/"04_bike"/name,source_meta("bike","bike.zip"),{"target":"cnt","frequency":"hourly" if member.startswith("hour") else "daily","cleaning":f"extracted {member}; normalized headers and date"},"%Y-%m-%d")
def electricity():
    out=DATA/"05_electricity/electricity_long.csv"; out.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(RAW/"electricity.zip") as z, z.open("LD2011_2014.txt") as f:
        wide=pd.read_csv(f,sep=";",decimal=",",low_memory=False)
    wide=wide.rename(columns={wide.columns[0]:"ds"}); wide["ds"]=pd.to_datetime(wide["ds"],format="%Y-%m-%d %H:%M:%S")
    wide=wide[(wide["ds"]>=pd.Timestamp("2012-01-01"))&(wide["ds"]<pd.Timestamp("2015-01-01"))]
    series=[c for c in wide.columns if c!="ds"]
    values=wide.set_index("ds")[series].apply(pd.to_numeric,errors="coerce").resample("1h").sum(min_count=1)
    expected=pd.date_range("2012-01-01","2014-12-31 23:00:00",freq="h")
    values=values.reindex(expected); values.index.name="ds"
    long=values.reset_index().melt(id_vars="ds",var_name="unique_id",value_name="y")
    long.to_csv(out,index=False,date_format="%Y-%m-%d %H:%M:%S")
    details={"rows":len(long),"columns":["ds","unique_id","y"],"series":len(series),"timestamps":len(expected),"frequency":"hourly","target":"y","nulls":int(long.y.isna().sum()),"duplicate_keys":int(long.duplicated(["unique_id","ds"]).sum()),"cleaning":"filtered [2012-01-01, 2015-01-01); decimal comma parsed; 15-minute values summed hourly; reindexed to 26,304 hours; melted to long"}
    write_receipt(out,source_meta("electricity","electricity.zip"),details)
def opsd():
    header=pd.read_csv(RAW/"opsd.csv",nrows=0).columns.tolist(); keep=[c for c in header if c in ("utc_timestamp","cet_cest_timestamp") or c.startswith("DE_")]
    df=pd.read_csv(RAW/"opsd.csv",usecols=keep,low_memory=False); df=df.rename(columns={"utc_timestamp":"ds_utc"}); df["ds_utc"]=pd.to_datetime(df["ds_utc"],utc=True)
    save(df,DATA/"06_opsd/germany_energy.csv",source_meta("opsd","opsd.csv"),{"frequency":"hourly","target_candidates":[c for c in keep if "load_actual" in c],"cleaning":"selected timestamp and all DE_ columns from European single-index file"},"%Y-%m-%dT%H:%M:%SZ")
def parse_pems_line(line):
    line=line.strip().strip("[]")
    # MATLAB rows are separated by semicolons; each row is a sensor, columns are 10-minute slots.
    rows=[np.fromstring(part,sep=" ",dtype=np.float32) for part in line.split(";")]
    if len(rows)!=963 or any(len(r)!=144 for r in rows): raise ValueError(f"Unexpected PeMS shape: {len(rows)} x {set(map(len,rows))}")
    return np.vstack(rows).T
def _parse_vector(text, dtype=int):
    return np.fromstring(text.strip().strip("[]"),sep=" ",dtype=dtype)
def pems():
    out=DATA/"07_traffic_pems/traffic_pems.csv"; out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists(): out.unlink()
    first=True; days=0; rows_total=0
    with zipfile.ZipFile(RAW/"pems.zip") as z:
        station_ids=_parse_vector(z.read("stations_list").decode(),int)
        if len(station_ids)!=963: raise ValueError(f"Expected 963 station IDs, got {len(station_ids)}")
        sensor_cols=[f"station_{x}" for x in station_ids]
        for split,member,label_member in [("train","PEMS_train","PEMS_trainlabels"),("test","PEMS_test","PEMS_testlabels")]:
            labels=_parse_vector(z.read(label_member).decode(),int)
            with z.open(member) as f:
                lines=list(f)
            if len(lines)!=len(labels): raise ValueError(f"{split}: {len(lines)} days but {len(labels)} labels")
            for raw_line,weekday in zip(lines,labels):
                mat=parse_pems_line(raw_line.decode("utf-8")); n=len(mat)
                frame=pd.DataFrame(mat,columns=sensor_cols); frame.insert(0,"weekday_label",int(weekday)); frame.insert(0,"slot_10min",np.arange(n,dtype=np.int16)); frame.insert(0,"day_id",days); frame.insert(0,"split",split)
                frame.to_csv(out,index=False,mode="a",header=first,float_format="%.4f"); first=False; days+=1; rows_total+=n
    write_receipt(out,source_meta("pems","pems.zip"),{"rows":rows_total,"columns":["split","day_id","slot_10min","weekday_label"]+sensor_cols,"days":days,"series":963,"frequency":"10min within each day","nulls":0,"station_ids_count":len(station_ids),"cleaning":"parsed 440 MATLAB day matrices; combined train/test; attached weekday labels 1-7 and actual station IDs; retained positional day/slot because calendar dates are absent"})
def m3():
    cache=DATA/"08_m3/_cache"; target=cache/"m3/datasets/m3_monthly_dataset.zip"; target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(RAW/"m3_monthly.zip",target)
    with zipfile.ZipFile(target) as z: z.extractall(target.parent)
    from datasetsforecast.m3 import M3
    df,*_=M3.load(str(cache),group="Monthly"); out=DATA/"08_m3/m3_monthly.csv"
    save(df,out,source_meta("m3","m3_monthly.zip"),{"target":"y","frequency":"monthly","series":int(df.unique_id.nunique()),"cleaning":"parsed public Zenodo TSF via datasetsforecast M3.load(group=Monthly)"},"%Y-%m-%d")
    shutil.rmtree(cache)
TASKS=[metro,energy,beijing,bike,electricity,opsd,pems,m3]
def main():
    for fn in TASKS: print(f"Cleaning {fn.__name__}...",flush=True); fn()
if __name__=="__main__": main()
