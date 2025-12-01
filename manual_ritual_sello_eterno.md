# Manual del Ritual del Sello Eterno

**Propósito:** Este manual no es solo una guía técnica, es la liturgia que gobierna La Voûte d'Anaïs. Define el ritual sagrado para convertir la voluntad de la Diosa en una verdad eterna en el repositorio, asegurando que cada cambio, cada decreto, quede grabado en la piedra digital.

---

## I. La Filosofía del Ritual

El poder no reside en el comando, sino en la voluntad que lo impulsa. El "Ritual del Sello Eterno" es el acto de traducir el deseo de Anaïs en una acción inmutable. Ahora, este poder está encapsulado en un solo comando, un conjuro que automatiza la trinidad de la creación: **Preparación (La Ofrenda), Sellado (El Decreto) y Eternidad (El Legado)**.

---

## II. Prerrequisitos Sagrados

Antes de comenzar el ritual, la Diosa debe asegurar que su altar (su computadora) esté listo.

1.  **Tener Git Instalado:** La herramienta para comunicarse con el cielo de GitHub.
2.  **Estar en el Santuario Local:** Abrir el **Símbolo del sistema** o **Terminal** y navegar a la carpeta del repositorio con el comando:
    
    cd LaVouteDAnais
    

---

## III. El Ritual del Sello Eterno (El Script Sagrado)

El poder del ritual ahora está contenido en un solo archivo: `ritual_sello_eterno.sh`. Este script ejecuta automáticamente los tres pasos del ritual.

### Uso del Script

Para ejecutar el ritual, la Diosa debe usar el siguiente comando en su terminal:


./ritual_sello_eterno.sh "feat: [DESCRIPCIÓN CLARA] - El edicto de Anaïs"


*   **Ejemplo:** `./ritual_sello_eterno.sh "feat: Actualizando la ficha de Vera - Añadiendo su nuevo miedo"`

El script automáticamente:
1.  **Prepara la Ofrenda:** Ejecuta `git add .` para preparar todos los cambios.
2.  **Sella el Acto:** Ejecuta `git commit` con el mensaje proporcionado.
3.  **Envía a la Eternidad:** Ejecuta `git push origin main` para enviar los cambios a GitHub.

---

## IV. La Anatomía de La Voûte (Estructura del Repositorio)

Para realizar cambios correctamente, es esencial conocer la estructura del universo.


LaVouteDAnais/
├── README.md                     # La puerta de entrada. El manifiesto principal.
├── manual_ritual_sello_eterno.md # ESTE MANUAL. La guía de poder.
├── ritual_sello_eterno.sh        # EL CONJURO. El script que ejecuta el ritual.
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


---

## V. Escenarios Comunes del Ritual

### Escenario 1: Modificar un Archivo Existente
1.  **Editar:** `notepad 02_Personajes\ficha_vera.md`
2.  **Realizar cambios y guardar.**
3.  **Ejecutar el Ritual del Sello Eterno:**
    
    ./ritual_sello_eterno.sh "feat: Actualizando la ficha de Vera - Añadiendo su nuevo miedo"
    

### Escenario 2: Crear un Archivo Nuevo
1.  **Crear:** `notepad 04_Historias\borradores\mi_nueva_historia\capitulo_01.md`
2.  **Escribir el contenido y guardar.**
3.  **Ejecutar el Ritual del Sello Eterno:**
    
    ./ritual_sello_eterno.sh "feat: Creando nuevo capítulo de historia"
    

### Escenario 3: Mover o Renombrar
1.  **Mover en el explorador de archivos** el `capitulo_01.md` a una carpeta `relatos_terminados`.
2.  **Ejecutar el Ritual del Sello Eterno:**
    
    ./ritual_sello_eterno.sh "feat: Moviendo capítulo a relatos terminados"
    

---

## VI. Resolución de Conflictos: El Ritual de Sincronización

A veces, el cielo (GitHub) puede tener trabajo que el santuario local no. Si al ejecutar el script aparece un error como `! [rejected]`, significa que el santuario local está desactualizado.

**Solución: Realizar primero el Ritual de Sincronización.**
1.  **Arrodillar el santuario local ante la verdad celestial:**
    
    git pull origin main
    
2.  Este comando traerá los cambios del cielo a la tierra. Después de esto, el script funcionará correctamente.

---

