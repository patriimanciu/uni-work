import operator
import random
import socket
import threading
import time

HOST = "0.0.0.0"
TCP_PORT = 1234
BROADCAST_PORT = 7777
QUIZ = 60
INTERVAL = 10

oper = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


class Server:
    def __init__(self):
        self.broadcast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.bind((HOST, TCP_PORT))
        self.tcp.listen(5)
        self.problems = []
        self.answers = []
        self.start = None
        self.lock = threading.Lock()
        # self.first_connection = threading.Event()

    def gen_quiz(self):
        self.problems.clear()
        self.answers.clear()
        for _ in range(random.randint(2, 5)):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            op = random.choice(list(oper.keys()))
            self.problems.append(f"{a} {op} {b} = ?")
            self.answers.append(int(oper[op](a, b)))

    def send_quiz(self):
        # self.first_connection.wait()
        while time.time() - self.start < QUIZ:
            self.gen_quiz()
            quiz_str = ";".join(self.problems)
            self.broadcast.sendto(quiz_str.encode(), (HOST, BROADCAST_PORT))
            print(f"Broadcast quiz {quiz_str}")
            time.sleep(INTERVAL)
        self.broadcast.close()

    def client(self, cs, addr):
        print(f"Client {addr} connected")
        try:
            score = 0
            for i in range(len(self.problems)):
                # Receive question index
                index_data = cs.recv(1024).decode().strip()
                if not index_data:
                    print(f"Client {addr} disconnected unexpectedly.")
                    break
                index = int(index_data)  # Convert to integer if valid

                # Receive the answer for the current question index
                answer_data = cs.recv(1024).decode().strip()
                if not answer_data:
                    print(f"Client {addr} disconnected unexpectedly.")
                    break
                answer = int(answer_data)  # Convert answer to integer

                # Check if the answer is correct
                if index == i and answer == self.answers[i]:
                    score += 1

                print(f"Received answer for question {index}: {answer} from {addr}")

                # Send final score to client after all answers are received
            cs.send(f"Your score: {score}/{len(self.problems)}".encode())
            print(f"Score sent to {addr}")
        except Exception as e:
            print(f"Error on {addr}: {e}")
        cs.close()
        print(f"Client {addr} disconnected")

    def receive_answers(self):
        while self.start is None or time.time() - self.start < QUIZ + 10:
            cs, addr = self.tcp.accept()
            client_thread = threading.Thread(target=self.client, args=(cs, addr))
            client_thread.daemon = True
            client_thread.start()

    def run(self):
        print("Server running...")
        # self.first_connection.wait()
        self.start = time.time()

        broadcast_thread = threading.Thread(target=self.send_quiz)
        broadcast_thread.start()

        self.receive_answers()

        broadcast_thread.join()
        self.tcp.close()
        print("Server stopped")


if __name__ == "__main__":
    s = Server()
    s.run()
