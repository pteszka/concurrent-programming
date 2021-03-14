import sys
import os


def is_esc(char):
    return ord(char) == 27


def get_client_name():
    return sys.argv[1]


def write_text():
    msg = ""
    while True:
        char = sys.stdin.read(1)
        if is_esc(char):
            print("Wiadomość została wysłana!")
            return msg
        else:
            msg += char