from copy import deepcopy

from src.board import Board, BoardError


class GameError(Exception):
    pass


class Game:
    def __init__(self, board: Board):
        self.__board = board
        self.__pattern = []

    def load_patterns(self, pattern, filename='pattern.txt'):
        """
        Function loads the pattern type from file and passes it to self.__pattern as a list of lists
        :param pattern: the name of the pattern
        :param filename: name of the file (optional)
        :raises: GameError if the file is empty
        """
        try:
            with open(filename, 'r') as file:
                if file.readable() and len(file.read()) == 0:
                    raise GameError("File is empty!")
                file.seek(0)
                for line in file:
                    p = line.split("=")
                    if p[0] == pattern:
                        self.__pattern = self.compute_matrix(p[1])
                        break
        except FileNotFoundError:
            pass

    def place(self, data):
        """
        the function first loads the pattern type from file and places it to the board if everything goes well
        :param data: data[0] is the name of the pattern adn data[1] holds the coord
        :raises: GameError if the pattern doesn't exits, the coord aren't ints or if there was a problem while placing the pattern
        """
        self.load_patterns(data[0])
        # print(self.__pattern)
        if not self.__pattern:
            raise GameError("Pattern doesn't exist.")
        coord = data[1].strip(' ').split(',')
        if len(coord) == 1:
            raise GameError("Not enough coord")
        try:
            i = int(coord[0])
            j = int(coord[1])
        except ValueError:
            raise GameError("Coord. should be integers")
        try:
            self.__board.place(self.__pattern, i, j)
        except BoardError as e:
            raise GameError(e)

    def tick(self, param=1):
        """
        The function computes the next generation due to some given features
        :param param: the number of generations we want to pass
        """
        new_board = [[0 for i in range(8)] for i in range(8)]
        for i in range(param):
            current_board = deepcopy(self.__board.get_board())
            for i in range(8):
                for j in range(8):
                    neighbours = self.get_neighbours(i, j, current_board)
                    if neighbours in [2, 3] and current_board[i][j] == 1:
                        new_board[i][j] = 1
                    elif neighbours < 2 and current_board[i][j] == 1:
                        new_board[i][j] = 0
                    elif neighbours > 3 and current_board[i][j] == 1:
                        new_board[i][j] = 0
                    elif neighbours == 3 and current_board[i][j] == 0:
                        new_board[i][j] = 1
        self.__board.set_board(new_board)

    @staticmethod
    def get_neighbours(i, j, board):
        """
        computes the number of live neighbours of each field
        :param i: coord
        :param j: coord
        :param board: the board we want to compute
        :return: the count of live neighbours
        """
        count = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < 8 and 0 <= y < 8 and (x != i or y != j):
                    if board[x][y] == 1:
                        count += 1
        return count

    def save(self, filename='game.txt'):
        try:
            board = self.__board.get_board()
            with open(filename, 'w') as file:
                for i in range(8):
                    for j in range(8):
                        file.write(str(board[i][j]) + ',')
                    file.write('\n')
        except FileNotFoundError:
            pass

    def load(self, filename='game.txt'):
        try:
            board = []
            with open(filename, 'r') as file:
                if file.readable() and len(file.read()) == 0:
                    raise GameError("File is empty!")
                file.seek(0)
                for line in file:
                    row = []
                    p = line.strip().split(",")
                    for i in range(len(p) - 1):
                        row.append(int(p[i]))
                    board.append(row)
                self.__board.set_board(board)
        except FileNotFoundError:
            pass

    def get_pattern(self):
        return self.__pattern

    @staticmethod
    def compute_matrix(param: str):
        listing = []
        row = []
        for i in range(len(param)):
            if param[i] == "[":
                row = []
            elif param[i] == ",":
                continue
            elif param[i] == "]":
                listing.append(row)
            elif param[i] == '\n':
                continue
            else:
                row.append(int(param[i]))
        return listing

