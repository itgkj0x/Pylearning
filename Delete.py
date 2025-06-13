import glob
import os

def delete(*extensions):
    for ext in extensions:
        files = glob.glob(f"Build/{ext}/*.{ext}")
        for file in files:
            os.remove(file)


a = delete("pdf", "html")