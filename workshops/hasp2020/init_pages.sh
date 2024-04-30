#!/bin/bash

FILE=$1

sed -i '4i<title>Hardware and Architectural Support for Security and Privacy (HASP) 2020</title>' $FILE
sed -i -e '5d' $FILE

sed -i '26i<a href="http://caslab.csl.yale.edu/workshops/hasp2019/">HASP 2019</a><br />' $FILE

sed -i '38i<h2>Hardware and Architectural Support for Security and Privacy (HASP) 2020</h2>' $FILE
sed -i '39i<h3>To be held October 2020</h3>' $FILE

sed -i -e '40d' $FILE
sed -i -e '40d' $FILE

