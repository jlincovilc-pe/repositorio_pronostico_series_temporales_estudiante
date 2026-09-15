from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
REQUIRED_DOCS=[
 "README.md","docs/INSTALLATION.md","docs/NOTEBOOK_GUIDE.md",
 "docs/ARCHITECTURE.md","docs/REPRODUCIBILITY.md",
 "docs/TROUBLESHOOTING.md","docs/COURSE_GUIDE.md",
 "docs/COURSE_SUMMARY.md","docs/DATA_GOVERNANCE.md",
 "docs/SOURCE_NOTES.md","CONTRIBUTING.md",
]
def test_required_documentation_exists():
 for rel in REQUIRED_DOCS:
  path=ROOT/rel
  assert path.is_file() and path.stat().st_size>200, rel

def test_readme_onboarding_contract():
 text=(ROOT/"README.md").read_text(encoding="utf-8")
 required=["Inicio rápido","Requisitos","Ruta de aprendizaje","Inventario de datos","Cómo usar el repositorio","Limitaciones que debe conocer","Integridad, licencia y citas"]
 assert all(section in text for section in required)
 assert "Python" in text and "RAM" in text and "Disco" in text and "GPU" in text

def test_notebook_guide_covers_all_weeks():
 text=(ROOT/"docs/NOTEBOOK_GUIDE.md").read_text(encoding="utf-8")
 for week in range(1,9):
  assert f"0{week}_semana_{week}" in text
 assert "Tiempo CPU" in text and "DeepAR opcional" in text

def test_relative_markdown_links_resolve():
 files=[ROOT/"README.md",ROOT/"notebooks/README.md"]
 pattern=re.compile(r"\[[^]]+\]\(([^)]+)\)")
 for source in files:
  for target in pattern.findall(source.read_text(encoding="utf-8")):
   if target.startswith(("http://","https://","#")): continue
   path=(source.parent/target).resolve()
   assert path.exists(), f"{source.relative_to(ROOT)} -> {target}"

def test_operational_helpers_exist():
 for rel in ["scripts/run_notebooks.py","scripts/clean_raw.py","scripts/build_manifest.py",".python-version"]:
  assert (ROOT/rel).is_file(), rel
 # el workflow de CI vive en la raíz del repo monorepo, no en este subpaquete,
 # porque GitHub Actions solo lee .github/workflows/ desde la raíz del repositorio.
 assert (ROOT.parent/".github/workflows/ci.yml").is_file()
