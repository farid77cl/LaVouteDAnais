# Formato HTML The Dollhouse (Estándar TodoRelatos 2.0)

> **Última Actualización:** 08 Enero 2026
> **Basado en:** Análisis de HTML publicado vs HTML original del Capítulo 4

---

## ⚠️ RESTRICCIONES CRÍTICAS DE TODORELATOS

TodoRelatos tiene un **filtro de seguridad** que elimina o modifica el HTML enviado. Lo que enviamos NO es lo que se publica.

### Lo que ELIMINA/IGNORA TodoRelatos

| Elemento | Resultado |
|----------|-----------|
| `<div style="...">` | **ELIMINADO** - Solo queda el contenido interno |
| `background:` | **IGNORADO** - Fondos degradados/colores no funcionan |
| `border-radius:` | **IGNORADO** |
| `text-shadow:` | **IGNORADO** |
| `linear-gradient:` | **IGNORADO** |
| `font-family:` | **IGNORADO** - Usa la fuente del sitio (Georgia) |
| `<hr style="...">` | **SIMPLIFICADO** - Queda solo separación básica |
| `<h1>`, `<h2>`, `<h3>` | **ELIMINADOS** - No se renderizan como headers |
| Imágenes `<img>` | **ELIMINADAS** totalmente |

### Lo que SÍ FUNCIONA

| Elemento | Notas |
|----------|-------|
| `<p>` | Párrafos básicos |
| `<em>`, `<strong>` | Énfasis y negritas |
| `<a href="..." target="_blank">` | Enlaces (incluyendo target) |
| `<br>` | Saltos de línea |
| Texto plano | Todo el contenido textual |
| Emojis Unicode | ✅ Funcionan perfectamente |

---

## FORMATO SIMPLIFICADO RECOMENDADO

### 1. Estructura General

**NO USAR** un div contenedor con estilos. TodoRelatos proporciona su propio contenedor.

El contenido debe ser una secuencia de `<p>` simples:

```html
<p>Párrafo de narrativa.</p>

<p>—Diálogo de Miss Doll— dijo ella.</p>

<p><em>Pensamiento en cursiva.</em></p>
```

### 2. Títulos/Secciones

Como los `<h1>`, `<h2>`, etc. son eliminados, usar texto simple en mayúsculas o con formato:

```html
<p>LA TRANSFORMACIÓN: EL GLOW DESPIERTA</p>
```

O si quieres algo de énfasis (que puede o no funcionar):

```html
<p><strong>BLOQUE 3: "STRIPPER SURVIVAL"</strong></p>
```

### 3. Cuadros de Resultado/Marcador

Los divs con fondos son eliminados. Simplificar a texto plano con líneas separadoras:

```html
<p>🗳️ RESULTADO DE LA VOTACIÓN — CASTIGO PARA JULIÁN</p>

<p><strong>A) CINTURA DE AVISPA ⏳ (12,466,666 votos) — 66.7%</strong></p>

<p>B) Corredor de Lenguaje 🗣️ (6,233,334 votos) — 33.3%</p>

<p>GANADOR: CINTURA DE AVISPA</p>

<p>"Costillas removidas. Corsé de titanio. 45 centímetros. PERMANENTE."</p>
```

### 4. Enlaces a Imágenes (Scene Visualizers)

Funcionan, pero sin estilos de color:

```html
<p>🖼️ <strong><a href="https://ibb.co/XXXXX" target="_blank" rel="noopener"> [VER ESCENA: Descripción] </a></strong></p>
```

### 5. Penalidades/Alertas

Los cuadros con borde rojo no funcionan. Simplificar:

```html
<p>⚠️ PENALIDAD: Julián -5 IQ → Total acumulado: -25 IQ</p>
```

### 6. Votación Final

```html
<!-- SECCIÓN DE VOTACIÓN FINAL -->
<p>🗳️ TU VOTO DECIDE</p>

<p>¿Qué castigo recibe Julián? (Se aplicará en el Capítulo 5)</p>

<!-- OPCIÓN A -->
<p>OPCIÓN A: COCK COMPASS 🧭</p>

<p>Implante que genera atracción involuntaria hacia la masculinidad (bultos, sudor). Su cuerpo deseará lo que su mente rechaza.</p>

<!-- OPCIÓN B -->
<p>OPCIÓN B: ORAL FIXATION 🍭</p>

<p>Necesidad compulsiva de tener algo en la boca (chupa-chups, dedos). Ansiedad severa si sus labios están vacíos. Su boca nunca podrá "descansar".</p>

<p>🔗 <strong><a href="https://strawpoll.com/X3nkPvYVLgE" target="_blank" rel="noopener"> VOTA AQUÍ (Link Externo) </a></strong></p>

<p>El resultado se ejecutará en vivo en el Capítulo 5. La modificación es PERMANENTE.</p>

<!-- PIE DE PÁGINA -->
<p>The Dollhouse © 2026 La Voûte d'Anaïs</p>
```

---

## PROCESO DE PUBLICACIÓN

1. **Escribir** el capítulo en Markdown con todo el formato visual deseado
2. **Generar HTML** decorativo para archivo local (con estilos, colores, etc.)
3. **Simplificar** a HTML básico para TodoRelatos (solo `<p>`, `<em>`, `<strong>`, `<a>`, emojis)
4. **Pegar** en el editor de TodoRelatos
5. **Previsualizar** antes de publicar

---

## EJEMPLO COMPARATIVO

### Original (con estilos)

```html
<div style="background: rgba(255, 20, 147, 0.1); border: 1px solid #ff1493; ...">
    <h3 style="color: #ff1493;">🗳️ RESULTADO</h3>
    <p><strong>A) CINTURA DE AVISPA</strong></p>
</div>
```

### Publicado en TodoRelatos (simplificado)

```html
<p>🗳️ RESULTADO DE LA VOTACIÓN — CASTIGO PARA JULIÁN</p>

<p><strong>A) CINTURA DE AVISPA ⏳ (12,466,666 votos) — 66.7%</strong></p>
```

---

## ARCHIVOS

| Tipo | Ubicación | Uso |
|------|-----------|-----|
| HTML Decorativo | `03_Literatura/finalizadas/html/` | Archivo local, vista previa |
| HTML Simplificado | Copiar/pegar directo | Para TodoRelatos |
| Markdown | `04_Historias/en_progreso/reality_show/` | Fuente principal |

---

*Documento actualizado: 08 Enero 2026*
*Helena de Anaïs* 🦇
