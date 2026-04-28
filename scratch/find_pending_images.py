import os

base_path = r'c:\Users\farid\LaVouteDAnais\05_Imagenes\ele'
pending_folders = []

for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(folder_path) and folder.startswith('look'):
        png_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]
        if not png_files:
            pending_folders.append(folder)

pending_folders.sort()
print("Folders with NO images:")
for f in pending_folders:
    print(f)
