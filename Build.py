import glob
from nbconvert import HTMLExporter
import shutil
import os

files = glob.glob("Notebook/*/*.ipynb")

if os.path.exists('Build/html'):
    shutil.rmtree('Build/html')

os.makedirs('Build/html')

for pathj in files:
    html_exporter = HTMLExporter(template_name="classic")
    body, resources = html_exporter.from_filename(pathj)
    pathh = pathj.replace('.ipynb', '.html')
    with open(pathh, 'w', encoding='utf-8') as f:
        f.write(body)
    shutil.move(pathh, './Build/html/')