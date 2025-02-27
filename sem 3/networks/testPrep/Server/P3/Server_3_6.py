import socket
import threading
# Clientul trimite o lista de numere, serverul intoarce suma acestora


def client(cs, addr):
    print(f"Client {addr} connected")
    try:
        arr = []
        while True:
            n = str(cs.recv(10).decode()).strip()
            if n == "stop":
                break
            arr.append(int(n))
        print(f"Received {arr} from {addr}")
        suma = str(sum(arr))
        cs.send(suma.encode())
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
