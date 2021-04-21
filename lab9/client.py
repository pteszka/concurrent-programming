#!/usr/bin/env python3

import socket
import struct

HOST = '127.0.0.1'
PORT = 5000

data = input('Podaj liczbe: ')
data = str.encode(data)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data)
    res = s.recv(32)
    res = res.decode()
    print(f'Otrzymałem: {res}')
