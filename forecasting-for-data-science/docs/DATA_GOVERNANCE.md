# Gobierno de datos

## Procedencia

Cada producto tiene un receipt JSON con URL, bytes y SHA-256 de la fuente, timestamp UTC, SHA-256 de salida, esquema, filas, nulos y limpieza. `MANIFEST.sha256` cubre todos los archivos del release.

## Restricciones

- Ninguna fuente supera 500 MiB; el helper aplica el límite durante streaming.
- No se usan Kaggle ni credenciales.
- `raw/` es temporal y no se empaqueta.
- La licencia MIT cubre código/documentación propios; cada dataset conserva sus términos.

## Política de cambios

No imputar, deduplicar, agregar ni inventar fechas silenciosamente. Todo cambio requiere actualizar script, ficha, `registry.yaml`, tests, receipt y manifiesto. Para datos extensos use procesamiento por bloques o una estimación explícita de memoria.

## Checklist de release

1. Ejecutar `download_all.py` y `clean_data.py`.
2. Validar shapes, hashes, nulos y claves.
3. Ejecutar tests.
4. Eliminar fuentes temporales/cachés.
5. Regenerar `MANIFEST.sha256` y comprobar el ZIP.
