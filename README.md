# SGICS (IngSw Sección 1)

Integración completa de SonarQube para Backend (Django) y Frontend (Vue + Vite), con tests y Quality Gate en CI. Además, el backend integra Sentry para monitoreo de errores y logging centralizado listo para ELK.

## 0) Instala la extensión recomendada

- Instala sonaqube en VS Code:
  - Este repositorio incluye `.vscode/extensions.json` con recomendaciones.

## 1) Backend: entorno y pruebas

- Usa el intérprete del proyecto (virtualenv):
  - `C:\Users\PC\Desktop\IngSw-seccion1-main\.venv\Scripts\python.exe`
- Instala dependencias desde `backend/`:

```powershell
cd "C:\Users\PC\Desktop\IngSw-seccion1-main\IngSw-seccion1-main\backend"
& "C:\Users\PC\Desktop\IngSw-seccion1-main\.venv\Scripts\python.exe" -m pip install -r requirements.txt
```

- Ejecuta tests con cobertura (respeta el umbral definido en `pytest.ini`):

```powershell
& "C:\Users\PC\Desktop\IngSw-seccion1-main\.venv\Scripts\python.exe" -m pytest --cov=apps --cov=scouts_platform --cov-report=xml:coverage.xml
```

- Variante local sin umbral (para generar `coverage.xml` rápido):

```powershell
& "C:\Users\PC\Desktop\IngSw-seccion1-main\.venv\Scripts\python.exe" -m pytest --cov=apps --cov=scouts_platform --cov-report=xml:coverage.xml --cov-fail-under=0
```

## 2) Frontend: dependencias y pruebas

Desde `frontend/`:

```powershell
cd "C:\Users\PC\Desktop\IngSw-seccion1-main\IngSw-seccion1-main\frontend"
npm ci
npm run test:coverage
```

Vitest genera `coverage/lcov.info`, que SonarQube utilizará.

## 3) Análisis con SonarQube

- Config archivos:
  - Backend: `backend/sonar-project.properties` (usa `coverage.xml`)
  - Frontend: `frontend/sonar-project.properties` (usa `coverage/lcov.info`)
- CI workflow: `.github/workflows/sonarqube.yml`
- Secrets requeridos (en GitHub):
  - `SONAR_HOST_URL` (p.ej. `https://sonarcloud.io` o tu servidor SonarQube)
  - `SONAR_TOKEN`

### (Opcional) Análisis local

Si tienes `sonar-scanner` instalado localmente y variables de entorno configuradas:

```powershell
# Backend
cd "C:\Users\PC\Desktop\IngSw-seccion1-main\IngSw-seccion1-main\backend"
sonar-scanner -Dproject.settings=sonar-project.properties

# Frontend
cd "C:\Users\PC\Desktop\IngSw-seccion1-main\IngSw-seccion1-main\frontend"
sonar-scanner -Dproject.settings=sonar-project.properties
```

## 4) Quality Gate y cobertura

- El umbral de cobertura del backend está en `backend/pytest.ini` (80%).
- En CI, el paso de tests continúa aunque falle la cobertura para que se ejecute igualmente el análisis de SonarQube y el Quality Gate determine el estado final del PR.
- Si prefieres que solo Sonar imponga el gate, puedes bajar el umbral local o quitarlo de `pytest.ini`.

## Estructura relevante

- `.github/workflows/sonarqube.yml` – pipeline de análisis (backend y frontend)
- `backend/sonar-project.properties` – configuración Sonar del backend
- `frontend/sonar-project.properties` – configuración Sonar del frontend
- `.vscode/extensions.json` – extensiones recomendadas (incluye SonarLint)
- `docs/SonarQube.md` – detalles ampliados sobre la configuración

## 5) Monitoreo de errores (Sentry) y logging centralizado

El backend está integrado con Sentry. Se inicializa automáticamente si hay DSN en variables de entorno.

- Variables de entorno relevantes (backend):
  - `SENTRY_DSN` (requerida para activar Sentry)
  - `SENTRY_ENVIRONMENT` (por defecto: `development`)
  - `SENTRY_TRACES_SAMPLE_RATE` (por defecto: `0.0`) – APM/performance sampling
  - `SENTRY_PROFILES_SAMPLE_RATE` (por defecto: `0.0`) – profiling sampling

Dónde está el código:

- Inicialización en `backend/scouts_platform/settings/sentry.py`
- Se invoca desde `backend/scouts_platform/settings/base.py`

Logging para ELK:

- Se generan logs a archivo en `backend/logs/django.log` y a consola.
- Para habilitar formato JSON estructurado (ideal para ELK), exporta `LOG_JSON=true` en el entorno del backend.
- Puedes apuntar tu shipper (Filebeat/Fluent Bit) a esa ruta o a stdout en contenedores.

Frontend (Vue) con Sentry:

- Variables de entorno (Vite):
  - `VITE_SENTRY_DSN` (para activar Sentry en el frontend)
  - `VITE_SENTRY_ENVIRONMENT` (por defecto: `development`)
  - `VITE_SENTRY_TRACES_SAMPLE_RATE` (por defecto: `0.0`)
- Inicialización en `frontend/src/main.ts` (se integra con el router para trazas de navegación).
- Subida de sourcemaps (opcional) con el plugin de Vite, si defines estas variables en el entorno de build:
  - `SENTRY_AUTH_TOKEN`, `SENTRY_ORG`, `SENTRY_PROJECT`
  - El plugin se activa automáticamente solo si están presentes.

## 6) Personas: búsqueda avanzada (API)

Endpoint: `GET /api/persons/search/`

Parámetros de consulta:
- `rut`: string (formateado o parcial)
- `nombre`: string (`icontains`)
- `grupo`: código exacto o parte del nombre del grupo
- `rama`: código exacto (p. ej., `MANADA`, `TROPA`) o parte del nombre
- `edad_min`, `edad_max`: enteros (años)
- `page`, `page_size` (máx. 100)

Respuesta paginada estándar de DRF con `count`, `next`, `previous` y `results`.
