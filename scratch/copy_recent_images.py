import os
import shutil
from datetime import datetime, timedelta

src_root = r"c:\Users\farid\LaVouteDAnais\05_Imagenes\ele"
dest_dir = r"C:\Users\farid\.gemini\antigravity\brain\b269c8db-6663-4f08-91fe-6353d8e65f35"
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

now = datetime.now()
yesterday = now - timedelta(days=1)

for root, dirs, files in os.walk(src_root):
    for file in files:
        if file.endswith(".png"):
            file_path = os.path.join(root, file)
            mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            if mtime > yesterday:
                shutil.copy(file_path, dest_dir)
                print(f"Copied {file} to {dest_dir}")
