import random
import socket
import struct
from multiprocessing import Process
from time import sleep


def handle_client(cs, addr, nr, twist):
    guessed = False
    print(f"Handling client {addr}")
    try:
        while not guessed:
            twist += 1
            data = cs.recv(4)
            if not data:
                break
            num1 = struct.unpack("!i", data)[0]
            print(f"Client {addr} guessed {num1}")
            sleep(1)
            if num1 == nr:
                guessed = True
                cs.send("Congrats!\n".encode())
            elif num1 < nr:
                cs.send("higher\n".encode())
            else:
                cs.send("lower\n".encode())
    finally:
        cs.close()
        print(f"Connection closed with {addr}")


if _name_ == "_main_":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 1235))
    server_socket.listen(5)
    nr = random.randint(1, 100)
    print("Generated number:", nr)

    while True:
        cs, addr = server_socket.accept()
        print(f"Connection accepted from {addr}")
        process = Process(target=handle_client, args=(cs, addr, nr))
        process.sta