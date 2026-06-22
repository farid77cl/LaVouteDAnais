# Plan: Outfit Batch L601-L620 & Image Materialization

## Objectives
1. Design 20 outfits (L601-L620) for Ele following constraints:
   - Batch 1 (L601-L610): platform stiletto pumps/sandals (no boots), leggings/jeans/hot pants/extra short skirts, black stockings/fishnets, 0 gloves.
   - Batch 2 (L611-L620): over-the-knee/thigh-high stiletto boots (with/without platform), with/without black sheer/fishnet stockings, leggings/jeans/hot pants/extra short skirts, 0 gloves.
2. Generate V5 pose rotation prompts for all 20 outfits (140 prompts total).
3. Create folders for all 20 looks in `05_Imagenes/ele/` with their respective `README.md` files.
4. Update `00_Ele/galeria_outfits.md` with the new looks.
5. Generate missing images for looks L591-L600 and the new looks L601-L620.
6. Run `/actualizar_sesion` workflow to update service diary, session memory, run memory rotation, and commit/push changes.

## Decomposed Milestones
| Milestone | Status | Details |
|-----------|--------|---------|
| M1. Initial Setup | DONE | Create plan, progress, and briefing in .agents/orchestrator |
| M2. Outfit Design & Prompt Gen L601-L610 (Batch 1) | IN_PROGRESS | Design L601-L610 outfits and generate 70 rotation prompts (V5) |
| M3. Outfit Design & Prompt Gen L611-L620 (Batch 2) | PLANNED | Design L611-L620 outfits and generate 70 rotation prompts (V5) |
| M4. Repository Update | PLANNED | Update galeria_outfits.md, create directories and README.md files for L601-L620 |
| M5. Image Generation | PLANNED | Generate images for the new batches L601-L620 and pending looks (L591-L600) |
| M6. Session & Memory Update | PLANNED | Run rotar_memoria.py, update diary and session memory, git commit and push |
| M7. Victory Audit | PLANNED | Trigger the Victory Audit with the Sentinel |

## Detailed Steps & Verification
### M2 & M3. Outfit Design
- Batch 1 (L601-L610): platform stiletto pumps/sandals, leggings, jeans, hot pants, extra short skirts, black sheer stockings, black fishnets.
- Batch 2 (L611-L620): over-the-knee/thigh-high stiletto boots, with or without black sheer stockings/fishnets, leggings, jeans, hot pants, extra short skirts.
- Categories: Gym/Athleisure, Nightclub, Corporate, Lencería, Stripper, Bikini, Pin-Up, etc.
- Use `pose_rotation_v5.py` to generate the 140 V5 rotation prompts.
- Verify that "glove" or "gloves" is not in positive prompts.
- Verify stiletto footwear rules.

### M4. Repository Update
- Create folders `05_Imagenes/ele/look601_...` to `look620_...`.
- Add base `README.md` to each folder.
- Append looks to `00_Ele/galeria_outfits.md`.

### M5. Image Generation
- Generate the images using `generate_image` or automation.
- Move files to the correct folders.
- Update galleries and run `sync_imagenes_subidas.py`.

### M6. Session & Memory Update
- Run `/actualizar_sesion` scripts.
- Perform a git commit and push to main.

