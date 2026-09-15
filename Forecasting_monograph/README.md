# Forecasting de Series Temporales

Monografía aplicada y presentación sobre ocho experimentos de forecasting (tráfico, energía, calidad del aire, movilidad, consumo eléctrico y M3), ejecutados sobre el repositorio de referencia `course-timeseries-benchmarks-pro` (v1.1.0).

La tesis: la complejidad no garantiza mejora; en cuatro de ocho experimentos el modelo sofisticado iguala o apenas supera a un baseline ingenuo.

Fuentes originales en [Typst](https://typst.app/) ≥ 0.15 (Inter, New Computer
Modern, DejaVu Sans Mono). Este repositorio público solo distribuye los PDF
compilados: las fuentes `.typ`, los scripts que generan las figuras
(`assets/_make_*.py`) y las bitácoras editoriales (`edit_mon.json`,
`edit_presentation.json`) son material de trabajo del autor y no se
publican.

## Documentos

| Archivo | Qué es |
|---|---|
| [`monografia_timeseries_benchmarks.pdf`](monografia_timeseries_benchmarks.pdf) | PDF compilado de la monografía (122 pp.), 10 capítulos + 6 apéndices (A–F). |
| [`presentacion.pdf`](presentacion.pdf) | PDF compilado de la presentación (25 pp.), 16:9, ~24 diapositivas. |

## Estructura de la monografía

| Cap. | Tema | Dataset / dominio |
|---|---|---|
| 1 | Marco teórico-metodológico (§1.2 fundamento estadístico; one-pager de decisión, Figura 2) | — |
| 2 | EDA, baselines y estacionalidad | Metro Interstate Traffic |
| 3 | ARIMA y estacionariedad | Appliances Energy |
| 4 | SARIMAX y exógenas | Beijing PM2.5 |
| 5 | Feature engineering y ML | Bike Sharing |
| 6 | Modelos globales y cross-learning | Electricity Load Diagrams |
| 7 | Deep learning (LSTM) | OPSD Germany |
| 8 | Arquitecturas modernas y transferencia | PeMS-SF |
| 9 | Forecasting probabilístico y MLOps (mapeo de stack, olvido ante concept drift) | M3 Monthly |
| 10 | Síntesis y conclusiones (§10.9 costo total de propiedad) | — |

Apéndices: (A) datasets, (B) modelos, (C) entorno computacional (con `Dockerfile`), (D) methodology cards, (E) glosario, (F) bibliografía.

## Adiciones ejecutivas

| # | Adición | Ubicación |
|---|---|---|
| 1 | Traducción a **costo total de propiedad** (TCO): costo de cómputo por corrida vs. costo del error evitado | §10.9 y Tabla 54 |
| 2 | **Mapeo MLOps**: del concepto de gobierno a la herramienta estándar (Evidently/NannyML · MLflow/W&B · Feast/Tecton · Airflow/Prefect) | §9.6 y Tabla 49 |
| 3 | Protocolo de **reentrenamiento ante concept drift** (ventana deslizante vs. decaimiento exponencial) | §9.6 |
| 4 | **Protocolos de ejecución** de las deudas prioritarias #1 (ablation OPSD) y #3 (few-shot) | §10.8 |
| 5 | Reproducibilidad byte-level: **`Dockerfile`** mínimo | Apéndice C |
| 6 | **One-pager ejecutivo**: mapa de decisión (árbol basado en la jerarquía de palancas) | Figura 2, cierre de §1.2 |

La presentación sigue el mismo recorrido: agenda, dos diapositivas por capítulo técnico (resultado + método/lección), síntesis y cierre.
