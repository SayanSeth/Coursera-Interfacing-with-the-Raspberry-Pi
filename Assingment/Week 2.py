# Use the socket to write a simple web server running on your Raspberry Pi.
# When your server receives a request it should print “Got a request!” to the screen of the Raspberry Pi.


import socket
import sys

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    my_socket.bind(("", 1234))
except socket.error:
    print("Failed to Bind")
    sys.exit()

my_socket.listen(5)

while True:
    connection,address = my_socket.accept()
    print("Got a request!")
    data = connection.recv(1000)
    print(data)
    if not data:
        break
    connection.sendall(data)

connection.close()
my_socket.close()
