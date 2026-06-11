#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rotar_memoria.py — Autopoda de la memoria de sesiones.

Mantiene `00_Ele/memoria_sesiones.md` como un SNAPSHOT corto: conserva el bloque
`## 🧿 ESTADO ACTUAL` intacto y solo las últimas N sesiones bajo
`## 🗓️ Sesiones recientes`. Las sesiones más viejas se mueven al tope del
`## 🧿 Historial archivado` en `memoria_historica/bitacora_sesiones_2026.md`.

Idempotente. Preserva EOL (CRLF/LF) y UTF-8 sin BOM. Las sesiones están ordenadas
más-reciente-arriba, así que las que sobran (las de más abajo) son las que se archivan.

Uso:
    python 99_Sistema/scripts/mantenimiento/rotar_memoria.py            # keep 7
    python 99_Sistema/scripts/mantenimiento/rotar_memoria.py --keep 5
    python 99_Sistema/scripts/mantenimiento/rotar_memoria.py --dry-run
"""
import sys, os, argparse

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
MEM = os.path.join(ROOT, "00_Ele", "memoria_sesiones.md")
BITACORA = os.path.join(ROOT, "00_Ele", "memoria_historica", "bitacora_sesiones_2026.md")

REC_HEADER = "## 🗓️ Sesiones recientes"
HIST_HEADER = "## 🧿 Historial archivado"
SESSION_PREFIX = "### Sesión"
PUNTERO_PREFIX = "> 📚"


def read_eol(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    eol = "\r\n" if "\r\n" in content else "\n"
    return content, eol


def split_sessions(block_lines):
    """Divide una lista de líneas en bloques de sesión. Devuelve (preamble, [bloques])."""
    sessions, current, preamble = [], None, []
    for line in block_lines:
        if line.startswith(SESSION_PREFIX):
            if current is not None:
                sessions.append(current)
            current = [line]
        elif current is None:
            preamble.append(line)
        else:
            current.append(line)
    if current is not None:
        sessions.append(current)
    return preamble, sessions


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep", type=int, default=7, help="Nº de sesiones recientes a conservar (default 7)")
    ap.add_argument("--dry-run", action="store_true", help="No escribe, solo reporta")
    args = ap.parse_args()

    content, eol = read_eol(MEM)
    lines = content.split(eol)

    # Localizar la sección "Sesiones recientes"
    try:
        rec_idx = next(i for i, l in enumerate(lines) if l.strip() == REC_HEADER)
    except StopIteration:
        print(f"[!] No se encontró '{REC_HEADER}' en memoria_sesiones.md — nada que rotar.")
        return 0

    # Fin de la sección = línea del puntero "> 📚" o un "---" final que lo precede, o EOF
    end_idx = len(lines)
    for i in range(rec_idx + 1, len(lines)):
        if lines[i].startswith(PUNTERO_PREFIX):
            # retroceder sobre "---" y vacías que preceden el puntero
            j = i
            while j - 1 > rec_idx and (lines[j - 1].strip() == "" or lines[j - 1].strip() == "---"):
                j -= 1
            end_idx = j
            break

    block = lines[rec_idx + 1:end_idx]
    preamble, sessions = split_sessions(block)

    print(f"Sesiones recientes encontradas: {len(sessions)} | keep={args.keep}")
    if len(sessions) <= args.keep:
        print("[=] Por debajo del umbral. Nada que archivar. ✅")
        return 0

    keep_sessions = sessions[:args.keep]
    archive_sessions = sessions[args.keep:]
    print(f"[→] A archivar: {len(archive_sessions)} sesión(es) más viejas.")
    for s in archive_sessions:
        print(f"      • {s[0]}")

    if args.dry_run:
        print("[dry-run] No se escribió nada.")
        return 0

    # --- Reescribir memoria_sesiones.md ---
    head = lines[:rec_idx + 1]                 # hasta e incluyendo el header de recientes
    tail = lines[end_idx:]                      # puntero + lo que siga
    kept_flat = []
    for s in keep_sessions:
        kept_flat.extend(s)
    new_block = preamble + kept_flat
    # quitar líneas vacías de cola sobrantes en new_block
    while new_block and new_block[-1].strip() == "":
        new_block.pop()
    nuevo_mem = eol.join(head + [""] + new_block + [""] + tail)
    if not nuevo_mem.endswith(eol):
        nuevo_mem += eol

    # --- Anteponer al historial de la bitácora ---
    bit_content, bit_eol = read_eol(BITACORA)
    bit_lines = bit_content.split(bit_eol)
    try:
        hist_idx = next(i for i, l in enumerate(bit_lines) if l.strip() == HIST_HEADER)
        insert_at = hist_idx + 1
        # saltar una línea en blanco tras el header si la hay
        if insert_at < len(bit_lines) and bit_lines[insert_at].strip() == "":
            insert_at += 1
    except StopIteration:
        print(f"[!] No se encontró '{HIST_HEADER}' en la bitácora — abortado para no corromper.")
        return 1

    archived_flat = []
    for s in archive_sessions:
        archived_flat.extend(s)
        if archived_flat and archived_flat[-1].strip() != "":
            archived_flat.append("")
    new_bit_lines = bit_lines[:insert_at] + archived_flat + bit_lines[insert_at:]
    nuevo_bit = bit_eol.join(new_bit_lines)
    if not nuevo_bit.endswith(bit_eol):
        nuevo_bit += bit_eol

    with open(MEM, "w", encoding="utf-8", newline="") as f:
        f.write(nuevo_mem)
    with open(BITACORA, "w", encoding="utf-8", newline="") as f:
        f.write(nuevo_bit)

    print(f"[✓] memoria_sesiones.md: {len(keep_sessions)} sesiones recientes conservadas.")
    print(f"[✓] bitácora: {len(archive_sessions)} sesión(es) archivada(s) al tope del historial.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
