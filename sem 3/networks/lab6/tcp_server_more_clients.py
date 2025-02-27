# to serve more clients at the same time, you have to either use threads or fork()

import socket
import threading

# Intoarce cuvantul cu cele mai multe vocale
def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count


def client(cs, addr):
    print(f"Client {addr} connected")
    try:
        n = int(cs.recv(10).decode())
        print(f"Received {n} from {addr}")
        array = []
        for _ in range(n):
            array.append(cs.recv(10).decode())
        print(f"Words from {addr}: {array}")

        arr = []
        for i in range(n):
            j = count_vowels(array[i])
            arr.append(j)
        maxx = 0
        for i in range(n):
            if arr[i] > maxx:
                maxx = arr[i]

        for i in range(n):
            if arr[i] == maxx:
                cs.send(array[i].encode())
                break
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
