# Instrucción para la monografía aplicada de Time Series Forecasting

## 1. Propósito y alcance

La monografía aplicada es el trabajo integrador del curso **course-timeseries-benchmarks-pro**. Consiste en un texto académico-técnico de ~40–60 páginas que documenta, analiza y sintetiza la experiencia completa de forecasting sobre los ocho datasets del repositorio, siguiendo la progresión pedagógica de los notebooks.

**Objetivo:** demostrar que el autor no solo ejecutó modelos, sino que comprende el ciclo completo del forecasting aplicado: desde la auditoría de datos y el diagnóstico exploratorio hasta la validación temporal, la selección de modelos, el diagnóstico de residuos, la estimación de incertidumbre y el gobierno MLOps.

**No es:** un reporte automático de outputs, una colección de capturas de pantalla ni un listado de métricas sin interpretación.

---

## 2. Requisitos previos

Antes de comenzar la redacción, el autor debe:

- [ ] Haber ejecutado los ocho notebooks en orden (interactivo o `python scripts/run_notebooks.py --all`).
- [ ] Tener el entorno instalado y validado (`python scripts/validate_repository.py && python -m pytest -q`).
- [ ] Haber leído la documentación complementaria: [`ARCHITECTURE.md`](docs/ARCHITECTURE.md), [`COURSE_GUIDE.md`](docs/COURSE_GUIDE.md), [`REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) y [`DATA_GOVERNANCE.md`](docs/DATA_GOVERNANCE.md).
- [ ] Tener acceso a los receipts JSON de cada dataset para verificar trazabilidad.

---

## 3. Estructura general de la monografía

La monografía se organiza en **10 capítulos** más anexos. Cada capítulo se corresponde con una etapa del curso, y los capítulos 2–9 se derivan directamente de los ocho notebooks.

```text
1.  Introducción y fundamentos
2.  Anatomía temporal, estacionalidad y baselines           ← Notebook 1
3.  ARIMA, estacionariedad y diagnóstico de residuos         ← Notebook 2
4.  SARIMAX y el valor marginal de las covariables           ← Notebook 3
5.  Feature engineering sin leakage y machine learning       ← Notebook 4
6.  Modelos globales, cross-learning y cold-start            ← Notebook 5
7.  Deep learning secuencial con LSTM                         ← Notebook 6
8.  Arquitecturas modernas y transferencia entre series      ← Notebook 7
9.  Forecasting probabilístico, calibración y MLOps          ← Notebook 8
10. Síntesis, lecciones transversales y conclusiones
A.  Apéndices
```

---

## 4. Especificaciones detalladas por capítulo

### 4.1 Capítulo 1 — Introducción y fundamentos (4–6 páginas)

| Elemento | Requerido | Detalle |
|---|---|---|
| Contexto del forecasting | Sí | Definir forecasting, tipos (univariado, multi-serie, multivariado, probabilístico), aplicaciones en industria |
| Principios del repositorio | Sí | Explicar los 6 principios de diseño: reproducibilidad, autocontenido, transparencia, realismo, progresión, gobierno |
| Arquitectura de 4 capas | Sí | Describir el flujo raw → curated → analysis → governance con el diagrama de la documentación |
| Sistema de reproducibilidad | Sí | Explicar receipts, MANIFEST.sha256, registry.yaml, seed 42 y entorno acotado por rangos |
| Taxonomía de los 8 datasets | Sí | Tabla resumen: dataset, dimensión, frecuencia, target, covariables, desafío principal |
| Mapa de ruta de modelos | Sí | Diagrama o tabla que muestre la progresión: naive → ARIMA → SARIMAX → ML → global → LSTM → Transformers → probabilístico |
| Preguntas de investigación | Sí | 2–3 preguntas transversales que la monografía buscará responder (ej. «¿cuándo un modelo complejo aporta valor sobre un baseline estacional?») |

### 4.2 Capítulos 2–9 — Capítulos técnicos (5–7 páginas cada uno)

Cada capítulo técnico se deriva de un notebook. Debe seguir **obligatoriamente** la misma estructura de siete secciones que los notebooks:

#### Estructura interna obligatoria de cada capítulo técnico

```
X.1  Configuración y contrato de datos
X.2  Análisis previo (pre-modeling)
X.3  Estrategia de validación
X.4  Modelado
X.5  Análisis posterior (post-modeling)
X.6  Lecciones metodológicas
X.7  Ejercicios propuestos (opcional, resumidos)
```

#### Contenido requerido por sección

**X.1 — Configuración y contrato de datos**

| Elemento | Obligatorio |
|---|---|
| Fuente del dataset (URL, institución, licencia) | Sí |
| Dimensiones exactas: filas × columnas | Sí |
| Esquema: nombre, tipo y rol de cada columna (target, covariable, índice temporal) | Sí |
| Auditoría de calidad: nulos (cantidad y ubicación), duplicados, gaps temporales | Sí |
| Rango temporal y frecuencia real (no la declarada) | Sí |
| Decisión documentada sobre imputación, agregación o filtrado | Sí (si aplica) |
| Estadísticos descriptivos del target (media, std, min, max, CV) | Recomendado |

**X.2 — Análisis previo (pre-modeling)**

| Elemento | Obligatorio |
|---|---|
| Visualización de la serie completa + zoom | Sí |
| Perfil estacional: por hora, día de semana, mes (según frecuencia) | Sí |
| Descomposición STL con periodo adecuado a la frecuencia | Sí |
| Tests de estacionariedad: ADF + KPSS (ambos, con interpretación contrastada) | Sí |
| ACF y PACF de la serie y de diferencias | Sí |
| Detección de outliers (método explícito, umbral, conteo) | Sí |
| Análisis de cambio estructural (CUSUM, Chow o similar) | Sí (al menos 1 método) |
| Correlación target-covariables y correlación cruzada | Sí (cuando hay covariables) |
| Disponibilidad temporal de covariables (conocidas a futuro vs. observadas en pasado) | Sí (cuando hay covariables) |
| Heatmap o visualización de interacción (hora × día, sensor × sensor, etc.) | Variable según dataset |

**X.3 — Estrategia de validación**

| Elemento | Obligatorio |
|---|---|
| Tipo de split: temporal, rolling-origin, walk-forward, por serie, holdout | Sí |
| Proporciones exactas y justificación | Sí |
| Diagrama temporal del split (eje con train/validation/test/horizonte/embargo) | Sí |
| Horizonte de forecasting y su relación con el ciclo operacional | Sí |
| Embargo o gap entre train y test (si aplica) | Sí |
| Contraste con un split inválido (random split, leakage) si el notebook lo incluye | Recomendado |
| Discusión de qué información estaría disponible en producción | Sí |

**X.4 — Modelado**

| Elemento | Obligatorio |
|---|---|
| **Methodology Card completa** (tabla con: pregunta, split, horizonte, features, modelos, métricas, seed, limitaciones) | Sí |
| Lista exhaustiva de features con su clasificación (estática, conocida a futuro, observada en pasado) | Sí |
| Baseline ingenuo (naive o seasonal naive) | Sí |
| Todos los modelos evaluados con sus hiperparámetros explícitos | Sí |
| Tabla comparativa de métricas (al menos MAE, RMSE, MASE/WAPE) | Sí |
| Visualización de forecasts sobre datos reales | Sí |
| Análisis de importancia de features (si aplica) | Sí |
| Coste computacional: tiempo de entrenamiento, memoria, tamaño del modelo | Recomendado |
| Discusión de escenario oracle vs. producción (si aplica) | Sí (notebooks 3, 5) |

**X.5 — Análisis posterior (post-modeling)**

| Elemento | Obligatorio |
|---|---|
| Residuos del mejor modelo: serie temporal, distribución | Sí |
| Test de Ljung–Box sobre residuos (autocorrelación residual) | Sí |
| Test de normalidad (Jarque–Bera, QQ-plot) | Sí |
| Test de heterocedasticidad (ARCH LM o similar) | Sí |
| Error por horizonte (¿degrada con H?) | Sí |
| Error segmentado: por hora, por cluster, por festivo, por escala de target | Variable según dataset |
| Cobertura empírica de intervalos (si el modelo los produce) | Sí (si aplica) |
| Diagnóstico de sesgo (bias por fold/serie/segmento) | Sí |

**X.6 — Lecciones metodológicas**

| Elemento | Obligatorio |
|---|---|
| 3–5 lecciones concretas, numeradas, derivadas de los resultados | Sí |
| Cada lección debe responder a «¿qué haría diferente la próxima vez?» o «¿qué implica esto para un proyecto real?» | Sí |
| Conexión explícita con el capítulo siguiente | Sí |

**X.7 — Ejercicios propuestos**

Resumir 2–3 ejercicios del notebook, indicando nivel (fácil/intermedio/difícil) y objetivo de aprendizaje. Esta sección es opcional.

### 4.3 Mapeo capítulo ↔ notebook

| Capítulo | Notebook | Dataset | Split | Énfasis metodológico |
|---|---|---|---|---|
| 2 | `01_semana_1_eda_baselines_estacionalidad.ipynb` | Metro Traffic | 80/20 temporal | EDA, estacionalidad, baseline ingenuo, split temporal vs aleatorio |
| 3 | `02_semana_2_arima_estacionariedad_diagnostico.ipynb` | Appliances Energy | 70/15/15 | Box–Jenkins, diagnóstico de residuos, AIC vs validación |
| 4 | `03_semana_3_sarimax_variables_exogenas.ipynb` | Beijing PM2.5 | Rolling-origin 3 folds | Exógenas, escenario oracle, imputación fold-causal |
| 5 | `04_semana_4_feature_engineering_ml.ipynb` | Bike Sharing | Walk-forward + embargo 24h | Checklist anti-leakage, lags/rolling, LightGBM |
| 6 | `05_semana_5_modelos_globales_cross_learning.ipynb` | Electricity (370 series) | 296/74 cold-start | Modelos globales, cold-start, métricas macro |
| 7 | `06_semana_6_deep_learning_lstm.ipynb` | OPSD Germany | Ventanas móviles 7 días | Tensores 3D, LSTM, one-step actualizado, coste DL |
| 8 | `07_semana_7_transformers_transfer_sensores.ipynb` | PeMS-SF (963 sensores) | 770/193 sensores | N-BEATS, TFT-like, transferencia, cohortes CPU |
| 9 | `08_semana_8_forecasting_probabilistico_mlops.ipynb` | M3 Monthly (1428 series) | Holdout 18 meses | Cuantiles, pinball, CRPS, cobertura, drift, Model Card |

### 4.4 Capítulo 10 — Síntesis y conclusiones (6–8 páginas)

| Elemento | Obligatorio |
|---|---|
| **Tabla sinóptica** de los 8 experimentos: dataset, split, modelos, métrica principal, lección | Sí |
| **Respuesta a las preguntas de investigación** planteadas en el capítulo 1 | Sí |
| **Análisis transversal:** ¿qué modelos funcionan consistentemente? ¿cuándo fallan? ¿qué características de los datos predicen el rendimiento relativo? | Sí |
| **Jerarquía de complejidad:** representación visual o narrativa de cuándo escalar de baseline → estadístico → ML → DL → probabilístico | Sí |
| **Lecciones transversales** (5–8) que apliquen a cualquier proyecto de forecasting, no solo a estos datasets | Sí |
| **Limitaciones globales:** datasets usados, protocolos, hardware, modelos no evaluados (DeepAR, transformers completos) | Sí |
| **Trabajo futuro:** 3–5 direcciones concretas de extensión | Sí |
| **Reflexión MLOps:** qué se necesita para que estos modelos funcionen en producción real | Sí |

---

## 5. Metodología y estándares de calidad

### 5.1 Reproducibilidad

| Requisito | Detalle |
|---|---|
| Seed explícita | Declarar seed = 42 en cada capítulo donde se usen modelos con componente aleatorio |
| Splits deterministas | Describir exactamente cómo se construye cada split; no usar «random state» sin fijar |
| Entorno declarado | Incluir en apéndice el output de `pip freeze` o las versiones exactas de pandas, scikit-learn, lightgbm, torch, statsmodels |
| Hashes de datos | Referenciar el SHA-256 de cada CSV desde su receipt JSON |
| Código | Incluir fragmentos esenciales en el cuerpo o remitir al notebook correspondiente; nunca describir un modelo sin mostrar su configuración exacta |
| Resultados numéricos | Reportar con 2–4 decimales significativos. Si un resultado varía entre ejecuciones, declarar el rango observado |

### 5.2 Metodología estadística

- Usar **siempre** ADF y KPSS juntos para evaluar estacionariedad, interpretando sus hipótesis complementarias.
- Reportar **p-values exactos** (no «p < 0.05») cuando sea posible.
- Para tests múltiples (ej. Ljung–Box en varios lags), declarar si se aplica corrección.
- No usar correlación como evidencia de causalidad.
- Distinguir explícitamente entre **error de ajuste** (train), **error de validación** (selección de modelo) y **error de test** (estimación de generalización).

### 5.3 Validación temporal

La regla de oro del forecasting debe respetarse en cada capítulo:

> El futuro no puede filtrarse al pasado. Train, validation y test deben ser contiguos en el tiempo, en ese orden. Los modelos se ajustan con train, se seleccionan con validation y se evalúan una sola vez con test.

Infracciones que invalidan un capítulo:
- Usar random split para forecasting.
- Ajustar hiperparámetros con métricas de test.
- Imputar valores usando datos futuros.
- Escalar features con estadísticas de todo el dataset.
- Incluir `casual` y `registered` como features cuando el target es `cnt` (bike sharing).
- Usar clima observado en test sin advertir que es escenario oracle.

### 5.4 Visualizaciones

| Tipo | Requisito |
|---|---|
| Series temporales | Eje x con fechas legibles, eje y etiquetado con unidad |
| Forecasts | Línea de real + línea de predicción + banda de incertidumbre si aplica |
| Residuos | Línea temporal + histograma + QQ-plot |
| Tablas comparativas | Modelos en filas, métricas en columnas, mejor resultado en negrita |
| Diagramas de split | Barras horizontales con bloques de color para train/val/test/horizonte |
| Mapas de calor | Hora × día, sensor × sensor, u otra interacción relevante |

Cada figura debe tener: número, título descriptivo, leyenda y una nota al pie indicando la fuente (notebook X, celda Y).

### 5.5 Estilo de redacción

- **Tono:** académico-técnico, preciso, sin adjetivos vacíos («muy bueno», «excelente»).
- **Voz:** impersonal o primera persona del plural consistente.
- **Extensión:** 40–60 páginas (sin apéndices). Cada capítulo técnico: 5–7 páginas.
- **Citas:** estilo APA 7ª edición o IEEE. Usar DOIs cuando existan.
- **Ecuaciones:** formato LaTeX (renderizadas o en texto plano con notación clara).
- **Tablas:** numeradas, con título descriptivo.
- **Código:** en bloques monoespaciados, con sintaxis resaltada. Incluir solo fragmentos esenciales; referenciar el notebook completo para la implementación detallada.

---

## 6. Formato de entrega

| Aspecto | Especificación |
|---|---|
| Formato | PDF (principal) + fuente Markdown/LaTeX (opcional) |
| Tipografía | 11–12 pt, serif para cuerpo; monoespaciada para código |
| Interlineado | 1.15–1.5 |
| Márgenes | 2.5 cm |
| Idioma | Español (términos técnicos en inglés aceptados si son estándar: *lookback*, *walk-forward*, *cold-start*) |
| Portada | Título, autor, fecha, repositorio de referencia, resumen de 150–250 palabras |
| Índice | Índice general + índice de figuras + índice de tablas |
| Referencias | Lista de referencias al final, solo obras citadas en el texto |

---

## 7. Apéndices obligatorios

| Apéndice | Contenido |
|---|---|
| A — Tabla de datasets | Los 8 datasets con fuente, dimensiones, frecuencia, target, nulos, peculiaridades |
| B — Tabla de modelos | Todos los modelos usados en la monografía: tipo, hiperparámetros, librería, tiempo de ejecución |
| C — Entorno computacional | `pip freeze` o lista de paquetes con versiones; CPU/RAM/OS; tiempo total |
| D — Methodology Cards | Las 8 fichas metodológicas completas en formato unificado |
| E — Glosario | 15–25 términos técnicos definidos (MASE, WAPE, CRPS, pinball, walk-forward, etc.) |

---

## 8. Criterios de evaluación

La monografía se evalúa sobre 100 puntos distribuidos en cinco dimensiones:

### 8.1 Corrección metodológica (30 puntos)

| Criterio | Puntos |
|---|---|
| Splits temporales correctos en todos los capítulos | 8 |
| Sin leakage en features, imputación ni escalado | 8 |
| Uso correcto de train/validation/test (test una sola vez) | 6 |
| Métricas apropiadas para cada problema (MASE para escala, pinball para cuantiles, etc.) | 4 |
| Baselines ingenuos incluidos en toda comparación | 4 |

### 8.2 Profundidad analítica (25 puntos)

| Criterio | Puntos |
|---|---|
| Diagnóstico de residuos completo (Ljung–Box, normalidad, heterocedasticidad) en cada capítulo | 8 |
| Análisis de error por horizonte, hora, segmento o cluster | 6 |
| Interpretación sustantiva de los resultados (no solo reportar números) | 6 |
| Contraste con escenarios oracle/producción donde aplica | 5 |

### 8.3 Síntesis transversal (20 puntos)

| Criterio | Puntos |
|---|---|
| Tabla sinóptica completa de los 8 experimentos | 5 |
| Lecciones transversales no triviales (no obviedades) | 6 |
| Jerarquía de complejidad fundamentada en resultados | 5 |
| Respuesta explícita a las preguntas de investigación | 4 |

### 8.4 Calidad de comunicación (15 puntos)

| Criterio | Puntos |
|---|---|
| Estructura clara y consistente entre capítulos | 4 |
| Figuras y tablas bien diseñadas, numeradas y referenciadas | 4 |
| Redacción precisa, sin ambigüedades ni adjetivos vacíos | 4 |
| Citas y referencias correctas y completas | 3 |

### 8.5 Reproducibilidad y gobierno (10 puntos)

| Criterio | Puntos |
|---|---|
| Methodology Card completa en cada capítulo | 4 |
| Entorno computacional documentado | 2 |
| Hashes o referencias a receipts de datos | 2 |
| Código esencial incluido o correctamente referenciado | 2 |

### Umbrales de aprobación

- **90–100:** Sobresaliente. Trabajo de calidad publicable como material docente.
- **75–89:** Notable. Monografía sólida con análisis riguroso.
- **60–74:** Aprobado. Cumple los requisitos mínimos.
- **< 60:** No aprobado. Requiere revisión sustancial.

---

## 9. Errores graves que invalidan secciones

Los siguientes errores, si se detectan en un capítulo, implican la invalidación de esa sección (0 puntos en corrección metodológica para ese capítulo):

1. **Random split** para forecasting sin advertirlo como error didáctico.
2. **Leakage de futuro** no detectado ni discutido.
3. **Test usado para selección de modelo** sin validación intermedia.
4. **Métrica incorrecta** para el tipo de problema (ej. R² en series con tendencia sin discutir).
5. **Afirmaciones causales** basadas únicamente en correlación.
6. **Resultados inventados** o no respaldados por ejecución real.
7. **DeepAR reportado como ejecutado** sin haberlo implementado.

---

## 10. Calendario orientativo

| Semana | Actividad | Entregable |
|---|---|---|
| 1 | Estudio notebook 1 + redacción capítulo 2 | Borrador cap. 2 |
| 2 | Estudio notebook 2 + redacción capítulo 3 | Borrador cap. 3 |
| 3 | Estudio notebook 3 + redacción capítulo 4 | Borrador cap. 4 |
| 4 | Estudio notebook 4 + redacción capítulo 5 | Borrador cap. 5 |
| 5 | Estudio notebook 5 + redacción capítulo 6 | Borrador cap. 6 |
| 6 | Estudio notebook 6 + redacción capítulo 7 | Borrador cap. 7 |
| 7 | Estudio notebook 7 + redacción capítulo 8 | Borrador cap. 8 |
| 8 | Estudio notebook 8 + redacción capítulo 9 | Borrador cap. 9 |
| 9 | Redacción capítulos 1 y 10 + apéndices | Primer borrador completo |
| 10 | Revisión, correcciones, formato final | Entrega final |

---

## 11. Referencias mínimas esperadas

La monografía debe citar al menos **12 referencias**, distribuidas así:

- **4+ fuentes de los datasets** (UCI Repository, OPSD, Zenodo M3, etc.) con sus DOIs o URLs.
- **4+ referencias metodológicas** (Box & Jenkins, Hyndman & Athanasopoulos, artículos de M4/M5, TFT paper).
- **2+ herramientas** (scikit-learn, LightGBM, PyTorch, statsmodels, statsforecast).
- **2+ artículos aplicados o benchmarks** que contextualicen resultados.

Se sugiere usar las referencias ya identificadas en las fichas `README.md` de cada carpeta `data/` y en [`SOURCE_NOTES.md`](docs/SOURCE_NOTES.md).

---

## 12. Recursos de apoyo

| Recurso | Ubicación |
|---|---|
| Guía de instalación | [`docs/INSTALLATION.md`](docs/INSTALLATION.md) |
| Guía de notebooks | [`docs/NOTEBOOK_GUIDE.md`](docs/NOTEBOOK_GUIDE.md) y [`notebooks/README.md`](notebooks/README.md) |
| Arquitectura del repositorio | [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) |
| Guía docente (evaluación, features, MLOps) | [`docs/COURSE_GUIDE.md`](docs/COURSE_GUIDE.md) |
| Reproducibilidad | [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) |
| Gobierno de datos | [`docs/DATA_GOVERNANCE.md`](docs/DATA_GOVERNANCE.md) |
| Notas de fuentes y transformaciones | [`docs/SOURCE_NOTES.md`](docs/SOURCE_NOTES.md) |
| FAQ y troubleshooting | [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) |
| Catálogo machine-readable | [`registry.yaml`](registry.yaml) |
| Readme principal | [`README.md`](README.md) |
| Guía de contribución | [`CONTRIBUTING.md`](CONTRIBUTING.md) |

---

## 13. Lista de verificación antes de la entrega

- [ ] Los 10 capítulos siguen la estructura especificada.
- [ ] Los 8 capítulos técnicos (2–9) contienen las 6 secciones obligatorias (X.1–X.6).
- [ ] Cada capítulo técnico incluye su **Methodology Card** en formato tabla.
- [ ] Todos los splits son temporales (no aleatorios) y están documentados con diagrama.
- [ ] Se incluyen baselines ingenuos en toda comparación.
- [ ] Se realizaron los 4 tests de diagnóstico de residuos: Ljung–Box, Jarque–Bera, QQ-plot, ARCH LM.
- [ ] No hay leakage: features desplazadas, escalado sobre train, imputación causal.
- [ ] Las afirmaciones causales están calificadas o evitadas.
- [ ] Las figuras y tablas están numeradas, tituladas y referenciadas en el texto.
- [ ] El apéndice A contiene la tabla de datasets.
- [ ] El apéndice B contiene la tabla de modelos con hiperparámetros.
- [ ] El apéndice D contiene las 8 Methodology Cards unificadas.
- [ ] La bibliografía tiene 12+ referencias en formato consistente.
- [ ] El entorno computacional está documentado (apéndice C).
- [ ] Se responden explícitamente las preguntas de investigación del capítulo 1.
- [ ] El capítulo 10 incluye tabla sinóptica, lecciones transversales y jerarquía de complejidad.
- [ ] No se reportan resultados de modelos no ejecutados (DeepAR, TFT completo).
- [ ] El PDF está generado y revisado visualmente.

---

*Documento generado a partir del repositorio `course-timeseries-benchmarks-pro` v1.1.0. Las especificaciones aquí contenidas reflejan la estructura y contenido de los ocho notebooks ejecutados y la documentación complementaria del repositorio.*
