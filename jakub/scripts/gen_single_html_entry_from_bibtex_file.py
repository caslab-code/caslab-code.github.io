#!/usr/bin/env python3

from pybtex.database.input import bibtex
import argparse

# Create argument parser

parser = argparse.ArgumentParser(description="Generate HTML entry from Bibtex file data.")
parser.add_argument("--file", type=str, required=True, help="Bibtex file")
args = parser.parse_args()

# Get and parse Bibtex file

parser      = bibtex.Parser()
bib_data    = parser.parse_file(args.file)
keys_list   = list(bib_data.entries.keys())

# Parse Bibtex file

key         = keys_list[0]
authors     = bib_data.entries[str(key)].persons['author']
title       = bib_data.entries[str(key)].fields['title']
year        = bib_data.entries[str(key)].fields['year']

try:
  venuetitle = bib_data.entries[str(key)].fields['booktitle']
except KeyError as e:
  try:
    venuetitle = bib_data.entries[str(key)].fields['howpublished']
  except KeyError as e:
    try:
      venuetitle = bib_data.entries[str(key)].fields['eprint']
    except KeyError as e:
      try:
        venuetitle = bib_data.entries[str(key)].fields['journal']
      except KeyError as e:
        venuetitle = ''
try:
  series       = bib_data.entries[str(key)].fields['series']
except KeyError as e:
  series       = ''

try:
  month        = bib_data.entries[str(key)].fields['month']
except KeyError as e:
  month        = ''

try:
  volume       = bib_data.entries[str(key)].fields['volume']
except KeyError as e:
  volume       = ''

try:
  issuenumber  = bib_data.entries[str(key)].fields['number']
except KeyError as e:
  issuenumber  = ''

# Output HTML code to be pasted into personal page

print("")

id_str = authors[0].first_names[0].lower() + year + title.split()[0].lower()
print(f"<div id=\"{id_str}\">")

str_authors = ''
for author in authors:
  if author == authors[0]:
    str_authors += (str(author.first_names[0]) + " " + str(author.last_names[0]) + "")
  elif author != authors[-1]:
    str_authors += (", " + str(author.first_names[0]) + " " + str(author.last_names[0]) + "")
  else:
    str_authors += (", and " + str(author.first_names[0]) + " " + str(author.last_names[0]) + ", ")
print(str_authors)

str_title = "\"" + title + "\","
print(str_title)

if series !='':
  series = series.replace('&','&amp;')
  venuetitle = venuetitle.replace('&','&amp;')
  str_venue_and_date = "in " + venuetitle + " (" + series + "), " + month + " " + year + ".<br/>"
else:
  venuetitle = venuetitle.replace('&','&amp;')
  str_venue_and_date = "in " + venuetitle + ", " + month + " " + year + ".<br/>"

print(str_venue_and_date)

print("[ <a href=\"/publications/" + str(key) + ".pdf\">PDF</a> ]&nbsp;")

print("[ <a href=\"/publications/" + str(key) + "-bibtex.txt\">BibTeX</a> ]&nbsp;")

print("<br/><br/>")

print("</div>")
