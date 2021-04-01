#!/usr/bin/env python3

import struct
import os
from database import db
import select
from message import create_msg, decode_msg_size, get_message

SERVER_FIFO="serverfifo"

def get_surname_from_db(id):
    return db[id] if id in db else "Nie ma"

def send_response(res, path_to_clientfifo):
    client_fifo = os.open(path_to_clientfifo, os.O_WRONLY)
    msg = create_msg(res.encode("utf8"))
    os.write(client_fifo, msg)
    # finally:
    #     os.close(client_fifo)


if __name__ == "__main__":
    # Make the named pipe and poll for new messages.
    os.mkfifo(SERVER_FIFO)
    try:
        # Open the pipe in non-blocking mode for reading
        server_fifo = os.open(SERVER_FIFO, os.O_RDONLY | os.O_NONBLOCK)
        try:
            # Create a polling object to monitor the pipe for new data
            poll = select.poll()
            poll.register(server_fifo, select.POLLIN)
            try:
                while True:
                    # Check if there's data to read. Timeout after 1 sec.
                    if (server_fifo, select.POLLIN) in poll.poll(1000):
                        msg, path_to_clientfifo = get_message(server_fifo).split(maxsplit=1)
                        response = get_surname_from_db(int(msg))
                        send_response(response, path_to_clientfifo)
            finally:
                poll.unregister(server_fifo)
        finally:
            os.close(server_fifo)
    finally:
        os.remove(SERVER_FIFO)