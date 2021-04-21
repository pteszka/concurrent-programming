import sys
from sysv_ipc import MessageQueue, IPC_CREAT

KLUCZ = 10
mq = MessageQueue(KLUCZ, IPC_CREAT)
message, type = mq.receive()
message = message.decode()
print('Otrzymałem: ', message)
message  = 'Witaj'
tekst = message.encode()
mq.send(tekst)
