import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg="hey"
s.sendto(str.encode(msg),("127.0.0.1",5555))
msg,adr=s.recvfrom(10)
print (msg.decode())
