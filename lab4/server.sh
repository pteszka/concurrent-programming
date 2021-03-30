#!/bin/bash

server="serwerfifo";
client="klientfifo";

trap "" SIGHUP
trap "" SIGTERM
trap "rm -f $server; exit 0" SIGUSR1

# if server get any parameter
if [[ ! $# -eq 0 ]] ; then
    echo $(($1*2)) > $client
    exit 0
fi

# create server if not exists
if [[ ! -p "$server" ]]; then
    mkfifo $server
fi

while true 
do
    if read line < $server; then
        x=$(echo "$line" | awk '{print $2}')
        if [[ $x == "end" ]]; then
            kill -SIGUSR1 $$
        fi
        $0 $x &
        wait $!
    fi
done

exit 0
