#!/bin/bash

declare -i flag
flag=1  

for file in $1/*
do
    # our file
    if [ -f "$file" ] && [ "$(basename $file)" = "$2" ]; then
        flag=0
        echo "$1"
    fi
    
    # dir
    if [ -d "$file" ]; then
        # some filler var as 3rd var
        ./search.sh "$file" "$2" filler &
        wait $!
        # if successful - flag=0
        if [ $? -eq 0 ];then
            flag=0
        fi
    fi
done

if [[ ! $# -eq 3 ]]; then
    if [[ $flag -eq 1 ]]; then
        echo "Nie znaleziono $2"
    fi
fi

exit $flag