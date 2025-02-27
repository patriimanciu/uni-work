import socket
import threading
from datetime import datetime

# -clientul citeste de la tastatura un numar reprezentat pe 4 octeti cu semn si il trimite serverului
# -serverul returneaza clientului data si ora cand un alt client anterior a trimis un numar identic cu numarul trimis de
# client sau 0 in caz contrar


HOST = "0.0.0.0"
PORT = 1234
received = {}


def client(cs, addr):
    print(f"Client {addr} connected")
    try:
        n = str(cs.recv(4).decode()).strip()
        print(f"Received {n} from {addr}")
        if n in received.keys():
            cs.send(received[n].encode())
        else:
            cs.send("0".encode())
        received[n] = str(datetime.date(datetime.now())) + " " + str(datetime.time(datetime.now()))

    except Exception as e:
        print(f"Error on {addr}: {e}")
    cs.close()
    print(f"Client {addr} disconnected")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Server running...")
while True:
    cs, addr = s.accept()
    client_thread = threading.Thread(target=client, args=(cs, addr))
    client_thread.daemon = True
    client_thread.start()
