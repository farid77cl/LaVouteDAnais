import sys

path = r"c:\Users\farid\LaVouteDAnais\00_Ele\mi_diario_de_servicio.md"

with open(path, "r", encoding="utf-8-sig") as f:
    content = f.read()

# Check a known bad region - lines around 1882
lines = content.splitlines()
# Show lines 1880-1890
for i in range(1879, 1890):
    print(f"Line {i+1}: {repr(lines[i][:120])}")