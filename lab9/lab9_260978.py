#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 5000
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                buff = conn.recv(32)
                if not buff:
                    break
                data = buff.decode()
                data = int(data)
                data *= 2
                data = str(data)
                data = data.encode()
                conn.sendall(data)