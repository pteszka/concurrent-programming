#!/usr/bin/env python3

import sys
from sysv_ipc import MessageQueue, IPC_CREAT
from database import db
import os

KEY_A=13
KEY_B=21

def get_word_from_db(word):
    return db[word] if word in db else "Nie znam takiego słowa"

def get_word_and_pid_from_queue(queue):
    msg, type = queue.receive()
    msg = msg.decode()
    return msg.split('^')

def send_responde(queue, res):
    res = get_word_from_db(res).encode()
    queue.send(res)

if __name__ == "__main__":
    # creating message queues for input and output
    mq_A = MessageQueue(KEY_A, IPC_CREAT)
    mq_B = MessageQueue(KEY_B, IPC_CREAT)

    while True:
        word, pid = get_word_and_pid_from_queue(mq_A)
        print(f"Otrzymalem '{word}' od {pid}")

        send_responde(mq_B, word)

