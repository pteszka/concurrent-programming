#!/bin/bash

echo -n "Enter number: "
read x
echo $x >> data
while true
do
    if [ -s "result" ] ;
    then
        echo $(head -n 1 result)
        > result
        kill -9 $BASHPID 
    fi
done

exit 0