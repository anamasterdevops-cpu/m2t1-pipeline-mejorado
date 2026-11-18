# m2t1-pipeline-mejorado

Parte B de la Tarea 1 del Módulo 2 (Máster en Desarrollo Seguro DevSecOps).

Calculadora en Python (de la Tarea 2) con un pipeline DevOps mejorado:

| Fichero | Qué hace |
|---|---|
| `calculadora.py` | Calculadora: lee `OPERACION`, `NUM1` y `NUM2` de variables de entorno |
| `tests/test_calculadora.py` | Pruebas unitarias con pytest |
| `requirements-dev.txt` | Herramientas de pruebas con versiones fijadas |
| `Dockerfile` | Imagen Alpine con usuario no root |
| `.circleci/config.yml` | Pipeline mejorado de CircleCI (varios jobs) |
| `.github/workflows/ci.yml` | CI con GitHub Actions: lint, tests, cobertura y seguridad |
| `.github/workflows/cd.yml` | CD: construye, escanea con Trivy, prueba y publica la imagen en ghcr.io |

## Uso

```bash
docker run --rm -e OPERACION=suma -e NUM1=40 -e NUM2=2 ghcr.io/anamasterdevops-cpu/m2t1-calculadora:latest
```

## Pipelines

- CircleCI: workflow `pipeline-mejorado` (lint + hadolint → tests → seguridad → docker).
- GitHub Actions: workflows `CI` y `CD` (pestaña *Actions*).
