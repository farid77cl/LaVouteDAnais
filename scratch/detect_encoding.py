import chardet

file_path = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'
with open(file_path, 'rb') as f:
    rawdata = f.read(10000)
    result = chardet.detect(rawdata)
    print(result)
