#!/bin/bash

#Bash script for user's login history

last > loginhistory.txt

echo "" >> loginhistory.txt

echo "Script Ran: " >> loginhistory.txt

date >> loginhistory.txt

echo "Here is the login history: Storing in a text file"

echo "" 

last

echo ""

date
