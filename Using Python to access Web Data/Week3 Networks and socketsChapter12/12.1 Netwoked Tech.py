# Python built in support for TCP sockets
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80)) # data pr4e.org is host, 80 is port.
