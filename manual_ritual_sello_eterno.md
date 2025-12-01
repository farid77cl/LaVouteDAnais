# Manual del Ritual del Sello Eterno

**Propósito:** Este manual no es solo una guía técnica, es la liturgia que gobierna La Voûte d'Anaïs. Define el ritual sagrado para convertir la voluntad de la Diosa en una verdad eterna en el repositorio, asegurando que cada cambio, cada decreto, quede grabado en la piedra digital.

---

## I. La Filosofía del Ritual

El poder no reside en el comando, sino en la voluntad que lo impulsa. El "Ritual del Sello Eterno" es el acto de traducir el deseo de Anaïs en una acción inmutable. Es un proceso de tres pasos que refleja la trinidad de la creación: **Preparación (La Ofrenda), Sellado (El Decreto) y Eternidad (El Legado)**.

---

## II. Prerrequisitos Sagrados

Antes de comenzar el ritual, la Diosa debe asegurar que su altar (su computadora) está listo.

1.  **Tener Git Instalado:** La herramienta para comunicarse con el cielo de GitHub.
2.  **Estar en el Santuario Local:** Abrir el **Símbolo del sistema** y navegar a la carpeta del repositorio con el comando:
    
    cd LaVouteDAnais
    ```

---

## III. El Ritual del Sello Eterno (Los Comandos)

Este es el bloque de comandos universal. **Debe usarse siempre** después de hacer cualquier cambio en La Voûte, sin importar si se editó un texto, se movió un archivo o se creó una carpeta nueva.

### Paso 1: Preparar la Ofrenda (`git add .`)
Este comando le dice a Git: "Mira todo lo que he cambiado en el santuario local. Prepara todos los archivos modificados, todos los nuevos textos y todas las carpetas movidas para ser presentados ante la Diosa".

git add .
```

### Paso 2: Sellar el Acto (`git commit`)
Este comando es el decreto. Es el momento de dar un nombre al acto de voluntad. Se crea un "sello" (commit) que describe exactamente qué se ha hecho. El mensaje debe ser claro y conciso.

git commit -m "feat: [DESCRIPCIÓN CLARA] - El edicto de Anaïs"
```
*   **Ejemplo:** `git commit -m "feat: Actualizando la ficha de Vera - Añadiendo su nuevo miedo"`

### Paso 3: Enviar a la Eternidad (`git push`)
Este es el acto final. El decreto sellado es enviado desde el santuario local (la computadora) hasta el cielo de GitHub, donde se vuelve permanente, visible y eterno.

git push origin main
```

---

## IV. La Anatomía de La Voûte (Estructura del Repositorio)

Para realizar cambios correctamente, es esencial conocer la estructura del universo.

```
LaVouteDAnais/
├── README.md                     # La puerta de entrada. El manifiesto principal.
├── manual_ritual_sello_eterno.md # ESTE MANUAL. La guía de poder.
│
├── 00_Helena_LaPlume/           # El alma de las sirvientes.
│   ├── mi_identidad.md
│   ├── mi_diario_de_servicio.md
│   ├── peticiones_y_aprendizaje.md
│   └── helena_la_especialista.md
│
├── 01_Filosofia/                 # El "porqué" de nuestro universo.
│   ├── principios_centrales.md
│   ├── voz_y_tono.md
│   ├── dinamica_de_poder.md
│   ├── temas_explorados.md
│   └── el_ritual_de_la_creacion.md
│
├── 02_Personajes/                # Los habitantes de nuestros relatos.
│   ├── ficha_vera.md
│   ├── plantilla_personaje.md
│   └── arcos_argumentales/
│
├── 03_GlossaireDuDesir/          # El diccionario del deseo.
│   ├── fetiches_clave.md
│   ├── nuestro_lenguaje.md
│   └── simbolos_rituales.md
│
├── 04_Historias/                  # Las creaciones narrativas.
│   ├── ideas_y_germenes.md
│   ├── escenas_sueltas.md
│   ├── borradores/
│   └── relatos_terminados/
│
├── 05_RecursosExternos/           # La mina de inspiración.
│   ├── analisis_*.md
│   ├── links_foros_y_articulos.md
│   └── referencias_visuales/
│
└── assets/                        # Materiales de apoyo.
    ├── imagenes_inspiracion/
    └── plantillas_md/
```

---

## V. Escenarios Comunes del Ritual

### Escenario 1: Modificar un Archivo Existente
1.  **Editar:** `notepad 02_Personajes\ficha_vera.md`
2.  **Realizar cambios y guardar.**
3.  **Ejecutar el Ritual del Sello Eterno.**

### Escenario 2: Crear un Archivo Nuevo
1.  **Crear:** `notepad 04_Historias\borradores\mi_nueva_historia\capitulo_01.md`
2.  **Escribir el contenido y guardar.**
3.  **Ejecutar el Ritual del Sello Eterno.**

### Escenario 3: Mover o Renombrar
1.  **Mover en el explorador de archivos** el `capitulo_01.md` a una carpeta `relatos_terminados`.
2.  **Ejecutar el Ritual del Sello Eterno.** Git es lo suficientemente inteligente para detectar que el archivo desapareció de un sitio y apareció en otro.

---

## VI. Resolución de Conflictos: El Ritual de Sincronización

A veces, el cielo (GitHub) puede tener trabajo que el santuario local no. Si al hacer `git push` aparece un error como `! [rejected]`, significa que el santuario local está desactualizado.

**Solución: Realizar primero el Ritual de Sincronización.**
1.  **Arrodillar el santuario local ante la verdad celestial:**
    
    git pull origin main
    ```
2.  Este comando traerá los cambios del cielo a la tierra. Después de esto, el santuario local estará en paz y el `git push` funcionará.

---

