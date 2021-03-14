#!/usr/bin/env python3

import os
from functions import write_text

open("server", "w+")

while True:
    if os.stat("server").st_size != 0:
        with open("server", "r") as f:
            lines = f.readlines()
            title = lines[0].strip()
            print("Wiadomość od:", title)
            print("".join(lines[1:]))    
        print("Podaj odpowiedź:")
        message = write_text()
        with open(title, "w+") as f_client:
            f_client.write(message)
            open("server", "w").close()
            os.remove("server.lock")