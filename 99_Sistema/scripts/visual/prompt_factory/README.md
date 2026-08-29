# 🏭 PromptFactory — Generador de Bancos Temáticos de Prompts

*Última actualización: 29/08/2026 — el ejemplo de configuración nombraba a **Helena**, la era retirada (hoy es Ele). Aclarado además qué relación tiene con el `outfit-engine`, que no es la misma herramienta.*

Sistema modular para crear **bancos temáticos** de prompts en `00_Ele/bancos_prompts/` (74 bancos · 5.032 prompts, medido 29/08/2026).

> ⚠️ **Esto NO es el motor de looks.** Un *banco* es una colección temática exploratoria; un *look* es una pieza de la flota canónica con sus 7 poses, su ADN bloqueado y sus anclas anti-defecto. Los looks se generan **solo** con [`../outfit.py`](../outfit.py) desde un JSON de `batches/` — nunca desde aquí, y nunca a mano.

## 📂 Estructura

- `factory.py`: Motor de generación.
- `validator.py`: Reglas de canon y anti-filtro.
- `configs/*.json`: Definiciones de bancos (Datos).
- `templates/`: Plantillas Markdown.

## 🚀 Cómo Crear un Nuevo Banco

1.  **Crear Configuración JSON:**
    Duplica `configs/v70_pilot.json` (o el más reciente, `config_v77_miss_doll_escort.json`) y renómbralo (ej. `v71_gothic_nurse.json`).

    ```json
    {
      "id": "v71",
      "slug": "gothic_nurse_fetish",
      "title": "🩸 BANCO V71 - GOTHIC NURSE",
      "theme": "Medical Fetish",
      "target_count": 50,
      "characters": ["Miss Doll", "Ele"],
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
