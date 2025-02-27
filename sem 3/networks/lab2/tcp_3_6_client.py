import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777))

num = input("Enter a number: ")
s.send(num.encode())

for i in range(int(num)):
    next_element = input("Enter the next element: ")
    s.send(next_element.encode())

print(s.recv(10).decode())
s.close()
