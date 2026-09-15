# M3 Competition — Monthly

## Resumen
1,428 series mensuales en formato largo, 167,562 observaciones, sin nulos. Las longitudes van de 66 a 144 meses, mediana 133.

## Esquema
`unique_id`: serie; `ds`: cierre de mes generado por el adaptador; `y`: target. No contiene covariables exógenas, pero cumple el criterio de panel extenso (>100 series).

## Literatura y uso docente
M3 comparó métodos sobre 3,003 series de varias frecuencias. Makridakis y Hibon subrayaron heterogeneidad y combinación de pronósticos; ningún método domina todas las series. Semana 8: probabilístico, model registry, evaluación macro y monitoreo.

## Protocolo y gotchas
Horizonte mensual oficial: 18. Cree validación interna antes del tramo final. Compare seasonal naive, ETS, Theta y modelo global. Reporte sMAPE/MASE con fórmula congelada; para cuantiles, pinball loss, cobertura y ancho. Un split por filas mezcla futuro entre series.

## Referencias
Makridakis, S., & Hibon, M. (2000). The M3-Competition. *International Journal of Forecasting, 16*(4), 451–476. https://doi.org/10.1016/S0169-2070(00)00057-1

Dataset: https://doi.org/10.5281/zenodo.4656298
