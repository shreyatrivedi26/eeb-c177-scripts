#!/bin/bash
INPUTFILE=$1
OUTPUTFILE=$2

tail -n+2 $1 | cut -d ";" -f 2-6|tr -s ";" " "| sort -r -n -k6  > $2
