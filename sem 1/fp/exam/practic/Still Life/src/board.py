from copy import deepcopy

from texttable import Texttable


class BoardError(Exception):
    pass


class Board:
    def __init__(self):
        self.__board = [[0 for i in range(8)] for i in range(8)]

    def get_board(self):
        return self.__board

    def set_board(self, board: list):
        self.__board = board

    def get_element(self, i, j):
        return self.__board[i][j]

    def __str__(self):
        t = Texttable()
        head = [i for i in range(9)]
        t.header(head)
        for i in range(8):
            row = [i + 1]
            for j in range(8):
                if self.__board[i][j] == 0:
                    row.append(" ")
                else:
                    row.append("X")
            t.add_row(row)
        return t.draw()

    def place(self, pattern, x, y):
        """
        This function ensures that the pattern doesn't have any live cell outside of the border
        :param pattern: matrix of the pattern
        :param x: the corner coord
        :param y: --||--
        """
        n = len(pattern)  # the pattern is a square matrix, so NxN
        for i in range(n):
            for j in range(n):
                if pattern[i][j] == 1 and (x + i - 1 > 7 or j + y - 1 > 7):
                    raise BoardError("Live cell outside of board.")
                elif pattern[i][j] == 0 and (x + i - 1 > 7 or j + y - 1 > 7):
                    continue
                elif self.__board[x + i - 1][j + y - 1] == 1 and pattern[i][j] == 0:
                    continue
                elif self.__board[x + i - 1][j + y - 1] == 1 and pattern[i][j] == 1:
                    raise BoardError("You cannot overlap a live cell.")
        for i in range(n):
            for j in range(n):
                if pattern[i][j] == 1 and (x + i - 1 > 7 or j + y - 1 > 7 or x + i - 1 < 0 or y + j - 1 < 0):
                    raise BoardError("Live cell outside of board.")
                elif pattern[i][j] == 0 and (x + i - 1 > 7 or j + y - 1 > 7):
                    continue
                elif self.__board[x + i - 1][j + y - 1] == 1 and pattern[i][j] == 0:
                    continue
                elif self.__board[x + i - 1][j + y - 1] == 1 and pattern[i][j] == 1:
                    raise BoardError("You cannot overlap a live cell.")
                else:
                    self.__board[x + i - 1][j + y - 1] = pattern[i][j]
