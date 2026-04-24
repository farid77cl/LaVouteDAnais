import sys

path = r"c:\Users\farid\LaVouteDAnais\00_Ele\mi_diario_de_servicio.md"

# Read the file as UTF-8 (which is what it is)
with open(path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Take a single bad line to test the fix
bad_line = "MAÃƒÆ'Ã¢â‚¬ËœANA (09:12) - INICIO DE SESIÃƒÆ'Ã¢â‚¬Å"N"

# Try fix: encode to cp1252, decode as utf-8
try:
    fixed_cp1252 = bad_line.encode('cp1252').decode('utf-8')
    print(f"cp1252 fix: {fixed_cp1252}")
except Exception as e:
    print(f"cp1252 failed: {e}")

try:
    fixed_latin1 = bad_line.encode('latin-1').decode('utf-8')
    print(f"latin1 fix: {fixed_latin1}")
except Exception as e:
    print(f"latin1 failed: {e}")

# Try double fix (triple encoding)
try:
    step1 = bad_line.encode('cp1252').decode('utf-8')
    step2 = step1.encode('cp1252').decode('utf-8')
    print(f"double cp1252 fix: {step2}")
except Exception as e:
    print(f"double fix failed: {e}")
