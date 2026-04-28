import sys

file_path = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'
with open(file_path, 'rb') as f:
    data = f.read(100)
    print(f"Bytes: {data}")

try:
    data.decode('utf-8')
    print("UTF-8: OK")
except UnicodeDecodeError:
    print("UTF-8: FAIL")

try:
    data.decode('latin-1')
    print("Latin-1: OK")
except UnicodeDecodeError:
    print("Latin-1: FAIL")
