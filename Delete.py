import glob
import os

files = glob.glob("Build/html/*.html")
i = 0

while i <= (len(files)-1):
    path = files[i]
    os.remove(path)
    i += 1