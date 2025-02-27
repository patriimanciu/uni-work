import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 5555))
print("Server is running...")
data, addr = s.recvfrom(10)
print("Message: ", data.decode())
print("From: ", addr)
response = "hello"
s.sendto(str.encode(response), addr)
