# Guía de instalación

## Entorno recomendado

- Python 3.11; rango soportado por el proyecto: 3.10–3.13.
- 8 GiB RAM para semanas 1–4/8; 16 GiB recomendados para 5–7.
- 2 GiB libres si se regeneran los datos.
- GPU opcional. Los resultados incluidos fueron producidos en CPU.

## Instalación estándar

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/validate_repository.py
python -m pytest -q
```

En Windows PowerShell active con `.venv\Scripts\Activate.ps1`.

## PyTorch

`requirements.txt` instala la distribución que pip seleccione para su plataforma. Para una build CPU/GPU específica siga el selector oficial de PyTorch y luego instale el resto de dependencias. GPU no es requisito para el curso.

## Verificación rápida

```bash
python -c "import pandas, statsmodels, lightgbm, torch; print('entorno OK')"
jupyter lab
```

## Instalación mínima sin notebooks DL

Si solo estudiará semanas 1–5 y 8 puede omitir PyTorch, pero los tests de ejecución histórica seguirán leyendo notebooks con outputs ya almacenados.
