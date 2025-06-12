import pypdf
import glob

writer = pypdf.PdfWriter()

files = glob.glob("Build/*/*.pdf")

weeks = int(input("何週から取得しますか"))
weeke = int(input("何週まで取得しますか"))

for x in range(weeks, weeke):
    file_path = f'Build/pdf/hw_week{x}.pdf'
    writer.append(file_path)

output_path = f'Build/pdf/{weeks}-{weeke}.pdf'
with open(output_path, 'wb') as f_out:
    writer.write(f_out)