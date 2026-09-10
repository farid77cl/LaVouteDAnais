# 📊 ESTADO DE MATERIALIZACIÓN (V4.0 — recortado 10/09/2026)

Registro vivo de pendientes de imagen. Se lee en cada `/inicio-ele` — por eso lleva SOLO lo que sigue abierto, con fecha de última verificación. El histórico resuelto (incidentes cerrados, auditorías ya aplicadas, tablas de flota congeladas) vive en `99_Sistema/auditoria_materializacion_historico_20260910.md` — evidencia completa, nunca se borra (regla 12).

## Pendientes vivos

- **Anaïs L91** «Encaje Esmeralda y Astracán»: 0/7 — primer look bajo el veto de corsetería (§5.6bis del perfil), 08/09.
- **Anaïs L95** «Le Smoking Berenjena en el Salón de Fumar»: 0/7 — estreno de la arquitectura S3 (traje sastre), 10/09. Antes de generar sus fotos: revisar si la Ama ya decidió sobre los dos bugs del motor anotados en `memoria_sesiones.md` (GLOSS_LOCK cruzado + prefijo cinematográfico sin inyectar) — este look ya esquiva el primero a mano, pero le falta el prefijo "8k ultra cinematic film noir portrait" que su arquetipo (Noche) pide en §5.7 y que el motor no puso.
- **Ele Look 812**: regenerar Standing/Seated/Back View cuando la Ama vuelva a pasar por la app — el texto ya trae la plataforma corregida (28/08); el hueco de busto es defecto de generación, no de texto, así que puede repetirse.
- **L200-L299**: único rango sin `SKIN_LOCK`/`SINGLE_FRAME` (0/100, medido 22/07/2026) — 21 looks del rango sin materializar; si la app genera ahí, sale con el defecto. Las poses que ya tienen imagen no se tocan.
- **⚠️ Sin re-medir desde 30/08/2026 — verificar contra `git ls-files` antes de asumir vigente:** Ele L813 back_view+pov · L814 seated · L815 back_view · L816 ditzy · Miss Doll L69 back_view · L70 standing · Anaïs L68 standing (auditoría prompt↔imagen del 30/08, anclas reforzadas, pendientes de materializar con el texto ya corregido).
- **Miss Doll L68** "Liquid Rose Catsuit": vetado a propósito por la Ama ("horrible outfit") — se conserva como contraejemplo, no se regenera ni se rediseña.

Flota, último look y materialización agregada: **`00_Ele/memoria_sesiones.md`** (dueño único) — este archivo no repite esos contadores.

## Flujo de imágenes (era app, looks ≥ 291)

Desde L291 la **app Android de la Ama** genera en Gemini y sube los PNG directo al repo en GitHub. El agente las encuentra ya commiteadas tras `git pull`. Al detectar imágenes nuevas:

1. `git pull` — traer lo que subió la app.
2. `python 99_Sistema/scripts/visual/sync_imagenes_subidas.py` — normaliza nombres no-canónicos (`back`→`back_view`, `profile`→`side_profile`) y refresca el tracker `### 📸 Imágenes (N/7)` en `galeria_outfits.md`, solo looks ≥ 291 en "Pendiente"/"parcial". Idempotente, no toca el fleet histórico (<291).
3. `python 99_Sistema/scripts/visual/sync_tracker_galeria_personaje.py [anais|miss_doll]` — mismo tracker para las otras dos muñecas (no lo mantiene `update_galleries.py`).
4. `python 99_Sistema/scripts/visual/update_galleries.py` — regenera READMEs + galería maestra.
5. Commit + push.

⚠️ Sin el paso 2/3 las poses se mapean mal en la galería maestra — la app nombra distinto de como nombra el canon.

## Lecciones permanentes

- **Auditar el repo miente:** las imágenes commiteadas son las sobrevivientes de los reintentos de la Ama — miden éxito post-filtro humano, no la tasa real del prompt. Si dice que tuvo que regenerar, el defecto existe aunque lo guardado se vea limpio.
- **Piso de resolución:** bajo ~0,3 MP (`Image.open(f).size`), "no se ve el defecto" significa "faltan píxeles", no que esté limpio. El 40% de la flota histórica (pre-20/07) quedó en ~286×512 por usar "Copiar" en vez de "Descargar" en Gemini — irrecuperable, la guardia de resolución vive hoy en `uploadImageToGithub` de LV-App y ya no se salta.
- **Un "pendiente" sin fecha de verificación envejece hacia la mentira** — re-medir contra `git ls-files` antes de actuar sobre un estado viejo, nunca contra el disco (sparse-checkout en la máquina literaria).

## Protocolo de actualización

1. **Post-generación:** tras materializar un set, actualizar el pendiente correspondiente aquí (o borrarlo si cerró).
2. **Post-sync:** tras `update_galleries.py`, verificar que los números coincidan con `git ls-files`.
3. **Notificación:** informar a la Ama el nuevo estado en el saludo.
