# Formato HTML The Dollhouse (Estándar Resiliente 1.2)

> **⚠️ PROHIBICIÓN CRÍTICA:** TodoRelatos elimina imágenes externas (`<img>`) y bloquea otros elementos incrustados. **NO USAR TAGS <img>**.

## Reglas de Publicación Estricta

### 1. Sistema de Enlaces (Scene Visualizers)

Las imágenes deben presentarse exclusivamente como enlaces externos estilizados. Esto garantiza que el lector pueda ver el arte sin que la plataforma rompa el formato.

- **Formato:** Un párrafo centrado con emoji, bold y color Cyan (`#00bfff`).
- **Código:**

```html
<p style="text-align: center; margin: 2rem 0;">
    🖼️ <strong><a href="URL" target="_blank" style="color: #00bfff; text-decoration: none;"><font color="#00bfff">[VER ESCENA: Descripción]</font></a></strong>
</p>
```

### 2. Votación Interactiva

No intentar incrustar el widget de votación. Usar links textuales claros y destacados con el color Rosa (`#ff1493`).

- **Formato:**

```html
<p style="font-size: 1.2rem; font-weight: bold; margin: 2rem 0;">
    🔗 <strong><a href="URL_STRAWPOLL" target="_blank" style="color: #ff1493; text-decoration: underline;"><font color="#ff1493">VOTA AQUÍ (Link Externo)</font></a></strong>
</p>
```

### 3. Soporte Híbrido (CSS + Font)

Seguir usando etiquetas `<font color="...">` envolviendo el texto dentro de los tags con `style="color:..."` para asegurar que el color sobreviva a la limpieza de TodoRelatos.

---
*Actualizado el 6 de Enero 2026: Restricción absoluta de tags <img> para TodoRelatos.*
