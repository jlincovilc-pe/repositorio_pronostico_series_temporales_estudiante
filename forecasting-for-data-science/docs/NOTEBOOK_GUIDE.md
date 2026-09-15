# Guía de los notebooks

## Cómo leer cada clase

Todos siguen el mismo contrato:

0. configuración y contrato de datos;
1. análisis previo;
2. validación temporal;
3. modelado y Methodology Card;
4. análisis posterior;
5. lecciones metodológicas;
6. ejercicios.

Las celdas Markdown explican el porqué; las celdas de código materializan el análisis. Ejecute en orden. No salte directamente al modelo: muchas decisiones dependen de la auditoría y del split.

## Recorrido recomendado

| # | Notebook | Prerrequisito | Función | Salida principal | Tiempo CPU* |
|---:|---|---|---|---|---:|
| 1 | `01_semana_1_eda_baselines_estacionalidad.ipynb` | pandas básico | Enseñar orden temporal y baselines | Comparación MAE/RMSE/MASE/WAPE | ~1 min |
| 2 | `02_semana_2_arima_estacionariedad_diagnostico.ipynb` | Notebook 1 | Aplicar Box–Jenkins | ARIMA/ETS/Theta y residuos | ~1 min |
| 3 | `03_semana_3_sarimax_variables_exogenas.ipynb` | ARIMA | Incorporar exógenas | SARIMA vs SARIMAX por fold | ~3 min |
| 4 | `04_semana_4_feature_engineering_ml.ipynb` | Validación temporal | Tabularizar sin leakage | LightGBM y feature importance | ~1 min |
| 5 | `05_semana_5_modelos_globales_cross_learning.ipynb` | ML tabular | Cross-learning/cold-start | Métricas macro por serie | ~1 min |
| 6 | `06_semana_6_deep_learning_lstm.ipynb` | NumPy/PyTorch | Tensores 3D y LSTM | Curvas de aprendizaje y comparación | ~2 min |
| 7 | `07_semana_7_transformers_transfer_sensores.ipynb` | PyTorch | Transferencia por sensor | N-BEATS/LSTM/TFT-like | ~10 min |
| 8 | `08_semana_8_forecasting_probabilistico_mlops.ipynb` | Métricas de forecast | Cuantiles y monitoreo | Calibración, drift y Model Card | ~1 min |

\*Tiempos orientativos del entorno de construcción.

## Resultados y outputs

Los gráficos y tablas están guardados dentro de los `.ipynb`. Reejecutar reemplaza esos outputs. Ningún notebook escribe modelos o predicciones a disco. Use `File > Save and Export Notebook As` para HTML/PDF si necesita distribución estática.

## Notebooks pesados

- **Semana 5:** lee Electricity en chunks y conserva una ventana temporal de 120 días.
- **Semana 6:** PyTorch CPU, 4 threads, lookback 168.
- **Semana 7:** cohorte real 48 sensores train/24 test; el split completo 770/193 queda definido.

## DeepAR opcional

Notebook 8 documenta DeepAR pero no reporta métricas porque no fue ejecutado. Para extenderlo instale una implementación compatible, congele su versión y evalúe exactamente el mismo holdout de 18 meses. No mezcle resultados de otro split.

## Cómo reiniciar un notebook

Use `Kernel > Restart Kernel and Run All Cells`. Si falla por memoria, cierre otros kernels, empiece por un notebook y consulte `TROUBLESHOOTING.md`.
