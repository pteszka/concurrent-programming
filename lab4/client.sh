#!/bin/bash

server="serwerfifo"
client="klientfifo"

if [ ! -f "$client" ]; then
    > $client
fi

echo -n "Enter number: "
read x
echo "$(realpath "$0") $x" > $server

while true
do
    if [ -s "$client" ] ; then
        echo $(head -n 1 $client)
        exit 0
    fi
done

exit 0