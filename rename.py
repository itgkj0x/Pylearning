import glob
import os
import shutil

path ="Notebook"
dirlist = []
files = os.listdir(path)

for filename in files:
    if os.path.isdir(os.path.join(path, filename)):
        if filename.startswith("Week"):
            dirlist.append(filename)
print(dirlist)


for dir in dirlist:
    os.rename(f"Notebook/{dir}",f"Notebook/{dir.zfill(6)}" )


