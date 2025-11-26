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
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
b'HTTP/1.1 400 Bad Request\r\nDate: Tue, 11 Sep 2018 12:12:29 GMT\r\nServer: Apache/2.4.7 (Ubuntu)\r\nContent-Length: 437\r\nConnection: close\r\nContent-Type: text/html; charset=iso-8859-1\r\n\r\n<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>400 Bad Request</title>\n</head><body>\n<h1>Bad Request</h1>\n<p>Your browser sent a request that this server could not understand.<br />\nReason: You\'re speaking plain HTTP to an SSL-enabled server port.<br />\n Instead use the HTTPS scheme to access this URL, please.<br />\n</p>\n<hr>\n<address>Apache/2.4.7 (Ubuntu) Server at 127.0.1.1 Port 443</address>\n</body></html>\n'
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++