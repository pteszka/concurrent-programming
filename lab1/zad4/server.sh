#!/bin/bash

# -s: FILE exists and has a size greater than zero
while true
do
    if [ -s "data" ] ;
    then
        # > filename: clear the file 
        x=$(head -n 1 data)
        > data
        echo $(($x*2)) >> result
    fi
done
exit 0