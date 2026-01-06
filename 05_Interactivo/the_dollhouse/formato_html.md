# Formato HTML The Dollhouse (Estándar Embed 2026)

> **⚠️ IMPORTANTE:** A partir del Capítulo 4, se utiliza EXCLUSIVAMENTE el formato "Embed" con estilos inline.
> **Plantilla Maestra:** utilizar `template_embed.html`

## Reglas de Publicación

### 1. Estructura del Archivo

- **PROHIBIDO:** Usar `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`.
- **REQUERIDO:** Todo el contenido debe ir dentro del `div` contenedor maestro.
- **FUENTE:** `font-family: Georgia, serif;` (Definida en el contenedor principal).
- **FONDO:** Degradado oscuro `#0a0a0a` a `#1a0a1a` (Definido en el contenedor principal).

### 2. Estilos CSS Inline

Como el contenido se inserta en un editor externo, no se pueden usar clases CSS externas. Todo debe ser inline.

- **Texto General:** Color `#fafafa`, `line-height: 1.8`.
- **Miss Doll (Diálogos):** `<p style="color: #ff69b4; font-style: italic;">`
- **Títulos Dorados:** `color: #ffd700;`
- **Títulos Rosas:** `color: #ff1493;`
- **Contenedores de Alerta:** Usar `rgba(255, 0, 0, 0.2)` para bordes rojos.

### 3. Imágenes

Deben ser responsivas y estéticamente integradas.

```html
<div style="text-align: center; margin: 2rem 0;">
    <a href="LINK_IMAGEN" target="_blank">
        <img src="LINK_IMAGEN" alt="..." style="max-width: 100%; border-radius: 10px; box-shadow: 0 0 15px #ff1493; border: 2px solid #ff1493;">
    </a>
    <p style="font-size: 0.8rem; color: #888; font-style: italic;">Pie de foto</p>
</div>
```

### 4. Componentes Especiales

#### Caja de Inicio (Status)

Ver `template_embed.html`. Fondo rosa transparente, borde sólido.

#### Penalidades

```html
<div style="background: rgba(255, 0, 0, 0.2); border-left: 4px solid #ff0000; padding: 1rem; margin: 1rem 0; font-family: monospace;">
    <strong>⚠️ PENALIDAD:</strong> Texto...
</div>
```

#### Sección de Votación

El bloque de votación final debe usar el diseño de "Tarjetas" para las opciones A y B, con fondo semitransparente. Ver plantilla.

---
*Documento actualizado post-Capítulo 4*
