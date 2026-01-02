# Formato HTML The Dollhouse

## Reglas para publicación (aprendido de Caps 1-2)

### 1. Estructura

- Sin `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`
- Etiquetas: `<p>`, `<em>`, `<strong>`, `<hr>`, `<a>`, `<h1>`, `<h2>`, `<h3>`
- SÍ incluir título `<h1>` y descripción inicial
- SÍ usar `<h2>` para episodios y `<h3>` para secciones

### 2. Imágenes = LINKS CLICKEABLES

```html
<p>🖼️ <a href="URL" target="_blank"><strong>[VER ESCENA: Descripción]</strong></a></p>
```

NO usar `<img>` tags.

**Ubicaciones típicas:**

- Inicio del episodio
- Momentos clave de transformación
- El chantaje/extorsión
- El castigo

### 3. Diálogos de Miss Doll

- Usar `<em>` para sus líneas
- Incluir emojis: 📺✨ 🥩 👁️ 🤫 📢 😉 🔍 🧠💖 etc.

### 4. Penalidades

```html
<p><strong>⚠️ PENALIDAD: Julián -5 IQ → Total: -X IQ</strong></p>
```

### 5. Votación al final

```html
<h2>🗳️ VOTACIÓN</h2>
<p><strong>¿Qué castigo recibe [NOMBRE]?</strong></p>
<p><strong>OPCIÓN A: "NOMBRE" EMOJI</strong><br>
Descripción detallada...</p>
<p><strong><a href="URL_STRAWPOLL" target="_blank">🔗 VOTA AQUÍ</a></strong></p>
<p>⚠️ <strong>TU VOTO DECIDE...</strong></p>
```

### 6. Firma

```html
<p><em>Avec dévotion obscure,</em><br>
<strong>Anaïs Belland</strong> 🦇💋<br>
📧 anais.belland@outlook.com</p>
```

---
*Formato aprendido de the_dollhouse_caps1-2.html*
