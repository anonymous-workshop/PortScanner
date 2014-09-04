__author__ = 'bigfoot'

import time
import socket


hostname = raw_input('Enter Host to scan: ')

for i in range(1, 9999):

    s = socket.socket()
    s.settimeout(.05)
    ip = socket.gethostbyname(hostname)

    response = s.connect_ex((ip,i))

    if response:
        continue
    else:
        print ("%d\topen" %i)

    s.close()
