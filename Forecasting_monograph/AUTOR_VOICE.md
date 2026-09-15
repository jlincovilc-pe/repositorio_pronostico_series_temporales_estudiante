# AUTOR_VOICE.md — Guía de enriquecimiento opcional

> **Documento de trabajo — no forma parte del entregable.** El PDF es entregable sin completar esto.
> Este archivo no se incluye en ningún `typst compile`. Su propósito es ofrecer al estudiante
> puntos concretos donde, si lo desea, puede enriquecer el documento con su voz real. No son
> vacíos que el documento necesite; son oportunidades de profundidad autoral.

## Cómo usar este archivo

Los 12 puntos listados abajo son lugares del documento donde la voz del autor podría añadir
profundidad subjetiva: expectativas, sorpresas, reacciones, dudas. La pasada 3 ya sea (a)
eliminó los placeholders que ocupaban esos lugares, (b) dejó prosa puente neutra que funciona
sin experiencia personal, o (c) reformuló en tercera persona lo que era objetivamente verificable.

El documento es entregable tal cual compila. Si el estudiante quiere enriquecerlo, los puntos
abajo indican dónde y cómo.

**Reglas de oro si decides completar un punto**:
1. Una o dos frases máximo por punto (no ensayar).
2. Anclar siempre a un número y un capítulo concreto del documento.
3. Sustituir la prosa puente existente por tu texto — no añadir encima.
4. Si decides no completar un punto, dejar la prosa puente existente.

---

## Puntos de enriquecimiento opcional

### 1. Capítulo 1 §1.1 (tras el segundo párrafo, donde antes había un callout)

**Qué añadiría valor**: una frase sobre por qué existe este documento — una sospecha inicial que se confirmó o refutó en algún capítulo concreto.

**Preguntas guía**:
- ¿Cuál fue tu intuición inicial sobre forecasting antes de empezar el curso?
- ¿En qué capítulo esa intuición se confirmó o se rompió? Cita el número (p. ej. "en el Cap. 5, al ver MASE 0.457 vs. 0.818, confirmé que…").

**Nota**: el documento actual fluye sin este punto; añadirlo daría más voz personal pero no es necesario para la entregabilidad.

---

### 2. Capítulo 2 §2.1 (apertura)

**Qué añadiría valor**: qué esperabas del primer dataset de tráfico y qué te sorprendió al ver que el random split producía un error MENOR (251.66 vs. 287.55).

**Preguntas guía**:
- Antes de ejecutar el notebook, ¿qué modelo esperabas que ganara?
- ¿Cuándo te diste cuenta de que el random split producía error menor? ¿Cuál fue tu reacción?

---

### 3. Capítulo 3 §3.1 (apertura)

**Qué añadiría valor**: qué esperabas del ARIMA antes del test y tu reacción al ver que ETS (0.681) ganaba al modelo elegido por AIC (0.901).

**Preguntas guía**:
- ¿Confiabas en que la selección por AIC te llevaría al mejor modelo?
- Cuando viste que ETS ganaba con MASE 0.681 vs. 0.901 de ARIMA, ¿qué pensaste?

---

### 4. Capítulo 4 §4.1 (apertura)

**Qué añadiría valor**: por qué la distinción entre 'clima observado' y 'clima disponible ex-ante' te costó interiorizarla, y qué momento del notebook te la clavó.

**Preguntas guía**:
- ¿Cuándo leíste por primera vez la distinción, te pareció obvia o sutil?
- ¿Hubo un momento del notebook donde la distinción se hizo real para ti?

---

### 5. Capítulo 5 §5.1 (apertura)

**Qué añadiría valor**: qué sospechabas sobre el feature engineering antes de ejecutar y tu reacción al ver la Tabla 5.3 (correlación con fuga 0.400 vs. segura 0.362).

**Preguntas guía**:
- Antes de ejecutar, ¿qué pensabas que iba a pasar con `casual` y `registered`?
- ¿Te sorprendió que la diferencia entre fuga y no-fuga fuera tan pequeña?

---

### 6. Capítulo 6 §6.1 (apertura)

**Qué añadiría valor**: qué esperabas del cross-learning y qué te costó aceptar del empate 0.01% entre LightGBM global y perfil hora×día.

**Preguntas guía**:
- ¿Esperabas que el modelo global superara al baseline por mucho?
- Cuando viste el empate 0.01%, ¿pensaste que había un bug?

---

### 7. Capítulo 7 §7.1 (apertura)

**Qué añadiría valor**: qué esperabas de la LSTM y tu reacción al ver que perdía también contra el seasonal naive (0.576 vs. 0.495).

**Preguntas guía**:
- ¿Esperabas que la LSTM ganara o perdiera? ¿Por qué?
- Cuando viste los números, ¿te pareció un fallo de la arquitectura o del setup?

---

### 8. Capítulo 8 §8.1 (apertura)

**Qué añadiría valor**: qué esperabas de TFT-like y tu reacción al ver que ganaba por 4% sobre LastValue pero que N-BEATS era el ganador práctico al cuarto del costo.

**Preguntas guía**:
- ¿Tenías la expectativa de que el Transformer ganaría por mucho?
- ¿Te sorprendió que N-BEATS (95.41 s) alcanzara casi el mismo resultado que TFT-like (398.45 s)?

---

### 9. Capítulo 9 §9.1 (apertura)

**Qué añadiría valor**: por qué este capítulo es 'cobro de deudas' — qué deuda específica de los caps 2-8 esperabas cobrar aquí.

**Preguntas guía**:
- A lo largo de los caps 2-8, ¿fuiste notando el patrón de no normalidad acumulada? ¿En qué capítulo te diste cuenta?
- ¿Esperabas que el probabilístico fuera la "victoria final" del documento?

---

### 10. Capítulo 10 §10.1 (apertura del capítulo)

**Qué añadiría valor**: una frase sobre qué te llevas realmente de estos ocho experimentos — algo que no podría cerrar otro documento sin modificar una palabra.

**Preguntas guía**:
- ¿Qué hallazgo te cambió la forma de pensar sobre forecasting?
- ¿Qué costumbre adquiriste?
- ¿Qué deuda confesable te llevas?

---

### 11. Capítulo 10 §10.3 (análisis transversal)

**Qué añadiría valor**: qué resultado te sorprendió más al verlo en perspectiva comparada.

**Preguntas guía**:
- Cuando viste los ocho experimentos juntos, ¿qué te sorprendió más? ¿El empate 0.01%? ¿La asimetría 44% vs. 2900%? ¿El asterisco del 0.234?

---

### 12. Capítulo 10 §10.10 (cierre)

**Qué añadiría valor**: una confesión personal sobre qué cambiarías del documento si lo volvieras a empezar.

**Preguntas guía**:
- Si pudieras volver a empezar el curso, ¿qué experimento ejecutarías distinto?
- ¿Qué sospecha tuya NO se confirmó?
- ¿Qué decisión metodológica te costó más de lo que merecía?

---

## Auditoría de primera persona (decisión por caso)

| # | Caso | Decisión | Justificación |
|---|------|----------|---------------|
| 1 | §1.1 "la distinción no la tomé de un manual, la reconstruí al notar..." | NEUTRALIZAR | Afirmaba experiencia subjetiva (proceso mental de descubrimiento) no verificable. Reemplazado por formulación neutra en tercera persona. |
| 2 | §1.9 "No planifiqué los ocho experimentos... la reconstruí después..." | NEUTRALIZAR (sobrio) | El contenido es objetivamente verificable (la estructura del repositorio muestra que la metodología se reconstruye a posteriori), pero la primera persona era innecesaria. Reescrito en tercera persona manteniendo el contenido verificable. |

**No se detectaron otras afirmaciones autobiográficas** en el documento. Todas las decisiones, veredictos y condiciones están formulados en tercera persona o construidos sobre evidencia numérica verificable.
