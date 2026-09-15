# Plan de migración a GitHub (Windows / Linux / macOS)

> **Estado: PUBLICADO.** Las 8 fases están completas. Repositorio en
> https://github.com/jlincovilc-pe/repositorio_pronostico_series_temporales_estudiante
> (público), CI en verde en Ubuntu/Windows/macOS, verificado con un clon
> limpio. Ver sección 4 para el registro completo de lo ejecutado.

Este documento define el plan para convertir el directorio actual (todavía sin
`git init`) en un repositorio de GitHub que, al clonarse en cualquiera de las
tres plataformas, funcione siguiendo el [`README.md`](README.md) tal como está
escrito hoy.

Se basa en una auditoría del estado real del directorio (tamaños, `git
status`, enlaces del README contra archivos en disco). Los hallazgos concretos
están en la sección 1; el plan de acción en la sección 2.

---

## 1. Diagnóstico

### 1.1 Bloqueante: el repo pesa ~6,7 GB y no existe `.gitignore`

| Carpeta/archivo | Tamaño | Problema |
|---|---|---|
| `forecasting-for-data-science/.venv/` | 5,6 GB | Entorno virtual local. Nunca debe versionarse. |
| `forecasting-for-data-science/data/05_electricity/electricity_long.csv` | 404 MB | Supera el límite duro de GitHub de **100 MB por archivo** (rechaza el push). **Decisión: excluir del repo, regenerar con `make download && make clean`.** |
| `forecasting-for-data-science/data/07_traffic_pems/traffic_pems.csv` | 409 MB | Igual que arriba. **Misma decisión.** |
| `forecasting-for-data-science/data/` (resto) | ~30 MB | Sin problema de tamaño. |
| `.pytest_cache/`, `.benchmarks/`, `tests/__pycache__/`, `notebooks/.ipynb_checkpoints/` | pequeño | Artefactos generados, no deben versionarse. |
| `html_presentation/monografia_interactiva.pre-unificacion.bak.html` | — | Archivo de respaldo, candidato a excluir o eliminar. |

No hay ningún `.gitignore` en el árbol (`find . -iname .gitignore` no devuelve
nada). Si se hace `git add .` tal cual, el primer push falla o crea un
repositorio inutilizable de varios GB.

### 1.2 Enlaces rotos en `README.md` (fallarán en Linux/macOS, sensibles a mayúsculas)

Confirmado contra el árbol real:

| Referencia en el README | Ruta real en disco | Impacto |
|---|---|---|
| `Silabo/silabo.pdf` (mapa de carpetas, TOC #7, tabla final) | `silabo/silabo.pdf` (minúscula) | Roto en Linux/macOS (case-sensitive). En Windows "funciona" por accidente, lo que esconde el bug hasta que alguien clona en Mac/Linux. |
| `Forecasting_monograph/output.pdf` | `Forecasting_monograph/monografia_timeseries_benchmarks.pdf` | El archivo `output.pdf` no existe con ese nombre; el enlace apunta a nada. |
| `html_presentations/html_1/1.html` | `html_presentation/monografia_interactiva.html` (carpeta en singular, sin subcarpeta `html_1`) | Enlace roto: ni el nombre de carpeta ni la estructura de subcarpetas existen. |
| Ancla del TOC `#presentaciones-html-html_presentations` | El encabezado real genera el ancla `#presentaciones-html-html_presentation` (singular) | El enlace de tabla de contenidos no salta a la sección en GitHub. |

Estos son bugs reales de contenido, no solo de "portabilidad" — hay que
corregirlos independientemente del destino (GitHub u otro).

### 1.3 Contenido inconsistente: `Forecasting_monograph/CONFIGURACION_TYPST.md`

Este archivo describe una estructura de carpetas (`02_monografia/`,
`07_diapositivas/`) y un curso (*"IA Causal en Producción", ECO-490/ECON-540*)
que **no existen en este repositorio**. Parece contenido copiado de otro
proyecto Typst. Hay que decidir si se reescribe para reflejar
`Forecasting_monograph/monografia_timeseries_benchmarks.typ` y
`presentacion_monografia.typ`, o se elimina.

### 1.4 Licencia

Solo existe `LICENSE` (MIT) dentro de `forecasting-for-data-science/`. El
README ya aclara que esa MIT cubre "el código, la documentación original y la
estructura de `forecasting-for-data-science/`" y que los demás datasets
conservan sus licencias de origen (UCI CC BY 4.0, OPSD, M3). Falta decidir si
el repositorio en su conjunto (monografía, sílabo, presentaciones, mapas JSON,
marco de calidad) necesita una licencia raíz explícita — GitHub no detecta
licencia automáticamente si solo vive en una subcarpeta.

### 1.5 Tres subcarpetas tenían su propio repo git anidado — **resuelto**

Se encontraron **tres** `.git` independientes, ninguno con remoto
configurado:

| Carpeta | Commits | Estado |
|---|---|---|
| `Forecasting_monograph/.git` | 5+ (rama `master`) | Working tree con cambios sin commitear |
| `forecasting-for-data-science/.git` | 1 ("Estado inicial versionado...") | Working tree limpio |
| `json_maps/.git` | 1 ("Estado inicial versionado...") | Working tree limpio |

Si se hubiera ejecutado `git init` en la raíz sin resolver esto, git habría
tratado cada carpeta como un **gitlink/submódulo roto**: su contenido habría
quedado fuera del commit de la raíz de forma silenciosa (sin error visible
en `git status`, solo una entrada de modo `160000` sin submódulo real
declarado).

**Acción tomada:** se revisó que ninguno tuviera remoto ni historial que
valiera la pena preservar aparte, y se eliminaron los tres con
`rm -rf Forecasting_monograph/.git forecasting-for-data-science/.git
json_maps/.git`. Verificado que no queda ningún `.git` anidado. El único
repositorio git para todo el árbol será el que se cree en la raíz (Fase 5).

### 1.6 Fuentes Typst: no se comparten, solo los PDF compilados

Decisión del autor: los `.typ` (fuente editable) no se suben al repo
público; solo los PDF ya compilados. Archivos `.typ` existentes:

- `silabo/silabo.typ`
- `silabo/criterios_calificacion.typ`
- `Forecasting_monograph/monografia_timeseries_benchmarks.typ`
- `Forecasting_monograph/presentacion_monografia.typ`

**Decidido: también se excluyen** los archivos relacionados que dependen de
esas fuentes: `Forecasting_monograph/assets/_make_figure.py` y
`_make_map.py` (generan las imágenes que consume el `.typ`),
`edit_mon.json` / `edit_presentation.json` (bitácoras editoriales del
proceso de edición del `.typ`), `CONFIGURACION_TYPST.md` (documenta cómo
compilar esas fuentes — ya señalado en 1.3 como contenido de otro proyecto,
y ahora además sin fuente que configurar), y los exports alternativos
`monografia_timeseries_benchmarks.html` / `.txt` (renders del mismo `.typ`,
no son el PDF final). En `Forecasting_monograph/` solo quedan versionados:
`monografia_timeseries_benchmarks.pdf`, `presentacion.pdf`, `README.md` y
`AUTOR_VOICE.md` (contexto de autor, no fuente de compilación). En
`silabo/` solo quedan `silabo.pdf` y `criterios_calificacion.pdf`.

### 1.7 Lo que ya funciona bien (no tocar)

- Todos los scripts (`scripts/*.py`) usan `pathlib` y no tienen rutas
  hardcodeadas de Linux/Windows/Mac (`grep` no encontró `C:\`, `/home/`,
  `/Users/`, `os.name`, `sys.platform`).
- `docs/INSTALLATION.md` y el README raíz ya documentan la activación de
  entorno para PowerShell (`.venv\Scripts\Activate.ps1`) y la instalación de
  PyTorch por plataforma.
- `.python-version` (3.11) con rango soportado 3.10–3.13 en
  `requirements.txt`, razonable para las tres plataformas.
- El diseño ya separa capa RAW (regenerable vía `scripts/download_all.py`,
  con licencias por fuente) de capa CURATED (CSV incluidos), lo cual es
  exactamente lo necesario para decidir qué versionar.

---

## 2. Plan de acción

### Fase 0 — Decisiones previas

1. **Nombre, owner y visibilidad del repo en GitHub** — **decidido**: nombre
   `repositorio_pronostico_series_temporales_estudiante` (igual que la
   carpeta local, sin renombrar), owner `jlincovilc-pe`
   (https://github.com/jlincovilc-pe), visibilidad **pública**.
2. **Manejo de los dos CSV >100 MB** — **decidido**: se excluyen del repo
   (`data/05_electricity/electricity_long.csv`,
   `data/07_traffic_pems/traffic_pems.csv`). No se usa Git LFS: para un
   repo de curso clonado repetidamente por compañeros/profesor, la cuota
   gratuita de LFS (1 GB/mes) se agota en 2-3 clones. En su lugar se
   regeneran bajo demanda con `make download && make clean` antes de
   trabajar las semanas 5 (electricidad) y 7 (PeMS). El resto de `data/`
   (7 CSV, ~30 MB) sí se versiona normal, así que 6 de 8 semanas siguen
   siendo "clonar y estudiar sin internet" tal como promete el README; solo
   semanas 5 y 7 requieren un `make download` puntual.
3. **Fuentes Typst (`.typ`)** — **decidido**: no se comparten. Solo se
   versionan los PDF compilados (`silabo.pdf`, `criterios_calificacion.pdf`,
   `monografia_timeseries_benchmarks.pdf`, `presentacion.pdf`). Ver detalle
   en 1.6.
4. **Licencia raíz** — **decidido**: se extiende MIT a todo el repositorio
   (raíz), con una nota explícita en el README de que los datasets
   (`forecasting-for-data-science/data/`) conservan sus licencias de origen
   (UCI CC BY 4.0, términos OPSD, términos M3) y no quedan cubiertos por la
   MIT del código.

### Fase 1 — Limpieza de artefactos generados

- Eliminar (o dejar fuera del control de versiones) `.venv/`,
  `.pytest_cache/`, `.benchmarks/`, `**/__pycache__/`,
  `notebooks/.ipynb_checkpoints/`.
- Decidir si `html_presentation/monografia_interactiva.pre-unificacion.bak.html`
  se conserva (¿tiene valor histórico?) o se borra.
- Revisar `forecasting-for-data-science/MANIFEST.sha256`: una vez limpio el
  árbol, regenerarlo con `make manifest` para que los hashes coincidan con lo
  que realmente se publica.

### Fase 2 — `.gitignore` y `.gitattributes`

- Crear `.gitignore` en la raíz cubriendo: `.venv/`, `__pycache__/`,
  `*.pyc`, `.pytest_cache/`, `.benchmarks/`, `.ipynb_checkpoints/`,
  `.DS_Store` (macOS), `Thumbs.db` (Windows), `*.swp`, cualquier `raw/`
  temporal que generen `scripts/download_all.py` / `clean_raw.py`, y
  explícitamente las dos rutas excluidas por tamaño:
  `data/05_electricity/electricity_long.csv` y
  `data/07_traffic_pems/traffic_pems.csv` (dejar el resto de `data/`
  versionado normal); y las fuentes Typst y sus archivos relacionados,
  excluidos por decisión editorial (ver 1.6): `silabo/*.typ`,
  `Forecasting_monograph/*.typ`, `Forecasting_monograph/assets/*.py`,
  `Forecasting_monograph/edit_mon.json`,
  `Forecasting_monograph/edit_presentation.json`,
  `Forecasting_monograph/CONFIGURACION_TYPST.md`,
  `Forecasting_monograph/monografia_timeseries_benchmarks.html`,
  `Forecasting_monograph/monografia_timeseries_benchmarks.txt`.
  Nota: si `assets/*.py` se excluye, las imágenes `assets/*.png` que
  generan también quedan sin uso en el repo público (ya están incrustadas
  en el PDF compilado) — excluirlas también salvo que se quieran como
  material aparte.
- Crear `.gitattributes` con `* text=auto eol=lf` para normalizar finales de
  línea entre Windows/Linux/macOS (evita diffs falsos y problemas de hashing
  en `MANIFEST.sha256` si alguien clona con `core.autocrlf=true`).
- No se necesita Git LFS (ver decisión en Fase 0.2).

### Fase 3 — Corregir el contenido roto (independiente de GitHub)

- `README.md`: `Silabo/` → `silabo/` (mapa de carpetas, TOC, tabla final);
  `output.pdf` → `monografia_timeseries_benchmarks.pdf`;
  `html_presentations/html_1/1.html` → `html_presentation/monografia_interactiva.html`;
  corregir el ancla del TOC de la sección de presentaciones HTML.
- Añadir un enlace de verificación de enlaces al `Makefile` o a CI (fase 6)
  para que este tipo de bug no vuelva a colarse silenciosamente.
- Eliminar `Forecasting_monograph/CONFIGURACION_TYPST.md`: ya estaba
  marcado como contenido de otro proyecto (1.3), y al no compartirse las
  fuentes `.typ` (1.6) no queda nada que documentar ahí.
- Actualizar el "Mapa de carpetas" del README raíz: quitar
  `monografia_timeseries_benchmarks.typ` y `presentacion_monografia.typ` de
  la entrada de `Forecasting_monograph/` (dejar solo los `.pdf`), y quitar
  `silabo.typ` / `criterios_calificacion.typ` de la entrada de `silabo/`
  (dejar solo los `.pdf`). Revisar también `Forecasting_monograph/README.md`
  y `silabo/` si mencionan cómo recompilar desde `.typ` — aclarar que las
  fuentes no forman parte del repo público.
- **Decidido:** también se excluyen los archivos relacionados listados en
  1.6 (`assets/_make_figure.py`, `_make_map.py`, `edit_mon.json`,
  `edit_presentation.json`, `CONFIGURACION_TYPST.md`, los exports
  `.html`/`.txt` de la monografía).
- Ajustar el README raíz y `forecasting-for-data-science/README.md`/
  `docs/INSTALLATION.md` para reflejar la exclusión de los dos CSV grandes:
  la frase "No hace falta descargar fuentes... para estudiar" debe matizarse
  a "...salvo para las semanas 5 y 7, que requieren `make download && make
  clean` una vez (~813 MB, requiere internet)". También actualizar el
  `registry.yaml`/`MANIFEST.sha256` y el inventario de datos del README si
  listan tamaños o presencia de esos CSV como "incluidos".

### Fase 4 — Licencia y atribución

- Añadir `LICENSE` en la raíz (o symlink/copia de la MIT existente) según lo
  decidido en fase 0.3, y una nota breve en el README raíz sobre qué cubre y
  qué no (ya existe texto parecido en "Licencia, atribución y citas"; solo
  falta que apunte a un archivo real en la raíz).

### Fase 5 — Inicializar git y primer commit

**Paso previo ya ejecutado:** los tres `.git` anidados
(`Forecasting_monograph/`, `forecasting-for-data-science/`, `json_maps/`,
hallazgo 1.5) fueron revisados (sin remoto, sin historial que preservar) y
eliminados. Verificado que no queda ningún `.git` fuera de la raíz.

```bash
cd /home/enrique/Escritorio/repositorio_pronostico_series_temporales_estudiante
git init
git add .gitignore .gitattributes
git add -A   # revisar con `git status` antes de commitear, según fases 1-4
git status | grep -i "160000\|submodule"   # confirmar que no quedó ningún gitlink
git commit -m "Initial commit"
```

Si se usa Git LFS: `git lfs install` antes del primer `git add` de los CSV
grandes, y verificar con `git lfs ls-files` que quedaron trackeados por LFS
antes de hacer commit.

### Fase 6 — Integración continua multiplataforma

Añadir `.github/workflows/tests.yml` con matriz
`os: [ubuntu-latest, windows-latest, macos-latest]` × Python 3.10–3.13 (o al
menos 3.11) que ejecute, dentro de `forecasting-for-data-science/`:

```bash
python -m pip install -r requirements.txt
python scripts/validate_repository.py
python -m pytest -q
```

Esto es la única forma real de confirmar "funciona en Windows/Linux/Mac" sin
tener las tres máquinas a mano — GitHub Actions las provee. Si el job de
Windows o macOS falla (p. ej. por `lightgbm`/`torch` sin wheel para alguna
combinación de versión), se ajusta el rango en `requirements.txt` o se
documenta la excepción en `docs/TROUBLESHOOTING.md`.

### Fase 7 — Crear el repo remoto y publicar

```bash
gh repo create jlincovilc-pe/repositorio_pronostico_series_temporales_estudiante \
  --public --source=. --remote=origin
git push -u origin master
```

(Requiere confirmación explícita antes de ejecutarse — es una acción visible
y no trivialmente reversible.)

### Fase 8 — Verificación post-publicación

- Clonar el repo recién creado en una carpeta limpia (`git clone` fresco, no
  el directorio de trabajo actual) y seguir exactamente los pasos de
  "Inicio rápido" del README, para confirmar que una persona nueva puede
  reproducirlo.
- Confirmar que los tres jobs de CI (Fase 6) pasan en verde.
- Revisar en la interfaz de GitHub que los enlaces corregidos (Fase 3)
  resuelven correctamente (README se renderiza con rutas relativas).
- Confirmar que, tras el clon limpio, `make download && make clean`
  reconstruye correctamente `electricity_long.csv` y `traffic_pems.csv`
  antes de ejecutar los notebooks de las semanas 5 y 7, y que
  `validate_repository.py`/`pytest` siguen pasando con esos archivos
  regenerados (no solo con los que estaban versionados).

---

## 4. Registro de ejecución

Ejecutado en esta sesión, en orden:

1. **Fase 1–2 (limpieza + `.gitignore`/`.gitattributes`):** creados en la
   raíz. `.venv/`, cachés, los 2 CSV grandes, las fuentes `.typ` y archivos
   editoriales asociados, y el `.bak.html` quedan fuera del control de
   versiones (no se borraron del disco, solo se excluyeron).
2. **Fase 3 (contenido):** corregidos los enlaces rotos del README raíz
   (`Silabo/`→`silabo/`, `output.pdf`→nombre real, `html_presentations/
   html_1/1.html`→`html_presentation/monografia_interactiva.html`, ancla del
   TOC), eliminado `Forecasting_monograph/CONFIGURACION_TYPST.md`,
   reescritas las tablas de `Forecasting_monograph/README.md` y las
   secciones correspondientes del README raíz para no listar archivos que
   ya no se publican, y añadido el matiz sobre los 2 CSV grandes en el
   README raíz y en `forecasting-for-data-science/README.md`.
3. **Hallazgo adicional no previsto en el plan original:** el "contrato de
   autocontenido" no era solo texto de README — estaba codificado como
   `assert` duro en `scripts/validate_repository.py` y en
   `tests/test_repository.py` (exigían los 9 CSV siempre presentes). Se
   confirmó con el autor y se modificaron ambos archivos (más
   `scripts/build_manifest.py` y una constante compartida
   `OPTIONAL_LARGE_DATASETS` en `scripts/_common.py`) para que los dos
   datasets grandes sean opcionales y regenerables sin romper `make
   validate` / `pytest -q` en un clon nuevo. Verificado localmente
   simulando su ausencia (se movieron a `/tmp`, se corrió la suite, se
   restauraron).
4. **Bug adicional encontrado y corregido:** `build_manifest.py` no excluía
   `.venv/` de su barrido (`ROOT.rglob("*")`), así que el primer
   `MANIFEST.sha256` regenerado tenía 39,131 entradas (39,067 del `.venv`
   local). Corregido para excluir también `.venv`, `.benchmarks` y
   `.ipynb_checkpoints`; el manifest regenerado quedó en 63 archivos.
5. **Fase 4 (licencia):** creado `LICENSE` (MIT) en la raíz, README raíz
   actualizado para apuntar ahí.
6. **Fase 5 (git init):** revisados y eliminados los tres `.git` anidados
   (ver 1.5), `git init` en la raíz, `git add -A`. Verificado que no hay
   gitlinks/submódulos rotos, que ningún archivo excluido quedó incluido
   (`git ls-files` no devuelve `.venv/`, los 2 CSV grandes, `.typ`, JSON
   editoriales, cachés ni el `.bak.html`), y que el total a commitear es
   ~49 MB con el archivo individual más grande en 15 MB (`germany_energy.csv`)
   — muy por debajo del límite de 100 MB de GitHub.
7. **Fase 6 (CI):** creado `.github/workflows/ci.yml` en la raíz (matriz
   `ubuntu-latest` / `windows-latest` / `macos-latest`, Python 3.11,
   `pip install -r requirements.txt` → `validate_repository.py` → `pytest
   -q`, todo dentro de `forecasting-for-data-science/`). Se corrigió
   `tests/test_documentation.py::test_operational_helpers_exist`, que
   comprobaba la existencia de `.github/workflows/ci.yml` **dentro** de
   `forecasting-for-data-science/` (herencia de cuando esa carpeta era su
   propio repo con `.git` — hallazgo 1.5); ahora comprueba la ruta real en
   la raíz del monorepo, que es la única que GitHub Actions ejecuta.
8. **Verificación local final:** `python scripts/validate_repository.py` y
   `python -m pytest -q` (13 tests) pasan limpio con los 9 CSV presentes en
   disco y con los 2 grandes ausentes (simulado). `git status` queda limpio
   tras el `add -A` salvo el commit pendiente.

9. **Commit inicial:** identidad configurada localmente
   (`git config user.name "jlincovilc-pe"`, email noreply de GitHub
   `260700074+jlincovilc-pe@users.noreply.github.com`, decidido con el
   autor). Commit `bb2b25b` creado.
10. **Autenticación GitHub:** `gh` CLI instalado y autenticado como
    `jlincovilc-pe` (scopes `repo`, `read:org`, `gist`) vía
    `gh auth login --web` (flujo de device code, confirmado por el autor en
    el navegador).

11. **Fase 7 (publicar):** `gh` CLI instalado, autenticado como
    `jlincovilc-pe` vía `gh auth login --web` (device code, confirmado por
    el autor en el navegador). Repo creado con `gh repo create` (público).
    Primer intento de `git push` rechazado por GitHub: el token no tenía el
    scope `workflow`, necesario para subir `.github/workflows/ci.yml`
    (protección estándar de GitHub contra apps que modifican Actions sin
    permiso explícito). Se pidió el scope adicional con `gh auth refresh -s
    workflow` (segunda autorización por device code, confirmada por el
    autor) y el push se completó.
12. **Bug encontrado post-push:** el workflow de CI (`.github/workflows/
    ci.yml`) estaba configurado para disparar en la rama `main`, pero
    `git init` había creado la rama como `master` — nunca se ejecutó tras
    el primer push. Corregido (`branches: [master]`), commiteado y
    empujado.
13. **Fase 6/8 (CI + verificación):** los tres jobs de la matriz
    (`ubuntu-latest`, `windows-latest`, `macos-latest`, Python 3.11)
    corrieron y pasaron en verde (`validate_repository.py` + `pytest -q`,
    13 tests) — confirmación real de que el repo funciona en las tres
    plataformas, no solo una afirmación del README.
14. **Fase 8 (verificación con clon limpio):** `gh repo clone` a un
    directorio temporal: 68 MB, 89 archivos, los dos CSV grandes ausentes
    (solo sus `.receipt.json`), y los cuatro enlaces corregidos
    (`silabo/silabo.pdf`, `Forecasting_monograph/
    monografia_timeseries_benchmarks.pdf`, `html_presentation/
    monografia_interactiva.html`, `LICENSE`) resuelven a archivos reales.
    Clon temporal eliminado tras la verificación.

**Repositorio publicado:**
https://github.com/jlincovilc-pe/repositorio_pronostico_series_temporales_estudiante

---

## 3. Orden recomendado de ejecución

1. Fase 0 (decisiones) — **necesito tu respuesta antes de tocar nada**.
2. Fases 1–4 (limpieza y fixes de contenido) — se pueden hacer ya, son
   reversibles y no dependen de las decisiones de la fase 0 salvo el punto
   de los CSV grandes.
3. Fase 5 (`git init` + commit) — una vez limpio el árbol.
4. Fase 6 (CI) antes de la Fase 7, para no publicar un repo roto.
5. Fase 7 (publicar) — solo con tu confirmación explícita del nombre/
   visibilidad del repo.
6. Fase 8 (verificación).
