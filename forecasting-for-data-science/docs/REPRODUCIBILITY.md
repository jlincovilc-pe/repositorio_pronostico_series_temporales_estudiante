# Reproducibilidad

## Niveles

1. **Bytes:** receipts y `MANIFEST.sha256` detectan cambios.
2. **Datos:** scripts de descarga y limpieza producen los CSV.
3. **Análisis:** seed 42, splits explícitos y notebooks ejecutados.
4. **Entorno:** dependencias acotadas por rangos; para una cohorte docente genere un lockfile.

## Validar release

```bash
sha256sum -c MANIFEST.sha256
python scripts/validate_repository.py
python -m pytest -q
```

## Reejecutar notebooks

```bash
python scripts/run_notebooks.py --notebook 03
python scripts/run_notebooks.py --all --timeout 1800
```

La ejecución completa usa datos reales y puede generar outputs ligeramente distintos en tiempos y optimización numérica. Las semillas reducen, pero no eliminan, diferencias entre plataformas/BLAS/versiones.

## Política de resultados

No copie métricas fuera de su contexto. Registre commit, hash de dataset, entorno, split, horizonte, features, modelo y métricas. Un resultado nuevo debe compararse bajo el mismo protocolo.
