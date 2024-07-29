#!/usr/bin/python3

import requests
from pybtex.database.input import bibtex

# Get Bibtex data

url = 'https://caslab.csl.yale.edu/publications/refs-caslab-combined.bib'
r = requests.get(url)
r.encoding = 'utf-8'
data = r.text

# Parse Bibtex

parser      = bibtex.Parser()
bib_data    = parser.parse_string(data)
keys_list   = list(bib_data.entries.keys())

for i in range(3):
    
  key         = keys_list[i]
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

  print("[ <a href=\"https://caslab.csl.yale.edu/publications/" + str(key) + ".pdf\">PDF</a> ]&nbsp;")

  print("[ <a href=\"https://caslab.csl.yale.edu/publications/" + str(key) + "-bibtex.txt\">BibTeX</a> ]&nbsp;")

  if i != 2:
    print("<br/><br/>")
