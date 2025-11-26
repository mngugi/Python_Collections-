import socket 

target_host = "www.google.com"
target_port = 80
target_port = 21
target_port = 22
target_port = 443
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect the client
client.connect((target_host,target_port))
#send some data
client.sendall(b'GET /HTTP/1.1\r\n\r\n')
# receive some data
response = client.recv(4096)
print (response)
