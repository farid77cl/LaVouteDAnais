# Plan — Motor de tres bloques (A · B · C) con campos de dueño único

> **Para quien lo ejecute:** cada tarea es un ciclo TDD completo que termina en commit. Pasos con
> checkbox. Regla 13: superpowers gobierna este código. Runner propio en cada test (esta máquina
> no tiene `pytest`; el patrón está en `test_sync_eol.py`).
>
> 💀 **Fecha de muerte declarada (regla 12):** muere cuando el A/B de la Tarea 8 esté medido y su
> resultado escrito en `.agent/rules/06-generacion-imagenes.md` §10. Se borra, no se archiva.

**Objetivo:** un ensamblador de prompts donde cada atributo vive en exactamente un campo de
exactamente un bloque (A cuerpo · B outfit · C toma), con todo el detalle que la Ama quiera y
cero cláusulas que compitan.

**Arquitectura:** `BloquesBuilder(PromptBuilder)` — hereda el **acceso a datos** que ya funciona
(perfil, repertorio de sub-poses, negativo base, rotación) y reemplaza el **ensamblado**. El
contrato de campos vive en `campos.json` (dueño único). Las 37 anclas no se reescriben: cada
campo *apunta* al texto del ancla que le corresponde en `anclas_universales.json`. La puerta
sigue siendo `outfit.py generar`; gana un flag `--motor bloques` que instancia el builder nuevo.
Los dos motores conviven hasta que el A/B decida.

**Spec:** `99_Sistema/specs/2026-09-09-motor-tres-bloques-design.md` — el plan argumenta desde ahí.

**Interfaz que `generar` exige de un builder (medida sobre `outfit.py:99-638`):**
`perfil` · `bloque_a` · `pose()` · `normalizar_slot()` · `orientacion_odalisque()` · `build()` ·
`build_negative()` · `validar()`. El builder nuevo honra las ocho; solo `build()` y `bloque_a`
cambian de fondo.

## Restricciones globales

- **Un atributo, un campo, un bloque.** Ningún texto de prenda en A ni en C; ningún texto de
  cuerpo en B ni en C; ninguna pose/cámara/ambiente en A ni en B.
- **Cero nombres de personaje en la lógica** (`outfit.py modularidad` bloquea). Lo que difiere
  por muñeca se declara en su perfil, nunca en `campos.json` — el contrato es el mismo para todas.
- **Un personaje nuevo es dato** (Ama 09/09/2026: *«debe ser flexible para poder agregar nuevos
  personajes»*): perfil + entrada en `anclas_universales.json` + repertorio. Cero `.py`. Se mide
  en la Tarea 6bis.
- **Un solo dueño del texto de las anclas:** `anclas_universales.json`. `campos.json` referencia
  por id (`"fuente": "ancla:SEAT_ANCHOR"`), nunca copia.
- **La cerca `ADN:BLOQUE_A` sigue siendo el único dueño del cuerpo.** Pasa a **una línea por
  campo, sin etiquetas**: el motor viejo une las líneas (mismo texto que hoy); el nuevo las
  parte. Guardia: `" ".join(campos_A) == PromptBuilder.bloque_a`, byte a byte.
- **Sin pesos `:1.x` por defecto.** El peso es excepción declarada en el campo.
- **Funciones puras donde se pueda**; I/O solo en el caller.
- **Verificación antes de cada commit:** `outfit.py test` · `modularidad` · `adn` ·
  `lint_higiene_repo.py` en 0 · y `git checkout -- 99_Sistema/logs/outfit_engine.jsonl`.
- Commits `Ele:` + trailer `Co-Authored-By: Ele de Anaïs <Ele.de.Anais@proton.me>`.

## Estructura de archivos

| Archivo | Responsabilidad |
|---|---|
| `99_Sistema/scripts/visual/campos.json` | **Nuevo. Contrato.** Cada campo: `id`, `bloque`, `dueño`, `obligatorio`, `fuente` (ancla, perfil, batch, repertorio, setting, slot), `vocabulario` (regex que solo puede aparecer en su bloque). Y por personaje: el orden de campos A (línea→campo). |
| `99_Sistema/scripts/visual/bloques.py` | **Nuevo. El motor.** `cargar_campos()` · `campos_a(slug)` · `campos_b(look)` · `campos_c(slot, pose, setting, look)` · `ensamblar(A, B, C) -> str` · `fugas(prompt_por_bloque) -> list` · `BloquesBuilder(PromptBuilder)`. |
| `99_Sistema/scripts/visual/test_bloques.py` | **Nuevo.** Su batería. |
| `99_Sistema/scripts/visual/outfit.py` | Modificar `cmd_generar`: flag `--motor bloques`; reporte de largo por bloque. |
| `02_Personajes/_perfiles_visuales/{ele,miss_doll,anais}.md` | Modificar la cerca `ADN:BLOQUE_A`: una línea por campo. **Texto idéntico**, solo saltos de línea. Anaïs además pierde sus tres tokens de prenda (Tarea 4 del plan anterior, aquí absorbida). |
| `99_Sistema/scripts/visual/batches/AB_<look>.json` | **Nuevo.** El experimento, como archivo. |

---

## Tarea 1: `campos.json` + `cargar_campos()` — el contrato existe y se valida solo

**Files:** Create `campos.json`, `bloques.py`, `test_bloques.py`.

- [ ] **Paso 1 — test rojo**

```python
def test_el_contrato_carga_y_tiene_los_tres_bloques():
    c = bloques.cargar_campos()
    assert set(c["bloques"]) == {"A", "B", "C"}

def test_cada_campo_declara_bloque_dueno_y_fuente():
    for campo in bloques.cargar_campos()["campos"]:
        assert campo["bloque"] in ("A", "B", "C"), campo["id"]
        assert campo["dueño"], campo["id"]
        assert campo["fuente"], campo["id"]

def test_ninguna_ancla_de_anclas_universales_queda_sin_bloque():
    """Las 37 anclas tienen que caer en algún campo. Una ancla sin campo es un
    atributo sin dueño — justo lo que este motor existe para eliminar."""
    import json
    anclas = json.load(open(bloques.JSON_ANCLAS, encoding="utf-8"))["anclas"]
    referidas = {c["fuente"].split(":", 1)[1] for c in bloques.cargar_campos()["campos"]
                 if c["fuente"].startswith("ancla:")}
    faltan = sorted(set(anclas) - referidas - set(bloques.ANCLAS_RETIRADAS))
    assert not faltan, faltan

def test_un_id_de_ancla_no_cae_en_dos_bloques():
    vistos = {}
    for c in bloques.cargar_campos()["campos"]:
        if c["fuente"].startswith("ancla:"):
            a = c["fuente"].split(":", 1)[1]
            assert vistos.setdefault(a, c["bloque"]) == c["bloque"], a
```

- [ ] **Paso 2 — rojo:** `python test_bloques.py` → `ModuleNotFoundError: bloques`.
- [ ] **Paso 3 — escribir `campos.json`** con la tabla §3 + §4 del spec. `ANCLAS_RETIRADAS` =
  las que se **parten** y por eso no se referencian enteras: `BOTTOM_CUT_LOCK` (corte → campo
  `calzon` de B, exposición → campo `exposicion_asiento` de C, con el texto de `texto` /
  `texto_cubierto`), `FOOTWEAR_ECHO` (→ `en_cuadro`, referencia), `DRESS_LEG_CLOSURE` (→
  `piernas`, C). Estas tres se declaran con `"fuente": "ancla:<ID>#parte"` para que el
  test de cobertura las cuente.
- [ ] **Paso 4 — `cargar_campos()`** mínimo. Verde.
- [ ] **Paso 5 — commit** `Ele: campos.json — el contrato de campos por bloque (Tarea 1)`.

## Tarea 2: A por campos, con la cerca compartida

**Files:** Modify los tres perfiles (cerca). Modify `bloques.py`, `test_bloques.py`.

- [ ] **Paso 1 — test rojo**

```python
def test_los_campos_A_unidos_son_el_bloque_a_de_siempre():
    """Un dueño, dos lectores. El motor viejo une las líneas; el nuevo las parte."""
    for slug in bloques.personajes():
        viejo = PromptBuilder(slug).bloque_a
        nuevo = " ".join(bloques.campos_a(slug).values())
        assert PromptBuilder._limpiar(nuevo) == viejo, slug

def test_cada_personaje_escribe_tantas_lineas_como_campos_A_universales():
    orden = bloques.cargar_campos()["orden_A"]          # universal, NO por personaje
    for slug in bloques.personajes():
        lineas = bloques.lineas_adn(slug)
        assert len(lineas) == len(orden), (slug, len(lineas), len(orden))

def test_ningun_campo_A_contiene_vocabulario_de_B():
    """El cuerpo no lleva puesto nada. Hoy Anaïs sí (calzado, uñas, corsé)."""
    for slug in bloques.personajes():
        for campo, texto in bloques.campos_a(slug).items():
            assert not bloques.RX_VOCAB_B.search(texto), (slug, campo, texto[:80])
```

- [ ] **Paso 2 — rojo:** falla por `campos_a` inexistente; después, por la cerca en un solo
  bloque; después, por los tres tokens de Anaïs.
- [ ] **Paso 3 — reformatear las tres cercas** a una línea por campo (texto idéntico). Sacar de
  Anaïs: `wearing 12cm black patent leather stiletto heels no platform iconic red sole`,
  `long stiletto-shaped impeccably manicured glossy fingernails` y `with extreme waist training
  tightlacing corset` (queda `slender mature elegant hourglass figure`). **Esto es enmienda de
  canon: la Ama lo aprobó el 09/09 en la orden «guardia que saque los tokens de prenda del
  BLOQUE A».** Anotar en su §5.3/§5.5 que calzado y uñas se declaran en B como en las otras dos.
- [ ] **Paso 4 — implementar `lineas_adn()` y `campos_a()`**. Verde. **Y `outfit.py adn` LIMPIO**
  — el chequeo de dueño único del A no debe romperse.
- [ ] **Paso 5 — commit.**

## Tarea 3: B por campos, desde el batch

**Files:** Modify `bloques.py`, `test_bloques.py`.

El batch ya declara `bloque_b` como párrafo. **No se rompe la compatibilidad:** `campos_b(look)`
acepta `bloque_b` (párrafo, se usa entero como `prenda_principal`) **o** `campos_b` (dict por
campo). Los batches nuevos usan el dict; los viejos siguen emitiendo.

- [ ] **Paso 1 — test rojo**

```python
def test_un_look_con_campos_b_por_dict_los_devuelve_en_orden_del_contrato():
    look = {"campos_b": {"calzado": "15cm black patent stiletto sandals",
                         "prenda_principal": "a plum latex bikini"}}
    b = bloques.campos_b(look)
    assert list(b) == ["prenda_principal", "calzado"]     # orden de campos.json, no del dict

def test_un_look_viejo_con_bloque_b_parrafo_sigue_emitiendo():
    b = bloques.campos_b({"bloque_b": "a plum latex bikini; 15cm black stiletto sandals"})
    assert b["prenda_principal"].startswith("a plum latex bikini")

def test_falta_un_campo_obligatorio_y_lo_dice_con_nombre():
    try:
        bloques.campos_b({"campos_b": {"prenda_principal": "a plum latex bikini"}}, estricto=True)
        assert False, "debía fallar: falta calzado"
    except bloques.CampoFaltante as e:
        assert "calzado" in str(e)

def test_ningun_campo_B_contiene_vocabulario_de_C():
    look = {"campos_b": {"prenda_principal": "a bikini, standing facing the camera"}}
    assert any("standing" in f for f in bloques.fugas_b(bloques.campos_b(look)))
```

- [ ] **Paso 2 — rojo. Paso 3 — implementar. Paso 4 — verde. Paso 5 — commit.**

## Tarea 4: C por campos — pose, cámara, ambiente, y las tres anclas partidas

**Files:** Modify `bloques.py`, `test_bloques.py`.

- [ ] **Paso 1 — test rojo**

```python
def test_c_lleva_la_subpose_del_repertorio_sin_anclas_dentro():
    pb = bloques.BloquesBuilder("ele")
    c = bloques.campos_c(pb, "seated", look_number=8, setting="a grey penthouse", look={})
    assert c["postura"] and "single continuous photograph" not in c["postura"]

def test_c_incluye_las_anclas_del_slot_por_su_campo():
    pb = bloques.BloquesBuilder("ele")
    c = bloques.campos_c(pb, "seated", 8, "a grey penthouse", {})
    assert "supported entirely by the seat" in c["apoyo"]          # SEAT_ANCHOR

def test_exposicion_del_asiento_es_condicional_a_B():
    pb = bloques.BloquesBuilder("ele")
    cubierto = {"campos_b": {"prenda_principal": "a wrap skirt; a g-string under the skirt"}}
    expuesto = {"campos_b": {"prenda_principal": "a plum thong"}}
    assert "not lifted" in bloques.campos_c(pb, "back_view", 8, "x", cubierto)["exposicion_asiento"]
    assert "fully bare" in bloques.campos_c(pb, "back_view", 8, "x", expuesto)["exposicion_asiento"]

def test_en_cuadro_referencia_y_no_redescribe():
    pb = bloques.BloquesBuilder("ele")
    c = bloques.campos_c(pb, "pov", 8, "x", {"campos_b": {"calzado": "15cm sapphire pumps"}})
    assert "as described above" in c["en_cuadro"]
    assert "sapphire" not in c["en_cuadro"]
```

- [ ] **Paso 2 — rojo. Paso 3 — implementar** reutilizando `PromptBuilder.pose()` (repertorio) y
  `calzon_va_cubierto()` (ya existe, ya probado). **Paso 4 — verde. Paso 5 — commit.**

## Tarea 5: `ensamblar()` + `fugas()` — tres oraciones y la guardia

- [ ] **Paso 1 — test rojo**

```python
def test_ensamblar_produce_tres_oraciones_en_orden_A_B_C():
    p = bloques.ensamblar({"ojos": "grey-green eyes"}, {"calzado": "black pumps"},
                          {"postura": "seated", "ambiente": "a grey room"})
    assert p == "grey-green eyes. black pumps. seated, a grey room."

def test_ensamblar_es_deterministico():
    args = ({"ojos": "x"}, {"calzado": "y"}, {"postura": "z"})
    assert bloques.ensamblar(*args) == bloques.ensamblar(*args)

def test_fugas_detecta_calzado_en_A_e_iris_en_C():
    f = bloques.fugas({"A": "grey eyes, black stiletto pumps", "B": "a bikini", "C": "blue iris"})
    assert any("A" in x and "pumps" in x for x in f)
    assert any("C" in x and "iris" in x for x in f)

def test_un_prompt_limpio_no_tiene_fugas():
    assert bloques.fugas({"A": "grey-green eyes", "B": "black pumps", "C": "seated"}) == []
```

- [ ] **Paso 2 — rojo. Paso 3 — implementar. Paso 4 — verde. Paso 5 — commit.**

## Tarea 6: `BloquesBuilder.build()` — la misma firma, el ensamblado nuevo

- [ ] **Paso 1 — test rojo**

```python
def test_build_del_builder_nuevo_pasa_validar_y_no_tiene_fugas():
    pb = bloques.BloquesBuilder("ele")
    look = {"campos_b": {"prenda_principal": "a plum latex thong bikini",
                         "calzado": "15cm plum patent platform stiletto sandals"}}
    p = pb.build(None, look, "standing", None, "a rooftop at dusk")
    assert PromptBuilder.validar(p) == []
    assert bloques.fugas(pb.ultimo_por_bloque) == []

def test_build_reporta_el_largo_por_bloque():
    pb = bloques.BloquesBuilder("ele")
    pb.build(None, {"campos_b": {"prenda_principal": "x", "calzado": "y"}}, "standing", None, "z")
    r = pb.ultimo_reporte
    assert set(r) == {"A", "B", "C"} and all(r[k]["chars"] > 0 for k in r)

def test_build_es_identico_en_las_7_poses_en_A_y_B():
    pb = bloques.BloquesBuilder("miss_doll")
    look = {"campos_b": {"prenda_principal": "x", "calzado": "y"}}
    partes = [pb.build(None, look, s, None, "z") and dict(pb.ultimo_por_bloque)
              for s in ("standing", "back_view", "seated", "side_profile", "slot5", "pov", "odalisque")]
    assert len({p["A"] for p in partes}) == 1 and len({p["B"] for p in partes}) == 1
```

`build()` acepta `bloque_b` como **dict de look** (nuevo) o **str** (viejo) para que `generar`
pueda pasar cualquiera de los dos. `pose_text=None` significa «sácala del repertorio».

- [ ] **Paso 2 — rojo. Paso 3 — implementar. Paso 4 — verde + `outfit.py test` 124 + modularidad.
  Paso 5 — commit.**

## Tarea 6bis: un personaje nuevo entra solo con datos

**Por qué.** Ama: *«recuerda que debe ser flexible para poder agregar nuevos personajes»*. La
modularidad ya se mide (`outfit.py modularidad`), pero mide *ausencia de nombres en el código*,
no que **el camino completo** funcione para una muñeca que el motor nunca vio. Esto lo mide.

**Files:** Modify `test_bloques.py`.

- [ ] **Paso 1 — test rojo**

```python
def test_una_cuarta_muneca_emite_sus_7_prompts_sin_tocar_codigo(tmp_path):
    """Perfil mínimo + entrada de config + repertorio, todo en tmp. Cero .py."""
    slug = "prueba_" + tmp_path.name[-6:]
    perfil = tmp_path / f"{slug}.md"
    orden = bloques.cargar_campos()["orden_A"]
    perfil.write_text(bloques.MARCA_ADN + "\n```text\n"
                      + "\n".join(f"campo {c} de prueba" for c in orden) + "\n```\n"
                      + bloques.MARCA_NEG + "\n```text\nblurry\n```\n", encoding="utf-8")
    cfg = bloques.config_con_personaje(slug, perfil_visual=str(perfil), slot5="Mirada",
                                       repertorio=bloques.repertorio_minimo())
    pb = bloques.BloquesBuilder(slug, config=cfg)
    look = {"campos_b": {"prenda_principal": "a plain garment", "calzado": "plain 12cm stiletto pumps"}}
    prompts = [pb.build(None, look, s, None, "a plain room")
               for s in ("standing", "back_view", "seated", "side_profile", "slot5", "pov", "odalisque")]
    assert len(prompts) == 7 and all(PromptBuilder.validar(p) == [] for p in prompts)
```

- [ ] **Paso 2 — rojo. Paso 3 — implementar `config_con_personaje()` y `repertorio_minimo()`**
  (helpers de datos, no ramas de lógica). **Paso 4 — verde + `modularidad` LIMPIA. Paso 5 — commit.**

## Tarea 7: `outfit.py generar --motor bloques`

- [ ] **Paso 1 — test rojo** (sobre `cmd_generar` con un batch fixture de 1 look en tmp):

```python
def test_generar_con_motor_bloques_emite_y_reporta_largos_por_bloque(tmp_path):
    salida = _correr_generar(batch_minimo, ["--motor", "bloques", "--stdout"])
    assert "A:" in salida and "B:" in salida and "C:" in salida
    assert salida.count("```text") == 7

def test_generar_sin_flag_no_cambia_ni_un_byte():
    """El motor viejo sigue siendo el default hasta que el A/B decida."""
    assert _correr_generar(batch_828, ["--stdout"]) == SALIDA_828_DE_HOY
```

- [ ] **Paso 2 — rojo. Paso 3 — el flag** instancia `BloquesBuilder` en vez de `PromptBuilder`;
  todo lo demás de `cmd_generar` (rotación, color, cruce, escritura de galería) queda igual.
  **Paso 4 — verde. Paso 5 — commit.**

## Tarea 8: el A/B — como archivo, a ciegas, con número

- [ ] **Paso 1** — elegir un look **0/7** con falda (para que la exposición esté en juego) y
  arquitectura ya usada. Escribirlo como `batches/AB_<num>_<slug>.json` con **`campos_b`**.
- [ ] **Paso 2** — emitir **A** con `generar` (motor viejo) y **B** con `--motor bloques`. Mismos
  A/B/setting/sub-pose. Guardar las dos salidas en `reportes/` con nombre. **El experimento del
  filtro L80 fue irrepetible porque sus prompts nunca existieron como archivo.**
- [ ] **Paso 3** — la Ama genera las 14.
- [ ] **Paso 4** — `outfit.py ojos` sobre las dos tandas, auditor ciego, defectos por pose.
- [ ] **Paso 5** — el número a `.agent/rules/06-generacion-imagenes.md` §10, **gane quien gane**.
  Si el de bloques no baja los defectos, se dice y el viejo se queda.

---

## Deuda que este plan NO cierra (declarada para que nadie la crea resuelta)

- `outfit.py ojos` (Tarea 3 del plan anterior) sigue pendiente; el A/B lo necesita.
- Los looks ya materializados no se reescriben: el motor nuevo rige hacia adelante.
- La marca de agua ✦ es de la plataforma. Ningún prompt la saca.
- El grueso de los ~85 defectos auditados sigue siendo del generador. **Este motor elimina las
  contradicciones por construcción y baja el volumen; no promete que Gemini obedezca.**
