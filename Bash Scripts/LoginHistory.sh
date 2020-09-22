
#!/bin/bash

#Script For Showing Login History
#and storing in a text file

echo "Here is the login history: Storing in a Text File"

echo ""

last 

echo ""

date

echo ""

last > loginhistory.txt

echo "" > loginhistory.txt

echo "Script Ran:  " > loginhistory.txt

date > loginhistory.txt
