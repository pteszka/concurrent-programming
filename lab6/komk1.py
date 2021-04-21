import sys
import sysv_ipc

KLUCZ = 10
mq = sysv_ipc.MessageQueue(KLUCZ)
message = 'Dzień dobry'
message = message.encode()
mq.send(message)
s, type =  mq.receive()
s = s.decode()
print('Od serwera otrzymalem:', s)
