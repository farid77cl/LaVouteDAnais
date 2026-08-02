# 👠 Lista GPU — Regeneración de poses (02/08/2026)

Poses a re-generar vía app (Gemini). El **prompt ya está correcto** en `galeria_outfits.md`
en todos estos casos salvo donde se indique — el fallo fue de generación (drift), no de texto.

## 🔴 Prioridad 1 — defectos confirmados a ojo (auditoría visual 02/08)

| Look | Pose(s) | Motivo | Acción |
|---|---|---|---|
| **L774** Blush Maid | `standing` | Salió vestido **negro** de látex + medias de red en vez del maid blush. Las otras 6 poses correctas. | Re-roll con el prompt actual (dice "blush maid", correcto) |
| **L786** Angular Couture | `standing`, `back_view`, `ditzy`, `pov` | Perdieron la silueta canónica (vestido largo plateado + hombros angulares). **Referencia (gold): Seated / Side Profile / Odalisque.** | Re-roll; si reincide, reforzar `floor-length` + `angular shoulder architecture` en el positivo |
| **L772** Pearl Boardroom | `seated` | **Watermark de texto** fantasma ("RAI?TIRIO") + sujetador negro sheer que las otras poses no llevan | Re-roll (negativo ya veta lettering/logo; añadir `watermark` si reincide) |

## 🟡 Prioridad 2 — opcional (drift leve)

| Look | Pose | Motivo |
|---|---|---|
| **L771** Salt Flat Pole | `ditzy` | Copa con keyhole + choker/pulseras que las otras 6 no tienen |

## 🟢 Prioridad 3 — realizar el fix de Back View (anti-reverso)

Se ancló la orientación de **71 back-views** de prendas de frente abierto (commit `891abbd2e`).
Las imágenes ya subidas NO cambian solas — hay que **re-generar la `back_view`** de esos looks
para materializar el fix, y **solo donde la imagen actual se vea con el blazer/bata al revés**
(varias sobrevivientes ya salieron bien). Priorizar los corporate/blazer recientes:
**L713, L732, L752, L772, L782, L786** · y los históricos si al mirarlos están reversados.

> El listado completo de los 71 looks anclados está en el commit `891abbd2e`
> (galeria_outfits.md + galeria_outfits_archivo.md, slot Back View).

## ⏳ Pendiente de mirar a píxel (para completar la P1)
Barrido visual de los ~27 looks recientes que aún no auditué (L700-L731 salvo los 4 vistos,
L773, L775-L785, L787-L800). Esa pasada puede sumar más poses a la Prioridad 1.
