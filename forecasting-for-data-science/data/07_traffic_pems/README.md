# PeMS-SF

## Resumen
Ocupación vial de 963 sensores, muestreada cada 10 minutos. El producto combina 440 días: 144 slots/día, 63,360 filas y 967 columnas (`split`, `day_id`, `slot_10min`, `weekday_label` y sensores con ID real).

## Formato y calidad
Los valores de sensores están entre 0 y 1 en la fuente. `weekday_label` usa enteros 1–7. No hay nulos. UCI eliminó festivos y dos días anómalos. El archivo original no proporciona fechas calendario en esta distribución; no se inventaron.

## Literatura y uso docente
Chen et al. presentan PeMS como sistema de minería de detectores de autopista. UCI formula este extracto como clasificación del día de semana; aquí también sirve para forecasting multivariado. Semana 7: Transformers, convoluciones temporales y modelos espacio-temporales.

## Protocolo y gotchas
Conserve el split de origen o reconstruya particiones por `day_id`; nunca mezcle slots del mismo día entre train/test. Para forecasting, prediga bloques futuros dentro del día o días completos y reporte por sensor. No infiera una matriz de adyacencia por orden de columnas; requiere metadatos viales externos. Atención no prueba influencia causal.

## Referencia
Chen, C., Petty, K., Skabardonis, A., Varaiya, P., & Jia, Z. (2001). Freeway Performance Measurement System: Mining loop detector data. *Transportation Research Record, 1748*, 96–102. https://doi.org/10.3141/1748-12
