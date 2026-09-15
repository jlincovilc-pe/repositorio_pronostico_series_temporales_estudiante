from pathlib import Path
import nbformat
ROOT=Path(__file__).resolve().parents[1]
NOTEBOOKS=sorted((ROOT/"notebooks").glob("0[1-8]_*.ipynb"))
DATA_PATHS=[
 "data/01_traffic_metro/traffic.csv","data/02_energy/energy.csv",
 "data/03_beijing/beijing_pm25.csv","data/04_bike/bike_hour.csv",
 "data/05_electricity/electricity_long.csv","data/06_opsd/germany_energy.csv",
 "data/07_traffic_pems/traffic_pems.csv","data/08_m3/m3_monthly.csv",
]
REQUIRED=["Sección 0","Análisis previo","Estrategia de validación","Modelado","Análisis posterior","Lecciones metodológicas","Ejercicios"]
def test_notebook_contract():
 assert len(NOTEBOOKS)==8
 for path in NOTEBOOKS:
  nb=nbformat.read(path,as_version=4); nbformat.validate(nb); assert 80<=len(nb.cells)<=120
  joined="\n".join(c.source for c in nb.cells if c.cell_type=="markdown").lower()
  assert "methodology card" in joined and "seed" in joined
  assert all(term.lower() in joined for term in REQUIRED)
def test_execution():
 for path in NOTEBOOKS:
  nb=nbformat.read(path,as_version=4); cells=[c for c in nb.cells if c.cell_type=="code"]
  assert all(c.execution_count is not None for c in cells)
  assert not [o for c in cells for o in c.get("outputs",[]) if o.output_type=="error"]
def test_data_references():
 for path,needle in zip(NOTEBOOKS,DATA_PATHS):
  nb=nbformat.read(path,as_version=4); assert needle in "\n".join(c.source for c in nb.cells)
def test_final_delivery_methods():
 s7="\n".join(c.source for c in nbformat.read(NOTEBOOKS[6],as_version=4).cells)
 s8="\n".join(c.source for c in nbformat.read(NOTEBOOKS[7],as_version=4).cells)
 assert "770" in s7 and "193" in s7 and "CompactNBeats" in s7 and "TFTLike" in s7
 assert "H=18" in s8.replace(" ","") and "QUANTILES" in s8 and "Model Card" in s8 and "Resumen global del curso" in s8
