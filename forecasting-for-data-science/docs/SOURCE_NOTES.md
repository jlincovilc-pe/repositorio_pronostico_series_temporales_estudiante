# Notas de fuente y transformaciones

## PeMS-SF

La URL solicitada `.../pems-sf.zip` devolvió 404. UCI sirve el mismo recurso mediante `.../pems+sf.zip`. El producto conserva 440 matrices diarias, 963 IDs reales de estación, slots de 10 minutos, etiquetas de día de semana y split original. No hay fechas calendario en el paquete.

## Electricity Load Diagrams

El archivo tiene separador `;`, coma decimal y frecuencia de 15 minutos. Se filtró el intervalo `[2012-01-01, 2015-01-01)`, se sumó por hora y se reindexó a 26,304 horas. El formato long tiene 9,732,480 claves únicas.

## OPSD

La URL proporcionada es un CSV separado por comas, pese a la instrucción `sep=';'`. Se seleccionaron timestamps y columnas alemanas `DE_`. La cobertura desigual explica 284,490 celdas nulas; no se imputaron.

## Metro y Beijing

Metro representa ausencia de festivo como token `None`, no como nulo. Beijing conserva 2,043 nulos interiores tras eliminar las primeras 24 filas; tratarlos dentro de cada fold.

## Referencias corregidas

La cita ARIMA–LSTM indicada para Electricity no corresponde a Cerqueira et al. en los metadatos localizados. El trabajo verificable con ese título es Siami-Namini, Tavakoli y Siami Namin (2018), DOI `10.1109/ICMLA.2018.00227`.
