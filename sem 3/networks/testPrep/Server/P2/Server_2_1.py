import socket
import threading
# Intoare cuvintele concatenate


def client(cs, addr):
    print(f"Client {addr} connected")
    try:
        n = int(cs.recv(10).decode())
        print(f"Received {n} from {addr}")
        # problem
        p = ""
        arr = []
        for i in range(n):
            n = str(cs.recv(10).decode()).strip()
            arr.append(n)
            p += str(n)
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
