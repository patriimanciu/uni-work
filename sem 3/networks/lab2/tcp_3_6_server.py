import socket
# Clientul trimite o lista de numere, serverul intoarce suma acestora
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)
cs, addr = s.accept()
array = []
n = int(cs.recv(10).decode())
print(n)
sum = 0
for i in range(n):
    array.append(int(cs.recv(10).decode()))
    sum += array[i]

cs.send(str(sum).encode())
cs.close()
