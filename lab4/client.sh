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

printf "Enter a number: "
read x

# write to serwerfifo path of client and number
echo "$(realpath "$0") $x" > $server

if [[ $x == "end" ]]; then
    echo "Server is down."
    exit 0
fi


while true 
do
    if read line < $client; then
        result=$(echo "$line" | awk '{print $1}')
        user=$(echo "$line" | awk '{print $2}')
        echo "2*$x = $result"
        echo "server: $user"
        exit 0
    fi
done
