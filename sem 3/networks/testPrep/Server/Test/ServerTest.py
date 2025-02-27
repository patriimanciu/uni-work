import random
import socket
import threading

# A server generates a random number. Multiple clients connect and take turns guessing the number. The server gives
# hints like "higher" or "lower."


def client(cs, addr, NUM):
    print(f"Client {addr} connected")
    guessed = False

    try:
        while not guessed:
            twist = random.randint(1, 10)
            num1 = int(cs.recv(10).decode())
            print(f"Client {addr} guessed {num1}")
            print(f"Twist: {twist}")
            if twist == 4:
                if num1 > NUM:
                    cs.send("higher\n".encode())
                else:
                    cs.send("lower\n".encode())

            if num1 == NUM:
                guessed = True
                cs.send("Congrats!\n".encode())
            elif num1 < NUM:
                cs.send("higher\n".encode())
            else:
                cs.send("lower\n".encode())
    finally:
        cs.close()
        print(f"Client {addr} disconnected")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
NUM = random.randint(1, 100)
print(f"Server started with number {NUM}")
s.listen(5)
while True:
    cs, addr = s.accept()
    client_thread = threading.Thread(target=client, args=(cs, addr, NUM))
    client_thread.daemon = True
    client_thread.start()
