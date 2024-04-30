#!/bin/bash

FILE=$1

sed -i '4i<title>Hardware and Architectural Support for Security and Privacy (HASP) 2019</title>' $FILE
sed -i -e '5d' $FILE

sed -i '25i<a href="http://caslab.csl.yale.edu/workshops/hasp2018/">HASP 2018</a><br />' $FILE

sed -i '36i<h2>Hardware and Architectural Support for Security and Privacy (HASP) 2019</h2>' $FILE
sed -i -e '37d' $FILE

sed -i '37i<h3>To be held June 23 (Sunday), 2019 in Phoenix, Arizona, USA -- in conjunction with <a href="http://iscaconf.org/isca2019/index.html">ISCA 2019</a></h3>' $FILE
sed -i -e '38d' $FILE

