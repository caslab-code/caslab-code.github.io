#!/bin/bash

INDEXPATH="/home/jakub/public_html/index.html"

LINENUMBERSTART=$(grep -n 'Start Seminar List' $INDEXPATH | cut -f1 -d:)
LINENUMBEREND=$(grep -n 'End Seminar List' $INDEXPATH | cut -f1 -d:)

LINENUMBERSTART=$(($LINENUMBERSTART + 2))
LINENUMBEREND=$(($LINENUMBEREND - 2))

echo $LINENUMBERSTART
echo $LINENUMBEREND

sed -i "$LINENUMBERSTART,$LINENUMBEREND d" $INDEXPATH

LINENUMBERSTART=$(($LINENUMBERSTART - 1))

/home/jakub/public_html/scripts/gen_html_seminar_list_from_json.py > /tmp/seminars.tmp

sed -i "$LINENUMBERSTART r /tmp/seminars.tmp" $INDEXPATH

rm -rf /tmp/seminars.tmp

