from domain.board import Board, BoardError


class BoardService:
    def __init__(self, board: Board):
        self.__board = board

    def is_valid_point(self, point: str):
        """
        :param point: a point on the board
        :return: True if it is a valid point, False otherwise
        """
        return point in self.__board.get_board().keys()

    def is_empty(self, point: str):
        """
        :param point: a point on the board
        :return: True if it is an empty point, False otherwise
        """
        return self.__board.get_point(point) == ' '

    def move(self, point: str, symbol: str):
        """
        Makes a move on the board
        :param point: the chosen point on the board
        :param symbol: the player's symbol (X or O)
        :raises BoardError("The point is not valid.") if point is not a valid format
                BoardError("The chosen point is not empty.") if that specific place is already taken by someone else
        """
        if not self.is_valid_point(point):
            raise BoardError("The point is not valid.")
        if not self.is_empty(point):
            raise BoardError("The chosen point is not empty.")
        self.__board.set_space(point, symbol)
