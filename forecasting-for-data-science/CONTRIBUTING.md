# Contribuir

Gracias por mejorar el curso. Mantenga trazabilidad y compatibilidad con los notebooks existentes.

## Desarrollo

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/validate_repository.py
python -m pytest -q
```

## Flujo recomendado

1. Cree una rama descriptiva.
2. Modifique el componente mínimo necesario.
3. Si cambia datos, actualice descargador, limpieza, receipt, ficha, registry y tests.
4. Si cambia un notebook, reinicie kernel, ejecute todas las celdas y confirme ausencia de errores.
5. Actualice documentación y changelog.
6. Ejecute `make validate` y `make manifest`.

## Reglas de integridad

- No incluya credenciales ni use Kaggle.
- Ninguna fuente individual debe superar 500 MiB.
- No impute, deduplique, agregue ni fabrique timestamps sin documentar la decisión.
- No use random split para estimar forecasting.
- No reporte resultados de modelos no ejecutados.
- Mantenga funciones propias con type hints y código PEP8.

## Pull request

Describa objetivo, archivos cambiados, impacto en datos, tiempo/RAM, tests ejecutados y diferencias numéricas esperadas. Incluya los hashes nuevos cuando corresponda.
