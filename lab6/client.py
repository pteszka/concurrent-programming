#!/usr/bin/env python3

import sys
from sysv_ipc import MessageQueue, IPC_CREAT, ftok
import os

KEY_A=13
KEY_B=21

def send_word(queue):
    word = input("Podaj słowo, które chcesz przetłumaczyć: ")
    msg = [word, str(os.getpid())]
    queue.send('^'.join(msg).encode())

def display_response(queue):
    word, type =  queue.receive()
    print(word.decode())

if __name__ == "__main__":
    mq_A = MessageQueue(KEY_A)
    mq_B = MessageQueue(KEY_B)

    send_word(mq_A)
    display_response(mq_B)
