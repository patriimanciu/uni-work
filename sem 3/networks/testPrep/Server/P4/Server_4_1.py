import socket
import threading

# Clientul trimite serverului un sir de caractere (de exemplu numele utilizatorului citit de la tastatura). Serverul
# afiseaza pe ecran sirul primit si portul clientului si ii raspunde acestuia cu suma cifrelor din Portul clientului.
# Clientul va afisa pe ecran numarul primit.


def client(cs, addr):
    """
    Function that handles the client connection
    :param cs: client socket
    :param addr: client address
    """
    print(f"Client {addr} connected - port {addr[1]}")
    try:
        n = cs.recv(20).decode().strip()
        print(f"Received {n} from {addr}")
        suma = 0
        for i in str(addr[1]):
            suma += int(i)
        cs.send(str(suma).encode())
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
