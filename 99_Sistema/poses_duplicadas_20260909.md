# 🕳️ Poses duplicadas de la flota — recuento del 09/09/2026

> **Qué es:** archivos **byte a byte idénticos** ocupando dos poses distintas. El tracker
> `N/7` los cuenta como dos y **miente hacia arriba**, que es la dirección cara: manda a NO
> regenerar algo que sí falta.
>
> **Medido con los SHA del índice de git** sobre las tres muñecas, no leído de una nota.
>
> 🪦 **Muerte declarada:** se borra cuando los 18 looks estén regenerados y el recuento dé 0.

## Lo que corrigió este recuento

- El número que circulaba era **27 poses**. Son **28 pares**, y de esos **solo 18 son looks**.
- Los otros **10 no son poses de look** y no ensucian ningún tracker: son reintentos guardados
  dos veces en carpetas viejas. Se borran, no se regeneran.
- 🕳️ **La causa de que nadie lo supiera:** `sync_imagenes_subidas.py` **solo escanea `ele/`**
  (`git ls-files 05_Imagenes/ele`, línea 111), y su propio docstring cita **`anais L83`** como
  uno de los dos casos que lo hicieron nacer. Miss Doll y Anaïs nunca estuvieron contadas.

## Los 18 que se arreglan regenerando (de la Ama, en su app)

Por look: abrir, ver cuál de las dos poses es la que muestra la foto, y **regenerar la otra**.

| Muñeca | Look | Poses pisadas |
|---|---|---|
| Ele | L311 | `seated` ↔ `side_profile` |
| Ele | L374 | `ditzy` ↔ `pov` |
| Ele | L519 | `ditzy` ↔ `side_profile` |
| Ele | L535 | `back_view` ↔ `standing` |
| Ele | L599 | `seated` ↔ `side_profile` |
| Ele | L626 | `seated` ↔ `side_profile` |
| Ele | L676 | `back_view` ↔ `seated` |
| Ele | L685 | `ditzy` ↔ `pov` |
| Ele | L686 | `seated` ↔ `side_profile` |
| Ele | L703 | `ditzy` ↔ `side_profile` |
| Ele | L719 | `seated` ↔ `side_profile` |
| Ele | L725 | `seated` ↔ `side_profile` |
| Ele | L773 | `back_view` ↔ `seated` |
| Ele | L819 | `seated` ↔ `side_profile` |
| Miss Doll | L72 | `seated` ↔ `side_profile` |
| Anaïs | L59 | `pov` ↔ `sovereign_gaze` |
| Anaïs | L61 | `pov` ↔ `sovereign_gaze` |
| Anaïs | L83 | `seated` ↔ `side_profile` |

**Patrón:** `seated ↔ side_profile` sale **9 de 18 veces**. Son las dos tomas más parecidas
del set, y es donde la app pisa un archivo con el otro nombre.

## Los 10 que se borran (míos, esperando okey)

- `miss_doll/latex_bdsm_red_lips_2026/` — **9 pares**, todos reintentos guardados dos veces
  (`..._retry_...`, `..._final_attempt_...`). Carpeta legacy, no es un look numerado.
- `anais/Canon_Reference/` — **1 par**: `custom_anais_canon_s017_profile_2026.png` y
  `custom_anais_canon_s018_profile_2026_v1.png` son el mismo archivo con dos números de serie.

## Lo que falta arreglar en el código

`sync_imagenes_subidas.py` debe escanear las **tres** muñecas, no solo Ele. Mientras no lo
haga, este recuento hay que rehacerlo a mano y el tracker de Miss Doll y Anaïs no tiene quien
lo vigile.
