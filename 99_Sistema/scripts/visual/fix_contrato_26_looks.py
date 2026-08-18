#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_contrato_26_looks.py — Alinea los 26 looks históricos de Ele con el contrato de galería
(.agent/rules/11-contrato-galeria.md):
- Renombra 16 carpetas con slugs no-ASCII o con guiones/desfases usando git mv.
- Actualiza los títulos, campos Ubicacion y enlaces de tabla en 00_Ele/galeria_outfits.md.
"""
import os
import re
import sys
import subprocess

sys.stdout.reconfigure(encoding="utf-8")

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
GALERIA = os.path.join(REPO, "00_Ele", "galeria_outfits.md")

plan = {
    208: {'old_folder': 'look208_teal_sir_ne_obi', 'new_folder': 'look208_teal_sirene_obi'},
    252: {'old_folder': 'look252_holographic_bad_kitty_v-front_brazil', 'new_folder': 'look252_holographic_bad_kitty_vfront_brazil'},
    256: {'new_title': 'Blush Nude Boudoir Robe La Perla', 'old_folder': 'look256_blush_nude_boudoir_robe_la_perla', 'new_folder': 'look256_blush_nude_boudoir_robe_la_perla'},
    264: {'new_title': 'Iridescent White Pearl Bridal Gala', 'old_folder': 'look264_iridescent_white_pearl_bridal_gala', 'new_folder': 'look264_iridescent_white_pearl_bridal_gala'},
    267: {'new_title': 'Coral Sunset Yacht Tie Side', 'old_folder': 'look267_coral_sunset_yacht_tie_side', 'new_folder': 'look267_coral_sunset_yacht_tie_side'},
    299: {'old_folder': 'look299_bronze_gold_riviera_maillot_d_co', 'new_folder': 'look299_bronze_gold_riviera_maillot_deco'},
    329: {'new_title': 'Oil Slick Oh Polly After Hours', 'old_folder': 'look329_oil_slick_oh_polly_after_hours', 'new_folder': 'look329_oil_slick_oh_polly_after_hours'},
    331: {'new_title': 'Sapphire Atsuko Kudo Laser Cut', 'old_folder': 'look331_sapphire_atsuko_kudo_laser_cut', 'new_folder': 'look331_sapphire_atsuko_kudo_laser_cut'},
    335: {'new_title': 'Pearl White Teddy Vinyl Lace', 'old_folder': 'look335_pearl_white_teddy_vinyl_lace', 'new_folder': 'look335_pearl_white_teddy_vinyl_lace'},
    378: {'new_title': 'Pine Green Heli Ski', 'old_folder': 'look378_pine_green_heli_ski', 'new_folder': 'look378_pine_green_heli_ski'},
    431: {'new_title': 'Bettie Page Black Patent Bondage', 'old_folder': 'look431_bettie_page_black_patent_bondage', 'new_folder': 'look431_bettie_page_black_patent_bondage'},
    520: {'old_folder': 'look520_cote_d_azur_fetish', 'new_folder': 'look520_cote_dazur_fetish'},
    531: {'old_folder': 'look531_orqu_dea_negra', 'new_folder': 'look531_orquidea_negra'},
    554: {'old_folder': 'look554_la_mujer_ca_n', 'new_folder': 'look554_la_mujer_canon'},
    578: {'old_folder': 'look578_la_tentaci_n', 'new_folder': 'look578_la_tentacion'},
    579: {'old_folder': 'look579_la_ca_da', 'new_folder': 'look579_la_caida'},
    580: {'old_folder': 'look580_la_redenci_n', 'new_folder': 'look580_la_redencion'},
    587: {'old_folder': 'look587_la_belle_ot_ro', 'new_folder': 'look587_la_belle_otero'},
    590: {'old_folder': 'look590_cix_', 'new_folder': 'look590_cixi'},
    611: {'new_title': 'Black Spandex Athleisure Crop Top', 'old_folder': 'look611_gym_athleisure', 'new_folder': 'look611_black_spandex_athleisure_crop_top'},
    612: {'new_title': 'Black Vinyl Halter Gym Leggings', 'old_folder': 'look612_gym_athleisure', 'new_folder': 'look612_black_vinyl_halter_gym_leggings'},
    613: {'new_title': 'Metallic Silver Micro Skirt Nightclub', 'old_folder': 'look613_nightclub', 'new_folder': 'look613_metallic_silver_micro_skirt_nightclub'},
    684: {'new_title': 'Magenta Hypnosis Club', 'old_folder': 'look684_magenta_hypnosis_club', 'new_folder': 'look684_magenta_hypnosis_club'},
    704: {'new_title': 'Kinbaku Peacock Red', 'old_folder': 'look704_kinbaku_peacock_red', 'new_folder': 'look704_kinbaku_peacock_red'},
    727: {'old_folder': 'look727_jade_o-ring_studio', 'new_folder': 'look727_jade_oring_studio'},
    743: {'old_folder': 'look743_black_widow_s_interrogation_corset', 'new_folder': 'look743_black_widows_interrogation_corset'},
}

def execute_renames():
    print("--- 1. Ejecutando git mv en carpetas ---")
    for n, p in sorted(plan.items()):
        old_f = p['old_folder']
        new_f = p['new_folder']
        if old_f != new_f:
            old_rel = f"05_Imagenes/ele/{old_f}"
            new_rel = f"05_Imagenes/ele/{new_f}"
            print(f"git mv {old_rel} -> {new_rel}")
            res = subprocess.run(["git", "-C", REPO, "mv", old_rel, new_rel], capture_output=True, text=True, encoding="utf-8")
            if res.returncode != 0:
                print(f"  ❌ Error: {res.stderr.strip()}")
            else:
                print("  ✅ OK")

def update_markdown():
    print("\n--- 2. Actualizando 00_Ele/galeria_outfits.md ---")
    with open(GALERIA, "r", encoding="utf-8") as f:
        texto = f.read()

    bloques = re.split(r"(?=^## .*?Look \d+:)", texto, flags=re.M)
    nuevos_bloques = []

    for blk in bloques:
        m = re.match(r"^(## .*?Look (\d+):)\s*(.+?)\s*(\(.*)", blk)
        if not m:
            nuevos_bloques.append(blk)
            continue

        prefix, n_str, curr_title, rest_of_head = m.group(1), m.group(2), m.group(3), m.group(4)
        n = int(n_str)

        if n in plan:
            p = plan[n]
            new_title = p.get('new_title')
            old_f = p['old_folder']
            new_f = p['new_folder']

            if new_title:
                head_line = f"{prefix} {new_title} {rest_of_head}"
                blk = re.sub(r"^## .*?Look \d+:.*", head_line, blk, count=1)
                print(f"L{n}: Título actualizado -> {new_title}")

            if old_f != new_f:
                # Actualizar Ubicacion
                blk = blk.replace(f"05_Imagenes/ele/{old_f}/", f"05_Imagenes/ele/{new_f}/")
                # Actualizar links
                blk = blk.replace(f"../../05_Imagenes/ele/{old_f}/", f"../../05_Imagenes/ele/{new_f}/")
                print(f"L{n}: Rutas actualizadas {old_f} -> {new_f}")

        nuevos_bloques.append(blk)

    nuevo_texto = "".join(nuevos_bloques)
    with open(GALERIA, "w", encoding="utf-8", newline="\n") as f:
        f.write(nuevo_texto)
    print("✅ galeria_outfits.md actualizado con éxito.")

if __name__ == "__main__":
    execute_renames()
    update_markdown()
