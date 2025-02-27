import socket
import threading
# Intoarce numarul cuvintelor din lista


def client(cs, addr):
    print(f"Client {addr} connected")
    try:
        arr = []
        while True:
            word = str(cs.recv(10).decode()).strip()
            if word == "stop":
                break
            arr.append(word)
        print(f"Received {arr} from {addr}")
        p = str(len(arr))
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
