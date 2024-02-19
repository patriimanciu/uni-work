class Player:
    def __init__(self, symbol):
        # dict of positions, key = position, value is a list of tuples with the positions where a morris can be made
        self.__moves = {}
        # key - position, value list of possible slides
        self.__slide = {}
        self.__hand = 9
        self.__symbol = symbol

    @staticmethod
    def get_adjacent(move: str):
        """
        :param move: a valid position in the board
        :return: the adjacent positions where a mill can be formed
        """
        if move == 'A1':
            return [("D1", "G1"), ("A4", "A7")]
        if move == 'A4':
            return [("A1", "A7"), ("B4", "C4")]
        if move == 'A7':
            return [("A1", "A4"), ("D7", "G7")]

        if move == 'B2':
            return [("D2", "F2"), ("B4", "B6")]
        if move == 'B4':
            return [("B2", "B6"), ("A4", "C4")]
        if move == 'B6':
            return [("B2", "B4"), ("D6", "F6")]

        if move == 'C3':
            return [("D3", "E3"), ("C4", "C5")]
        if move == 'C4':
            return [("C3", "C5"), ("A4", "B4")]
        if move == 'C5':
            return [("C3", "C4"), ("D5", "E5")]

        if move == 'D1':
            return [("A1", "G1"), ("D2", "D3")]
        if move == 'D2':
            return [("D1", "D3"), ("B2", "F2")]
        if move == 'D3':
            return [("D1", "D2"), ("C3", "E3")]
        if move == 'D5':
            return [("D6", "D7"), ("C5", "E5")]
        if move == 'D6':
            return [("D5", "D7"), ("B6", "F6")]
        if move == 'D7':
            return [("D5", "D6"), ("A7", "G7")]

        if move == 'E3':
            return [("C3", "D3"), ("E4", "E5")]
        if move == 'E4':
            return [("F4", "G4"), ("E3", "E5")]
        if move == 'E5':
            return [("C5", "D5"), ("E3", "E4")]

        if move == 'F2':
            return [("B2", "D2"), ("F4", "F6")]
        if move == 'F4':
            return [("E4", "G4"), ("F2", "F6")]
        if move == 'F6':
            return [("B6", "D6"), ("F2", "F4")]

        if move == 'G1':
            return [("A1", "D1"), ("G4", "G7")]
        if move == 'G4':
            return [("E4", "F4"), ("G1", "G7")]
        if move == 'G7':
            return [("A7", "D7"), ("G1", "G4")]

    @staticmethod
    def get_slide(move: str):
        """
        :param move: a valid position in the board
        :return: the adjacent positions where the piece can slide
        """
        if move == 'A1':
            return ["D1", "A4"]
        if move == 'A4':
            return ["A1", "A7", "B4"]
        if move == 'A7':
            return ["A4", "D7"]

        if move == 'B2':
            return ["D2", "B4"]
        if move == 'B4':
            return ["B2", "B6", "A4", "C4"]
        if move == 'B6':
            return ["B4", "D6"]

        if move == 'C3':
            return ["D3", "C4"]
        if move == 'C4':
            return ["C3", "C5", "B4"]
        if move == 'C5':
            return ["C4", "D5"]

        if move == 'D1':
            return ["A1", "G1", "D2"]
        if move == 'D2':
            return ["D1", "D3", "B2", "F2"]
        if move == 'D3':
            return ["D2", "C3", "E3"]
        if move == 'D5':
            return ["D6", "C5", "E5"]
        if move == 'D6':
            return ["D5", "D7", "B6", "F6"]
        if move == 'D7':
            return ["D6", "A7", "G7"]

        if move == 'E3':
            return ["D3", "E4"]
        if move == 'E4':
            return ["F4", "E3", "E5"]
        if move == 'E5':
            return ["D5", "E4"]

        if move == 'F2':
            return ["D2", "F4"]
        if move == 'F4':
            return ["E4", "G4", "F2", "F6"]
        if move == 'F6':
            return ["D6", "F4"]

        if move == 'G1':
            return ["D1", "G4"]
        if move == 'G4':
            return ["F4", "G1", "G7"]
        if move == 'G7':
            return ["D7", "G4"]

    def symbol(self):
        """
        :return: the symbol of the player
        """
        return self.__symbol

    def placed_all(self):
        """
        :return: True if all 9 pieces were placed, False otherwise
        """
        return self.__hand == 0

    def dec_hand(self):
        """
        :return: decreases the value of hand with 1
        """
        self.__hand -= 1

    def get_hand(self):
        """
        :return: the numbers of pieces left to be placed
        """
        return self.__hand

    def set_move(self, point):
        """
        :param point: a place on the board
        """
        self.__moves[point] = self.get_adjacent(point)
        self.__slide[point] = self.get_slide(point)

    def get_moves(self):
        """
        :return: all moves ot that player
        """
        return self.__moves

    def remove_move(self, point: str):
        """
        :param point: move to be removed
        """
        if point in self.__moves.keys():
            self.__moves.pop(point)
            self.__slide.pop(point)
        # print(self.get_moves())

    def __len__(self):
        return len(self.__moves)
