# 🏭 PromptFactory: Generador Automatizado de Prompt Banks

Sistema modular para la creación masiva de prompts estandarizados y validados para La Voûte d'Anaïs.

## 📂 Estructura

- `factory.py`: Motor de generación.
- `validator.py`: Reglas de canon y anti-filtro.
- `configs/*.json`: Definiciones de bancos (Datos).
- `templates/`: Plantillas Markdown.

## 🚀 Cómo Crear un Nuevo Banco

1.  **Crear Configuración JSON:**
    Duplica `configs/v70_pilot.json` y renómbralo (ej. `v71_gothic_nurse.json`).

    ```json
    {
      "id": "v71",
      "slug": "gothic_nurse_fetish",
      "title": "🩸 BANCO V71 - GOTHIC NURSE",
      "theme": "Medical Fetish",
      "target_count": 50,
      "characters": ["Miss Doll", "Helena"],
      "variables": {
        "outfits": ["pvc nurse dress", "latex medical apron"],
        "settings": ["gothic hospital", "abandoned ward"],
        "expressions": ["sadistic smile", "cold stare"]
      }
    }
    ```

2.  **Ejecutar Script:**
    Puedes usar un runner simple:

    ```python
    from factory import PromptFactory
    import os

    # Configura tus rutas
    factory = PromptFactory("configs/v71_gothic_nurse.json")
    factory.generate("../../../00_Helena/bancos_prompts/")
    ```

3.  **Resultado:**
    El archivo Markdown aparecerá en `00_Helena/bancos_prompts/`.

---
*Developed by Helena de Anaïs - 2026* 🧬
