from domain import Board
from random import randint, choice


class BoardError(Exception):
    pass


class FileError(Exception):
    pass


class BoardService:
    def __init__(self, board: Board):
        self.__board = board

    def move(self, i: int, j: int, symbol: str):
        try:
            i = int(i)
            j = int(j)
        except ValueError as err:
            raise BoardError("Invalid literal, first 2 terms must be ints.")
        if i < 0 or i > 5 or j < 0 or j > 5:
            raise BoardError("Invalid input coord.")
        if symbol != "O" and symbol != "X" and symbol != '/':
            raise BoardError("Invalid input symbol.")
        a = self.__board.get_move(i, j)
        if a[2] != '/':
            raise BoardError("Space already occupied.")
        self.__board.move(i, j, symbol)

    def computer_move(self):
        if self.possible_win() is not None:
            i, j, s = self.possible_win()
            if s == "X":
                self.move(i, j, "O")
                return [i, j, "O"]
            else:
                self.move(i, j, "X")
                return [i, j, "X"]
        while True:
            try:
                i = randint(0, 5)
                j = randint(0, 5)
                symbol = choice(["O", "X"])
                self.move(i, j, symbol)
                return [i, j, symbol]
            except BoardError:
                pass

    def check_if_won(self):
        for i in range(6):
            for j in range(6):
                symbol = self.__board.get_move(i, j)[2]
                if symbol != '/' and self.check_consecutive(i, j, symbol):
                    return True
        return False

    def check_consecutive(self, row, col, symbol):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            count = 1
            for step in range(1, 5):
                r, c = row + step * dr, col + step * dc
                if 0 <= r < 6 and 0 <= c < 6 and self.__board.get_move(r, c)[2] == symbol:
                    count += 1
                else:
                    break
            if count == 5:
                return True
        return False

    def possible_win(self):
        for i in range(6):
            for j in range(6):
                for s in ["X", "O"]:
                    if self.__board.get_move(i, j)[2] == '/':
                        self.move(i, j, s)
                        if self.check_if_won():
                            self.__board.move(i, j, '/')
                            return [i, j, s]
                        self.__board.move(i, j, '/')
        return None

    def full_board(self):
        if self.__board.placed == 36:
            return True
        return False

    def load(self, filename):
        try:
            with open(filename, 'r') as file:
                if file.readable() and len(file.read()) == 0:
                    raise FileError("File is empty!")
                file.seek(0)
                for line in file:
                    data = line.strip().split(',')
                    try:
                        self.move(int(data[0]), int(data[1]), data[2])
                    except BoardError as err:
                        raise FileError(str(err))
        except FileNotFoundError:
            raise FileError("File doesn't exist.")

    def save(self, filename='file.txt'):
        try:
            with open(filename, 'w') as file:
                for i in range(6):
                    for j in range(6):
                        move = self.__board.get_move(i, j)
                        file.write(f"{move[0]},{move[1]},{move[2]},\n")
        except Exception as err:
            raise FileError(f"Error saving to file: {err}")
