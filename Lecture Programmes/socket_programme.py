# Demostration of socket programming


import socket
import sys

try:
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create Socket")
    sys.exit()

print(my_socket)

try:
    host = socket.gethostbyname('www.google.com')
except socket.gaierror():
    print("Failed to get Host")

print(host)

try:
    my_socket.connect((host, 80))
    print("Connection Successful")
except:
    print("Cannot Connect to Host")
    sys.exit()

message = "GET /HTTP/1.1\r\n\r\n"

try:
    my_socket.sendall(message)
except socket.error:
    print("Failed to send")
    sys.exit()
data = my_socket.recv(1000)
print(data)
my_socket.close()