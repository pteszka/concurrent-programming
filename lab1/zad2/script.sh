#!/bin/bash
# echo "MENU:"
# echo "0 - odczyt ostatniej linii"
# echo "1 - odczyt całego pliku"
# echo "2 - zapis jednej linii"
# echo "3 - koniec pracy"

while true
do
    echo -n "Enter option number: "
    read x
    case $x in
    0) 
        head -n 1 test 
        ;;
    1)
        cat test
        ;;
    2)
        echo "Enter some text: ";
        read text;
        echo $text >> test;
        ;;
    3) 
        echo "Goodbye!"; 
        kill -9 $BASHPID
        ;;
    esac
done
exit 0
