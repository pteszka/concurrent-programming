#!/usr/bin/env python3

from functions import get_client_name, write_text
from filelock import FileLock, Timeout
from time import sleep
import os
import sys
import pathlib
from pathlib import Path


client_name = get_client_name()
print("Nazwa klienta:", client_name)


file_path = "server"
lock_path = "server.lock"

lock = FileLock("server.lock")

while Path(lock_path).is_file():
    print("Serwer zajęty, prosze czekac")
    sleep(3)


with lock:
    print("Wpisz pytanie: ")
    lines = write_text()
    f = open("server", "w")
    f.write("\n".join([client_name, lines]))
    f.close()
    print("...Czekam na odpowiedź")
    while True:
        if Path(client_name).is_file():
            with open(client_name, 'r') as f:
                print(f.read())
            os.remove(client_name)
            sys.exit()
