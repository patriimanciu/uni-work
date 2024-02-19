from texttable import Texttable


class Board:
    def __init__(self):
        # list of lists
        self.__board = [[[i, j, '/'] for i in range(6)] for j in range(6)]
        self.placed = 0

    def symbols(self, row):
        r = []
        for i in range(6):
            if self.__board[i][row][2] == '/':
                r.append(' ')
            else:
                r.append(self.__board[i][row][2])
        return r

    def __str__(self):
        t = Texttable()
        header_row = ['/']
        for i in range(6):
            header_row.append(i)
        t.header(header_row)
        for j in range(6):
            t.add_row([j] + self.symbols(j))
        return t.draw()

    def board(self):
        return self.__board

    def get_move(self, i, j):
        return self.__board[i][j]

    def move(self, i: int, j: int, symbol):
        self.__board[i][j] = [i, j, symbol]
        if symbol != '/':
            self.placed += 1
