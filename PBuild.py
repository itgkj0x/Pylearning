import glob
import shutil
import os
from weasyprint import HTML
from nbconvert import HTMLExporter


files = glob.glob("Notebook/*/*.ipynb")

if not files:
    print("No .ipynb files found in Notebook subdirectories.")
    exit(1)

if os.path.exists('Build/pdf'):
    shutil.rmtree('Build/pdf')

os.makedirs('Build/pdf', exist_ok=True)

for pathj in files:
    html_exporter = HTMLExporter(template_name="classic")
    body, resources = html_exporter.from_filename(pathj)
    pathp = os.path.join('Build', 'pdf', os.path.basename(pathj).replace('.ipynb', '.pdf'))
    HTML(string=body).write_pdf(pathp)