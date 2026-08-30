import argparse
import os
from datetime import datetime

def generate_ficha(title, project_code, type_story, series, pov, tone, logline, acts):
    template = f"""# 📄 FICHA DE IDEA: {title}
**Código de Proyecto:** {project_code}  
**Estado:** 🌱 Semilla 

---

## 🧬 ADN DEL RELATO
- **Tipo de Relato:** {type_story}
- **Universo/Serie:** {series}
- **Punto de Vista (POV):** {pov}
- **Tono Narrativo:** {tone}

---

## 📸 CONFIGURACIÓN ESTÉTICA
- **Atmósfera Dominante:** Pendiente de definición detallada.
- **Paleta de Colores:** Pendiente.

---

## 🧠 MECÁNICA NARRATIVA (TRAMA)
### La Chispa (Logline)
*{logline}*

### Estructura de los 3 Actos
{acts}

---

## 🫦 INGENIERÍA HIPNÓTICA & BDSM
- **Disparadores Técnicos:** Definidos en diálogo.
- **Palabras Gatillo (PNL):** Pendiente.

---

> [!TIP]
> **Reflexión sobre el Quiebre:** Generado automáticamente por el Oráculo de Ideación. 🫦👠✨
"""
    return template

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generar Ficha de Idea de La Voûte')
    parser.add_argument('--title', default="Nuevo Relato", help='Título del relato')
    parser.add_argument('--tema', required=True, help='Tema central')
    parser.add_argument('--pov', default="2da Persona (Tú)", help='Punto de vista')
    parser.add_argument('--arco', default="1. Resistencia\n2. Quiebre\n3. Rendición", help='Resumen de actos')
    
    args = parser.parse_args()
    
    # Logic to save the file could go here
    print(generate_ficha(args.title, "LV-2026-XXX", args.tema, "Misceláneo", args.pov, "Premium", "Logline descriptiva...", args.arco))
