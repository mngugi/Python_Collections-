import socket

lasocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lasocket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
lasocket.send(cmd)

while True:
    data = lasocket.recv(512)
    if (len(data) < 1 ):
        break
    print(data.decode(), end='')

lasocket.close()
