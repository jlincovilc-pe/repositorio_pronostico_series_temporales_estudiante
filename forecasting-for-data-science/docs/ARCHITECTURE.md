# Arquitectura del repositorio

## Flujo de datos

```text
URLs públicas / Zenodo
        │
        ▼
scripts/download_all.py ── límite 500 MiB, SHA-256 ──► raw/ temporal
        │
        ▼
scripts/clean_data.py ── validación y transformación ──► data/<dataset>/*.csv
        │                                                   │
        │                                                   ├─ README.md
        │                                                   └─ *.receipt.json
        ▼
scripts/validate_repository.py + tests/ ──► notebooks/ ──► release ZIP
```

## Componentes

- `registry.yaml`: inventario machine-readable de datasets, productos, frecuencia, target y covariables.
- `scripts/_common.py`: descarga streaming con límite, `sha256()` y escritura de receipts.
- `download_all.py`: descarga las ocho fuentes a `raw/`.
- `clean_data.py`: transforma las fuentes en nueve CSV reproducibles.
- `run_notebooks.py`: ejecución selectiva o completa con `nbclient`.
- `validate_repository.py`: verifica hashes, tamaños y contratos de paneles grandes.
- `tests/`: contratos de datos y notebooks.
- `MANIFEST.sha256`: integridad de todos los archivos del release.

## Capas

- **Raw:** reproducible, temporal, excluida del release.
- **Curated:** CSV incluidos y versionados en el artefacto.
- **Analysis:** notebooks ejecutados con outputs.
- **Governance:** receipts, registry, tests, manifiesto y documentación.

## Decisiones de escala

Electricity está en formato long para modelos globales. PeMS permanece ancho para evitar 61 millones de filas long. OPSD conserva todas las columnas alemanas. Estas decisiones están documentadas y pueden cambiar el coste de I/O, no la fuente original.
