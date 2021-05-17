# pip install fpdf

import urllib.request
import os
from PIL import Image
from glob import glob
import os
from fpdf import FPDF

# URL to flip-book
url="https://online.flipbuilder.com/qzxg/ywtm/"

# No of pages
totalNoPages = 99

output = os.path.join(os.getcwd(), r'output')

if not os.path.exists(output):
   os.makedirs(output)

url = url.strip('/')

for i in range(1,totalNoPages+1):
    urllib.request.urlretrieve('{}/files/mobile/{}.jpg'.format(url,i), 'output/{}.jpg'.format(i))
    print("Downloaded {} of {} pages".format(i,totalNoPages))

print("Converting to PDF")

imagelist = sorted(glob("output/*.jpg"), key=os.path.getmtime)

image_directory = 'output'

extensions = ('*.jpg','*.png')

margin = 10

cover = Image.open(imagelist[0])

width, height = cover.size

pdf = FPDF(unit="pt", format=[width + 2*margin, height + 2*margin])

for imagePath in imagelist:
    cover = Image.open(imagePath)
    width, height = cover.size
    pdf.add_page()
    pdf.image(imagePath, margin, margin)

pdf.output("outputpdf" + ".pdf", "F")

print("Complete")
