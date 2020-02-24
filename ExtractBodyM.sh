#!/bin/bash
INPUTFILE=$1
OUTPUTFILE=$2
DELIMITER=$3

tail -n+2 $1 | cut -d ";" -f 2-6|tr -s $3 " "| sort -r -n -k6  > $2
