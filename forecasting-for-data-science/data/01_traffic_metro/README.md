# Metro Interstate Traffic Volume

## Resumen
Tráfico horario de la I-94 oeste en la estación ATR 301 entre Minneapolis y St. Paul. El producto contiene 48,204 filas entre 2012-10-02 y 2018-09-30, target `y` y siete covariables meteorológicas/calendario.

## Esquema
- `ds`: timestamp horario; `y`: volumen de tráfico.
- `holiday`: festivo o `None`; `temp`: Kelvin; `rain_1h`, `snow_1h`: mm; `clouds_all`: porcentaje.
- `weather_main`, `weather_description`: categorías meteorológicas.

Perfil observado: `y` media 3,259.82, rango 0–7,280. La fuente contiene 17 filas exactamente repetidas, preservadas. No hay nulos después de convertir el token de “sin festivo” a `None`.

## Literatura y uso docente
UCI describe el problema como regresión secuencial con clima y festivos. La ficha solicitada atribuye el recurso a Dwork et al.; UCI no muestra un paper introductorio canónico en su página actual, por lo que se cita el registro del dataset y no se inventa un DOI. Semana 1: EDA, perfiles hora/día, seasonal naive, ETS y regresión con covariables.

## Protocolo y gotchas
Use horizonte 24, backtesting semanal y lags 24/168. Compare un baseline estacional con modelos sin y con clima. `weather_main` y `weather_description` describen el mismo estado a distinta granularidad. Los duplicados deben resolverse con una política explícita; no los elimine después del split. Clima observado puede no estar disponible al origen en producción.

## Fuente
UCI Machine Learning Repository. *Metro Interstate Traffic Volume*. https://archive.ics.uci.edu/dataset/492/metro+interstate+traffic+volume
