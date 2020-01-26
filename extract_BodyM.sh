#!/bin/bash
#The above line is not a comment but a special line telling where to find the bash
#program to execute the script;

#to find the location of bash run 'whereis bash'

#the special line helps to execute .sh scripts without calling bash first
#always add 'special line' at the 'beginning' of every script to avoid calling bash.



tail -n +2 Pacifici2013_data.csv|cut -d ";" -f 2-6|tr ";" " "|sort -r -n -k 6 > BodyM.csv

 # pipeline command first 'cuts' and selcets only columns 2-6 from the dataset
 # 'tr' translates the delimiters from ; to " "
 # sort command arranges the dataset in a reverse (descending) order of column 6
 # viz numeric column (-n) of Body mass.



# How to execute the .sh script without using bash? 
# 1. Change the permissions to allow execution of the script file: 
# ls -l extract_BodyM.sh 
#     -rw-r--r-- 1 eebc177student eebc177student 340 Jan 25 15:27 extract_BodyM.sh
# chmod +x exrtact_BodyM.csv will make it  user executable
# ls -l extract_BodyM.sh 
#     -rwxr-xr-x 1 eebc177student eebc177student 340 Jan 25 15:27 extract_BodyM.sh
