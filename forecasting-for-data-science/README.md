# Forecasting for Data Science

Nombre técnico del repositorio: `forecasting-for-data-science` (anteriormente `course-timeseries-benchmarks-pro`).

Curso profesional, reproducible y autocontenido de **Time Series Forecasting y MLOps**. Ocho datasets reales, ocho notebooks ejecutados de principio a fin, scripts de descarga y limpieza, documentación de calidad, pruebas automáticas y garantías de integridad criptográfica.

> **Empiece aquí:** si solo quiere estudiar, instale el entorno y abra los notebooks en orden. Los CSV limpios ya están incluidos, salvo `electricity_long.csv` (semana 5) y `traffic_pems.csv` (semana 7): superan el límite de tamaño de GitHub y se regeneran con `make download && make clean` (requiere internet). Para el resto de semanas no necesita descargar fuentes externas ni ejecutar scripts de preparación.

---

## Tabla de contenidos

1. [Qué aprenderá](#qué-aprenderá)
2. [Filosofía del repositorio](#filosofía-del-repositorio)
3. [Inicio rápido](#inicio-rápido)
4. [Ruta de aprendizaje](#ruta-de-aprendizaje)
5. [Inventario de datos](#inventario-de-datos)
6. [Arquitectura y flujo de datos](#arquitectura-y-flujo-de-datos)
7. [Sistema de reproducibilidad](#sistema-de-reproducibilidad)
8. [Cómo usar el repositorio](#cómo-usar-el-repositorio)
9. [Scripts y tooling](#scripts-y-tooling)
10. [Pruebas y CI](#pruebas-y-ci)
11. [Estructura completa](#estructura-completa)
12. [Documentación complementaria](#documentación-complementaria)
13. [Limitaciones que debe conocer](#limitaciones-que-debe-conocer)
14. [Integridad, licencia y citas](#integridad-licencia-y-citas)

---

## Qué aprenderá

El curso sigue una progresión pedagógica que avanza desde baselines ingenuos y modelos estadísticos clásicos hasta redes neuronales profundas, modelos globales multi-serie, forecasting probabilístico y prácticas de MLOps. Cada semana introduce un nuevo dataset, un nuevo protocolo de validación y un nuevo paradigma de modelado:

| Semana | Tema central | Técnicas | Dataset |
|:---:|---|---|---|
| 1 | Anatomía temporal, estacionalidad y baselines | STL, seasonal naive, ETS, regresión con covariables | Metro Interstate Traffic |
| 2 | Box–Jenkins, estacionariedad y residuos | ADF, KPSS, ACF/PACF, ARIMA, diagnóstico de residuos | Appliances Energy |
| 3 | SARIMAX y disponibilidad de covariables | SARIMA vs SARIMAX, rolling-origin, exógenas meteorológicas | Beijing PM2.5 |
| 4 | Feature engineering sin leakage | Lags, rolling windows, time-based cross-validation, LightGBM | Bike Sharing |
| 5 | Modelos globales y cold-start | Paneles multi-serie, cross-learning, escalado por serie | Electricity (370 clientes) |
| 6 | LSTM y tensores secuenciales | Ventanas móviles, tensores 3D, PyTorch LSTM/GRU | OPSD Germany |
| 7 | Transferencia entre sensores y Transformers | N-BEATS, TFT-like, atención espacial, multi-serie neuronal | PeMS-SF (963 sensores) |
| 8 | Cuantiles, calibración y MLOps | Quantile LightGBM, pinball loss, cobertura, drift, Model Card | M3 Monthly (1,428 series) |

Todos los notebooks incluyen **Methodology Cards** (fichas que documentan split, horizonte, features, seed, métricas y limitaciones), tests estadísticos, validación temporal, diagnóstico de residuos y ejercicios propuestos.

---

## Filosofía del repositorio

Este repositorio se diseñó bajo seis principios que gobiernan cada decisión técnica:

1. **Reproducibilidad total.** Todo artefacto tiene un hash SHA-256 registrado. Las fuentes se descargan con verificación de integridad en streaming. Los splits son explícitos y deterministas (seed 42). El entorno de dependencias está acotado por rangos compatibles.

2. **Autocontenido.** Los CSV limpios se incluyen en el repositorio. Una persona puede clonar, instalar dependencias y ejecutar cualquier notebook sin acceso a internet ni scripts de preparación. `raw/` es temporal y está excluido del release.

3. **Transparencia.** Cada transformación aplicada a los datos está documentada en un receipt JSON que registra URL fuente, bytes descargados, SHA-256 de origen y destino, filas, columnas, nulos y pasos de limpieza. Nada se imputa, deduplica o agrega silenciosamente.

4. **Realismo.** Los datasets contienen las imperfecciones del mundo real: timestamps duplicados, targets ausentes, fechas faltantes, variables con distinta granularidad y covariables que no estarían disponibles en producción. Los notebooks enseñan a detectar y manejar estas situaciones, no a ocultarlas.

5. **Progresión pedagógica.** Cada semana construye sobre la anterior. La complejidad crece en datos (univariado → multi-serie → multivariado), modelos (naive → estadístico → ML → DL) y evaluación (point forecast → probabilístico → MLOps).

6. **Gobierno explícito.** `registry.yaml` es el catálogo machine-readable de datasets. Los tests validan contratos de forma, integridad y documentación. El CI ligero corre en cada push. No se usan credenciales, Kaggle ni fuentes que requieran autenticación.

---

## Inicio rápido

### Requisitos

| Recurso | Mínimo | Recomendado | Notas |
|---|---|---|---|
| **Python** | 3.10 | 3.11 | Compatible con 3.10–3.13 según rangos de `requirements.txt` |
| **RAM** | 8 GiB | 16 GiB | 8 GiB bastan para semanas 1–4 y 8; semanas 5–7 requieren más |
| **Disco** | 1.0 GiB | 2.0 GiB libres | `raw/` añade ~495 MiB temporalmente si regenera datos |
| **CPU** | 2 núcleos | 4 núcleos | GPU no es obligatoria; todos los notebooks se ejecutaron en CPU |
| **SO** | Linux, macOS, Windows+WSL2 | Linux | Los paths usan `/`; en Windows PowerShell active con `.venv\Scripts\Activate.ps1` |

### Instalación

```bash
# 1. Clonar y crear entorno virtual
python -m venv .venv
source .venv/bin/activate              # Windows PowerShell: .venv\Scripts\Activate.ps1

# 2. Instalar dependencias
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# 3. Validar integridad del repositorio
python scripts/validate_repository.py

# 4. Ejecutar tests
python -m pytest -q

# 5. Lanzar JupyterLab
jupyter lab
```

Abra [`notebooks/01_semana_1_eda_baselines_estacionalidad.ipynb`](notebooks/01_semana_1_eda_baselines_estacionalidad.ipynb) y continúe en orden numérico. Cada notebook indica en su primera celda qué librerías necesita y qué conceptos previos asume.

### Verificación rápida del entorno

```bash
python -c "import pandas, statsmodels, lightgbm, torch; print('entorno OK')"
```

Si solo va a estudiar las semanas 1–5 y 8, puede omitir PyTorch (`torch`). Los tests de ejecución histórica seguirán pasando porque leen notebooks con outputs ya almacenados, sin re-ejecutar celdas.

---

## Ruta de aprendizaje

Cada fila de esta tabla es un notebook autocontenido con datos reales, outputs ejecutados y resultados numéricos concretos:

| Semana | Notebook | Dataset | Split | Modelo/tema central | Resultado reproducido | Tiempo CPU* |
|---:|---|---|---|---|---:|---:|
| 1 | [EDA y baselines](notebooks/01_semana_1_eda_baselines_estacionalidad.ipynb) | Metro Traffic | Temporal 80/20 | Seasonal naive, ETS, regresión múltiple | Seasonal Naive 168 obtuvo menor MASE entre baselines | ~1 min |
| 2 | [ARIMA y diagnóstico](notebooks/02_semana_2_arima_estacionariedad_diagnostico.ipynb) | Appliances Energy | 70/15/15 | ARIMA, ETS, Theta | ETS obtuvo menor MASE; ARIMA(1,0,2) seleccionado en validación | ~1 min |
| 3 | [SARIMAX y exógenas](notebooks/03_semana_3_sarimax_variables_exogenas.ipynb) | Beijing PM2.5 | Rolling-origin, 3 folds | SARIMA vs SARIMAX | SARIMAX redujo MAE medio 18.4% en escenario oracle | ~3 min |
| 4 | [Features y ML](notebooks/04_semana_4_feature_engineering_ml.ipynb) | Bike Sharing | Walk-forward + embargo 24 h | LightGBM | MASE medio 0.457 | ~1 min |
| 5 | [Modelos globales](notebooks/05_semana_5_modelos_globales_cross_learning.ipynb) | Electricity | 296/74 series, 120 días | Cold-start y LightGBM global | Sin contexto histórico no se recuperó escala de clientes nuevos | ~1 min |
| 6 | [LSTM](notebooks/06_semana_6_deep_learning_lstm.ipynb) | OPSD Germany | Ventanas móviles 7 días | PyTorch LSTM | LightGBM superó a LSTM en este protocolo (one-step actualizado) | ~2 min |
| 7 | [Transformers](notebooks/07_semana_7_transformers_transfer_sensores.ipynb) | PeMS-SF | Split 770/193 sensores | N-BEATS, LSTM, TFT-like | TFT-like MAE 0.013122 en cohorte CPU 48/24 | ~10 min |
| 8 | [Probabilístico y MLOps](notebooks/08_semana_8_forecasting_probabilistico_mlops.ipynb) | M3 Monthly | Holdout 18 meses | Quantile LightGBM | CRPS aprox. 356.27; cobertura empírica P10–P90 0.789 | ~1 min |

\*Tiempos observados en el entorno de construcción (CPU, sin GPU). Varían con CPU, RAM, BLAS y caché de disco. No son garantías de rendimiento.

### Resultados clave y lecciones

Cada notebook entrega no solo métricas, sino **lecciones metodológicas** explícitas:

1. **Semana 1:** Un baseline estacional ingenuo con ventana 168 (7 días × 24 h) puede ser sorprendentemente competitivo. La estacionalidad domina la señal; el clima añade poder predictivo pero con rendimientos decrecientes.
2. **Semana 2:** La selección por AIC en validación no garantiza la mejor métrica en test. ETS superó al ARIMA seleccionado, ilustrando el riesgo de sobre-optimizar criterios de información.
3. **Semana 3:** Las covariables exógenas reales (meteorología observada) reducen el error ~18%, pero constituyen un *escenario oracle*: en producción no se conoce el clima futuro. El notebook discute el gap entre validación académica y despliegue real.
4. **Semana 4:** El feature engineering sin leakage es el arte central del ML forecasting. Lags y rolling windows deben desplazarse respecto al horizonte; `casual + registered = cnt` implica que esas columnas no pueden usarse como features.
5. **Semana 5:** El cold-start es un resultado negativo central: un modelo global entrenado en 296 clientes no puede predecir la escala de 74 clientes nuevos sin contexto histórico. Esto enseña los límites del cross-learning sin features estáticas.
6. **Semana 6:** LightGBM superó a una LSTM cuidadosamente diseñada bajo el protocolo de evaluación usado. No es una declaración universal: es un recordatorio de que deep learning no es automáticamente superior y que la evaluación justa requiere idénticas condiciones.
7. **Semana 7:** La transferencia entre sensores funciona. Un TFT-like entrenado en 770 sensores predice 193 nuevos con MAE 0.013122. Pero la atención espacial no sustituye features geográficas reales.
8. **Semana 8:** Un LightGBM con cinco cuantiles (P10, P25, P50, P75, P90) produce intervalos de predicción con cobertura cercana a la nominal. El CRPS es una aproximación. La Model Card cierra el curso formalizando qué se debe registrar para gobernar un modelo en producción.

---

## Inventario de datos

Ocho datasets, nueve archivos CSV. Todos están en `data/` con su ficha `README.md` y receipt JSON. **Excepción:** las filas 5 y 7 (>100 MiB) no se versionan en GitHub; se regeneran con `make download && make clean` (el receipt JSON sí queda versionado siempre).

| Semana | Producto | Dimensión | Tamaño aprox. | Target | Frecuencia | Covariables destacadas |
|---:|---|---|---:|---|---:|---|
| 1 | `data/01_traffic_metro/traffic.csv` | 48,204 × 9 | 3.04 MiB | `y` (volumen) | Horaria | Festivos, temperatura, lluvia, nieve, nubes, clima |
| 2 | `data/02_energy/energy.csv` | 19,735 × 29 | 5.45 MiB | `y` (electrodomésticos) | 10 minutos | 27 sensores interiores/exteriores, clima, variables de control |
| 3 | `data/03_beijing/beijing_pm25.csv` | 43,800 × 14 | 2.95 MiB | `pm2.5` | Horaria | Punto de rocío, temperatura, presión, viento, lluvia/nieve |
| 4 | `data/04_bike/bike_hour.csv` | 17,379 × 17 | 1.14 MiB | `cnt` (alquileres) | Horaria | Calendario, clima, temperatura normalizada |
| | `data/04_bike/bike_day.csv` | 731 × 16 | | `cnt` | Diaria | Agregado diario de las mismas variables |
| 5 | `data/05_electricity/electricity_long.csv` | 9,732,480 × 3 | 403.20 MiB | `y` (consumo) | Horaria | Identidad de serie (370 clientes, 26,304 horas c/u) |
| 6 | `data/06_opsd/germany_energy.csv` | 50,401 × 43 | 14.19 MiB | `DE_load_actual_entsoe_transparency` | Horaria | Forecasts de carga, precios, generación solar/eólica, perfiles |
| 7 | `data/07_traffic_pems/traffic_pems.csv` | 63,360 × 967 | 408.22 MiB | Vector de ocupación | 10 min intradía | `weekday_label`, `day_id`, `slot_10min`, `split` (train/test) |
| 8 | `data/08_m3/m3_monthly.csv` | 167,562 × 3 | 3.99 MiB | `y` | Mensual | Identidad de serie; 1,428 series del benchmark M3 |

### Notas sobre los datos

- **Cada carpeta** `data/<semana>/` contiene tres archivos: el CSV limpio, un `README.md` con esquema, literatura, protocolo y *gotchas*, y un `.receipt.json` con la trazabilidad completa.
- **Electricity** está en formato long (`ds`, `unique_id`, `y`) tras pivotar la matriz ancha original de 370 columnas. Se filtró al rango 2012–2014, se parsearon comas decimales, se agregaron valores de 15 minutos a frecuencia horaria y se reindexó a exactamente 26,304 timestamps.
- **PeMS-SF** se mantiene en formato ancho (963 columnas de sensores) para evitar generar ~61 millones de filas en formato long. Cada día tiene 144 slots de 10 minutos. No existen fechas calendario reales; se usan identificadores posicionales.
- **OPSD** conserva todas las columnas con prefijo `DE_` del archivo europeo unificado, más los timestamps UTC y CET/CEST.
- **Beijing** retiene 2,043 targets de PM2.5 ausentes (gaps interiores), que se tratan dentro de cada fold.
- **Metro** contiene 17 filas exactamente duplicadas, preservadas intencionalmente para enseñar políticas de manejo de duplicados.

---

## Arquitectura y flujo de datos

El repositorio sigue un diseño en **cuatro capas** que separa la procedencia de los datos, su transformación, el análisis y el gobierno:

```text
                        CAPA RAW (temporal, excluida del release)
                        ═══════════════════════════════════════
URLs públicas / Zenodo
        │
        ▼
scripts/download_all.py ── streaming con límite 500 MiB ──► raw/*.zip, raw/*.csv
        │                        + SHA-256 en tránsito
        │
        │                   CAPA CURATED (incluida, versionada)
        │                   ═══════════════════════════════════
        ▼
scripts/clean_data.py ────► data/01_traffic_metro/traffic.csv
                       ────► data/02_energy/energy.csv
                       ────► data/03_beijing/beijing_pm25.csv
                       ────► data/04_bike/{bike_hour,bike_day}.csv
                       ────► data/05_electricity/electricity_long.csv
                       ────► data/06_opsd/germany_energy.csv
                       ────► data/07_traffic_pems/traffic_pems.csv
                       ────► data/08_m3/m3_monthly.csv
                                │
                                ├─ README.md (esquema, protocolo, gotchas)
                                └─ *.receipt.json (trazabilidad)
        │
        │                   CAPA ANALYSIS (notebooks ejecutados)
        │                   ═══════════════════════════════════
        ▼
notebooks/01_*.ipynb ... notebooks/08_*.ipynb
        │
        │                   CAPA GOVERNANCE (contratos e integridad)
        │                   ═══════════════════════════════════
        ▼
registry.yaml  +  MANIFEST.sha256  +  tests/  +  scripts/validate_repository.py
```

### Decisiones de escala

| Decisión | Motivación |
|---|---|
| Electricity en formato long | Necesario para modelos globales multi-serie; 9.7M filas pero solo 3 columnas |
| PeMS-SF en formato ancho | Evitar ~61M filas long; 63K filas × 967 columnas es manejable en CPU |
| OPSD: todas las columnas DE_ | Máxima flexibilidad para selección de features sin perder información |
| Límite 500 MiB por fuente | Compatible con entornos de estudiante; el helper `_common.py` lo fuerza en streaming |
| Sin Kaggle ni credenciales | Acceso público sin barreras; verificado por test automático |

---

## Sistema de reproducibilidad

La reproducibilidad se garantiza en cinco niveles complementarios:

### 1. Integridad a nivel de bytes

**`MANIFEST.sha256`** contiene el hash SHA-256 de cada archivo del release (excepto `.git/` y cachés). Verifique en cualquier momento:

```bash
sha256sum -c MANIFEST.sha256
```

Se regenera con `make manifest` (ejecuta `scripts/build_manifest.py`).

### 2. Trazabilidad de datos

Cada CSV tiene un **receipt JSON** (`*.receipt.json`) que registra de forma inmutable:

- **Origen:** URL, bytes descargados y SHA-256 de la fuente original.
- **Producto:** path, bytes y SHA-256 del CSV generado.
- **Transformación:** timestamp UTC, filas, columnas, nulos y pasos de limpieza aplicados.

Esto permite auditar exactamente qué se descargó, cómo se transformó y con qué resultado.

### 3. Catálogo machine-readable

**`registry.yaml`** es la fuente canónica de metadatos. Declara para cada dataset: id, semana, título, archivos, dimensiones, frecuencia, target y lista de covariables. Los scripts de validación y los tests lo usan como contrato.

### 4. Entorno acotado

`requirements.txt` usa rangos compatibles (ej. `pandas>=2.1,<3`, `lightgbm>=4,<5`) en lugar de versiones exactas, equilibrando reproducibilidad con flexibilidad. Para una cohorte docente que requiera byte-reproducibility, genere un lockfile (`pip freeze > requirements.lock.txt`).

### 5. Semilla y splits deterministas

Todos los notebooks usan **seed 42** y splits explícitos (temporales, no aleatorios). Los resultados numéricos pueden variar ligeramente entre plataformas por diferencias en BLAS, pero la estructura de los resultados es estable.

---

## Cómo usar el repositorio

### Solo estudiar (sin regenerar datos)

Los CSV y outputs de notebook están incluidos. Clone, instale dependencias y abra los notebooks:

```bash
git clone <repo>
cd course-timeseries-benchmarks-pro
python -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

Las rutas dentro de los notebooks son portables: buscan `data/...` desde la raíz y `../data/...` desde `notebooks/`.

### Reproducir los datos desde fuentes

Si quiere verificar que los CSV se generan correctamente desde las fuentes originales:

```bash
make download      # descarga las 8 fuentes a raw/ (~495 MiB)
make clean         # regenera los 9 CSV limpios
make validate      # valida hashes, shapes, receipts y tests
make clean-raw     # elimina raw/ para liberar espacio
```

Cada paso es independiente. `make download` obtiene las fuentes con verificación SHA-256 en streaming. `make clean` ejecuta las 8 funciones de limpieza que producen los CSV.

### Ejecutar notebooks de forma no interactiva

```bash
# Un notebook específico
python scripts/run_notebooks.py --notebook 03

# Todos en orden (20–30 minutos en total)
python scripts/run_notebooks.py --all

# Con timeout personalizado por celda (segundos)
python scripts/run_notebooks.py --all --timeout 3600
```

La ejecución no interactiva usa `nbclient` y `nbformat`. Los outputs se sobrescriben dentro del `.ipynb`. El notebook 7 domina el tiempo total (~10 minutos).

### Qué producen los notebooks

Los notebooks conservan gráficos, tablas y resultados **dentro del `.ipynb`**. No escriben modelos serializados, archivos de predicciones ni artefactos externos. Esto mantiene el repositorio limpio, facilita la auditoría y evita archivos ocultos.

Para producción, adapte las celdas finales de cada notebook para persistir artefactos en su model registry (MLflow, DVC, W&B, etc.).

---

## Scripts y tooling

Todos los scripts están en `scripts/` y usan `Path(__file__).resolve().parents[1]` para resolver la raíz del repositorio, lo que los hace ejecutables desde cualquier directorio:

| Script | Propósito | Invocación |
|---|---|---|
| `_common.py` | Utilidades compartidas: descarga streaming con límite 500 MiB, `sha256()`, `write_receipt()` | Importado por otros scripts |
| `download_all.py` | Descarga las 8 fuentes originales a `raw/` | `make download` |
| `clean_data.py` | Transforma fuentes en 9 CSV con receipts | `make clean` |
| `clean_raw.py` | Elimina `raw/` reportando espacio liberado | `make clean-raw` |
| `run_notebooks.py` | Ejecuta notebooks con `nbclient` | `make notebooks` |
| `validate_repository.py` | Verifica hashes, receipts, shapes y sintaxis Python | `make validate` (parte 1) |
| `build_manifest.py` | Regenera `MANIFEST.sha256` | `make manifest` |

### El helper `_common.py` en detalle

- **`download(url, dest, max_bytes=500MB)`**: streaming HTTP con `urlopen`, escritura a archivo temporal `.part`, cálculo de SHA-256 en tránsito, verificación de `Content-Length` y límite estricto. Si la descarga supera 500 MiB, lanza `RuntimeError`. Al finalizar, renombra atómicamente `.part` → destino.
- **`sha256(path)`**: hash SHA-256 de cualquier archivo, leyendo en chunks de 1 MiB.
- **`write_receipt(output, source, details)`**: escribe el receipt JSON con timestamp UTC, metadatos de fuente, hash del producto y detalles de la transformación.

---

## Pruebas y CI

### Suite de tests

Los tests validan contratos sin ejecutar los notebooks (la ejecución histórica ya está verificada por separado):

| Archivo | Qué valida |
|---|---|
| `tests/test_repository.py` | 8 datasets, 9 CSVs existen con tamaño > 0; receipts coherentes; límite 500 MiB; contratos de Electricity (9,732,480 filas, 0 duplicados) y PeMS (63,360 filas, 963 series); ausencia de referencias a Kaggle o credenciales |
| `tests/test_notebooks.py` | 8 notebooks con 80–120 celdas cada uno; todas las celdas de código ejecutadas sin error; cada notebook referencia su CSV correcto; presencia de "Methodology Card" y "seed" en markdown; secciones requeridas (Análisis previo, Estrategia de validación, Modelado, etc.); contratos de semana 7 (770/193 sensores, N-BEATS, TFT-like) y semana 8 (H=18, QUANTILES, Model Card) |
| `tests/test_documentation.py` | 11 documentos requeridos existen con >200 bytes; README contiene todas las secciones obligatorias y requisitos de sistema; `NOTEBOOK_GUIDE.md` referencia las 8 semanas con nombres correctos; todos los enlaces relativos en markdown resuelven; existen `run_notebooks.py`, `clean_raw.py`, `build_manifest.py`, `ci.yml` y `.python-version` |

### CI (GitHub Actions)

El workflow `.github/workflows/ci.yml` es ligero por diseño: se ejecuta en cada push y pull request, instala solo `PyYAML`, `pytest` y `nbformat`, y corre exclusivamente los tests de documentación y notebooks (que no requieren pandas, scikit-learn ni torch). Esto mantiene el CI rápido (< 30 segundos) y sin dependencias pesadas. La validación completa de datos se ejecuta localmente con `make validate`.

```bash
# Equivalente local del CI
python -m pytest -q tests/test_documentation.py tests/test_notebooks.py
```

---

## Estructura completa

```text
course-timeseries-benchmarks-pro/
│
├── README.md                          # Este documento: puerta de entrada y referencia completa
├── requirements.txt                   # Dependencias acotadas por rangos compatibles
├── registry.yaml                      # Catálogo machine-readable de datasets
├── MANIFEST.sha256                    # Hashes SHA-256 de todos los archivos del release
├── Makefile                           # Accesos directos: download, clean, validate, etc.
├── .python-version                    # Python 3.11 (para pyenv y similares)
├── .gitignore                         # raw/, .part, cachés, .venv
├── CHANGELOG.md                       # Historial de versiones (1.0.0 → 1.1.0)
├── CONTRIBUTING.md                    # Guía para contribuidores
├── LICENSE                            # MIT (código y documentación)
│
├── data/                              # Capa curated: CSV + ficha + receipt
│   ├── 01_traffic_metro/
│   │   ├── traffic.csv
│   │   ├── traffic.csv.receipt.json
│   │   └── README.md
│   ├── 02_energy/
│   ├── 03_beijing/
│   ├── 04_bike/                       # Dos CSVs: bike_hour.csv, bike_day.csv
│   ├── 05_electricity/
│   ├── 06_opsd/
│   ├── 07_traffic_pems/
│   └── 08_m3/
│
├── notebooks/                         # Capa analysis: 8 notebooks ejecutados
│   ├── README.md                      # Guía rápida de notebooks
│   ├── 01_semana_1_eda_baselines_estacionalidad.ipynb
│   ├── 02_semana_2_arima_estacionariedad_diagnostico.ipynb
│   ├── 03_semana_3_sarimax_variables_exogenas.ipynb
│   ├── 04_semana_4_feature_engineering_ml.ipynb
│   ├── 05_semana_5_modelos_globales_cross_learning.ipynb
│   ├── 06_semana_6_deep_learning_lstm.ipynb
│   ├── 07_semana_7_transformers_transfer_sensores.ipynb
│   └── 08_semana_8_forecasting_probabilistico_mlops.ipynb
│
├── docs/                              # Documentación complementaria
│   ├── INSTALLATION.md                # Guía detallada de instalación
│   ├── NOTEBOOK_GUIDE.md              # Guía de notebooks y extensiones opcionales
│   ├── ARCHITECTURE.md                # Flujo de datos y decisiones de diseño
│   ├── COURSE_GUIDE.md                # Guía docente: secuencia, evaluación, features, MLOps
│   ├── COURSE_SUMMARY.md              # Resumen ejecutivo del curso
│   ├── REPRODUCIBILITY.md             # Política de reproducibilidad y resultados
│   ├── TROUBLESHOOTING.md             # Problemas comunes y soluciones
│   ├── DATA_GOVERNANCE.md             # Gobierno de datos y checklist de release
│   └── SOURCE_NOTES.md                # Notas sobre fuentes y requisitos de atribución
│
├── scripts/                           # Tooling de descarga, limpieza y validación
│   ├── _common.py                     # Helpers: download(), sha256(), write_receipt()
│   ├── download_all.py                # Descarga las 8 fuentes
│   ├── clean_data.py                  # Transforma fuentes en 9 CSV con receipts
│   ├── clean_raw.py                   # Elimina raw/
│   ├── run_notebooks.py               # Ejecución no interactiva de notebooks
│   ├── validate_repository.py         # Validación de integridad
│   └── build_manifest.py              # Regenera MANIFEST.sha256
│
├── tests/                             # Suite de tests (contratos, no ejecución)
│   ├── test_repository.py             # Contratos de datos
│   ├── test_notebooks.py              # Contratos de notebooks
│   └── test_documentation.py          # Contratos de documentación
│
└── .github/workflows/ci.yml           # CI ligera: docs + notebooks contracts
```

---

## Documentación complementaria

Cada archivo en `docs/` tiene un propósito específico. Use esta guía para encontrar lo que necesita:

| Documento | Para quién | Contenido |
|---|---|---|
| [`INSTALLATION.md`](docs/INSTALLATION.md) | Todos | Instalación detallada, variantes Windows, PyTorch CPU/GPU, verificación |
| [`NOTEBOOK_GUIDE.md`](docs/NOTEBOOK_GUIDE.md) | Estudiantes | Guía de cada notebook, resultados reproducidos, extensiones opcionales (DeepAR, GPU) |
| [`ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Contribuidores, docentes | Flujo de datos, capas, componentes, decisiones de escala |
| [`COURSE_GUIDE.md`](docs/COURSE_GUIDE.md) | Docentes | Secuencia de 8 semanas, evaluación obligatoria, contrato de features, MLOps |
| [`COURSE_SUMMARY.md`](docs/COURSE_SUMMARY.md) | Todos | Resumen ejecutivo de una página |
| [`REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) | Investigadores | Niveles de reproducibilidad, cómo validar y reejecutar, política de resultados |
| [`TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) | Todos | Problemas comunes: instalación, memoria, rutas, diferencias numéricas |
| [`DATA_GOVERNANCE.md`](docs/DATA_GOVERNANCE.md) | Contribuidores | Procedencia, restricciones, política de cambios, checklist de release |
| [`SOURCE_NOTES.md`](docs/SOURCE_NOTES.md) | Todos | Notas por fuente: licencias, atribución, limitaciones conocidas |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribuidores | Flujo de desarrollo, reglas de integridad, PR checklist |

---

## Limitaciones que debe conocer

Estas limitaciones son conocidas y están documentadas, no son defectos. Conocerlas evita interpretaciones incorrectas de los resultados:

### Datos

- **Beijing** conserva 2,043 targets de PM2.5 ausentes (gaps interiores en la serie). Se tratan dentro de cada fold de validación, no con imputación global.
- **PeMS-SF** no incluye fechas calendario reales. Se usan `day_id`, `slot_10min` y `weekday_label` como identificadores posicionales, sin fabricar timestamps artificiales.
- **Metro** contiene 17 filas con timestamp exactamente repetido. Se preservan para enseñar políticas explícitas de manejo de duplicados.
- **Electricity** (notebook 5) usa los últimos 120 días de 370 series para controlar RAM/CPU. El dataset completo (26,304 timestamps) está disponible en el CSV; la restricción es solo del notebook.
- Las fuentes se descargaron entre 2024 y 2025. Si una URL cambia, `download_all.py` fallará; los CSV incluidos no se ven afectados.

### Modelos

- **TFT-like** (notebook 7) es un Transformer compacto *inspirado* en TFT (Temporal Fusion Transformer), no una reproducción exacta de la arquitectura del paper original. Omite ciertos componentes como variable selection networks y processing de static covariates.
- **CRPS** (notebook 8) es una aproximación numérica calculada con cinco cuantiles (P10, P25, P50, P75, P90). No es el CRPS analítico ni una aproximación de alta resolución con más cuantiles.
- **DeepAR** queda especificado conceptualmente en el notebook 8 pero no ejecutado. La guía de notebooks indica cómo añadirlo como extensión opcional.
- **Notebook 7** ejecuta los modelos neuronales en una cohorte reducida (48 sensores de entrenamiento, 24 de test) para viabilidad en CPU. El split completo (770/193) está definido y disponible.

### Resultados

- Los resultados pertenecen a los splits, horizontes, ventanas e hiperparámetros específicos de cada notebook. **No son rankings universales** de algoritmos. No deben citarse fuera de contexto.
- Las diferencias numéricas entre re-ejecuciones en distintas plataformas son esperables (BLAS, versión de compilador, orden de operaciones en punto flotante). Las conclusiones cualitativas se mantienen.
- En el notebook 3, el escenario SARIMAX es *oracle*: usa clima observado en el futuro. La reducción del 18.4% en MAE no es alcanzable en producción sin un forecast meteorológico externo.

---

## Integridad, licencia y citas

### Verificación de integridad

```bash
# Verificar que ningún archivo fue alterado
sha256sum -c MANIFEST.sha256

# Validación completa del repositorio
python scripts/validate_repository.py
python -m pytest -q
```

### Licencia

El código, la documentación original y la estructura del repositorio se distribuyen bajo la **licencia MIT** (ver [`LICENSE`](LICENSE)). Los datasets incluidos mantienen sus licencias originales y requisitos de atribución. Consulte la ficha `README.md` de cada carpeta en `data/` y [`SOURCE_NOTES.md`](docs/SOURCE_NOTES.md) para los términos específicos de cada dataset.

### Atribución de datasets

| Dataset | Fuente | Licencia/Atribución |
|---|---|---|
| Metro Traffic | UCI ML Repository | CC BY 4.0 (UCI) |
| Appliances Energy | UCI ML Repository | CC BY 4.0 (UCI) |
| Beijing PM2.5 | UCI ML Repository | CC BY 4.0 (UCI) |
| Bike Sharing | UCI ML Repository | CC BY 4.0 (UCI) |
| Electricity | UCI ML Repository | CC BY 4.0 (UCI) |
| OPSD Germany | Open Power System Data | OPSD terms (attribution) |
| PeMS-SF | UCI ML Repository | CC BY 4.0 (UCI) |
| M3 Monthly | Zenodo / M Competition | M3 competition terms |

### Advertencia

Las asociaciones observacionales encontradas en estos datasets no constituyen evidencia causal. Los modelos predictivos aquí construidos tienen fines educativos y de benchmark. No utilice estos resultados para tomar decisiones operativas sin validación independiente en el dominio de aplicación.

---

## Créditos

Este repositorio fue diseñado como un curso profesional autocontenido de Time Series Forecasting. La arquitectura de cuatro capas, el sistema de receipts, el registro machine-readable, los contratos de tests y la documentación exhaustiva reflejan prácticas de ingeniería de datos y MLOps aplicadas a la educación en forecasting.

*Última actualización: enero 2025. Versión 1.1.0.*
