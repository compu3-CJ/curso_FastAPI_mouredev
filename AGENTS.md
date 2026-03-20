# AGENTS.md - Curso FastAPI

## Descripción del Proyecto

Este es un proyecto de curso de FastAPI. Contiene ejemplos básicos de endpoints API,
modelos Pydantic, parámetros path/query, y configuración para desarrollo en equipo
usando OpenCode.

---

## Comandos de Ejecución

### Servidor FastAPI (Desarrollo)
```bash
uvicorn main2:app --reload
uvicorn path_query:app --reload
uvicorn users2_class:app --reload
```

### Gestión de Dependencias (Conda)
```bash
conda install -c conda-forge fastapi pydantic uvicorn
pip install fastapi pydantic uvicorn
```

### Instalación de Herramientas de Testing
```bash
pip install pytest pytest-asyncio httpx
```

---

## Comandos de Testing

### Ejecutar Tests
```bash
pytest                    # Ejecutar todos los tests
pytest tests/             # Directorio específico
pytest -v                 # Modo verbose
pytest -v --tb=short      # Con traceback corto
pytest -k "test_name"     # Filtrar por keyword
```

### Ejecutar un Solo Test
```bash
pytest tests/test_api.py::test_endpoint -v
pytest -k "test_users" -v
```

### Cobertura de Tests
```bash
pytest --cov=. --cov-report=html
pytest --cov=. --cov-report=term-missing
```

---

## Code Style - Convenciones del Proyecto

### Imports
```python
# 1. Stdlib
from typing import Optional, List

# 2. Third-party
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 3. Local (nunca hacer import relativo)
from app.models import User
```

### Type Hints (OBLIGATORIO)
```python
# Correcto
def search_user(id: int) -> dict:
    ...

async def get_user(user_id: int) -> User:
    ...

# Incorrecto (evitar)
def search_user(id):
    ...
```

### Nomenclatura
| Elemento | Convención | Ejemplo |
|----------|------------|---------|
| Funciones | `snake_case` | `get_user_by_id` |
| Variables | `snake_case` | `users_list` |
| Clases | `PascalCase` | `class User(BaseModel)` |
| Constantes | `SCREAMING_SNAKE` | `MAX_RETRIES = 3` |
| Módulos | `snake_case` | `path_query.py` |

### Pydantic Models
```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
```

### Endpoints Async
```python
@app.get("/users/{user_id}")
async def get_user(user_id: int) -> User:
    return search_user(user_id)
```

### Comentarios
- **Español** para contexto local y documentación del código
- **Inglés** para funciones/métodos exportables
- Evitar comentarios innecesarios que expliquen el "qué"

---

## Manejo de Errores

### Correcto - Usar HTTPException
```python
from fastapi import HTTPException

def search_user(id: int) -> User:
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")
```

### Incorrecto - Evitar Bare Except
```python
# MAL - Nunca usar
try:
    return list(users)[0]
except:
    return {"error": "Usuario no valido"}

# BIEN - Especificar el tipo de excepción
try:
    return list(users)[0]
except IndexError:
    raise HTTPException(status_code=404, detail="User not found")
```

### Validación con Pydantic
```python
from fastapi import HTTPException, status

@app.post("/users/")
async def create_user(user: User):
    if user.age < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Age cannot be negative"
        )
    return user
```

---

## Estructura de Archivos

```
Curso_FastAPI/
├── main2.py              # Endpoint raíz básico
├── path_query.py         # Parámetros path y query
├── users2_class.py        # Modelos Pydantic y listas
├── post.py               # (en desarrollo - POST endpoints)
├── .agents/              # Skills OpenCode para el equipo
├── skills-lock.json      # Configuración de skills
└── .gitignore            # Archivos ignorados
```

---

## Git Conventions

Ver `.agents/skills/git-commit/SKILL.md` para convenciones completas.

### Formato de Commits
```
<tipo>[opcional_scope]: <descripción>

Tipos permitidos:
- feat: Nueva funcionalidad
- fix: Corrección de bug
- docs: Documentación
- style: Formato (sin lógica)
- refactor: Refactorización
- test: Tests
- build: Build/dependencias
- chore: Mantenimiento
```

### Reglas de Seguridad Git
- NUNCA hacer commit de secrets (`.env`, credenciales)
- NUNCA usar `--force` en push
- NUNCA hacer `hard reset` sin autorización expresa
- Commits atómicos: un cambio lógico por commit

---

## Recursos

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Uvicorn Docs](https://www.uvicorn.org/)
