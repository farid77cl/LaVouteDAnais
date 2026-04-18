import os

path = r'C:\Users\farid\LaVouteDAnais\00_Ele\memoria_sesiones.md'
# We read as bytes to avoid encoding issues with the AI tool's interpretation
with open(path, 'rb') as f:
    content = f.read().decode('utf-8', errors='replace')

lines = content.splitlines(keepends=True)

# 1. Add new entry in ESTADO ACTUAL
# Find the line after "## 🎯 ESTADO ACTUAL" (or however it decodes)
estado_actual_idx = -1
for i, line in enumerate(lines):
    if "ESTADO ACTUAL" in line:
        estado_actual_idx = i
        break

if estado_actual_idx != -1:
    new_entry = "- **18/04/2026 (MEDIODÍA - GENERACIÓN PARCIAL LOTE 3):** Generados y sincronizados 13 activos purificados (Looks 132-136). ADN V3.3 Hard-Sync. Bloqueo de cuota API en Look 136. Repositorio sincronizado. 🫦✨👠\n"
    lines.insert(estado_actual_idx + 1, new_entry)

# 2. Update Proyecto Activo Principal
for i in range(len(lines)):
    if "| **Último Look Ele** |" in lines[i]:
        lines[i] = "  | **Último Look Ele** | **Look 136 (Plum Velvet Romance — Parcial 2/5)** — 18/04/2026 🟡 |\n"
    if "| **Sincronización** |" in lines[i]:
        lines[i] = "  | **Sincronización** | **Total** (Parcial L3 Completa) ✅ |\n"
    if "| **Estado Visual** |" in lines[i]:
        lines[i] = "  | **Estado Visual** | ADN V3.3 Blindada. Lote 3 en progreso (13/32). Cuota API agotada ⏳. 🫦 |\n"

# 3. Update Cola de Producción Visual
for i in range(len(lines)):
    if "- [/] **Look 136 (Plum Lingerie):**" in lines[i]:
        lines[i] = "  - [/] **Look 136 (Plum Lingerie):** En progreso (2/5) ⏳\n"

# 4. Final verification of Última actualización date at the bottom if it existed (though it was mostly in READMEs)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("memoria_sesiones.md updated successfully.")
