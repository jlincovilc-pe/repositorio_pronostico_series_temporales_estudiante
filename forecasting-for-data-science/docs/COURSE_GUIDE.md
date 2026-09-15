# Guía docente y de modelado

## Secuencia de ocho semanas

1. **Metro:** EDA, estacionalidad diaria/semanal, seasonal naive y efecto incremental de clima/feriados.
2. **Appliances:** ARIMA, residuos y regresión dinámica con sensores interiores/exteriores.
3. **Beijing:** SARIMAX, exógenas meteorológicas y missingness temporal.
4. **Bike:** feature engineering, lags/rolling desplazados y boosting global.
5. **Electricity:** 370 series, cross-learning, escalado por serie y LightGBM global.
6. **OPSD:** LSTM/GRU, covariables energéticas y disponibilidad temporal.
7. **PeMS-SF:** forecasting multivariado, Transformers y límites de la atención espacial.
8. **M3 Monthly:** modelos locales/globales, cuantiles, calibración y registro de modelos.

## Evaluación obligatoria

- Splits temporales y rolling-origin. No barajar.
- Ajustar imputación, escalado, selección y tuning solo con train.
- Incluir naive/seasonal naive y medir error por horizonte.
- Para paneles: macro por serie y agregación ponderada documentada.
- Para probabilístico: pinball loss, cobertura y ancho de intervalo.
- Reportar tiempo, memoria y tamaño del modelo junto con precisión.

## Contrato de features

Clasifique cada variable como estática, conocida a futuro, observada en el pasado o no disponible en inferencia. Clima observado, carga real, generación real y componentes del target no deben usarse como covariables futuras salvo que se sustituyan por pronósticos disponibles en el origen.

## MLOps

Cada corrida debe persistir commit, SHA-256 del dataset, split, horizonte, features, transformaciones, seed, hiperparámetros, métricas, predicciones, latencia y RAM. Monitoree frescura, gaps, duplicados, drift de covariables, error por horizonte, sesgo y cobertura.
