import socket
import threading
import time

HOST = "0.0.0.0"
TCP_PORT = 1234
BROADCAST_PORT = 7777
INTERVAL = 5
MAP = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']


class Server:
    def __init__(self):
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.bind((HOST, TCP_PORT))
        self.tcp.listen(5)

    def client(self, cs, addr):
        print(f"Client {addr} connected")
        try:
            while True:
                n = str(cs.recv(10).decode()).strip()
                a, b = n.split(" ")
                print(f"Received index:{a}, char: {b} from {addr}")

                if 0 <= int(a) < len(MAP) and MAP[int(a)] == 'u':
                    MAP[int(a)] = b
                print(f"Updated MAP: {MAP}")
        except Exception as e:
            print(f"Error on {addr}: {e}")
            cs.close()
            print(f"Client {addr} disconnected")

    def update(self):
        while True:
            time.sleep(INTERVAL)
            print("Broadcasting...")
            self.udp.sendto(str(MAP).encode(), (HOST, BROADCAST_PORT))

    def run(self):
        print("Server running...")
        broadcast_thread = threading.Thread(target=self.update)
        broadcast_thread.daemon = True
        broadcast_thread.start()

        try:
            while True:
                cs, addr = self.tcp.accept()
                client_thread = threading.Thread(target=self.client, args=(cs, addr))
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            print("Shutting down...")
        self.tcp.close()
        print("Server stopped")


if __name__ == "__main__":
    s = Server()
    s.run()
