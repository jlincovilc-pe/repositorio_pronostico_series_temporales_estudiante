# Open Power System Data — Germany

## Resumen
50,401 observaciones horarias de 2014-12-31 a 2020-09-30 y 43 columnas alemanas (`DE_`). Incluye demanda real/pronosticada, precio day-ahead, generación/capacidad solar y eólica, perfiles y zonas de control.

## Calidad
Hay 284,490 celdas nulas porque la cobertura de variables cambia por periodo y zona. La demanda nacional tiene 50,400 valores no nulos de 50,401. No se imputó ni se recortó el periodo.

## Literatura y uso docente
Wiese et al. describen OPSD como infraestructura de datos trazables para modelado de sistemas eléctricos. Semana 6: LSTM/GRU multivariable, covariables conocidas frente a observadas y cambios de cobertura.

## Protocolo y gotchas
Defina un target, por defecto `DE_load_actual_entsoe_transparency`, y seleccione covariables con cobertura suficiente en el periodo de estudio. No use demanda pronosticada o precio contemporáneo sin verificar disponibilidad. Mantenga `ds_utc` para modelado y use CET/CEST solo para features calendario, atendiendo horario de verano. Impute dentro de cada fold.

## Referencia
Wiese, F., et al. (2019). Open Power System Data – Frictionless data for electricity system modelling. *Applied Energy, 236*, 401–409. https://doi.org/10.1016/j.apenergy.2018.11.097
