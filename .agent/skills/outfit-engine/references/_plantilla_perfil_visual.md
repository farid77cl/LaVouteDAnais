# 🎭 Plantilla — Perfil Visual de Personaje

> **Contrato del `outfit-engine`.** Copia este archivo a
> `02_Personajes/_perfiles_visuales/<slug>.md` y rellena TODAS las secciones.
> El engine lee estas secciones por su número: si falta una, **se detiene y
> pregunta** en vez de improvisar.
>
> **Regla dueño-único:** este archivo es el **dueño** de estos campos para el
> personaje. Ningún otro archivo los copia — apuntan aquí. Si el canon profundo
> del personaje vive en otra parte (ficha literaria, canon visual extenso),
> este perfil **enlaza**, no duplica.

---

## §1 · Identidad y Rutas

| Campo | Valor |
|---|---|
| **Nombre canónico** | |
| **Slug** (archivos/prefijo de imagen) | |
| **Galería (dueño de los looks)** | `00_Ele/galeria_outfits.md` / `…` |
| **Carpeta de imágenes** | `05_Imagenes/<slug>/look<N>_<tema>/` |
| **Convención de nombre de archivo** | `<slug>_<N>_<pose>.png` |
| **Numeración** | correlativa / con prefijo especial (indicar) |
| **Canon profundo (enlace, NO copiar)** | |

---

## §2 · BLOQUE A — ADN Inamovible

> El token físico del personaje. Se copia **textualmente e idéntico** en cada
> una de las N poses de un look. Nunca se resume, nunca se escribe de memoria,
> nunca se adapta "porque la pose lo pedía".

```text
[ TOKEN LITERAL COMPLETO AQUÍ — en inglés ]
```

**Rasgos que NO se negocian jamás** (los que, si cambian, ya no es el personaje):

- …

---

## §3 · Negative Prompt

**Base (siempre):**
```text
[ … ]
```

**Adicionales por pose** (si alguna pose tiene una deriva conocida):

| Pose | Añadir al negative | Por qué |
|---|---|---|
| | | |

---

## §4 · Poses Canónicas

| # | Nombre canónico | Slug de archivo |
|---|---|---|
| 1 | | |

- **Total de poses por look:** N
- **Repertorio de variaciones:** enlace o "no aplica"
- **Excepciones por sub-arquetipo:** (ej. un set de poses distinto para cierto arquetipo)

---

## §5 · BLOQUE B — Reglas de Vestuario

> Todo lo que gobierna **cómo se viste** el personaje. El engine valida el
> outfit propuesto contra esta sección antes de escribir un solo prompt.

### 5.1 · Universo de materiales

- **Permitidos:**
- **Prohibidos (absoluto):**
- **Lente de identidad** (la frase que decide si un material entra o no):

### 5.2 · Paleta y reglas cromáticas

- **Paleta:**
- **Colores reservados al ADN** (no usables como prenda dominante):
- **Reglas de composición vigentes:** (anti-monoblock, cuotas, etc.)
- **Reglas derogadas** (anotar con fecha, para que nadie las reviva):

### 5.3 · Calzado (canon inamovible)

- **Regla:**
- **Altura mínima:**
- **Prohibido:**
- **Atributos obligatorios del token de calzado:** (nº de atributos que debe nombrar cada pose)

### 5.4 · Prohibiciones absolutas del vestuario

| Prohibido | Sustituto autorizado | Directiva |
|---|---|---|
| | | |

### 5.5 · Campos obligatorios de descripción del outfit

El BLOQUE B debe nombrar explícitamente, sin excepción:

1. …

> **Token de vestuario bloqueado:** las prendas complejas (opaco vs. sheer,
> capas, transparencias) se anclan una vez y se copian **idénticas** en las N
> poses. Nunca se parafrasean entre poses.

---

## §6 · Arquetipos y Metas

| Arquetipo / Sub-arquetipo | Descripción | Meta % |
|---|---|---|
| | | |

- **Regla de déficit:** si un arquetipo está bajo su meta → el próximo look debe pertenecer a esa categoría.
- **Prioridad de desempate:**
- **Biblioteca de siluetas / specs por sub-arquetipo (enlace):**

---

## §7 · Ventanas Anti-Repetición

| Elemento | Ventana de bloqueo |
|---|---|
| Silueta | ≥ N looks del mismo sub-arquetipo |
| Setting / escenario | ≥ N looks del mismo sub-arquetipo |
| | |

- **Regla de outfit único:** ¿se prohíbe repetir outfit? (sí/no)

---

## §8 · Cuotas Vivas

Cuotas que el engine debe **contar** antes de diseñar (no son ventanas de
bloqueo sino obligaciones periódicas):

| Cuota | Frecuencia | Alcance |
|---|---|---|
| | | |

---

## §9 · Banderas Rojas Específicas

Errores que este personaje en concreto ha sufrido y que hay que vigilar:

- …
