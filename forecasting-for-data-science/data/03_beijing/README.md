# Beijing PM2.5

## Resumen
43,800 observaciones horarias desde 2010-01-02 hasta 2014-12-31. Combina PM2.5 de la Embajada de EE. UU. y meteorología del aeropuerto de Beijing.

## Esquema
Target `pm2.5`; covariables `DEWP`, `TEMP`, `PRES`, `cbwd`, `Iws`, `Is`, `Ir`; `ds` es el timestamp. `No` es índice y no debe tratarse como predictor causal.

Se eliminaron las primeras 24 filas según la instrucción. Persisten 2,043 nulos interiores en `pm2.5`; media observada 98.61, rango 0–994.

## Literatura y uso docente
Liang et al. analizaron severidad, asociación meteorológica, el periodo APEC y calefacción invernal. Es evidencia observacional, no identificación causal. Semana 3: SARIMAX, disponibilidad de exógenas y máscaras de missingness.

## Protocolo y gotchas
Impute dentro de cada fold y agregue indicador de missingness. Compare persistencia, SARIMAX y boosting con lags desplazados. Evalúe MAE global y episodios altos con umbral declarado. Interpolación bidireccional antes del split filtra futuro.

## Referencias
Liang, X., et al. (2015). Assessing Beijing’s PM2.5 pollution. *Proceedings of the Royal Society A, 471*, 20150257. https://doi.org/10.1098/rspa.2015.0257

UCI dataset: https://doi.org/10.24432/C5JS49
