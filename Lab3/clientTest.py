import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.99.85', 8080))
client.sendall('I am CLIENT'.encode())
from_server = client.recv(4096)
client.close()
print(from_server)
