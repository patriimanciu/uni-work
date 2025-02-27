import socket
import threading
# Intoarce lungimea cuvantului

def client(cs, addr):
    print(f"Client {addr} connected")
    try:
        n = str(cs.recv(10).decode())
        print(f"Received {n.strip()} from {addr}")
        # problem
        p = str(len(n.strip()))
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
