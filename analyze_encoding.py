import sys

path = r"c:\Users\farid\LaVouteDAnais\00_Ele\mi_diario_de_servicio.md"

with open(path, "rb") as f:
    raw = f.read()

# Strip UTF-8 BOM if present
if raw[:3] == b"\xef\xbb\xbf":
    raw = raw[3:]

# Split into lines
lines_raw = raw.split(b"\n")
print(f"Total lines: {len(lines_raw)}")

# Scan for invalid UTF-8 lines
bad_lines = []
for i, line in enumerate(lines_raw):
    try:
        line.decode("utf-8")
    except UnicodeDecodeError as e:
        bad_lines.append((i+1, line[:60], str(e)))

print(f"Lines with invalid UTF-8 bytes: {len(bad_lines)}")
if bad_lines:
    print("First 5 bad lines:")
    for ln, data, err in bad_lines[:5]:
        print(f"  Line {ln}: {data} | Error: {err}")
    print("Last 5 bad lines:")
    for ln, data, err in bad_lines[-5:]:
        print(f"  Line {ln}: {data} | Error: {err}")