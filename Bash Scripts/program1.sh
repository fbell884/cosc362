#!/bin/bash

HEIGHT=15
WIDTH=40
CHOICE_HEIGHT=4
BACKTITLE="Your Options Back Title"
TITLE="Big Time Options"
MENU="You must choose!"

OPTIONS=(1 "Option 1"
2 "Option 2" 
3 "Option 3")


CHOICE=($dialog --clear \
--backtitle "$BACKTITLE" \
--title "$TITLE"\
--menu "$MENU"\
$HEIGHT $WIDTH $CHOICE_HEIGHT \
${OPTIONS[@]}" \
2>& 1 >/dev/tty)

clear 

case $CHOICE in 
1) 
    echo "You chose option 1"
    ;;
2)	    
    echo "You chose Option 2 YEAH"
    ;;
3) 
    echo "Darth Vader Will Come to Your House and Look at Your Files."
    ls
    echo "See he looked"
    ;;
esac
