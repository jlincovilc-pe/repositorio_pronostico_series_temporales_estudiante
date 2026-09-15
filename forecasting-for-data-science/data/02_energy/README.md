# Appliances Energy Prediction

## Resumen
Consumo de electrodomésticos en una vivienda de bajo consumo, cada 10 minutos durante ~4.5 meses. El archivo tiene 19,735 filas y 29 columnas.

## Esquema
- `ds`: timestamp; `y`: energía de electrodomésticos; `lights`: iluminación.
- `t1`–`t9`, `rh_1`–`rh_9`: temperatura y humedad interior por zona.
- `t_out`, `press_mm_hg`, `rh_out`, `windspeed`, `visibility`, `tdewpoint`: clima exterior.
- `rv1`, `rv2`: variables aleatorias de control, no señales operativas.

No hay nulos ni duplicados. `y` tiene media 97.69 Wh y rango 10–1,080.

## Literatura y uso docente
Candanedo, Feldheim y Deramaix compararon regresión lineal, support vector regression, random forest y gradient boosting. El paper destaca la utilidad de temperatura/humedad y añade variables aleatorias para comprobar si el modelo selecciona ruido. Semana 2: ARIMA sobre target, diagnóstico residual y comparación con regresión dinámica.

## Protocolo y gotchas
Use horizontes 6/36 pasos (1/6 horas), splits diarios y escalado ajustado en train. `rv1` y `rv2` sirven como controles negativos. No use variables meteorológicas contemporáneas sin aclarar si son observadas o pronosticadas.

## Referencia
Candanedo, L. M., Feldheim, V., & Deramaix, D. (2017). Data driven prediction models of energy use of appliances in a low-energy house. *Energy and Buildings, 140*, 81–97. https://doi.org/10.1016/j.enbuild.2017.01.083
