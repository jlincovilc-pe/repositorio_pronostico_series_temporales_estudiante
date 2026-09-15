# Guía rápida de notebooks

Los ocho notebooks están numerados y deben estudiarse en orden. Todos incluyen datos reales, outputs ejecutados, Methodology Cards, tests estadísticos, validación temporal, diagnóstico posterior y ejercicios.

| # | Archivo | Propósito | Prerrequisitos | Tiempo CPU* | Limitación clave |
|---:|---|---|---|---:|---|
| 1 | `01_semana_1_eda_baselines_estacionalidad.ipynb` | EDA, STL, baselines y orden temporal | pandas, estadística descriptiva | ~1 min | Metro tiene gaps y timestamps repetidos |
| 2 | `02_semana_2_arima_estacionariedad_diagnostico.ipynb` | Box–Jenkins y residuos | Notebook 1 | ~1 min | Serie agregada de 10 min a hora |
| 3 | `03_semana_3_sarimax_variables_exogenas.ipynb` | SARIMAX y rolling-origin | ARIMA | ~3 min | Clima observado en test es escenario oracle |
| 4 | `04_semana_4_feature_engineering_ml.ipynb` | Lags, rolling y ML sin leakage | Validación temporal | ~1 min | `casual+registered=cnt`; se excluyen |
| 5 | `05_semana_5_modelos_globales_cross_learning.ipynb` | Paneles, cold-start y modelos globales | LightGBM, groupby | ~1 min | Ventana de 120 días; 370 series completas |
| 6 | `06_semana_6_deep_learning_lstm.ipynb` | Tensores 3D y LSTM | PyTorch básico | ~2 min | Evaluación one-step actualizada |
| 7 | `07_semana_7_transformers_transfer_sensores.ipynb` | N-BEATS/TFT-like y transferencia | PyTorch, Notebook 6 | ~10 min | Cohorte CPU 48/24; TFT-like no es TFT completo |
| 8 | `08_semana_8_forecasting_probabilistico_mlops.ipynb` | Cuantiles, calibración, drift y Model Card | Métricas de forecast | ~1 min | CRPS aproximado; DeepAR no ejecutado |

\*Tiempos observados, no garantías.

## Ejecución

Desde la raíz:

```bash
jupyter lab
# o, no interactivo:
python scripts/run_notebooks.py --notebook 04
```

Las rutas buscan `data/...` y `../data/...`. Todos los outputs se guardan dentro del notebook. Una reejecución puede modificar el archivo por cambios de resultados y metadatos.

## Resultados reproducidos

1. Seasonal Naive 168 fue el mejor baseline de Metro.
2. Validation seleccionó ARIMA (1,0,2); ETS ganó por MASE en test.
3. SARIMAX redujo MAE medio 18.4% frente a SARIMA en escenario oracle.
4. LightGBM logró MASE medio 0.457 en Bike.
5. Cold-start sin contexto no recuperó escala individual; resultado negativo central.
6. LightGBM superó LSTM, ARIMA y seasonal naive en OPSD bajo el protocolo usado.
7. TFT-like obtuvo MAE 0.013122 en la cohorte PeMS ejecutada.
8. LightGBM cuantílico obtuvo cobertura P10–P90 0.789 y CRPS aproximado 356.27.

Son resultados específicos de estos splits, ventanas e hiperparámetros. No son rankings universales.

## Extensiones opcionales

- DeepAR en semana 8: instale y congele una implementación compatible; use el mismo holdout de 18 meses.
- GPU en semanas 6–7: opcional. Registre hardware, duración y versiones.
- HTML/PDF: exporte desde JupyterLab. El repositorio no incluye copias redundantes para limitar tamaño.
