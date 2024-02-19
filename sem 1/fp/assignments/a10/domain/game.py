from domain.board import Board
from domain.player import Player
from service.board import BoardService
from service.game import GameService, ServiceError


class GameError(Exception):
    pass


class Game:
    def __init__(self):
        self.__board = Board()
        self.__service = BoardService(self.__board)
        self.__game_service = GameService(self.__board)
        self.human = Player("X")
        self.computer = Player("O")
        self.won = False
        self.winner = ''

    def add_move(self, move: str, symbol="O"):
        """
        :param move: the position in dict you want to move to
        :param symbol: X or O
        """
        if symbol == "X":
            if not self.human.placed_all():
                self.human.set_move(move)
                self.human.dec_hand()
        else:
            if not self.computer.placed_all():
                self.computer.set_move(move)
                self.computer.dec_hand()

    def move(self, point: str, symbol="O"):
        """
        :param point: the position in dict you want to move to
        :param symbol: X or O
        """
        self.__service.move(point, symbol)
        self.add_move(point, symbol)

    def mill(self, point, player: Player):
        """
        :param point: the position in dict you want to move to
        :param player: a player object, for which we check if a mill was formed
        :return: True/False, tuple for the adjacent pieces where's a mill, player.symbol()
        """
        return self.__game_service.milled_formed(point, player)

    def strategy(self, last_move):
        """
        :param last_move: the last placed piece of the opponent
        :return: the best place for me to place a piece based on the current state of the board
        """
        return self.__game_service.strategy(self.computer, self.human, last_move)

    # def computer_move(self):
    #     return self.__game_service.computer_move()

    def board_display(self):
        self.__board.display()

    def best_remove(self):
        """
        :return: the best piece of the opponent to be removed
        :raises: GameError if there was a ServiceError while trying to remove a piece
        """
        try:
            return self.__game_service.choose_best_to_remove(self.human)
        except ServiceError as e:
            raise GameError(e)

    def remove(self, point, player: Player, opponent: Player):
        """
        :param point: piece on the board
        :param player: the player that has to make a move now
        :param opponent: the player that just made a move
        :raises: GameError if there was a ServiceError while trying to remove a piece
        """
        try:
            self.__game_service.remove_piece(point, player, opponent)
            if len(opponent.get_moves()) < 3:
                self.won = True
                self.winner = player.symbol()
            if opponent.symbol() == "X":
                self.human.remove_move(point)
                # print(self.human.get_moves())
            elif opponent.symbol() == "O":
                self.computer.remove_move(point)
                # print(self.computer.get_moves())
        except ServiceError as e:
            raise GameError(e)

    def slide(self, player: Player, from_here, to_here):
        """
        :param player: the player that has to make a move now
        :param from_here: from where you want to take the piece
        :param to_here: where you want to place it
        :raises: GameError if there was a ServiceError while trying to move the piece
        """
        try:
            self.__game_service.slide(player, from_here, to_here)
        except ServiceError as e:
            raise GameError(e)

    def blocked(self, player: Player):
        """
        :param player: self.human or self.computer
        :return: True if the game is over, False otherwise
        """
        return self.__game_service.blocked(player)

    def slide_strategy(self):
        """
        :return: the best (from here, to here) move for the computer
        """
        return self.__game_service.slide_strategy(self.computer)

    def fly(self, player: Player, from_here, to_here):
        """
        :param player: the player that has to make a move now
        :param from_here: from where you want to take the piece
        :param to_here: where you want to place it
        :raises: GameError if there was a ServiceError while trying to move the piece
        """
        try:
            self.__game_service.fly(player, from_here, to_here)
        except ServiceError as e:
            raise GameError(e)

    def fly_strategy(self):
        """
        :return: the best (from here, to here) move for the computer
        """
        return self.__game_service.fly_strategy(self.computer, self.human)
