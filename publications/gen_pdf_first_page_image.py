#!/usr/bin/python3

import argparse
from pdf2image import convert_from_path

# Parse arguments
parser = argparse.ArgumentParser(description='Generate JPEG image of the first page of PDF file.',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-p', '--pdf', dest='pdf', type=str, required=True,
          help='path to PDF file')
args = parser.parse_args()

# Save path to the input PDF file
pdf_path = args.pdf

# Generate output file name
jpg_path = pdf_path[:-4] + "-first-page.jpg"
print("The image will be saved as " + jpg_path)

# Store Pdf with convert_from_path function
images = convert_from_path(pdf_path,dpi=50)

# Save first page as JPEG image
images[0].save(jpg_path)

# Done
print("")
