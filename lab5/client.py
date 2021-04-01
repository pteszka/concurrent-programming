#!/usr/bin/env python3

import os
import select
import sys
import struct
from message import create_msg, get_message 

SERVER_FIFO="serverfifo"

def send_msg(content):
    server_fifo = os.open(SERVER_FIFO, os.O_WRONLY)
    try:
        msg = create_msg(content)
        os.write(server_fifo, msg)
    finally:
        os.close(server_fifo)

def get_response_from_server(CLIENT_FIFO):
    fifo = os.open(CLIENT_FIFO, os.O_RDONLY | os.O_NONBLOCK)
    poll = select.poll()
    poll.register(fifo, select.POLLIN)
    try:
        while True:
            # Check if there's data to read. Timeout after 1 sec.
            if (fifo, select.POLLIN) in poll.poll(5000):
                print(get_message(fifo))
                break
    finally:
        poll.unregister(fifo)


if __name__ == "__main__":
    path_to_clientfifo = sys.argv[1]
    id = sys.argv[2]
    # Make the client named pipe
    os.mkfifo(path_to_clientfifo)
    try:
        path = path_to_clientfifo
        content = f"{id} {path}".encode("utf8")
        send_msg(content)
        get_response_from_server(path_to_clientfifo)
    finally:
        os.remove(path_to_clientfifo)