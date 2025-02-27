import socket
import threading


def client(cs, addr):
    print("Client connected")
    b = cs.recv(10)
    print(b)
    cs.send("Hello")
    cs.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)
while True:
    cs, addr = s.accept()
    client_thread = threading.Thread(target=client, args=(cs, addr))
    client_thread.daemon = True
    client_thread.start()

