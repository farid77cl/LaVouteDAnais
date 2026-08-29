# 🔧 Prompt #20 · LV-App 2.0 — PASO 2.2: Parche del Parser (el P2.1 compila pero la galería sale vacía)

> **Auditoría del clon real, 27/07/2026.** El P2.1 aterrizó con la arquitectura CORRECTA y verificada — pero con seis nombres de clave equivocados que dejan la galería vacía en el 100% de los casos, online y offline.
> **No anula el P2.1.** Lo parcha. Alcance: un archivo de parseo, un modelo, dos líneas de UI y un test.

---

## 🩺 El diagnóstico (medido sobre el índice real, no opinado)

`IndexApi.parseIndex` lee claves largas. El índice trae claves cortas. Conteo sobre los 242.636 bytes reales de `app_index.json`:

| Lo que el parser busca | Apariciones en el índice | Lo que el índice trae | Apariciones |
|---|---|---|---|
| `"dir"` | **0** | `"d"` | **734** |
| `"portada"` | **0** | `"c"` | **734** |
| `"nPoses"` | **0** | `"np"` | **734** |
| `"poses"` (por look) | **0** | `"p"` | **734** |
| `"titulo"` / `"fecha"` | **0** / **0** | `"t"` / `"f"` | 734 / 734 |

La única clave que coincide es `n`.

**Ruta exacta del fallo:**

1. `IndexApi.kt:44` usa `item.getString("dir")` — variante **estricta**, no `optString`.
2. Lanza `JSONException("No value for dir")` en el **primer look** del array.
3. `LookRepository.refresh()` lo atrapa en `runCatching` → `Result.failure`.
4. `VisualViewModel` pone el error en el flow → `uiState = Success(emptyList(), error)`.
5. La pantalla renderiza: **"No looks found or repository not cloned yet."**

**Y offline es peor:** `LookRepository.loadCached()` (líneas 20-30) usa el mismo parser roto y **se traga la excepción en silencio** (`// Ignore parsing errors on cache`). No muestra ni el error. Por eso la afirmación *"todo funciona sin conexión"* no es verificable: nunca hubo nada cacheado que se pudiera leer.

> **Nota de responsabilidad:** el prompt P2.1 documentó bien el JSON (§ "El índice YA EXISTE") pero en el punto 2c dictó el data class con nombres largos —`Look(n, titulo, fecha, dir, poses, portada, nPoses)`— **sin escribir el mapeo `t→titulo, d→dir, c→portada, np→nPoses`**. La ambigüedad fue del prompt. Este parche la cierra de forma explícita.

## ✅ Lo que NO hay que tocar (está verificado y correcto)

Auditado archivo por archivo en el clon de `farid77cl/LV-app-2` @ `6f3faf8`:

- JGit, `PoseMatcher`, `GitRepository`, `LookLocalDataSource`, `update_libs.sh`, `update_versions.sh` y los 13 logs: **borrados de verdad** (`grep` da vacío; el commit elimina 1.539 líneas).
- Coil 3 coherente: `coil3.compose` contra `io.coil-kt.coil3:3.0.0`. **Cero `import coil.*`**.
- `gradle.properties` con `-Xmx2g`, `parallel=false`, `workers.max=2`, `in-process`. Wrapper completo.
- `INTERNET` en el manifest. SDK 37 coherente. `material-icons` resueltos por el BOM.
- La infraestructura de datos responde: índice `HTTP 200` (242.636 bytes) e imagen concreta `HTTP 200` (593.750 bytes) sobre el raw público.

**La arquitectura del pivote es correcta. Solo hay que arreglar el mapeo de claves.**

---

## 📋 PROMPT PARA PEGAR EN AI STUDIO

```markdown
PASO 2.2 de LV-App 2.0: PARCHE DEL PARSER DEL ÍNDICE.

Repo: farid77cl/LV-app-2 · paquete com.lavoute.app · estado: commit 6f3faf8.

El P2.1 compiló y el APK corre, pero LA GALERÍA SALE VACÍA SIEMPRE. Muestra
"No looks found or repository not cloned yet." tanto con red como sin red.

CAUSA (verificada contra el JSON real, no es una hipótesis):
IndexApi.parseIndex busca las claves "dir", "portada", "nPoses", "poses",
"titulo", "fecha". Ninguna de esas seis existe en app_index.json. El índice usa
claves CORTAS a propósito, para pesar poco. item.getString("dir") lanza
JSONException en el primer look y revienta el parseo entero.

Este es un parche QUIRÚRGICO. NO rehagas la arquitectura, NO agregues
dependencias, NO toques la navegación, el tema, el manifest ni gradle.properties.
Alcance: 4 archivos + 1 test nuevo.

=====================================================================
## 1. LA TABLA DE MAPEO (esto es el corazón del parche)
=====================================================================
Clave JSON  ->  campo del modelo Kotlin
    n       ->  n        (Int)      única que ya coincidía
    t       ->  titulo   (String?)  puede venir JSON null
    f       ->  fecha    (String?)  puede venir JSON null
    d       ->  dir      (String)   carpeta, termina en "/"
    p       ->  poses    (Map<String,String>)  pose canónica -> nombre de archivo
    c       ->  portada  (String)   pose de portada, ya resuelta
    np      ->  nPoses   (Int)      el N de "N/7"
    x       ->  (ignorar) archivos extra sin pose, informativo

Y en la RAÍZ del JSON (no dentro de cada look):
    raw          -> URL base para construir cualquier URL de imagen
    looks        -> el array
    v, generado, poses, total_looks, total_imagenes -> metadata, puedes ignorarla

Ejemplo REAL, copiado literal del índice en producción:

{"v":1,"generado":"2026-07-27",
 "raw":"https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/",
 "poses":["standing","side_profile","seated","back_view","ditzy","pov","odalisque"],
 "total_looks":734,"total_imagenes":4203,
 "looks":[
   {"n":1,"t":null,"f":null,"d":"05_Imagenes/ele/look001_morticia/",
    "p":{"standing":"helena_001_standing.png","seated":"helena_001_seated.png"},
    "c":"standing","np":5,"x":3}
 ]}

=====================================================================
## 2. data/remote/IndexApi.kt — reescribe SOLO parseIndex
=====================================================================
Deja fetchIndexRaw() como está (funciona: el índice responde HTTP 200).

Reemplaza parseIndex por esto:

    fun parseIndex(jsonString: String): AppIndex {
        val root = JSONObject(jsonString)
        val rawBase = root.optString("raw", DEFAULT_RAW)
        val arr = root.optJSONArray("looks") ?: JSONArray()
        val looks = mutableListOf<Look>()
        for (i in 0 until arr.length()) {
            val item = arr.getJSONObject(i)
            val poses = mutableMapOf<String, String>()
            item.optJSONObject("p")?.let { p ->
                p.keys().forEach { k -> poses[k] = p.getString(k) }
            }
            looks.add(
                Look(
                    n = item.getInt("n"),
                    titulo = item.optString("t").takeIf { it.isNotEmpty() },
                    fecha = item.optString("f").takeIf { it.isNotEmpty() },
                    dir = item.optString("d"),
                    poses = poses,
                    portada = item.optString("c"),
                    nPoses = item.optInt("np")
                )
            )
        }
        return AppIndex(raw = rawBase, looks = looks)
    }

REGLAS DURAS de este punto:
- Usa optString/optInt/optJSONObject, NO getString/getInt (salvo "n"). Un look
  con un campo faltante debe degradar, no reventar la lista entera.
- Quita el fallback "trata el JSON como array suelto": el índice SIEMPRE es un
  objeto con "looks". Ese try/catch solo escondía el error.
- DEFAULT_RAW es una const de respaldo:
  "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"

=====================================================================
## 3. domain/model/AppIndex.kt — que lleve la URL base
=====================================================================
    data class AppIndex(val raw: String, val looks: List<Look>)

Hoy la URL base está HARDCODEADA en DOS sitios (IndexApi.kt:17 y
VisualScreen.kt:135). El índice trae el campo "raw" justamente para que no se
duplique. Que viaje por el modelo.

LookRepository debe exponer ese raw junto a los looks (un StateFlow<String> o
dentro del estado; elige lo más simple, pero que la UI lo reciba, NO lo escriba).

=====================================================================
## 4. ui/screens/visual/VisualScreen.kt — 3 arreglos chicos
=====================================================================
a) LookCard: borra la línea
       val rawUrl = "https://raw.githubusercontent.com/..."
   y recibe el raw por parámetro desde el estado. Cero URLs escritas en la UI.

b) El filtro de lotes está hardcodeado hasta "L701-L800" y la flota YA va en el
   look 800. El próximo look desaparece de la grilla. Deriva la lista de lotes
   de los datos:
       looks.maxOf { it.n }  ->  genera los tramos de 100 hasta cubrirlo
   Nada de listas de strings escritas a mano.

c) El texto de estado vacío dice "No looks found or repository not cloned yet."
   La app ya NO clona nada — quedó del diseño anterior. Cámbialo por:
       sin error   -> "No hay looks para este filtro."
       con error   -> "No se pudo cargar el índice: <mensaje>"  + botón Reintentar

=====================================================================
## 5. TEST OBLIGATORIO — sin esto el paso NO se da por hecho
=====================================================================
Crea app/src/test/java/com/lavoute/app/data/remote/IndexApiTest.kt

Este test es el punto MÁS importante del parche. El P2.1 reportó
"testDebugUnitTest BUILD SUCCESSFUL" mientras la app no mostraba ni un look,
porque el único test que existe cuenta rutas de navegación y no toca el parser.
Un BUILD SUCCESSFUL que no prueba el parseo no significa nada.

Debe usar el JSON del punto 1 como string literal (2 looks, uno con "t":null) y
afirmar, como mínimo:

  1. parseIndex(json).looks.size == 2
  2. El look 1 tiene titulo == null y NO lanza excepción
  3. looks[0].dir == "05_Imagenes/ele/look001_morticia/"
  4. looks[0].nPoses == 5
  5. looks[0].poses["standing"] == "helena_001_standing.png"
  6. parseIndex(json).raw termina en "/"
  7. LA ASERCIÓN CLAVE — la URL completa, string exacto:
     looks[0].urlPortada(index.raw) ==
     "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look001_morticia/helena_001_standing.png"

     (Esa URL está verificada: responde HTTP 200, 593.750 bytes.)

PROHIBIDO assertTrue(true) o tests que no afirmen valores concretos.

=====================================================================
## 6. CÓMO COMPILAR (igual que el P2.1 — respétalo)
=====================================================================
  1. ./gradlew --stop
  2. ./gradlew --no-daemon :app:compileDebugKotlin      <- itera con este
  3. ./gradlew --no-daemon :app:testDebugUnitTest
  4. Solo al final: ./gradlew --no-daemon :app:assembleDebug

=====================================================================
## CRITERIO DE ÉXITO
=====================================================================
- Los tres gradlew en verde.
- IndexApiTest pasa con las 7 aserciones.
- Al abrir la pestaña Visual: la grilla se puebla con CENTENARES de looks
  (el índice trae 734), con portada real y badge N/7 real.
- Cero URLs "raw.githubusercontent.com" escritas en la capa de UI.

=====================================================================
## AL TERMINAR, REPORTA (texto, fuera del código)
=====================================================================
- Salida LITERAL de testDebugUnitTest, incluyendo el nombre de IndexApiTest y
  sus casos. No escribas "tests passed": pega las líneas.
- Cuántos looks devuelve parseIndex sobre el índice real, si pudiste probarlo.
- Confirmación de que no queda ninguna URL base escrita en VisualScreen.
- Si NO pudiste con algún punto, DILO explícitamente. No lo omitas.
```

---

## ✅ Cómo verificar antes del paso siguiente

1. **Salida literal** de `testDebugUnitTest` **con el nombre `IndexApiTest`** en ella. Si el nombre no aparece, el test no existe.
2. `grep -rn "raw.githubusercontent" app/src/main/java/com/lavoute/app/ui/` → **vacío**.
3. `grep -n "getString(\"dir\")\|\"portada\"\|\"nPoses\"" app/src/` → **vacío**.
4. **En el teléfono:** la galería muestra cientos de tarjetas, no el cartel de vacío. Esta es la prueba que ningún BUILD SUCCESSFUL reemplaza.
5. **Pushear** desde AI Studio (sus commits no llegan a GitHub hasta que la Ama pushea).

## 🧭 Lección de método para los prompts siguientes

El P2.1 pidió "que compile" y obtuvo exactamente eso: código que compila y no funciona. **Compilar no es un criterio de éxito para una capa de datos.** De aquí en adelante, todo paso que parsee, transforme o suba algo lleva **un test que afirme un valor concreto** — y el reporte debe pegar la salida del test, no del build.
