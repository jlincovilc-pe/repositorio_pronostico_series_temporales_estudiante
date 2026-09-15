# Troubleshooting y FAQ

## `MemoryError` o kernel muerto

Cierre otros kernels. No cargue Electricity completo; use `chunksize`. En PeMS seleccione columnas. Se recomiendan 16 GiB RAM para semanas 5–7.

## Notebook 7 tarda demasiado

Es el notebook más costoso (~10 min en la máquina de construcción). Reduzca épocas para exploración, pero documente el cambio. GPU es opcional; los outputs entregados son CPU.

## No encuentro los datos

Ejecute Jupyter desde la raíz. Los notebooks prueban `data/...` y `../data/...`. Valide con `python scripts/validate_repository.py`.

## Fallan los hashes después de editar

Es esperado. Los hashes protegen el release. Tras un cambio legítimo ejecute tests y regenere `MANIFEST.sha256` con el script de release o la receta de gobierno.

## `raw/` ocupa mucho

```bash
make clean-raw
```

Elimina solo fuentes descargadas, no CSV curados.

## PyTorch no instala

Compruebe Python y plataforma. Use el selector oficial de PyTorch para instalar una build CPU o CUDA compatible. GPU no es necesaria.

## DeepAR no aparece

Es una extensión opcional no ejecutada. Notebook 8 conserva una especificación honesta sin métricas fabricadas.

## ¿Por qué PeMS no tiene fechas?

La distribución UCI incluida no entrega calendario completo. El notebook usa posiciones y etiquetas de día sin fabricar timestamps.

## ¿Los notebooks guardan modelos?

No. Guardan outputs dentro del `.ipynb`. Para serving, añada explícitamente serialización, model registry y validación de artefactos.
