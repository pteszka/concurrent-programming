#!/bin/bash

declare -i flag
flag=1  

for file in $1/*
do
    # file
    if [ -f "$file" ] && [ "$(basename $file)" = "$2" ]; then
        flag=0
        echo "$1"
    fi
    
    # dir
    if [ -d "$file" ]; then
        # add some filler var as 3rd parameter
        ./search.sh "$file" "$2" filler &
        wait $!
        # if successful - flag=0
        if [ $? -eq 0 ];then
            flag=0
        fi
    fi
done

if [[ $# -eq 2 ]]; then
    if [[ $flag -eq 1 ]]; then
        echo "Nie znaleziono $2"
    fi
fi

exit $flag