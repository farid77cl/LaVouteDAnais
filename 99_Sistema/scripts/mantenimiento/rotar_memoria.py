#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rotar_memoria.py — Autopoda de la memoria de sesiones Y del diario de servicio.

1) `00_Ele/memoria_sesiones.md` (SNAPSHOT corto): conserva el bloque
   `## 🧿 ESTADO ACTUAL` intacto y solo las últimas N sesiones bajo
   `## 🗓️ Sesiones recientes`. Las viejas se mueven al tope del
   `## 🧿 Historial archivado` en `memoria_historica/bitacora_sesiones_2026.md`.

2) `00_Ele/mi_diario_de_servicio.md` (prepend, más-reciente-arriba): conserva
   las últimas M entradas `#### SESIÓN`; las viejas se mueven al tope de
   `memoria_historica/diario_de_servicio_archivo_2026.md` (se crea si no existe).
   Sin rotación el diario llegó a 822 KB / 429 sesiones (02/07/2026).

Idempotente. Preserva EOL (CRLF/LF) y UTF-8 sin BOM. En ambos archivos las
entradas están ordenadas más-reciente-arriba: las que sobran (abajo) se archivan.

Uso:
    python 99_Sistema/scripts/mantenimiento/rotar_memoria.py                 # keep 7 / diario 15
    python 99_Sistema/scripts/mantenimiento/rotar_memoria.py --keep 5 --keep-diario 20
    python 99_Sistema/scripts/mantenimiento/rotar_memoria.py --dry-run
"""
import sys, os, argparse

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
MEM = os.path.join(ROOT, "00_Ele", "memoria_sesiones.md")
BITACORA = os.path.join(ROOT, "00_Ele", "memoria_historica", "bitacora_sesiones_2026.md")
DIARIO = os.path.join(ROOT, "00_Ele", "mi_diario_de_servicio.md")
DIARIO_ARCHIVO = os.path.join(ROOT, "00_Ele", "memoria_historica", "diario_de_servicio_archivo_2026.md")

REC_HEADER = "## 🗓️ Sesiones recientes"
HIST_HEADER = "## 🧿 Historial archivado"
SESSION_PREFIX = "### Sesión"
PUNTERO_PREFIX = "> 📚"
DIARIO_PREFIX = "#### SESI"  # cubre "#### SESIÓN —" y "#### SESIÓN -"
DIARIO_ARCH_HEADER = "## 📚 Entradas archivadas"

DIARIO_ARCH_STUB = [
    "# 📚 Diario de Servicio — Archivo Histórico 2026",
    "",
    "> Entradas archivadas de `00_Ele/mi_diario_de_servicio.md` (el diario vivo conserva solo las últimas N sesiones; `/inicio-ele` lee las primeras 50 líneas). Más-reciente-arriba. NO se lee en el inicio.",
    "",
    "---",
    "",
    DIARIO_ARCH_HEADER,
    "",
]


def read_eol(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    eol = "\r\n" if "\r\n" in content else "\n"
    return content, eol


def split_sessions(block_lines, prefix=SESSION_PREFIX):
    """Divide una lista de líneas en bloques de sesión. Devuelve (preamble, [bloques])."""
    sessions, current, preamble = [], None, []
    for line in block_lines:
        if line.startswith(prefix):
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


def rotar_memoria_sesiones(keep, dry_run):
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

    print(f"[memoria] Sesiones recientes: {len(sessions)} | keep={keep}")
    if len(sessions) <= keep:
        print("[memoria] Por debajo del umbral. Nada que archivar. ✅")
        return 0

    keep_sessions = sessions[:keep]
    archive_sessions = sessions[keep:]
    print(f"[memoria] A archivar: {len(archive_sessions)} sesión(es) más viejas.")
    for s in archive_sessions:
        print(f"      • {s[0]}")

    if dry_run:
        print("[dry-run] No se escribió nada.")
        return 0

    # --- Reescribir memoria_sesiones.md ---
    head = lines[:rec_idx + 1]                 # hasta e incluyendo el header de recientes
    tail = lines[end_idx:]                      # puntero + lo que siga
    kept_flat = []
    for s in keep_sessions:
        kept_flat.extend(s)
    new_block = preamble + kept_flat
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


def rotar_diario(keep, dry_run):
    content, eol = read_eol(DIARIO)
    lines = content.split(eol)
    preamble, sessions = split_sessions(lines, prefix=DIARIO_PREFIX)

    print(f"[diario] Entradas: {len(sessions)} | keep={keep}")
    if len(sessions) <= keep:
        print("[diario] Por debajo del umbral. Nada que archivar. ✅")
        return 0

    keep_sessions = sessions[:keep]
    archive_sessions = sessions[keep:]
    print(f"[diario] A archivar: {len(archive_sessions)} entrada(s) más viejas → {os.path.basename(DIARIO_ARCHIVO)}")

    if dry_run:
        print("[dry-run] No se escribió nada.")
        return 0

    # --- Reescribir el diario vivo ---
    kept_flat = list(preamble)
    for s in keep_sessions:
        kept_flat.extend(s)
    while kept_flat and kept_flat[-1].strip() == "":
        kept_flat.pop()
    nuevo_diario = eol.join(kept_flat)
    if not nuevo_diario.endswith(eol):
        nuevo_diario += eol

    # --- Anteponer al archivo histórico (se crea si no existe) ---
    if os.path.exists(DIARIO_ARCHIVO):
        arch_content, arch_eol = read_eol(DIARIO_ARCHIVO)
        arch_lines = arch_content.split(arch_eol)
    else:
        arch_eol = eol
        arch_lines = list(DIARIO_ARCH_STUB)
    try:
        hdr_idx = next(i for i, l in enumerate(arch_lines) if l.strip() == DIARIO_ARCH_HEADER)
        insert_at = hdr_idx + 1
        if insert_at < len(arch_lines) and arch_lines[insert_at].strip() == "":
            insert_at += 1
    except StopIteration:
        print(f"[!] No se encontró '{DIARIO_ARCH_HEADER}' en el archivo del diario — abortado para no corromper.")
        return 1

    archived_flat = []
    for s in archive_sessions:
        archived_flat.extend(s)
        if archived_flat and archived_flat[-1].strip() != "":
            archived_flat.append("")
    new_arch_lines = arch_lines[:insert_at] + archived_flat + arch_lines[insert_at:]
    nuevo_arch = arch_eol.join(new_arch_lines)
    if not nuevo_arch.endswith(arch_eol):
        nuevo_arch += arch_eol

    with open(DIARIO, "w", encoding="utf-8", newline="") as f:
        f.write(nuevo_diario)
    with open(DIARIO_ARCHIVO, "w", encoding="utf-8", newline="") as f:
        f.write(nuevo_arch)

    print(f"[✓] diario: {len(keep_sessions)} entradas vivas conservadas.")
    print(f"[✓] archivo histórico: {len(archive_sessions)} entrada(s) antepuesta(s).")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep", type=int, default=7, help="Nº de sesiones a conservar en memoria_sesiones (default 7)")
    ap.add_argument("--keep-diario", type=int, default=15, help="Nº de entradas a conservar en el diario vivo (default 15)")
    ap.add_argument("--dry-run", action="store_true", help="No escribe, solo reporta")
    args = ap.parse_args()

    rc1 = rotar_memoria_sesiones(args.keep, args.dry_run)
    rc2 = rotar_diario(args.keep_diario, args.dry_run)
    return max(rc1, rc2)


if __name__ == "__main__":
    raise SystemExit(main())
