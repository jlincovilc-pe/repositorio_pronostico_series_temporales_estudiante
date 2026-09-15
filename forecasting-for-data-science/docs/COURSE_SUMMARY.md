# Resumen global del curso


| Semana | Dataset | Split usado | Modelo principal | Métrica clave | Lección metodológica |
|---:|---|---|---|---|---|
| 1 | Metro Traffic | Temporal 80/20 | Seasonal Naive 168 | MASE | El orden temporal importa; random split filtra futuro. |
| 2 | Appliances Energy | 70/15/15 | ARIMA/ETS | MASE | Validation selecciona hiperparámetros; test se usa una vez. |
| 3 | Beijing PM2.5 | Rolling-origin, 3 folds | SARIMAX | MAE | Exógenas ayudan solo si existen en inferencia y son estables. |
| 4 | Bike Sharing | Walk-forward + embargo 24 h | LightGBM | MASE | Lags y rolling requieren `shift`; embargo reduce leakage. |
| 5 | Electricity | 296/74 series cold-start | LightGBM global | MASE macro | Sin contexto/metadatos no se recupera la escala del cliente nuevo. |
| 6 | OPSD Germany | Ventanas móviles de 7 días | LightGBM/LSTM | MASE | Deep learning debe justificar coste frente a baselines fuertes. |
| 7 | PeMS-SF | 770/193 sensores | TFT-like compacto | MAE | Transferencia por sensor no equivale a causalidad espacial. |
| 8 | M3 Monthly | Holdout oficial de 18 meses | LightGBM cuantílico | CRPS aproximado y cobertura | Forecast probabilístico exige calibración y monitoreo. |

Los resultados pertenecen a los protocolos ejecutados en estos notebooks. No constituyen rankings universales entre familias de modelos.