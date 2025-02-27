import socket
import threading
# Se transmite o litera de la client la server, serveru trimite inapoi litera dublata


def client(cs, addr):
    print(f"Client {addr} connected")
    try:
        n = str(cs.recv(10).decode())
        m = list(n)
        print(f"Received {m[0]} from {addr}")
        # problem
        p = m[0] + m[0]
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
