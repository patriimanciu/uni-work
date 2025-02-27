import socket
import threading
# Clientul trimite 2 numere, serverul intoarce cel mai mic/mare numar


def client(cs, addr):
    print(f"Client {addr} connected")
    try:
        n1 = cs.recv(10).decode()
        n2 = cs.recv(10).decode()
        print(f"Received {n1} and {n2} from {addr}")
        if n1 > n2:
            cs.send(n2.encode())
        else:
            cs.send(n1.encode())
    except Exception as e:
        print(f"Error on {addr}: {e}")
    cs.close()
    print(f"Client {addr} disconnected")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 1234))
s.listen(5)
while True:
    cs, addr = s.accept()
    client_thread = threading.Thread(target=client, args=(cs, addr))
    client_thread.daemon = True
    client_thread.start()
