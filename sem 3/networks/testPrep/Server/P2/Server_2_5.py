import socket
import threading
# Intoarce cuvantul cu cele mai multe consoane


def countCons(word: str):
    vowels = "aeiou"
    count = 0
    for i in word:
        if i not in vowels:
            count += 1
    return count


def client(cs, addr):
    print(f"Client {addr} connected")
    try:
        arr = []
        numMostCons = 0
        mostCons = ""
        while True:
            word = str(cs.recv(10).decode()).strip()
            if word == "stop":
                break
            arr.append(word)
            consWord = countCons(word)
            if consWord > numMostCons:
                numMostCons = consWord
                mostCons = word
        print(f"Received {arr} from {addr}")
        if mostCons == "":
            cs.send("No words entered".encode())
        else:
            cs.send(mostCons.encode())
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
