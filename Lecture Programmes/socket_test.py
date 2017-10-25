import socket
import sys

try:
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create Socket")
    sys.exit()

print(my_socket)
host = "192.168.1.219"
print(host)

try:
    my_socket.connect((host, 1234))
    print("Connection Successful")
except:
    print("Cannot Connect to Host")
    sys.exit()

message = b"Hello Raspberry Pi"

try:
    my_socket.sendall(message)
except socket.error:
    print("Failed to send")
    sys.exit()
data = my_socket.recv(1000)
print(data)
my_socket.close()