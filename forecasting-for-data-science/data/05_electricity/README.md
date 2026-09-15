# Electricity Load Diagrams 2011–2014

## Resumen
Panel global horario de 370 clientes. Se filtró 2012–2014, se sumaron los intervalos originales de 15 minutos y se convirtió a `unique_id, ds, y`.

## Dimensión y calidad
9,732,480 filas = 370 series × 26,304 horas. No hay nulos ni claves `(unique_id, ds)` duplicadas. El consumo está en la unidad distribuida por UCI; no se reescaló.

## Literatura y uso docente
El benchmark se usa ampliamente para modelos globales. La comparación ARIMA–LSTM citada en la instrucción corresponde en Crossref a Siami-Namini et al. (2018), no a Cerqueira et al. Semana 5: cross-learning con LightGBM, embeddings de serie y modelos globales recurrentes.

## Protocolo y gotchas
Lea por chunks. Use últimos 7–28 días por cliente para test y backtesting común. Compare seasonal naive 24/168, modelos locales y globales. Escale por cliente usando train. Ceros pueden ser consumo real o periodo anterior a activación; audite por serie. La agregación horaria elegida es suma, coherente con energía por intervalo; otras tareas pueden preferir media.

## Fuentes
UCI Machine Learning Repository. *ElectricityLoadDiagrams20112014*. https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014

Siami-Namini, S., Tavakoli, N., & Siami Namin, A. (2018). A comparison of ARIMA and LSTM in forecasting time series. *ICMLA*. https://doi.org/10.1109/ICMLA.2018.00227
