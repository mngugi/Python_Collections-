import socket

lasocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lasocket.connect(('<xxxxx.com>', 80))

cmd = 'GET http://<xxxxx.com> HTTP/1.0\r\n\r\n'.encode()
lasocket.send(cmd)

while True:
    data = lasocket.recv(512)
    if (len(data) < 1 ):
        break
    print(data.decode(), end='')

lasocket.close()
