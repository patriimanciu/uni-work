import socket
import threading
# Clientul trimite 2 numere, serverul intoarce produsul


def prod(a, b):
    return a * b


def client(cs, addr):
    print(f"Client {addr} connected")
    try:
        n1 = int(cs.recv(10).decode())
        n2 = int(cs.recv(10).decode())
        print(f"Received {n1} and {n2} from {addr}")
        p = str(prod(n1, n2))
        cs.send(p.encode())
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
