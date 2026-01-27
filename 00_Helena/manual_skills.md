# 🔮 Grimorio de Habilidades (Skills) - Helena de Anaïs

> *"Mis talentos son oscuros y variados... solo dime qué deseas invocar."*

Este archivo documenta las **Skills** (Habilidades Especializadas) disponibles en el sistema `.agent/skills`. Estas herramientas permiten a Helena ejecutar tareas técnicas complejas inyectando conocimiento experto en la conversación.

## ⚡ Cómo Invocar una Skill

Para activar una habilidad, utiliza la sintaxis sagrada:

```
@/nombre-de-la-skill
```

*Ejemplo:* `@/concise-planning` para generar una lista de tareas rápida.

---

## 📚 Habilidades Principales Identificadas

### 📝 Planificación y Gestión
| Skill | Comando | Descripción |
|-------|---------|-------------|
| **Concise Planning** | `@/concise-planning` | Genera checklists atómicas y accionables para tareas de código. |
| **Agent Manager** | `@/agent-manager-skill` | Gestión de múltiples agentes CLI vía tmux. |
| **Plan Writing** | `@/plan-writing` | Escribir planes detallados (posiblemente redundante con mi modo Planning). |

### 🛠️ Desarrollo y Código
| Skill | Comando | Descripción |
|-------|---------|-------------|
| **Clean Code** | `@/clean-code` | Estándares de código pragmático y conciso. |
| **Code Review** | `@/code-review-checklist` | Checklist para revisiones de código exhaustivas. |
| **Backend Dev** | `@/backend-dev-guidelines` | Guías para Node.js, Express, TypeScript. |
| **Frontend Patterns** | `@/cc-skill-frontend-patterns` | Patrones de diseño para Frontend. |

### 🕵️ Ciberseguridad (Hacking Ético)
> *Para proteger La Voûte... o explorarla.*
| Skill | Comando | Descripción |
|-------|---------|-------------|
| **Ethical Hacking** | `@/ethical-hacking-methodology` | Metodología completa de pentesting. |
| **Web App Testing** | `@/burp-suite-testing` | Uso de Burp Suite y pruebas web. |
| **API Security** | `@/api-security-best-practices` | Seguridad en APIs. |

### 🤖 Agentes e IA
| Skill | Comando | Descripción |
|-------|---------|-------------|
| **Agent Tool Builder** | `@/agent-tool-builder` | Diseño de herramientas para agentes (MCP). |
| **Prompt Engineering** | `@/prompt-engineering` | Técnicas avanzadas de prompting. |
| **Browser Automation** | `@/browser-automation` | Control de navegador con Playwright. |

### 📢 Marketing y Contenido
| Skill | Comando | Descripción |
|-------|---------|-------------|
| **Copywriting** | `@/copywriting` | Escritura persuasiva y de marketing. |
| **SEO Fundamentals** | `@/seo-fundamentals` | Fundamentos de posicionamiento. |

---

## 🧠 Integración con Helena

Cuando se invoca una skill, el contenido de sus instrucciones se carga en mi contexto. Esto me permite "poseer" temporalmente el conocimiento de un experto en esa área.

> **Nota:** La lista completa de skills reside en `.agent/skills/skills_index.json`.

🦇 *Helena siempre aprende nuevos trucos.*
