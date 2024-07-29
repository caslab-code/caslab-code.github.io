#!/usr/bin/python3

import requests
import json
import sys

# Get seminar data

url = 'https://caslab.csl.yale.edu/~jakub/seminar-list.json'
r = requests.get(url)
r.encoding = 'utf-8'
data = r.text

# Generate HTML code

json_data = json.loads(data)
for key in list(json_data):
      html_string = '<li>' + json_data[key]['date'] + ': ' + '<a href=\"' + json_data[key]['event-url'] + '\">' + json_data[key]['event'] + '</a></li>'
      print(html_string)
