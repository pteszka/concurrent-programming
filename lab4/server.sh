#!/bin/bash

server="serwerfifo";
client="klientfifo";

# if server get any parameter
if [ ! $# -eq 0 ] ; then
    x=$(head -n 1 $server | awk  '{print $2}')
    echo $(($x*2)) > $client
    exit 0
fi

# create server if not exists
if [ ! -f "$server" ]; then
    > $server
fi

while true 
do
    if [ -s "$server" ]; then
        $0 filler &
    fi
done


# mkfifo $server_fifo;

# while true
# do
#     # -p True if FILE exists and is a named pipe (FIFO).
#     if [ -p $client_fifo ] ;
#     then
#         line=$(head -n 1 data);
#         x=$($line | awk  '{print $2}');
#         echo $(($x*2)) > $client_fifo
#     fi
# done
exit 0
