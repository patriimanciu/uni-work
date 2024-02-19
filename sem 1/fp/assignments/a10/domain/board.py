class BoardError(Exception):
    pass


class Board:
    def __init__(self):
        self.__board = {
            'A1': ' ', 'A4': ' ', 'A7': ' ',
            'B2': ' ', 'B4': ' ', 'B6': ' ',
            'C3': ' ', 'C4': ' ', 'C5': ' ',
            'D1': ' ', 'D2': ' ', 'D3': ' ', 'D5': ' ', 'D6': ' ', 'D7': ' ',
            'E3': ' ', 'E4': ' ', 'E5': ' ',
            'F2': ' ', 'F4': ' ', 'F6': ' ',
            'G1': ' ', 'G4': ' ', 'G7': ' '
        }

    def get_board(self):
        """
        :return: a dict representing the current state of the board
        """
        return self.__board

    def get_point(self, point: str):
        """
        :param point: an index of the dict
        :return: the symbol on that position
        :raises BoardError is the point does not appear in the dict
        """
        if point in self.__board.keys():
            return self.__board[point]
        else:
            raise BoardError(f"Key {point} not found!")

    def display(self):
        print("    A      B      C    D    E      F      G")
        print("1   {} ---------------- {} ---------------- {}".format(self.__board['A1'], self.__board['D1'],
                                                                      self.__board['G1']))
        print("    |                  |                  |")
        print("2   |      {} --------- {} --------- {}      |".format(self.__board['B2'], self.__board['D2'],
                                                                      self.__board['F2']))
        print("    |      |           |           |      |")
        print("3   |      |      {} -- {} -- {}      |      |".format(self.__board['C3'], self.__board['D3'],
                                                                      self.__board['E3']))
        print("    |      |      |         |      |      |")
        print("4   {} ---- {} ---- {}         {} ---- {} ---- {}".format(self.__board['A4'], self.__board['B4'],
                                                                         self.__board['C4'], self.__board['E4'],
                                                                         self.__board['F4'], self.__board['G4']))
        print("    |      |      |         |      |      |")
        print("5   |      |      {} -- {} -- {}      |      |".format(self.__board['C5'], self.__board['D5'],
                                                                      self.__board['E5']))
        print("    |      |           |           |      |")
        print("6   |      {} --------- {} --------- {}      |".format(self.__board['B6'], self.__board['D6'],
                                                                      self.__board['F6']))
        print("    |                  |                  |")
        print("7   {} ---------------- {} ---------------- {}".format(self.__board['A7'], self.__board['D7'],
                                                                      self.__board['G7']))

    def set_space(self, point, symbol: str):
        """
        :param point: an index of the dict
        :param symbol: O or X
        """
        self.__board[point] = symbol
