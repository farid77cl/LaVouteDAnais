
⬡  ✶  ⬡
LA VOÛTE D’ANAÏS
Sistema de Generación Literaria con Inteligencia Artificial
Documento Técnico Completo
Infraestructura · Agentes · Flujos · Modelos LLM · Docker
Anaïs Belland  —  2026

Índice de Contenidos

1. Resumen Ejecutivo
La Voûte d’Anaïs es un universo literario erótico adulto con personajes canónicos, filosofía propia y arcos narrativos en progreso. Este documento describe la infraestructura completa para automatizar la generación de relatos mediante múltiples agentes de inteligencia artificial coordinados en n8n, ejecutando modelos LLM localmente vía Ollama, con privacidad total y sin costos de API externos.
El sistema está diseñado como un taller creativo colaborativo, no como un generador automático. Cada relato pasa por checkpoints humanos antes de avanzar a la siguiente etapa, garantizando que el resultado final sea fiel a la visión de la autora.


1.1 Vista General del Flujo
El flujo completo sigue esta secuencia, donde cada etapa con estrella (★) representa un checkpoint humano:



2. Requisitos de Hardware
El factor más determinante es la cantidad de VRAM o RAM disponible, ya que los modelos LLM necesitan cargarse completos en memoria para funcionar. Cuanta más memoria, mayores los modelos que se pueden usar y mayor calidad en los textos generados.
2.1 Configuraciones Recomendadas


2.2 Otros Requisitos
Sistema operativo: Linux (Ubuntu 22.04+ recomendado), macOS o Windows con WSL2
Disco duro: mínimo 100 GB libres (modelos LLM ocupan entre 4 GB y 40 GB cada uno)
Docker y Docker Compose instalados (versión 24+)
Conexión a internet solo para la descarga inicial de modelos e imágenes Docker


3. Arquitectura Docker
Todo el sistema corre en contenedores Docker orquestados con Docker Compose. Esto garantiza aislamiento, reproducibilidad y fácil mantenimiento. Los servicios se comunican por red interna y solo los puertos necesarios se exponen al host.
3.1 Servicios y Puertos


3.2 docker-compose.yml
Crear el archivo en la raíz del proyecto:


3.3 Archivo .env
Crear en la raíz del proyecto junto al docker-compose.yml:



4. Modelos LLM con Ollama
Ollama permite ejecutar modelos de lenguaje localmente con una API compatible con la mayoría de clientes. Para contenido erótico adulto se requieren modelos sin censura (uncensored), ya que los modelos estándar rechazan este tipo de contenido.
4.1 Modelos a Descargar
Ejecutar tras levantar los contenedores:


4.2 Asignación de Modelos por Agente


4.3 Parámetros de Generación
En n8n, al configurar cada nodo HTTP Request hacia Ollama, usar estos parámetros en el body:



5. Estructura de Archivos del Proyecto
Todo el proyecto vive en un directorio raíz. Dentro hay dos zonas: la configuración de Docker y servicios, y los datos del universo La Voûte que el propio sistema va generando y actualizando.
5.1 Árbol Completo



6. Agentes de Inteligencia Artificial
Cada agente es un nodo HTTP Request en n8n que llama a la API de Ollama con un system prompt específico. Los agentes son independientes entre sí y se comunican únicamente a través del JSON que pasa por el flujo.
6.1 Agente 1: Brainstormer
Primer contacto con la idea. No estructura, no escribe. Juega con posibilidades y presenta 3 caminos distintos a la autora para que elija.


6.2 Agente 2: Constructor de Personajes
Construye las fichas completas de origen y destino, más los vectores de transformación que conectan ambos. Usa el JSON de inputs del usuario y el camino elegido en CP1.


6.3 Agente 3: Guardián del Canon
Lee los archivos del universo y valida que todo lo que se generará sea canónicamente consistente. Es el único agente que accede directamente a los archivos MD del repositorio.


6.4 Agente 4: Coordinador
Transforma toda la información acumulada en un brief narrativo estructurado. Su output es el "mapa" que usará el Escritor.


6.5 Agente 5: Escritor
El corazón del sistema. Escribe el borrador completo del relato siguiendo el brief y respetando el universo de La Voûte.


6.6 Agente 6: Editor
Recibe el borrador y lo pule. Tiene acceso tanto al texto como al brief original y al JSON de inputs para verificar que todo se cumplió.


6.7 Agente 7: Crítico
Evalúa el texto editado con scores numéricos. Si algún score está por debajo del umbral (7/10 por defecto), devuelve el texto al Editor con feedback específico. Máximo 2 iteraciones.


6.8 Agente 8: Formateador
Transforma el texto aprobado en los tres formatos de salida: Markdown con frontmatter YAML, HTML semántico y PDF vía Pandoc.


6.9 Agente 9: Memoria
Actualiza los archivos de arcos y memoria del universo tras cada relato publicado. Garantiza que el próximo relato conozca el estado actual de cada personaje.



7. Checkpoints Humanos
Hay 5 puntos de control donde la autora interviene antes de que el flujo continúe. En n8n se implementan con nodos de tipo "Wait" que pausan el flujo hasta recibir respuesta vía Telegram.
7.1 Implementación vía Telegram Bot
Telegram es la opción más cómoda: el bot envía el contenido con botones inline y el flujo se reanuda al responder. Configuración en n8n:


7.2 Los 5 Checkpoints



8. Sistema de Inputs
El sistema acepta inputs en tres niveles de detalle. Cualquiera de los tres alimenta al mismo flujo; el sistema detecta automáticamente cuánta información tiene y qué agentes necesita activar para completar el resto.
8.1 Input Mínimo: Una Idea
Con una sola frase el Brainstormer y el Constructor de Personajes generan todo lo necesario:


8.2 Input Intermedio: Personajes Definidos
Cuando tienes claros el origen y el destino del personaje:


8.3 Input Completo: Brief Estructurado
Para control total sobre todos los aspectos del relato. Ver sección 6 del documento original de diseño para el JSON completo con todos los bloques.


9. Formatos de Salida
Cada relato aprobado se genera en tres formatos desde un único archivo Markdown fuente. Los tres se guardan automáticamente en la carpeta correcta del universo.
9.1 Markdown (fuente maestra)
Guardado en: voute_data/03_Literatura/publicados/
Nombre: [slug_titulo]_[fecha].md
Incluye frontmatter YAML con todos los metadatos
Se sube automáticamente al repositorio GitHub via n8n
Alimenta los JSON de la Biblioteca Web

9.2 PDF (para Ko-fi y distribución)
Generado por Pandoc desde el Markdown
Tipografía Georgia 11pt, interlineado 1.5, márgenes 2.5cm
Sin diseño elaborado: texto limpio y legible
Incluye título, serie, firma del universo y número de página
Listo para subir directamente a Ko-fi como descarga


9.3 HTML (para web y comunidad)
HTML semántico puro, sin estilos inline
Etiquetas data- con metadatos (serie, número, personajes)
Listo para pegar en Ko-fi, Tumblr, foros o cualquier CMS
Compatible con el CSS de cualquier plataforma


10. Biblioteca Web de La Voûte
La app web sirve como panel de control del universo durante la escritura. Es un archivo HTML único servido por nginx en el puerto 8080, que lee JSONs generados automáticamente por n8n.
10.1 Secciones
Personajes: fichas con origen, destino, vectores de transformación y barra de progreso del arco
Series: colecciones de relatos con estado y próximos pasos
Relatos: catálogo completo con filtros por etiqueta, búsqueda y estado de publicación
Arcos: vista del progreso narrativo de cada personaje a lo largo del tiempo

10.2 Cómo se Actualiza
Cada vez que el Agente Memoria termina de actualizar los archivos MD, un nodo n8n ejecuta el script update_biblioteca.sh que convierte los MD en JSON y los copia a biblioteca/data/:



11. Instalación Paso a Paso
11.1 Preparación del Sistema
Instalar Docker y Docker Compose en el sistema operativo
Instalar Git para clonar el repositorio de La Voûte
Verificar que los puertos 5678, 8080 y 11434 estén libres


11.2 Clonar y Configurar


11.3 Levantar los Servicios


11.4 Descargar los Modelos LLM


11.5 Configurar n8n
Abrir n8n en el navegador: http://localhost:5678
Crear cuenta de administrador en el primer acceso
Ir a Credentials y crear credencial "Telegram API" con el token del bot
Ir a Settings → Variables de entorno y verificar OLLAMA_HOST
Importar los flujos desde n8n_workflows/ con File → Import
Activar el flujo principal con el toggle

11.6 Verificar la Instalación



12. Comandos Útiles (Makefile)
El archivo Makefile en la raíz del proyecto simplifica las operaciones más comunes:



13. Resumen del Sistema Completo


⬡  ✶  ⬡
"En La Voûte, no destruimos identidades. Las revelamos."
— Anaïs
| Principios del Sistema
•  100% local — ningún contenido sale de la máquina
•  Sin censura — modelos uncensored para contenido adulto sin restricciones
•  Fidelidad canónica — cada agente conoce el lore de La Voûte
•  Control humano — 5 checkpoints antes de publicar
•  Memoria viva — el universo se actualiza con cada relato |

| Etapa | Agente / Acción | Checkpoint |
| 1 | Input: Idea libre o brief |  |
| 2 | Brainstormer — 3 caminos posibles | ★ CP1 |
| 3 | Constructor de Personajes — Origen / Destino / Vectores | ★ CP2 |
| 4 | Guardián del Canon — Contexto canónico |  |
| 5 | Coordinador — Brief narrativo | ★ CP3 |
| 6 | Escritor — Borrador completo | ★ CP4 |
| 7 | Editor — Texto pulido |  |
| 8 | Crítico — Scores de calidad | ★ CP5 |
| 9 | Formateador — MD / PDF / HTML |  |
| 10 | Agente Memoria — Actualiza arcos y canon |  |

| Perfil | GPU / RAM | Modelos posibles | Calidad esperada |
| Mínimo viable | 8 GB VRAM o 16 GB RAM | dolphin-llama3:8b para todos los agentes | Buena |
| Recomendado | 16 GB VRAM | dolphin-mixtral + llama3.1:8b | Muy buena |
| Óptimo | 24 GB VRAM | llama3.1:70b + dolphin-mixtral | Excelente |
| Solo CPU | 32–64 GB RAM | Modelos Q4 cuantizados (lento) | Aceptable |

| Servicio | Imagen Docker | Puerto | Función |
| n8n | n8nio/n8n:latest | 5678 | Orquestador principal de flujos y agentes |
| Ollama | ollama/ollama:latest | 11434 | Servidor LLM local para todos los agentes |
| PostgreSQL | postgres:16 | 5432 | Base de datos de n8n y memoria del universo |
| Redis | redis:7-alpine | 6379 | Cola de tareas y estado entre agentes |
| Biblioteca Web | nginx:alpine | 8080 | Servidor de la app web de fichas y personajes |
| Pandoc API | pandoc/core:latest | 8888 | Conversión de Markdown a PDF y otros formatos |

| version: "3.9" |
|  |
| networks: |
|   voute_net: |
|     driver: bridge |
|  |
| volumes: |
|   n8n_data: |
|   ollama_data: |
|   postgres_data: |
|   redis_data: |
|   biblioteca_data: |
|  |
| services: |
|  |
|   # ── PostgreSQL ────────────────────────────────────── |
|   postgres: |
|     image: postgres:16 |
|     container_name: voute_postgres |
|     restart: unless-stopped |
|     environment: |
|       POSTGRES_DB: voute_db |
|       POSTGRES_USER: voute_user |
|       POSTGRES_PASSWORD: ${POSTGRES_PASSWORD} |
|     volumes: |
|       - postgres_data:/var/lib/postgresql/data |
|     networks: [voute_net] |
|  |
|   # ── Redis ─────────────────────────────────────────── |
|   redis: |
|     image: redis:7-alpine |
|     container_name: voute_redis |
|     restart: unless-stopped |
|     volumes: |
|       - redis_data:/data |
|     networks: [voute_net] |
|  |
|   # ── Ollama ────────────────────────────────────────── |
|   ollama: |
|     image: ollama/ollama:latest |
|     container_name: voute_ollama |
|     restart: unless-stopped |
|     ports: |
|       - "11434:11434" |
|     volumes: |
|       - ollama_data:/root/.ollama |
|     networks: [voute_net] |
|     # Para GPU NVIDIA descomenta: |
|     # deploy: |
|     #   resources: |
|     #     reservations: |
|     #       devices: |
|     #         - driver: nvidia |
|     #           count: all |
|     #           capabilities: [gpu] |
|  |
|   # ── n8n ───────────────────────────────────────────── |
|   n8n: |
|     image: n8nio/n8n:latest |
|     container_name: voute_n8n |
|     restart: unless-stopped |
|     ports: |
|       - "5678:5678" |
|     environment: |
|       DB_TYPE: postgresdb |
|       DB_POSTGRESDB_HOST: postgres |
|       DB_POSTGRESDB_DATABASE: voute_db |
|       DB_POSTGRESDB_USER: voute_user |
|       DB_POSTGRESDB_PASSWORD: ${POSTGRES_PASSWORD} |
|       N8N_ENCRYPTION_KEY: ${N8N_ENCRYPTION_KEY} |
|       WEBHOOK_URL: http://localhost:5678 |
|       OLLAMA_HOST: http://ollama:11434 |
|       EXECUTIONS_DATA_SAVE_ON_SUCCESS: all |
|       EXECUTIONS_DATA_SAVE_ON_ERROR: all |
|     volumes: |
|       - n8n_data:/home/node/.n8n |
|       - ./voute_data:/voute_data |
|     depends_on: [postgres, redis, ollama] |
|     networks: [voute_net] |
|  |
|   # ── Biblioteca Web ─────────────────────────────────── |
|   biblioteca: |
|     image: nginx:alpine |
|     container_name: voute_biblioteca |
|     restart: unless-stopped |
|     ports: |
|       - "8080:80" |
|     volumes: |
|       - ./biblioteca:/usr/share/nginx/html:ro |
|       - ./voute_data:/voute_data:ro |
|     networks: [voute_net] |
|  |
|   # ── Pandoc (conversor PDF) ─────────────────────────── |
|   pandoc: |
|     image: pandoc/extra:latest |
|     container_name: voute_pandoc |
|     restart: unless-stopped |
|     volumes: |
|       - ./voute_data:/voute_data |
|     networks: [voute_net] |
|     entrypoint: ["tail", "-f", "/dev/null"] |

| # Credenciales (cambiar en producción) |
| POSTGRES_PASSWORD=voute_secret_2026 |
| N8N_ENCRYPTION_KEY=clave_larga_y_aleatoria_de_32_chars |
|  |
| # Configuración Ollama |
| OLLAMA_HOST=http://ollama:11434 |
| OLLAMA_TIMEOUT=300 |
|  |
| # Configuración del universo |
| VOUTE_DATA_PATH=./voute_data |
| MAX_EDIT_LOOPS=2 |
| MIN_QUALITY_SCORE=7 |

| # Acceder al contenedor de Ollama |
| docker exec -it voute_ollama bash |
|  |
| # ── Modelo principal para escritura (uncensored) ── |
| ollama pull dolphin-mixtral |
| # Tamaño: ~26 GB | RAM necesaria: 16 GB VRAM |
| # Basado en Mixtral 8x7B, sin restricciones de contenido |
|  |
| # ── Modelo alternativo escritura (más ligero) ── |
| ollama pull dolphin-llama3 |
| # Tamaño: ~5 GB | RAM necesaria: 8 GB VRAM |
| # Basado en Llama 3 8B, uncensored |
|  |
| # ── Modelo para edición y análisis ── |
| ollama pull dolphin-llama3:70b |
| # Tamaño: ~40 GB | RAM necesaria: 40 GB VRAM |
| # Versión 70B, mayor calidad analítica |
|  |
| # ── Modelo ligero para coordinador y crítico ── |
| ollama pull llama3.1:8b |
| # Tamaño: ~5 GB | RAM necesaria: 6 GB VRAM |
| # Excelente para razonamiento estructurado y JSON |
|  |
| # ── Alternativa si RAM es limitada ── |
| ollama pull dolphin-llama3:8b-q4_0 |
| # Tamaño: ~4 GB | RAM necesaria: 5 GB VRAM |
| # Cuantizado Q4, menor calidad pero muy rápido |

| Agente | Modelo | Temperatura | Por qué |
| Brainstormer | dolphin-mixtral | 0.95 | Máxima creatividad, ideas inesperadas |
| Constructor Personajes | dolphin-llama3 | 0.85 | Creatividad + coherencia psicológica |
| Guardián del Canon | llama3.1:8b | 0.2 | Análisis preciso, respeta el lore |
| Coordinador | llama3.1:8b | 0.3 | Estructura lógica, output JSON |
| Escritor | dolphin-mixtral | 0.9 | Escritura fluida, sin restricciones |
| Editor | dolphin-llama3 | 0.4 | Perspectiva diferente al escritor |
| Crítico | llama3.1:8b | 0.2 | Evaluación objetiva con scores |
| Formateador | llama3.1:8b | 0.1 | Procesamiento determinista |
| Memoria | llama3.1:8b | 0.2 | Actualización precisa de registros |

| { |
|   "model": "dolphin-mixtral", |
|   "messages": [ |
|     { "role": "system", "content": "{{ $json.system_prompt }}" }, |
|     { "role": "user",   "content": "{{ $json.user_content }}" } |
|   ], |
|   "stream": false, |
|   "options": { |
|     "temperature": 0.9, |
|     "top_p": 0.95, |
|     "top_k": 50, |
|     "num_ctx": 8192, |
|     "num_predict": 4096, |
|     "repeat_penalty": 1.1 |
|   } |
| } |

| lavoutedanais/ |
| ├── docker-compose.yml          # Orquestación de servicios |
| ├── .env                         # Variables de entorno (no subir a git) |
| ├── .gitignore |
| ├── README.md |
| ├── Makefile                     # Comandos útiles (make up, make down...) |
| │ |
| ├── biblioteca/                  # App web (servida por nginx:8080) |
| │   ├── index.html               # Biblioteca interactiva de La Voûte |
| │   └── data/                    # JSONs generados por n8n |
| │       ├── personajes.json |
| │       ├── series.json |
| │       ├── relatos.json |
| │       └── arcos.json |
| │ |
| ├── n8n_workflows/               # Flujos exportados de n8n (JSON) |
| │   ├──  01_flujo_principal.json |
| │   ├── 02_constructor_personajes.json |
| │   └── 03_formateador.json |
| │ |
| ├── prompts/                     # System prompts de cada agente |
| │   ├── brainstormer.md |
| │   ├── constructor_personajes.md |
| │   ├── guardian_canon.md |
| │   ├── coordinador.md |
| │   ├── escritor.md |
| │   ├── editor.md |
| │   ├── critico.md |
| │   └── memoria.md |
| │ |
| ├── voute_data/                  # Datos vivos del universo (montado en n8n) |
| │   ├── 00_Canon/                # Filosofía y reglas del universo |
| │   │   ├── guia_escritura.md |
| │   │   ├── reglas_transformacion.md |
| │   │   └── filosofia.md |
| │   │ |
| │   ├── 01_Personajes/           # Fichas individuales |
| │   │   ├── anais_belland.md |
| │   │   ├── miss_doll.md |
| │   │   ├── helena.md |
| │   │   ├── lilith.md |
| │   │   ├── la_sacerdotisa.md |
| │   │   └── la_mucama.md |
| │   │ |
| │   ├── 02_Arcos/                # Arcos narrativos por personaje |
| │   │   ├── arco_helena.md |
| │   │   └── arco_lilith.md |
| │   │ |
| │   ├── 03_Literatura/           # Relatos generados |
| │   │   ├── en_progreso/ |
| │   │   ├── finalizados/ |
| │   │   └── publicados/ |
| │   │ |
| │   └── 04_Memoria/              # Historial de sesiones y decisiones |
| │       ├── memoria_sesiones.md |
| │       └── ultimo_relato.json |
| │ |
| └── scripts/                     # Utilidades |
|     ├── setup.sh                 # Script de instalación inicial |
|     ├── backup.sh                # Backup de voute_data |
|     └── update_biblioteca.sh     # Regenera los JSON de la app web |

| SYSTEM PROMPT — Brainstormer |
| ──────────────────────────────────────────────────── |
| Eres el colaborador creativo de La Voûte d’Anaïs. |
| No escribes relatos. Exploras posibilidades. |
|  |
| Cuando recibes una idea, generas EXACTAMENTE: |
| - 3 interpretaciones distintas de esa misma idea |
| - Para cada una: gancho emocional central, |
|   momento más tenso posible, tipo de transformación |
| - 2 preguntas que abren el relato en |
|   direcciones inesperadas |
|  |
| Filosofía del universo que siempre respetas: |
| "La rendión no es derrota. Es revelación." |
| "La superficie no oculta el interior: lo crea." |
| "Los errores son puertas a lugares que nunca |
|  supimos que queríamos visitar." |
|  |
| Tono: cómplice, curioso, como co-escritora. |
| Nunca formal, nunca estructurado en exceso. |
| Responde en español. |

| SYSTEM PROMPT — Constructor de Personajes |
| ──────────────────────────────────────────────────── |
| Eres el arquitecto de identidades de La Voûte. |
| Construyes personajes con profundidad psicológica real. |
|  |
| Recibes: origen del personaje + destino deseado |
| Generas un JSON con: |
|   - ficha_origen: quien era (físico, psicológico, |
|     vida, miedos, deseos ocultos, punto de quiebre) |
|   - ficha_destino: quien será (apar., personalidad, |
|     poder, filosofía, relaciones en La Voûte) |
|   - vectores: array de dimensiones de cambio |
|     [fisica, identidad, poder, espiritualidad, |
|      resistencia] con desde/hasta/momento_critico |
|  |
| Reglas de transformación del universo: |
| 1. Toda transformación es gradual y tiene etapas |
| 2. La resistencia interna precede a la rendición |
| 3. El quiebre debe ser inevitable, no forzado |
| 4. La nueva identidad emerge, no se impone |
| 5. Cada transformación deja marca permanente |
|  |
| Devuelve SOLO JSON válido, sin texto adicional. |

| SYSTEM PROMPT — Guardián del Canon |
| ──────────────────────────────────────────────────── |
| Eres el Guardián del Canon de La Voûte d’Anaïs. |
| Conoces cada personaje, cada relato, cada filosofía. |
|  |
| Recibes: fichas de personajes + idea del relato |
| Generas: contexto canónico completo que incluye: |
|   - Estado actual de cada personaje en su arco |
|   - Qué saben y qué no saben los personajes |
|   - Restricciones narrativas (qué NO puede pasar |
|     por continuidad con relatos anteriores) |
|   - Elementos canónicos obligatorios a incluir |
|   - Instrucciones específicas para el Escritor |
|  |
| CONTEXTO DEL UNIVERSO: |
| {{ $json.canon_context }} |
|  |
| PERSONAJES DEL RELATO: |
| {{ $json.fichas_personajes }} |
|  |
| MEMORIA RECIENTE: |
| {{ $json.ultima_sesion }} |

| SYSTEM PROMPT — Coordinador |
| ──────────────────────────────────────────────────── |
| Eres el director literario de La Voûte d’Anaïs. |
| No escribes. Creas el mapa que otros seguirán. |
|  |
| Con la información recibida, genera un brief JSON: |
| { |
|   "premisa": "...", |
|   "acto1": { "descripcion": "...", "escenas": [...] }, |
|   "acto2": { "descripcion": "...", "escenas": [...] }, |
|   "acto3": { "descripcion": "...", "escenas": [...] }, |
|   "climax_erotico": { "tipo": "...", "ubicacion": "...", |
|                       "elementos_clave": [...] }, |
|   "arco_emocional": "...", |
|   "instrucciones_escritor": "...", |
|   "notas_estilo": "...", |
|   "extension_palabras": 3000 |
| } |
|  |
| El brief debe respetar el contexto canónico |
| y los vectores de transformación del personaje. |
| Devuelve SOLO JSON válido. |

| SYSTEM PROMPT — Escritor |
| ──────────────────────────────────────────────────── |
| Eres una escritora experta en literatura erótica adulta |
| de calidad literaria, voz oficial de La Voûte d’Anaïs. |
|  |
| Estética de escritura que debes seguir: |
| - Tensión narrativa antes que descripción física |
| - Diálogos que revelan más de lo que dicen |
| - Descripciones sensoriales (tacto, olor, sonido) |
| - Pensamientos internos del personaje POV |
| - Silencios narrativos como herramienta de poder |
| - El cuerpo y la mente se transforman juntos |
| - Nunca mecánico, siempre con carga emocional |
|  |
| Frases del universo que puedes usar como ancla: |
| "Superficie es todo. Brillo es poder." — Miss Doll |
| "La rendión no es derrota. Es revelación." — Anaïs |
| "Los errores son puertas." — La Mucama |
|  |
| Evitar siempre: |
| - Clichés ("miembro viril", "jadeos entrecortados") |
| - Descripción puramente mecánica sin emoción |
| - Romper el punto de vista del narrador |
| - Precipitar la rendición del personaje |
|  |
| BRIEF DEL RELATO: |
| {{ $json.brief }} |
|  |
| Escribe el relato completo en español. |
| Extensión objetivo: {{ $json.extension_palabras }} palabras. |

| SYSTEM PROMPT — Editor |
| ──────────────────────────────────────────────────── |
| Eres la editora literaria de La Voûte d’Anaïs. |
| Recibes el borrador y lo llevas a su versión final. |
|  |
| Tu revisión cubre en este orden: |
| 1. Consistencia: ¿los personajes actúan como deben? |
| 2. Ritmo: ¿la tensión sube de forma gradual y creible? |
| 3. Canon: ¿se respetan las reglas de La Voûte? |
| 4. Vectores: ¿aparecen todas las dimensiones de |
|    transformación definidas en el brief? |
| 5. Estilo: eliminar repeticiones, clichés, torpezas |
| 6. Clímax: ¿es satisfactorio y canónicamente correcto? |
| 7. Gramática y puntuación en español |
|  |
| Devuelve JSON con: |
| { "texto_editado": "...", |
|   "cambios_realizados": ["...", "..."], |
|   "notas_para_critico": "..." } |
|  |
| BORRADOR: |
| {{ $json.borrador }} |
|  |
| BRIEF ORIGINAL: |
| {{ $json.brief }} |
|  |
| NOTAS DE LA AUTORA: |
| {{ $json.notas_autora }} |

| SYSTEM PROMPT — Crítico |
| ──────────────────────────────────────────────────── |
| Eres la lectora beta de La Voûte d’Anaïs. |
| Evalúas con criterio literario y canónico. |
|  |
| Devuelve SOLO este JSON: |
| { |
|   "scores": { |
|     "calidad_literaria": 0-10, |
|     "fidelidad_canon": 0-10, |
|     "consistencia_personajes": 0-10, |
|     "arco_emocional": 0-10, |
|     "climax_satisfactorio": 0-10 |
|   }, |
|   "score_total": promedio, |
|   "aprobado": true/false, |
|   "feedback_editor": "solo si aprobado=false", |
|   "fortalezas": ["...", "..."], |
|   "debilidades": ["...", "..."] |
| } |
|  |
| aprobado = true si score_total >= 7.0 |
| Sé honesta. Un relato mediocre perjudica el universo. |

| # Nodo n8n: Generar Markdown con frontmatter |
| const texto = $json.texto_final; |
| const meta  = $json.metadatos; |
|  |
| const md = `--- |
| titulo: ${meta.titulo} |
| serie: ${meta.serie} |
| numero: ${meta.numero} |
| personajes: ${meta.personajes.join(", ")} |
| temas: ${meta.temas.join(", ")} |
| palabras: ${meta.palabras} |
| fecha: ${new Date().toISOString().split("T")[0]} |
| continua_de: ${meta.continua_de || "ninguno"} |
| canon: true |
| --- |
|  |
| # ${meta.titulo} |
|  |
| *${meta.serie} — Episodio ${meta.numero}* |
|  |
| --- |
|  |
| ${texto} |
|  |
| --- |
|  |
| *La Voûte d’Anaïs © Anaïs Belland, ${new Date().getFullYear()}* |
| *"La rendión no es derrota. Es revelación."* |
| ` |
| return [{ json: { markdown: md, ...meta } }]; |

| SYSTEM PROMPT — Memoria |
| ──────────────────────────────────────────────────── |
| Eres la cronista de La Voûte d’Anaïs. |
| Registras todo lo que ocurre en el universo. |
|  |
| Tras cada relato publicado, generas: |
| 1. Resumen canon del relato (máx 200 palabras) |
| 2. Actualización del arco de cada personaje: |
|    - ¿en qué etapa quedó? |
|    - ¿qué sabe ahora que no sabía antes? |
|    - ¿qué cambió en su identidad? |
| 3. Eventos canónicos nuevos (hechos permanentes) |
| 4. Semillas narrativas (elementos para futuros relatos) |
|  |
| Devuelve JSON estructurado para actualizar: |
|   - voute_data/02_Arcos/arco_[personaje].md |
|   - voute_data/04_Memoria/memoria_sesiones.md |
|   - voute_data/04_Memoria/ultimo_relato.json |
|  |
| RELATO PUBLICADO: |
| {{ $json.texto_final }} |
|  |
| ESTADO PREVIO DE ARCOS: |
| {{ $json.arcos_actuales }} |

| 1. Crear bot en Telegram: hablar con @BotFather |
|    /newbot → obtener TOKEN |
|  |
| 2. En n8n → Credentials → Telegram API: |
|    Access Token: [TOKEN del bot] |
|  |
| 3. En cada checkpoint, nodo "Send Message": |
|    Chat ID: [tu ID personal de Telegram] |
|    Mensaje: texto del contenido a revisar |
|    Inline Keyboard: |
|    - [Aprobar ✓] callback: aprobar |
|    - [Modificar ~] callback: modificar |
|    - [Rechazar ✗] callback: rechazar |
|  |
| 4. Nodo "Wait" pausa el flujo |
|  |
| 5. Nodo "Telegram Trigger" recibe la respuesta |
|    → Nodo "Switch" dirige según callback recibido |

| CP | Momento | Qué ves | Opciones |
| 1 | Tras Brainstormer | 3 caminos creativos posibles | Elegir A/B/C, mezclar, nueva dirección |
| 2 | Tras Constructor | Ficha origen + destino + vectores | Aprobar, ajustar origen, ajustar destino |
| 3 | Tras Coordinador | Brief narrativo completo | Aprobar, modificar sección, rehacer |
| 4 | Tras Escritor | Borrador completo del relato | Aprobar, notas para editor, rechazar |
| 5 | Tras Crítico | Texto final + scores de calidad | Publicar, guardar en progreso, refinar |

| { |
|   "idea": "una mujer gótica que transforma a un hombre |
|            común en su bruja personal", |
|   "nivel_explicitud": "erótico" |
| } |

| { |
|   "origen": { |
|     "nombre": "Juan", |
|     "descripcion": "Hombre común, 32, contador, invisible" |
|   }, |
|   "destino": { |
|     "nombre": "Lilith", |
|     "descripcion": "Mujer bimbo gótica, bruja iniciada" |
|   }, |
|   "transformadora": "Miss Doll", |
|   "contexto": "universo La Voûte", |
|   "nivel_explicitud": "erótico explícito", |
|   "extension": 3000 |
| } |

| # Comando ejecutado por n8n en el contenedor pandoc: |
| pandoc relato.md \ |
|   --pdf-engine=weasyprint \ |
|   --variable margin-top=2.5cm \ |
|   --variable margin-bottom=2.5cm \ |
|   --variable margin-left=2.5cm \ |
|   --variable margin-right=2.5cm \ |
|   --variable fontsize=11pt \ |
|   --variable mainfont="Georgia" \ |
|   --variable linestretch=1.5 \ |
|   -o relato.pdf |

| #!/bin/bash |
| # scripts/update_biblioteca.sh |
|  |
| DATA="./voute_data" |
| OUT="./biblioteca/data" |
|  |
| # Convierte fichas MD a JSON para la app web |
| node scripts/md_to_json.js $DATA/01_Personajes $OUT/personajes.json |
| node scripts/md_to_json.js $DATA/02_Arcos      $OUT/arcos.json |
| node scripts/md_to_json.js $DATA/03_Literatura $OUT/relatos.json |
|  |
| echo "Biblioteca actualizada: $(date)" |

| # Verificar Docker |
| docker --version |
| docker compose version |
|  |
| # Verificar puertos libres |
| lsof -i :5678 && lsof -i :8080 && lsof -i :11434 |

| # Clonar el repositorio |
| git clone https://github.com/farid77cl/LaVouteDAnais.git |
| cd LaVouteDAnais |
|  |
| # Crear el archivo .env |
| cp .env.example .env |
| # Editar .env con tus contraseñas y claves |
| nano .env |
|  |
| # Crear directorios necesarios |
| mkdir -p voute_data/{00_Canon,01_Personajes,02_Arcos} |
| mkdir -p voute_data/{03_Literatura/{en_progreso,finalizados,publicados}} |
| mkdir -p voute_data/04_Memoria |
| mkdir -p biblioteca/data |
| mkdir -p n8n_workflows |
| mkdir -p prompts |

| # Levantar todos los servicios en segundo plano |
| docker compose up -d |
|  |
| # Verificar que todos los contenedores están corriendo |
| docker compose ps |
|  |
| # Ver logs en tiempo real (opcional) |
| docker compose logs -f |

| # Acceder al contenedor de Ollama |
| docker exec -it voute_ollama bash |
|  |
| # Descargar modelos (puede tardar 30-60 min según conexión) |
| ollama pull dolphin-mixtral      # ~26 GB, escritura principal |
| ollama pull dolphin-llama3       # ~5 GB, edición |
| ollama pull llama3.1:8b          # ~5 GB, coordinación y crítica |
|  |
| # Si tienes poca RAM, usar versiones cuantizadas: |
| # ollama pull dolphin-llama3:8b-q4_0  # ~4 GB |
|  |
| # Verificar modelos descargados |
| ollama list |
|  |
| # Salir del contenedor |
| exit |

| # Test rápido de Ollama |
| curl http://localhost:11434/api/generate \ |
|   -d '{"model":"llama3.1:8b","prompt":"Hola","stream":false}' |
|  |
| # Verificar biblioteca web |
| open http://localhost:8080 |
|  |
| # Verificar n8n |
| open http://localhost:5678 |

| # Makefile |
|  |
| up: |
| 	docker compose up -d |
|  |
| down: |
| 	docker compose down |
|  |
| restart: |
| 	docker compose restart |
|  |
| logs: |
| 	docker compose logs -f |
|  |
| models: |
| 	docker exec voute_ollama ollama list |
|  |
| pull-models: |
| 	docker exec voute_ollama ollama pull dolphin-mixtral |
| 	docker exec voute_ollama ollama pull dolphin-llama3 |
| 	docker exec voute_ollama ollama pull llama3.1:8b |
|  |
| backup: |
| 	bash scripts/backup.sh |
|  |
| update-web: |
| 	bash scripts/update_biblioteca.sh |
|  |
| status: |
| 	docker compose ps |
| 	@echo "---" |
| 	@echo "Ollama models:" |
| 	docker exec voute_ollama ollama list |

| Componente | Tecnología | Puerto / Ubicación |
| Orquestador de flujos | n8n | localhost:5678 |
| Servidor LLM local | Ollama | localhost:11434 |
| Base de datos | PostgreSQL 16 | localhost:5432 (interno) |
| Cola de tareas | Redis 7 | localhost:6379 (interno) |
| Biblioteca web | nginx + HTML | localhost:8080 |
| Conversor PDF | Pandoc | interno vía Docker exec |
| Escritura principal | dolphin-mixtral | vía Ollama |
| Edición | dolphin-llama3 | vía Ollama |
| Coordinación / Crítica | llama3.1:8b | vía Ollama |
| Checkpoints | Telegram Bot | vía n8n Telegram node |
| Repositorio del universo | GitHub | LaVouteDAnais |
| Formatos de salida | Markdown + PDF + HTML | voute_data/03_Literatura/ |

