import glob
from nbconvert import HTMLExporter
import shutil
import os

files = glob.glob("Notebook/*/*.ipynb")

i = 0

if not os.path.exists('Build/html'):
    os.makedirs('Build/html')

for pathj in files:
    html_exporter = HTMLExporter(template_name="classic")
    HTML = html_exporter.from_filename(pathj)
    pathh = pathj.replace('.ipynb', '.html')
    with open(pathh, 'w', encoding='utf-8') as f:
        f.write(HTML[0])
    shutil.move(pathh, './Build/html/')