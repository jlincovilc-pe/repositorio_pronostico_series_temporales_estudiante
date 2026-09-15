# Pronóstico de series temporales

Repositorio de trabajo del estudiante para el curso **Forecasting de Series Temporales: de modelos paramétricos a deep learning en producción**.

El material cubre ocho semanas, ocho datasets reales y una progresión de baselines ingenuos hasta forecasting probabilístico y MLOps. El hallazgo transversal que recorre notebooks, monografía y sílabo es el mismo: **la complejidad no garantiza mejora**. En varios experimentos el modelo sofisticado iguala o apenas supera a un baseline bien elegido bajo validación temporal correcta.

> **Empiece aquí.** Si solo quiere estudiar: instale el entorno en `forecasting-for-data-science/`, abra los notebooks en orden y use este README como mapa del resto de artefactos (sílabo, monografía, presentaciones).

---

## Tabla de contenidos

1. [Qué es este repositorio](#qué-es-este-repositorio)
2. [Mapa de carpetas](#mapa-de-carpetas)
3. [Ruta de las ocho semanas](#ruta-de-las-ocho-semanas)
4. [Inicio rápido](#inicio-rápido)
5. [Curso práctico (`forecasting-for-data-science`)](#curso-práctico-forecasting-for-data-science)
6. [Monografía y defensa (`Forecasting_monograph`)](#monografía-y-defensa-forecasting_monograph)
7. [Sílabo y evaluación (`silabo`)](#sílabo-y-evaluación-silabo)
8. [Presentaciones HTML (`html_presentation`)](#presentaciones-html-html_presentation)
9. [Mapas de capítulos (`json_maps`)](#mapas-de-capítulos-json_maps)
10. [Marco de calidad (`quality_production`)](#marco-de-calidad-quality_production)
11. [Inventario de datos](#inventario-de-datos)
12. [Cómo usar el repositorio según el objetivo](#cómo-usar-el-repositorio-según-el-objetivo)
13. [Reproducibilidad](#reproducibilidad)
14. [Limitaciones que debe conocer](#limitaciones-que-debe-conocer)
15. [Licencia, atribución y citas](#licencia-atribución-y-citas)

---

## Qué es este repositorio

Este directorio no es un único proyecto de software. Es el **espacio de trabajo del curso**: código ejecutable, datos curados, documentación pedagógica, sílabo, monografía aplicada y artefactos de presentación.

| Pieza | Rol |
|---|---|
| Curso reproducible | Ocho notebooks ejecutados, nueve CSV limpios, scripts, tests y hashes SHA-256 |
| Trabajo integrador | Monografía de ~10 capítulos + presentación de defensa (Typst → PDF) |
| Contrato docente | Sílabo de 8 semanas y pauta de evaluación |
| Material de clase | Presentación HTML interactiva de la semana 1 |
| Trazabilidad editorial | Mapas JSON capítulo a capítulo de la monografía |
| Criterio de calidad | Marco de coherencia ontológica, epistémica y pragmática (CCT) |

El núcleo técnico vive en [`forecasting-for-data-science/`](forecasting-for-data-science/). El resto de carpetas documenta, evalúa o comunica ese núcleo. La guía detallada del curso (instalación, contratos de datos, CI, troubleshooting) está en [`forecasting-for-data-science/README.md`](forecasting-for-data-science/README.md).

**Público.** Data scientists, ML engineers, analistas de demanda y operaciones. Se asume Python intermedio (pandas, NumPy) y estadística básica. No se exige cálculo multivariable ni demostraciones.

**Duración de referencia.** 8 semanas / 8 módulos, 40–48 horas lectivas más trabajo autónomo (según el sílabo).

---

## Mapa de carpetas

```text
repositorio_pronostico_series_temporales_estudiante/
│
├── README.md                          # Este documento (puerta de entrada)
│
├── forecasting-for-data-science/      # Curso ejecutable (datos + notebooks + tests)
│   ├── README.md                      # Referencia completa del curso
│   ├── requirements.txt
│   ├── registry.yaml                  # Catálogo machine-readable de datasets
│   ├── MANIFEST.sha256                # Integridad criptográfica del release
│   ├── Makefile
│   ├── data/                          # 8 datasets, 9 CSV + receipts + fichas
│   ├── notebooks/                     # Semanas 1–8, outputs ya ejecutados
│   ├── scripts/                       # Descarga, limpieza, validación, ejecución
│   ├── tests/
│   ├── docs/                          # Instalación, arquitectura, gobierno, etc.
│   └── instruccion_libro.md           # Brief de la monografía aplicada
│
├── Forecasting_monograph/             # Monografía + presentación (solo PDF; fuentes Typst no publicadas)
│   ├── monografia_timeseries_benchmarks.pdf
│   ├── presentacion.pdf
│   └── README.md
│
├── silabo/                            # Contrato del curso y pauta de evaluación (solo PDF)
│   ├── silabo.pdf
│   └── criterios_calificacion.pdf
│
├── html_presentation/                # Material interactivo de clase
│   └── monografia_interactiva.html                  # Semana 1: EDA, baselines y estacionalidad
│
├── json_maps/                         # Grafos de contenido por capítulo (00–09)
│   └── json_cap00.json … json_cap09.json
│
└── quality_production/                # Marco CCT de coherencia científica
    ├── high.md
    └── high.json
```

---

## Ruta de las ocho semanas

Cada semana introduce un dataset, un protocolo de validación y un paradigma de modelado. Los notebooks están en `forecasting-for-data-science/notebooks/`. Los capítulos 2–9 de la monografía siguen el mismo orden.

| Semana | Tema | Técnicas | Dataset | Pregunta de negocio | Anti-patrón |
|:---:|---|---|---|---|---|
| 1 | Anatomía temporal y baselines | STL, seasonal naive, ETS, regresión | Metro Interstate Traffic | ¿Cuándo reforzar operación? | Random split en series temporales |
| 2 | Box–Jenkins y residuos | ADF, KPSS, ACF/PACF, ARIMA | Appliances Energy | ¿ARIMA supera a modelos simples? | Elegir modelo solo por AIC |
| 3 | SARIMAX y exógenas | SARIMA vs SARIMAX, rolling-origin | Beijing PM2.5 | ¿Las exógenas estarán en producción? | Usar clima observado como si fuera futuro |
| 4 | Feature engineering sin leakage | Lags, rolling, walk-forward, LightGBM | Bike Sharing | ¿Cómo evitar leakage? | Ventanas centradas; `casual`/`registered` como features |
| 5 | Modelos globales y cold-start | Paneles, cross-learning | Electricity (370 clientes) | ¿Cómo predecir clientes nuevos? | Modelo global sin historia del cliente |
| 6 | Deep learning secuencial | Ventanas, tensores 3D, LSTM/GRU | OPSD Germany | ¿LSTM vale la pena? | LSTM por defecto |
| 7 | Transferencia y arquitecturas modernas | N-BEATS, TFT-like, atención | PeMS-SF (963 sensores) | ¿Cómo transferir a sensores nuevos? | Transformer sin baseline |
| 8 | Probabilístico y MLOps | Cuantiles, pinball, cobertura, drift, Model Card | M3 Monthly | ¿Qué intervalo usar para decidir con riesgo? | Intervalos gaussianos sin calibrar |

**Resultados reproducidos (protocolos de estos notebooks, no rankings universales):**

1. Seasonal Naive 168 fue el mejor baseline de Metro.
2. Validation seleccionó ARIMA(1,0,2); ETS ganó por MASE en test.
3. SARIMAX redujo MAE medio ~18.4 % frente a SARIMA en escenario *oracle*.
4. LightGBM logró MASE medio 0.457 en Bike Sharing.
5. Cold-start sin contexto no recuperó la escala de clientes nuevos (resultado negativo central).
6. LightGBM superó a LSTM, ARIMA y seasonal naive en OPSD bajo el protocolo one-step usado.
7. TFT-like obtuvo MAE 0.013122 en la cohorte CPU de PeMS (48/24 sensores).
8. LightGBM cuantílico: cobertura empírica P10–P90 0.789; CRPS aproximado 356.27.

Detalle de lecciones, tiempos CPU y Methodology Cards: [`forecasting-for-data-science/notebooks/README.md`](forecasting-for-data-science/notebooks/README.md) y [`forecasting-for-data-science/docs/COURSE_SUMMARY.md`](forecasting-for-data-science/docs/COURSE_SUMMARY.md).

---

## Inicio rápido

### Requisitos

| Recurso | Mínimo | Recomendado | Notas |
|---|---|---|---|
| Python | 3.10 | 3.11 | Rango 3.10–3.13 según `requirements.txt` |
| RAM | 8 GiB | 16 GiB | 8 GiB bastan para semanas 1–4 y 8; 5–7 piden más |
| Disco | ~1 GiB | 2 GiB libres | Regenerar `raw/` añade ~495 MiB temporales |
| CPU | 2 núcleos | 4 núcleos | GPU no es obligatoria; los outputs incluidos son de CPU |
| SO | Linux, macOS, Windows+WSL2 | Linux | En Windows PowerShell: `.venv\Scripts\Activate.ps1` |
| Typst | ≥ 0.15 | — | Solo si va a recompilar monografía o sílabo |

### Entorno del curso

Los CSV limpios **ya están incluidos**, salvo dos: `electricity_long.csv` (semana 5, ~404 MiB) y `traffic_pems.csv` (semana 7, ~409 MiB) superan el límite de tamaño de GitHub y se regeneran bajo demanda con `make download && make clean` (requiere internet, ~813 MiB). Para las semanas 1–4, 6 y 8 no hace falta descargar nada ni ejecutar scripts de preparación.

```bash
cd forecasting-for-data-science

python -m venv .venv
source .venv/bin/activate              # Windows PowerShell: .venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python scripts/validate_repository.py
python -m pytest -q

jupyter lab
```

Abra [`notebooks/01_semana_1_eda_baselines_estacionalidad.ipynb`](forecasting-for-data-science/notebooks/01_semana_1_eda_baselines_estacionalidad.ipynb) y continúe en orden numérico.

Verificación rápida:

```bash
python -c "import pandas, statsmodels, lightgbm, torch; print('entorno OK')"
```

Si solo estudiará las semanas 1–5 y 8, puede omitir PyTorch (`torch`). Los tests de ejecución histórica leen notebooks con outputs ya almacenados.

Instalación detallada, variantes Windows y builds CPU/GPU de PyTorch: [`forecasting-for-data-science/docs/INSTALLATION.md`](forecasting-for-data-science/docs/INSTALLATION.md).

---

## Curso práctico (`forecasting-for-data-science`)

Nombre técnico del paquete: `forecasting-for-data-science` (anteriormente `course-timeseries-benchmarks-pro`). Versión documentada: **1.1.0**.

Seis principios gobiernan el diseño:

1. **Reproducibilidad.** Hashes SHA-256, splits explícitos, seed 42, dependencias acotadas por rangos.
2. **Autocontenido.** CSV limpios en el repo; se puede clonar y estudiar sin internet.
3. **Transparencia.** Cada transformación queda en un receipt JSON (URL, bytes, SHA-256, filas, nulos, pasos).
4. **Realismo.** Duplicados, gaps, granularidades mixtas y covariables que no existirían en producción se conservan a propósito.
5. **Progresión pedagógica.** Univariado → multi-serie → multivariado; naive → estadístico → ML → DL; point forecast → probabilístico → MLOps.
6. **Gobierno explícito.** `registry.yaml` es el catálogo; los tests validan contratos; no hay Kaggle ni credenciales.

### Arquitectura en cuatro capas

```text
RAW (temporal, excluida)     URLs públicas → scripts/download_all.py → raw/
CURATED (incluida)           scripts/clean_data.py → data/<semana>/*.csv + README + receipt
ANALYSIS                     notebooks/01_*.ipynb … 08_*.ipynb
GOVERNANCE                   registry.yaml + MANIFEST.sha256 + tests/ + validate_repository.py
```

### Comandos útiles

Desde `forecasting-for-data-science/`:

```bash
make install       # pip install -r requirements.txt
make validate      # integridad + pytest
make test          # pytest
make notebooks     # reejecuta los 8 notebooks (20–30 min en CPU)
make download      # regenera raw/ desde fuentes (~495 MiB)
make clean         # regenera los 9 CSV y receipts
make clean-raw     # borra raw/
make manifest      # regenera MANIFEST.sha256
```

Un notebook concreto, sin Jupyter:

```bash
python scripts/run_notebooks.py --notebook 03
python scripts/run_notebooks.py --all --timeout 3600
```

### Documentación del curso

| Documento | Contenido |
|---|---|
| [`README.md`](forecasting-for-data-science/README.md) | Referencia completa |
| [`docs/INSTALLATION.md`](forecasting-for-data-science/docs/INSTALLATION.md) | Instalación y PyTorch |
| [`docs/NOTEBOOK_GUIDE.md`](forecasting-for-data-science/docs/NOTEBOOK_GUIDE.md) | Guía de cada notebook y extensiones |
| [`docs/ARCHITECTURE.md`](forecasting-for-data-science/docs/ARCHITECTURE.md) | Flujo de datos y decisiones de escala |
| [`docs/COURSE_GUIDE.md`](forecasting-for-data-science/docs/COURSE_GUIDE.md) | Secuencia docente, evaluación, features, MLOps |
| [`docs/COURSE_SUMMARY.md`](forecasting-for-data-science/docs/COURSE_SUMMARY.md) | Resumen de una página |
| [`docs/REPRODUCIBILITY.md`](forecasting-for-data-science/docs/REPRODUCIBILITY.md) | Política de resultados |
| [`docs/TROUBLESHOOTING.md`](forecasting-for-data-science/docs/TROUBLESHOOTING.md) | Problemas comunes |
| [`docs/DATA_GOVERNANCE.md`](forecasting-for-data-science/docs/DATA_GOVERNANCE.md) | Procedencia y checklist de release |
| [`docs/SOURCE_NOTES.md`](forecasting-for-data-science/docs/SOURCE_NOTES.md) | Licencias y atribución por fuente |
| [`instruccion_libro.md`](forecasting-for-data-science/instruccion_libro.md) | Especificación de la monografía |
| [`CONTRIBUTING.md`](forecasting-for-data-science/CONTRIBUTING.md) | Flujo de contribución |

Dependencias principales (`requirements.txt`): pandas, numpy, statsmodels, statsforecast, scikit-learn, LightGBM, matplotlib/seaborn, Jupyter, pytest, PyYAML, torch.

---

## Monografía y defensa (`Forecasting_monograph`)

Trabajo integrador sobre los ocho experimentos. No es un volcado de outputs: documenta contrato de datos, validación temporal, modelado, residuos y lecciones verificadas contra la ejecución real.

| Archivo | Qué es |
|---|---|
| [`monografia_timeseries_benchmarks.pdf`](Forecasting_monograph/monografia_timeseries_benchmarks.pdf) | PDF compilado (A4), 10 capítulos + apéndices |
| [`presentacion.pdf`](Forecasting_monograph/presentacion.pdf) | PDF de la presentación de defensa (~24 diapositivas, 16:9) |
| [`AUTOR_VOICE.md`](Forecasting_monograph/AUTOR_VOICE.md) | Puntos opcionales de voz autoral (no es entregable) |

Las fuentes Typst (`.typ`), los scripts que generan las figuras y las
bitácoras editoriales (`edit_mon.json`, `edit_presentation.json`) son
material de trabajo del autor y **no se publican** en este repositorio;
solo se comparten los PDF ya compilados.

**Capítulos**

| Cap. | Tema | Origen |
|---:|---|---|
| 1 | Marco teórico-metodológico | — |
| 2–9 | Un experimento por dominio | Notebooks 1–8 |
| 10 | Síntesis y conclusiones | — |
| A–E | Datasets, modelos, entorno, methodology cards, glosario | — |

Guía de carpeta: [`Forecasting_monograph/README.md`](Forecasting_monograph/README.md).

---

## Sílabo y evaluación (`silabo`)

Contrato pedagógico del curso: competencias, casos de negocio, anti-patrones, métricas y criterio de escalamiento de complejidad.

| Archivo | Qué es |
|---|---|
| [`silabo.pdf`](silabo/silabo.pdf) | Sílabo: *Forecasting de Series Temporales Aplicado a la Industria* |
| [`criterios_calificacion.pdf`](silabo/criterios_calificacion.pdf) | Pauta de evaluación de propuestas y manuscritos (marco CCT) |

Las fuentes Typst (`silabo.typ`, `criterios_calificacion.typ`) no se
publican; solo los PDF compilados.

El sílabo es **business y code-first**: no se aprueba por usar el modelo más complejo. Todo modelo avanzado debe superar a un baseline (Naive, Seasonal Naive, media móvil) bajo validación temporal correcta.

**Niveles de complejidad (criterio de escalamiento)**

| Nivel | Qué exige |
|---:|---|
| 0 | Baseline obligatorio |
| 1 | Modelo estadístico (ARIMA / SARIMA / SARIMAX) |
| 2 | ML tabular con features temporales (LightGBM, etc.) |
| 3 | Deep learning secuencial, solo si justifica el costo |
| 4 | Arquitecturas modernas (N-BEATS, TFT) si hay transferencia o multi-horizonte |
| 5 | Forecasting probabilístico y monitoreo para producción |

---

## Presentaciones HTML (`html_presentation`)

Material de clase interactivo, independiente de Typst.

| Ruta | Contenido |
|---|---|
| [`html_presentation/monografia_interactiva.html`](html_presentation/monografia_interactiva.html) | Semana 1 — *La estacionalidad es la señal*: EDA, STL, estacionariedad, split temporal, métricas, baselines, residuos y covariables |

Ábralo en el navegador (archivo local).

---

## Mapas de capítulos (`json_maps`)

Grafos de contenido que alinean monografía, notebooks y declaraciones de posicionamiento (CCT). Útiles para navegar el trabajo integrador o para herramientas que consuman el índice.

| Archivo | Cubre |
|---|---|
| `json_cap00.json` | Capítulo 1 de la monografía (fundamentos, ética, uso de IA) |
| `json_cap01.json` … `json_cap08.json` | Semanas 1–8 / capítulos técnicos 2–9 |
| `json_cap09.json` | Síntesis (capítulo 10) |

Cada nodo puede incluir `label`, `type`, contrato CCT (nivel ontológico, RRL epistémico, audiencia) y referencias a slides.

---

## Marco de calidad (`quality_production`)

[`quality_production/high.md`](quality_production/high.md) (y su espejo [`high.json`](quality_production/high.json)) formula la **Condición de Coherencia Tripartita (CCT)**: un artefacto científico es coherente solo si afirma lo que su nivel de análisis permite, con la solidez que su evidencia sostiene, para una audiencia con una necesidad real.

| Eje | Pregunta |
|---|---|
| Ontológico | ¿En qué nivel opera y qué puede afirmar ahí? |
| Epistémico | ¿Qué madurez tiene la evidencia? |
| Pragmático | ¿Qué problema de qué actor resuelve? |

La pauta de [`silabo/criterios_calificacion.pdf`](silabo/criterios_calificacion.pdf) opera este marco sobre propuestas y manuscritos. La monografía declara explícitamente nivel de análisis, límites de inferencia y deudas no ejecutadas (p. ej. DeepAR).

---

## Inventario de datos

Ocho datasets, nueve CSV, todos en `forecasting-for-data-science/data/`. Cada carpeta incluye el CSV, un `README.md` (esquema, protocolo, *gotchas*) y un `.receipt.json`.

| Semana | Producto | Dimensión (aprox.) | Target | Frecuencia |
|---:|---|---|---|---|
| 1 | `01_traffic_metro/traffic.csv` | 48,204 × 9 | volumen `y` | Horaria |
| 2 | `02_energy/energy.csv` | 19,735 × 29 | electrodomésticos `y` | 10 min |
| 3 | `03_beijing/beijing_pm25.csv` | 43,800 × 14 | `pm2.5` | Horaria |
| 4 | `04_bike/bike_hour.csv` | 17,379 × 17 | alquileres `cnt` | Horaria |
| 4 | `04_bike/bike_day.csv` | 731 × 16 | `cnt` | Diaria |
| 5 | `05_electricity/electricity_long.csv` | 9,732,480 × 3 | consumo `y` | Horaria (370 series) |
| 6 | `06_opsd/germany_energy.csv` | 50,401 × 43 | carga `DE_load_actual_entsoe_transparency` | Horaria |
| 7 | `07_traffic_pems/traffic_pems.csv` | 63,360 × 967 | ocupación por sensor | 10 min intradía |
| 8 | `08_m3/m3_monthly.csv` | 167,562 × 3 | `y` | Mensual (1,428 series) |

Notas de diseño: Electricity está en formato *long*; PeMS-SF se mantiene *ancho* para no generar ~61 M de filas; Beijing conserva 2,043 PM2.5 ausentes; Metro conserva 17 timestamps duplicados a propósito.

Catálogo machine-readable: [`forecasting-for-data-science/registry.yaml`](forecasting-for-data-science/registry.yaml).

---

## Cómo usar el repositorio según el objetivo

### Estudiar las ocho semanas

1. Instale el entorno (sección [Inicio rápido](#inicio-rápido)).
2. Lea el sílabo: pregunta de negocio y anti-patrón de la semana.
3. Abra el notebook correspondiente; no salte el orden.
4. Opcional: presentación HTML de la semana 1; PDF de defensa para el panorama.

### Reproducir o auditar datos

```bash
cd forecasting-for-data-science
make download && make clean && make validate && make clean-raw
sha256sum -c MANIFEST.sha256
```

### Escribir o recompilar la monografía

Las fuentes Typst (`.typ`) no forman parte de este repositorio público; solo
se publican los PDF compilados. Para consultar el contenido: lea
[`forecasting-for-data-science/instruccion_libro.md`](forecasting-for-data-science/instruccion_libro.md)
(especificación) y use `json_maps/` como índice de capítulos.

### Impartir o evaluar el curso

- Contrato: [`silabo/silabo.pdf`](silabo/silabo.pdf).
- Rúbrica: [`silabo/criterios_calificacion.pdf`](silabo/criterios_calificacion.pdf).
- Secuencia docente: [`forecasting-for-data-science/docs/COURSE_GUIDE.md`](forecasting-for-data-science/docs/COURSE_GUIDE.md).

---

## Reproducibilidad

Cinco niveles, implementados en el curso:

1. **Bytes.** `MANIFEST.sha256` cubre el release (excepto `.git/` y cachés).
2. **Datos.** Receipt JSON por CSV: origen, hash, filas, nulos, pasos de limpieza.
3. **Catálogo.** `registry.yaml` declara id, semana, shape, frecuencia, target y covariables.
4. **Entorno.** Rangos en `requirements.txt` (`pandas>=2.1,<3`, `lightgbm>=4,<5`, …). Para byte-reproducibility de cohorte: `pip freeze > requirements.lock.txt`.
5. **Splits.** Seed 42 y cortes temporales explícitos. Pueden variar décimas entre plataformas (BLAS); las conclusiones cualitativas se mantienen.

Los notebooks **no escriben** modelos serializados ni predicciones a disco: gráficos y tablas viven dentro del `.ipynb`.

---

## Limitaciones que debe conocer

No son defectos ocultos; están documentados para no sobreinterpretar resultados.

- **Beijing:** 2,043 targets ausentes; se tratan por fold, no con imputación global.
- **PeMS-SF:** no hay fechas calendario reales; identificadores posicionales (`day_id`, `slot_10min`).
- **Metro:** 17 timestamps duplicados, preservados para enseñar política de duplicados.
- **Electricity (notebook 5):** el notebook usa 120 días para RAM/CPU; el CSV completo está en el repo.
- **TFT-like (notebook 7):** Transformer compacto inspirado en TFT, no la arquitectura completa del paper. Cohorte CPU 48/24; el split 770/193 está definido.
- **CRPS (notebook 8):** aproximación con cinco cuantiles, no CRPS analítico.
- **DeepAR:** especificado, no ejecutado.
- **SARIMAX (notebook 3):** escenario *oracle* (clima observado en el futuro). La reducción de MAE no es alcanzable en producción sin un forecast meteorológico.
- Los números pertenecen a **estos** splits, horizontes e hiperparámetros. No cite rankings universales de algoritmos.

---

## Licencia, atribución y citas

El código, la documentación original y la estructura de este repositorio se distribuyen bajo **MIT**. Ver [`LICENSE`](LICENSE).

Los datasets conservan licencias y atribución de origen:

| Dataset | Fuente | Términos |
|---|---|---|
| Metro Traffic, Appliances Energy, Beijing PM2.5, Bike Sharing, Electricity, PeMS-SF | UCI ML Repository | CC BY 4.0 (UCI) |
| OPSD Germany | Open Power System Data | Términos OPSD (atribución) |
| M3 Monthly | Zenodo / M Competition | Términos de la competición M3 |

Detalle por fuente: fichas `data/<semana>/README.md` y [`docs/SOURCE_NOTES.md`](forecasting-for-data-science/docs/SOURCE_NOTES.md).

**Advertencia.** Las asociaciones observacionales de estos datasets no son evidencia causal. Los modelos tienen fines educativos y de benchmark. No los use para decisiones operativas sin validación independiente en el dominio de aplicación.

---

## Dónde ir después

| Si necesita… | Abra |
|---|---|
| Estudiar ya | `forecasting-for-data-science/notebooks/01_….ipynb` |
| Entender el curso entero | [`forecasting-for-data-science/README.md`](forecasting-for-data-science/README.md) |
| Ver el contrato docente | [`silabo/silabo.pdf`](silabo/silabo.pdf) |
| Leer o defender el trabajo integrador | [`Forecasting_monograph/monografia_timeseries_benchmarks.pdf`](Forecasting_monograph/monografia_timeseries_benchmarks.pdf) y [`presentacion.pdf`](Forecasting_monograph/presentacion.pdf) |
| Clase de la semana 1 en el navegador | [`html_presentation/monografia_interactiva.html`](html_presentation/monografia_interactiva.html) |
| Instalar o depurar el entorno | [`docs/INSTALLATION.md`](forecasting-for-data-science/docs/INSTALLATION.md) y [`docs/TROUBLESHOOTING.md`](forecasting-for-data-science/docs/TROUBLESHOOTING.md) |
