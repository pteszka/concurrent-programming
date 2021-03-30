#!/bin/bash

server="serwerfifo"
client="klientfifo"

trap "rm -f $client; exit 0" EXIT

# -f dont work
if [[ ! -p "$server" ]]; then
    echo "Server is down."
    exit 1
fi

if [[ ! -f "$client" ]]; then
    mkfifo $client
fi

printf "Enter the number: "
read x

# write to serwerfifo path $(realpath "$0")
echo "$HOME $x" > $server

if [[ $x == "end" ]]; then
    echo "Server is down."
    exit 0
fi


while true 
do
    if read line < $client; then
        echo "2*$x = $line"
        exit 0
    fi
done
