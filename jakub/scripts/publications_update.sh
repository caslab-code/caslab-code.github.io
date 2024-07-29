#!/bin/bash

INDEXPATH="/home/jakub/public_html/index.html"

LINENUMBERSTART=$(grep -n 'Start Publications List' $INDEXPATH | cut -f1 -d:)
LINENUMBEREND=$(grep -n 'End Publications List' $INDEXPATH | cut -f1 -d:)

LINENUMBERSTART=$(($LINENUMBERSTART + 2))
LINENUMBEREND=$(($LINENUMBEREND - 2))

echo $LINENUMBERSTART
echo $LINENUMBEREND

sed -i "$LINENUMBERSTART,$LINENUMBEREND d" $INDEXPATH

LINENUMBERSTART=$(($LINENUMBERSTART - 1))

/home/jakub/public_html/scripts/gen_html_entries_from_bibtex.py > /tmp/citations.tmp

sed -i "$LINENUMBERSTART r /tmp/citations.tmp" $INDEXPATH

rm -rf /tmp/citations.tmp

