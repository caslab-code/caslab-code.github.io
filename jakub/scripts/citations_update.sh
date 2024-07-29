#!/bin/bash

INDEXPATH="/home/jakub/public_html/index.html"

CITATIONSTEXT=$(/home/jakub/public_html/scripts/get_google_scholar_stats.sh.txt)
LINENUMBER=$(grep -n 'Citations' /home/jakub/public_html/index.html | cut -f1 -d:)

sed -i "$LINENUMBER i$CITATIONSTEXT" $INDEXPATH

LINENUMBER=$(($LINENUMBER + 1))

sed -i "$LINENUMBER d" $INDEXPATH

DATETEXT="<span style=\"font-size: 0.7em\">Citation data was updated on $(date +%F).</span>"

LINENUMBER=$(($LINENUMBER + 4))

sed -i "$LINENUMBER i$DATETEXT" $INDEXPATH

LINENUMBER=$(($LINENUMBER + 1))

sed -i "$LINENUMBER d" $INDEXPATH

