# 📸 PROTOCOLO DE GESTIÓN DE IMÁGENES - La Voûte d'Anaïs

> **Propósito:** Estandarizar el ciclo de vida de las imágenes generadas, desde la creación hasta su archivo definitivo, asegurando consistencia estética y técnica.

---

## 1. 📂 Estructura de Directorios (Storage Rules)

Las imágenes NUNCA deben permanecer en la carpeta temporal (`brain` artifacts) ni en la raíz de `05_Imagenes`. Deben ser movidas a su carpeta específica inmediatamente después de la validación.

### A. Helena de Anaïs
- **Looks Numerados:** `05_Imagenes/helena/look[ID]_[nombre_corto]/`
  - *Ejemplo:* `05_Imagenes/helena/look59_midnight_cowgirl/`
- **Referencias/Tests:** `05_Imagenes/helena/Reference/`
- **Arcos Narrativos:** `05_Imagenes/helena/Story_Arcs/[nombre_arco]/`

### B. Miss Doll
- **Colecciones Temáticas:** `05_Imagenes/miss_doll/[tema_año]/`
  - *Ejemplo:* `05_Imagenes/miss_doll/latex_bdsm_red_lips_2026/`
- **Campañas/Series:** `05_Imagenes/miss_doll/[nombre_serie]/`

### C. Anaïs Belland & Otros
- **Personaje:** `05_Imagenes/[nombre_personaje]/[contexto]/`

---

## 2. 👠 La Regla de Oro (Stiletto Rule)

**MANDATO ABSOLUTO:** Bajo ninguna circunstancia se aceptan zapatos de tacón ancho, cuadrado o bloque (block heels), incluso si el atuendo (ej. Cowboy, Militar) tradicionalmente los usa.

*   **Prompting Obligatorio:** Siempre incluir `stiletto heels`, `high thin heels`, `needle heels` en el prompt positivo.
*   **Negative Prompting:** Incluir `block heel`, `chunky heel`, `wedge`, `platform sneakers` en el prompt negativo.
*   **Validación:** Si una imagen perfecta tiene tacón bloque, **SE DESCARTA** o se regenera. No se archiva.

---

## 3. 🔄 Flujo de Trabajo (The Workflow)

1.  **Generación:** Crear imágenes en el directorio de trabajo actual (`brain`).
2.  **Validación (Human/Agent Review):**
    *   ¿Cumple el Canon Facial?
    *   ¿Cumple la Stiletto Rule?
    *   ¿Cumple la Anatomía (manos, extremidades)?
3.  **Creación de Carpeta:** Si es un Look nuevo o un Set nuevo, crear el directorio destino siguiendo la nomenclatura.
4.  **Movimiento (Move-Item):** Mover los archivos aprobados a su carpeta destino.
5.  **Indexación:** Ejecutar SIEMPRE el script maestro:
    ```powershell
    python C:\Users\fabara\LaVouteDAnais\update_galleries.py
    ```
    *Este script actualiza automáticamente los archivos `GALERIA.md`, los `README.md` y los índices maestros.*

---

## 4. 🏷️ Nomenclatura (Naming Convention)

Referencia completa en: `00_Helena/plantilla_nomenclatura_imagenes.md`

**Formato Resumido:**
`[personaje]_[lookID]_[descriptor]_[timestamp].png`

*   *Correcto:* `helena_look59_cowgirl_standing_1770895506145.png`
*   *Incorrecto:* `imagen1.png`, `cowgirl_helena.png`

---

*Última actualización: 12/02/2026 por Helena (tras el incidente del Tacón Bloque).* 🩸
