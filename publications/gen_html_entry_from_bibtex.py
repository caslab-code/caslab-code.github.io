#!/usr/bin/python3

import argparse
from pybtex.database.input import bibtex
#from pylatexenc.latex2text import LatexNodes2Text

parser = argparse.ArgumentParser(description='Generate HTML entry for publications page based on data from a Bibtex file',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-b', '--bibtex', dest='bibtex', type=str, required=True,
          help='path to Bibtex file')
parser.add_argument('-p', '--gen-pdf-link', dest='p', default=False, action='store_true', required=False,
          help='add dummy PDF link in HTML entry for paper')
#parser.add_argument('-b', '--gen-bibtex-link', dest='b', default=True, action='store_true', required=False,
#          help='add dummy Bibtex link in HTML entry for paper')
parser.add_argument('-e', '--gen-eprint-link', dest='e', default=False, action='store_true', required=False,
          help='add dummy ePrint link in HTML entry for paper')
parser.add_argument('-c', '--gen-code-link', dest='c', default=False, action='store_true', required=False,
          help='add dummy Code page link in HTML entry for paper')
args = parser.parse_args()

bibtex_path = args.bibtex
gen_pdf = args.p
#gen_bibtex = args.b
gen_eprint = args.e
gen_code = args.c

# Parse Bibtex

parser      = bibtex.Parser()
bib_data    = parser.parse_file(bibtex_path)
keys_list   = list(bib_data.entries.keys())
key         = keys_list[0]
authors     = bib_data.entries[str(key)].persons['author']
title       = bib_data.entries[str(key)].fields['title']
year        = bib_data.entries[str(key)].fields['year']

try:
  venuetitle   = bib_data.entries[str(key)].fields['booktitle']
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
# venuetitle   = bib_data.entries[str(key)].fields['eprint']
# venuetitle   = bib_data.entries[str(key)].fields['booktitle']
# venuetitle   = bib_data.entries[str(key)].fields['howpublished']
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

# Output HTML code to be pasted into publications page

print('')
print("<div id=\"" + str(key) + "\">")

str_authors = ''
for author in authors:
    if author == authors[0]:
        str_authors += (str(author.first_names[0]) + " " + str(author.last_names[0]) + "")
    elif author != authors[-1]:
        str_authors += (", " + str(author.first_names[0]) + " " + str(author.last_names[0]) + "")
    else:
        str_authors += (", and " + str(author.first_names[0]) + " " + str(author.last_names[0]) + ", ")
#print(LatexNodes2Text().latex_to_text(str_authors))
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

# if PDF link not requested now, add commented out for future
if gen_pdf:
  print("[ <a href=\"/publications/" + str(key) + ".pdf\">PDF</a> ]&nbsp;")

# always will generate Bibtex link, gen_bibtex defaults to True even if not specified on command line
#if gen_bibtex:
print("[ <a href=\"/publications/" + bibtex_path + "\">BibTeX</a> ]&nbsp;")

# optional
if gen_eprint:
  print("[ <a href=\"#\">prior ePrint</a> ]&nbsp;")

# optional
if gen_code:
  print("[ <a href=\"/code/#\">CODE</a> ]&nbsp;")

# final part of html entry
print("<br/><br/>")
print("</div>")
print("")

# print data useful for copying into Google Scholar
print("Google Scholar form data:")
print("")

str_title = title

str_authors_google = ''
for author in authors:
    if author == authors[0]:
        str_authors_google += (str(author.last_names[0]) + ", " + str(author.first_names[0]) + "")
    elif author != authors[-1]:
        str_authors_google += ("; " + str(author.last_names[0]) + ", " + str(author.first_names[0]) + "")
    else:
        str_authors_google += ("; " + str(author.last_names[0]) + ", " + str(author.first_names[0]) + "")

str_date_google = '' + (year if (year != '')  else  "") + ("/"+month if (month != '') else "")

str_venuetitle = venuetitle

str_volume = volume

str_issue = issuenumber

print("Title:               " + str_title)
print("Authors:             " + str_authors_google)
print("Publication date:    " + str_date_google)
print("Journal/Conference:  " + str_venuetitle)
print("Volume:              " + str_volume)
print("Issue:               " + str_issue)
print("")


# work-in-progress curl command to update Google Scholar
print("FIXME not correct")
print('''
curl 'https://scholar.google.com/citations?view_op=edit_citation&update_op=save_citation&hl=en' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:88.0) Gecko/20100101 Firefox/88.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.7,pl;q=0.3' --compressed -H 'Referer: https://scholar.google.com/citations?hl=en&user=NO1Je2kAAAAJ&view_op=list_works&sortby=pubdate' -H 'X-Requested-With: XHR' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://scholar.google.com' -H 'DNT: 1' -H 'Alt-Used: scholar.google.com' -H 'Connection: keep-alive' -H 'Cookie: 1P_JAR=2022-04-24-02; NID=511=EE_537bCBF7vALeX8HlOJZNWZ0Enw3wrSZX-sgs5BSJdQwStLZr3yHA0g01Gx6HRswMOAXsEyRDSAB9PC5OXV_PAHq8kDzaluH8pFF2CSk9IE2g4J8r5Nj9LaU8_GrgL4X2bIVWhADJP-O3vXcpbsdLbojdA5kD5gZINw0oPniMO6rVAeRNoy37IbZrWNuJv0VH0F8EjX5EQDoO7CWMBRQoetU-fssYcqidQjZfCYqhQ6KmTYRqZPmKeCBKQHAs; OGPC=19027681-1:19022552-1:; ANID=AHWqTUkGdqG4RoPUk7zRJTc9P6herUrNFfi3mRLsT9IYhRV3vEz7eMGnS_NF2THU; SID=JQg07RiECq115W2azcGkFP_kva-oSktkXI0ujbXBxP_7Ht-zsbMy0w8qjhS5gMsqJkU2aA.; __Secure-1PSID=JQg07RiECq115W2azcGkFP_kva-oSktkXI0ujbXBxP_7Ht-z0oxLc6W0c5EwwFPaeYKMCA.; __Secure-3PSID=JQg07RiECq115W2azcGkFP_kva-oSktkXI0ujbXBxP_7Ht-zbh3Q1e0BfwLXnAZGCU8W9g.; HSID=A8MYsOscNsdDA4SK2; SSID=AqZC2aHI1Lm9vQLU5; APISID=l-cQMfggQos64aW6/ANR__kgtz0Av2nmuj; SAPISID=_kZNEuthEAMj3i6f/AgaGtn0G9KLuwEyff; __Secure-1PAPISID=_kZNEuthEAMj3i6f/AgaGtn0G9KLuwEyff; __Secure-3PAPISID=_kZNEuthEAMj3i6f/AgaGtn0G9KLuwEyff; SIDCC=AJi4QfG7-gU8s0b2PizlK_ePjKffylA28WN-Opn3iuuBseaKILXA8-Sk02qiDLqFiPD7stQMNpU; __Secure-3PSIDCC=AJi4QfEq1kIU7gWKTprAYXyIDkzKB7F76PiEksOB_ZfOixnhVfdJe7U3D4HW__Hpn81HBqFSQRE; SEARCH_SAMESITE=CgQImZUB; GSP=LM=1650377610:S=u_ZXwkKS04i-LCZC' -H 'Sec-GPC: 1' --data-raw 'json=&xsrf=AMD79ooAAAAAYmdL5CXxYZZbX3dkpozV_a_KCaNtH8V3&articletype=3&title=&authors=test&court=&pubdate=&pubvenue=&volume=&issue=&pages=&publisher=&patoffice=0&patnumber=&patapplic=&reporter0=&reporter1=&reporter2=&docketid=&continue=%2Fcitations%3Fhl%3Den%26user%3DNO1Je2kAAAAJ%26view_op%3Dlist_works%26sortby%3Dpubdate'
''')
print("")
