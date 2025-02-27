import socket
import threading
import time

HOST = "0.0.0.0"
TCP_PORT = 1234
BROADCAST_PORT = 7777


class Server:
    def __init__(self):
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.INSIDE = 0
        self.TOTAL = 0
        self.PI_APPROX = 0
        self.tcp.bind((HOST, TCP_PORT))
        self.tcp.listen(5)

    def client(self, cs, addr):
        print(f"Client {addr} connected")
        try:
            while True:
                n = cs.recv(10).decode().strip()
                a, b = map(int, n.split(" "))
                n = a / 50.0 - 1
                m = b / 50.0 - 1
                print(f"Received x:{n}, y: {m} from {addr} -> {a}, {b}")
                if m * m + n * n <= 1:
                    self.INSIDE += 1
                    print("Inside")
                else:
                    print("Outside")
                self.TOTAL += 1
                old = self.PI_APPROX
                self.PI_APPROX = 4 * self.INSIDE / self.TOTAL
                print(f"PI_APPROX: {self.PI_APPROX}")
                if old != 0 and abs(old - self.PI_APPROX) < 0.0001:
                    print("Converged")
                    break
        except Exception as e:
            print(f"Error on {addr}: {e}")
        finally:
            cs.close()
            print(f"Client {addr} disconnected")

    def update(self):
        while True:
            time.sleep(5)
            print("Broadcasting PI_APPROX...")
            self.udp.sendto(str(self.PI_APPROX).encode(), ("255.255.255.255", BROADCAST_PORT))

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
        except (KeyboardInterrupt, Exception) as e:
            print("Shutting down...")
        finally:
            self.tcp.close()
            print("Server stopped")


if __name__ == "__main__":
    s = Server()
    s.run()
