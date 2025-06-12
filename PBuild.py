import glob
import shutil
import os
from weasyprint import HTML
from nbconvert import HTMLExporter
import pdfkit

# wkhtmltopdfの実行ファイルパスを設定
# このパスは実際のインストールパスに合わせて変更してください
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
options = {
    'page-size': 'A4',
    'margin-top': '3mm',
    'margin-right': '2mm',
    'margin-bottom': '3mm',
    'margin-left': '2mm',
    'encoding': "UTF-8",
    'no-outline': None,
    'disable-smart-shrinking': '',
}



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
    html_path = pathj.replace('.ipynb', '.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(body)
    pdfkit.from_file(html_path, pathp, options=options, configuration=config)
    os.remove(html_path)