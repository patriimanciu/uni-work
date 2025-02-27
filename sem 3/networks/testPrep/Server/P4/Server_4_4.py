import socket
import threading
# Transforma o cifra in cuvinte [1234-Una mii doua sute trei zeci si patru] (max 4 cifre)

def client(cs, addr):
    """
    Function that handles the client connection
    :param cs: client socket
    :param addr: client address
    """
    print(f"Client {addr} connected - port {addr[1]}")
    try:
        n = cs.recv(10).decode().strip()
        print(f"Received {n} from {addr}")
        cif = ""
        cnt = len(n) - 1
        for i in n:
            if i == "1":
                if cnt == 0:
                    cif += "unu "
                else:
                    cif += "una "
            if i == "2":
                if cnt == 0:
                    cif += "doi "
                else:
                    cif += "doua "
            if i == "3":
                cif += "trei "
            if i == "4":
                cif += "patru "
            if i == "5":
                cif += "cinci "
            if i == "6":
                cif += "sase "
            if i == "7":
                cif += "sapte "
            if i == "8":
                cif += "opt "
            if i == "9":
                cif += "noua "
            if cnt == 3:
                cif += "mii "
            if cnt == 2:
                cif += "sute "
            if cnt == 1:
                cif += "zeci si "
            cnt -= 1
        cs.send(cif.encode())
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
