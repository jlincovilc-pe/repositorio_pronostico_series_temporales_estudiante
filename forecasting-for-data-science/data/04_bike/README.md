# Bike Sharing

## Resumen
Dos productos: 17,379 filas horarias y 731 diarias de Capital Bikeshare, 2011–2012. Incluyen calendario y meteorología normalizada.

## Esquema
Target `cnt`; calendario `season`, `yr`, `mnth`, `hr`, `holiday`, `weekday`, `workingday`; clima `weathersit`, `temp`, `atemp`, `hum`, `windspeed`; componentes `casual`, `registered`.

No hay nulos. En horario, `cnt` tiene media 189.46 y rango 1–977.

## Literatura y uso docente
Fanaee-T y Gama trataron el sistema como red de sensores urbanos para etiquetar eventos mediante detectores y conocimiento contextual. Semana 4: lags, rolling windows, codificación cíclica y gradient boosting.

## Protocolo y gotchas
Construya el timestamp horario con `dteday + hr`. `cnt = casual + registered`: usar estos dos componentes para predecir `cnt` es leakage directo. Compare lag 24/168, SARIMAX y boosting. Separe escenario con clima observado del escenario con pronóstico meteorológico.

## Referencias
Fanaee-T, H., & Gama, J. (2014). Event labeling combining ensemble detectors and background knowledge. *Progress in Artificial Intelligence, 2*, 113–127. https://doi.org/10.1007/s13748-013-0040-3

UCI dataset: https://doi.org/10.24432/C5W894
