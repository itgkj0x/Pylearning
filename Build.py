import glob
import subprocess
import shutil
import os

files = glob.glob("*/*.ipynb")

print(files[1])
i = 0

if not os.path.exists('Build/html'):
    os.makedirs('Build/html')

while i <= (len(files)-1):
    pathj = files[i]
    result = subprocess.run(['jupyter', 'nbconvert','--to','html',pathj], shell=True,stdout=subprocess.PIPE)
    pathh = pathj.replace('.ipynb','.html')
    shutil.move(pathh, './Build/html/')
    i = i+1 