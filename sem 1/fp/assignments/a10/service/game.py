from random import choice

from domain.board import Board, BoardError
from domain.player import Player
from service.board import BoardService


class ServiceError(Exception):
    pass


class GameService(BoardService):
    def __init__(self, board: Board):
        super().__init__(board)
        self.__board = board

    # def computer_move(self):
    #     board = self.__board.get_board()
    #     for b in board.keys():
    #         if self.is_empty(b):
    #             # self.move(b, "O")
    #             return b

    def milled_formed(self, point, player: Player):
        """
        :param point: the position in dict you want to move to
        :param player: a player object, for which we check if a mill was formed
        :return: True/False, tuple for the adjacent pieces where's a mill, player.symbol()
        """
        first, second = player.get_adjacent(point)
        if self.__board.get_point(first[0]) == self.__board.get_point(first[1]) == player.symbol():
            return True, first, player.symbol()
        elif self.__board.get_point(second[0]) == self.__board.get_point(second[1]) == player.symbol():
            return True, second, player.symbol()
        return False, (0, 0), player.symbol()

    def random_choice(self, board):
        """
        :param board: current state of the board
        :return: a random available move
        """
        comp_move = choice(list(board.keys()))
        while not self.is_empty(comp_move):
            comp_move = choice(list(board.keys()))
        return comp_move

    def strategy(self, player: Player, human: Player, last_move):
        """
        :param human: takes self.human as the opponent
        :param player: self.computer as my player
        :param last_move: the last placed piece of the opponent
        :return: the best place for me to place a piece based on the current state of the board
        """
        board = self.__board.get_board()
        moves = player.get_moves()
        human_move = human.get_moves()
        one, two = human_move[last_move]
        # first it tries to block the human moves
        if self.is_empty(one[0]) and self.__board.get_point(one[1]) == human.symbol():
            return one[0]
        elif self.is_empty(one[1]) and self.__board.get_point(one[0]) == human.symbol():
            return one[1]
        elif self.is_empty(two[0]) and self.__board.get_point(two[1]) == human.symbol():
            return two[0]
        elif self.is_empty(two[1]) and self.__board.get_point(two[0]) == human.symbol():
            return two[1]

        # then it tries to make a morris itself
        if len(moves) == 0:
            return self.random_choice(board)
        elif moves:
            # print(moves)
            for key, value in moves.items():
                first = value[0]
                second = value[1]
                if self.is_empty(first[0]) and self.__board.get_point(first[1]) == player.symbol():
                    return first[0]
                elif self.is_empty(first[1]) and self.__board.get_point(first[0]) == player.symbol():
                    return first[1]
                elif self.is_empty(second[0]) and self.__board.get_point(second[1]) == player.symbol():
                    return second[0]
                elif self.is_empty(second[1]) and self.__board.get_point(second[0]) == player.symbol():
                    return second[1]

            for key, value in moves.items():
                first = value[0]
                second = value[1]
                if self.is_empty(first[0]) and self.is_empty(first[1]):
                    return first[0]
                elif self.is_empty(second[0]) and self.is_empty(second[1]):
                    return second[0]
            return self.random_choice(board)

    def choose_best_to_remove(self, opponent: Player):
        """
        :return: the best piece of the opponent to be removed
        """
        # A piece in an opponent's mill, however, can be removed only if no other pieces are available.
        human = opponent.get_moves()
        # remove if the opponent is close to making a mill
        for h in human.values():
            one = h[0]
            two = h[1]
            if self.is_empty(one[0]) and self.__board.get_point(one[1]) == opponent.symbol():
                # self.remove_piece(one[1], player, opponent)
                if not self.milled_formed(one[1], opponent)[0]:
                    return one[1]
            elif self.is_empty(one[1]) and self.__board.get_point(one[0]) == opponent.symbol():
                # self.remove_piece(one[0], player, opponent)
                if not self.milled_formed(one[0], opponent)[0]:
                    return one[0]
            elif self.is_empty(two[0]) and self.__board.get_point(two[1]) == opponent.symbol():
                # self.remove_piece(two[1], player, opponent)
                if not self.milled_formed(two[1], opponent)[0]:
                    return two[1]
            elif self.is_empty(two[1]) and self.__board.get_point(two[0]) == opponent.symbol():
                # self.remove_piece(two[0], player, opponent)
                if not self.milled_formed(two[0], opponent)[0]:
                    return two[0]

        for key, val in human.items():
            one = val[0]
            two = val[1]
            if self.__board.get_point(one[1]) == "O" and self.__board.get_point(one[0]) == "O":
                if not self.milled_formed(one[1], opponent)[0]:
                    return key
            elif self.__board.get_point(two[1]) == "O" and self.__board.get_point(two[0]) == "O":
                if not self.milled_formed(one[1], opponent)[0]:
                    return key

        # remove pieces that are alone and not part of mills
        hum = list(human.keys())
        for h in hum:
            mill, _, _ = self.milled_formed(h, opponent)
            if not mill:
                return h

        # remove from mill random
        return choice(hum)

    def slide(self, player: Player, from_here, to_here):
        """
        :param player: the player that has to make a move now
        :param from_here: from where you want to take the piece
        :param to_here: where you want to place it
        :raises: ServiceError if there was a BoardError while trying to move the piece
        """
        try:
            if from_here not in self.__board.get_board().keys() or to_here not in self.__board.get_board().keys():
                raise ServiceError("The places chosen are invalid")
            if self.__board.get_point(from_here) != player.symbol():
                raise ServiceError("You can slide only your own pieces.")
            if to_here not in player.get_slide(from_here):
                raise ServiceError(f"The place you want to slide into is not adjacent to your original piece. {from_here} {to_here}")
            if self.__board.get_point(to_here) != " ":
                raise ServiceError("You can only slide into an empty spot.")
            player.remove_move(from_here)
            # print(player.get_moves())
            player.set_move(to_here)
            # print(player.get_moves())
            self.__board.set_space(from_here, ' ')
            self.__board.set_space(to_here, player.symbol())
        except BoardError as e:
            raise ServiceError(e)

    def blocked(self, player: Player):
        """
        :param player: self.human or self.computer
        :return: True if the game is over, False otherwise
        """
        moves = player.get_moves()
        if len(player) < 3:
            return True
        elif len(player) >= 3:
            return False
        for move in moves.keys():
            slide = player.get_slide(move)
            for s in slide:
                if self.is_empty(s):
                    return False
        return True

    @staticmethod
    def remove_from_mill(opponent: Player):
        """
        :param opponent: a player object that is the opposite of the current player
        :return: True if there are pieces, not part of a mill, that can be removed, False it there's only mills on the board
        """
        # returns True/False depending on weather or not there are pieces that can be removed that are not mills
        moves = list(opponent.get_moves().keys())
        original_moves = list(opponent.get_moves().keys())
        for move in moves:
            m = opponent.get_adjacent(move)
            first = m[0]
            second = m[1]
            if first[0] in original_moves and first[1] in original_moves:
                if first[0] in moves:
                    moves.remove(first[0])
                if first[1] in moves:
                    moves.remove(first[1])
                moves.remove(move)
            elif second[0] in original_moves and second[1] in original_moves:
                if second[0] in moves:
                    moves.remove(second[0])
                # check if is in list BUT GO BACK CA NU MAI MERGE
                if second[1] in moves:
                    moves.remove(second[1])
                moves.remove(move)
        if len(moves) == 0:
            return False
        return True

    def remove_piece(self, point, player: Player, opponent: Player):
        """
        :param point: piece on the board
        :param player: the player that has to make a move now
        :param opponent: the player that just made a move
        :raises: ServiceError if the piece we want removed is not valid, if the player's own piece, etc
        """
        if point not in self.__board.get_board().keys():
            raise ServiceError("The piece you're trying to remove is invalid.")
        if self.__board.get_point(point) == player.symbol():
            raise ServiceError(f"Your are trying to remove your own piece {point}. Remove one of the opponent's.")
        if self.__board.get_point(point) == ' ':
            raise ServiceError("That space is empty, remove something else.")
        if self.__board.get_point(point) == opponent.symbol():
            move = opponent.get_adjacent(point)
            first = move[0]
            second = move[1]
            if self.remove_from_mill(opponent):
                if self.__board.get_point(first[0]) == opponent.symbol() and self.__board.get_point(
                        first[1]) == opponent.symbol():
                    raise ServiceError(f"That is part of a mill {first}, you cannot remove from it.")
                if self.__board.get_point(second[0]) == opponent.symbol() and self.__board.get_point(
                        second[1]) == opponent.symbol():
                    raise ServiceError(f"That is part of a mill {first}, you cannot remove from it.")
                self.__board.set_space(point, ' ')
            else:
                self.__board.set_space(point, ' ')

    def slide_strategy(self, player: Player):
        """
        :param player: the one tha has to make a move
        :return: (from, to) in the best format
        """
        # returns (from, to)
        moves = player.get_moves()
        for key, value in moves.items():
            first = value[0]
            second = value[1]
            # if it needs one more move to form a mill and that is available, it makes it
            if self.is_empty(first[0]) and self.__board.get_point(first[1]) == player.symbol():
                slides = player.get_slide(first[0])
                for s in slides:
                    if self.__board.get_point(s) == player.symbol() and (s != first[1] and s != key):
                        return s, first[0]
            elif self.is_empty(first[1]) and self.__board.get_point(first[0]) == player.symbol():
                slides = player.get_slide(first[1])
                for s in slides:
                    if self.__board.get_point(s) == player.symbol() and (s != first[0] and s != key):
                        return s, first[1]
            elif self.is_empty(second[0]) and self.__board.get_point(second[1]) == player.symbol():
                slides = player.get_slide(second[0])
                for s in slides:
                    if self.__board.get_point(s) == player.symbol() and (s != second[1] and s != key):
                        return s, second[0]
            elif self.is_empty(second[1]) and self.__board.get_point(second[0]) == player.symbol():
                slides = player.get_slide(second[1])
                for s in slides:
                    if self.__board.get_point(s) == player.symbol() and (s != second[0] and s != key):
                        return s, second[1]

        for key, value in moves.items():
            first = value[0]
            second = value[1]
            # there needs to be 2 on one row, slide one and the new empty space has to have another one of the player's
            # pieces adjacent
            if self.is_empty(first[0]) and self.__board.get_point(first[1]) == player.symbol() and first[1] in player.get_slide(first[0]):
                slides = player.get_slide(first[1])
                for s in slides:
                    # if there exists a possibility for a future mill
                    if self.__board.get_point(s) == player.symbol() and (s != first[0] and s != key):
                        return first[1], first[0]
            elif self.is_empty(first[1]) and self.__board.get_point(first[0]) == player.symbol() and first[0] in player.get_slide(first[1]):
                slides = player.get_slide(first[0])
                for s in slides:
                    if self.__board.get_point(s) == player.symbol() and (s != first[1] and s != key):
                        return first[0], first[1]
            elif self.is_empty(second[0]) and self.__board.get_point(second[1]) == player.symbol() and second[1] in player.get_slide(second[0]):
                slides = player.get_slide(second[1])
                for s in slides:
                    if self.__board.get_point(s) == player.symbol() and (s != second[0] and s != key):
                        return second[1], second[0]
            elif self.is_empty(second[1]) and self.__board.get_point(second[0]) == player.symbol() and second[0] in player.get_slide(second[1]):
                slides = player.get_slide(second[0])
                for s in slides:
                    if self.__board.get_point(s) == player.symbol() and (s != second[1] and s != key):
                        return second[0], second[1]

        # break and then remake a morris
        for key, value in moves.items():
            formed, here, _ = self.milled_formed(key, player)
            if formed:
                slide, where = self.can_slide(here[0], player)
                if slide:
                    return here[0], where

                slide, where = self.can_slide(here[1], player)
                if slide:
                    return here[1], where

                slide, where = self.can_slide(key, player)
                if slide:
                    return key, where

        for key, value in moves.items():
            slides = player.get_slide(key)
            for s in slides:
                if self.is_empty(s):
                    return key, s

    def can_slide(self, point, player: Player):
        """
        :param point: a place from where you want to slide
        :param player: the player that has to make the current move
        :return: True/False, the space where it can slide
        """
        slide = player.get_slide(point)
        for s in slide:
            if self.__board.get_point(s) == ' ':
                return True, s
        return False, ' '

    def fly(self, player: Player, from_here, to_here):
        """
        :param player: the player that has to make a move now
        :param from_here: from where you want to take the piece
        :param to_here: where you want to place it
        :raises: GameError if there was a ServiceError while trying to move the piece
        """
        # same as slide, except you're allowed to move to places that are not adjacent
        if from_here not in self.__board.get_board().keys() or to_here not in self.__board.get_board().keys():
            raise ServiceError("The places chosen are invalid")
        if self.__board.get_point(from_here) != player.symbol():
            raise ServiceError("You can slide only your own pieces.")
        if self.__board.get_point(to_here) != " ":
            raise ServiceError("You can only slide into an empty spot.")
        player.remove_move(from_here)
        player.set_move(to_here)
        self.__board.set_space(from_here, ' ')
        self.__board.set_space(to_here, player.symbol())

    def fly_strategy(self, player: Player, opponent: Player):
        """
        :return: the best (from here, to here) move for the computer in the current state
        """
        # the goal is to form mills, returns (from, to)
        moves = player.get_moves()

        # if there are already 2 pieces in a row/col it moves the 3rd there, to form a mill
        for key, value in moves.items():
            first = value[0]
            second = value[1]
            if self.is_empty(first[0]) and self.__board.get_point(first[1]) == player.symbol():
                for k in moves.keys():
                    if k != key and k != first[1]:
                        return k, first[0]
            elif self.is_empty(first[1]) and self.__board.get_point(first[0]) == player.symbol():
                for k in moves.keys():
                    if k != key and k != first[0]:
                        return k, first[1]

            elif self.is_empty(second[0]) and self.__board.get_point(second[1]) == player.symbol():
                for k in moves.keys():
                    if k != key and k != second[1]:
                        return k, second[0]
            elif self.is_empty(second[1]) and self.__board.get_point(second[0]) == player.symbol():
                for k in moves.keys():
                    if k != key and k != second[0]:
                        return k, second[1]

        human = opponent.get_moves()
        for key, value in human.items():
            from_here = choice(list(moves.keys()))
            one = value[0]
            two = value[1]
            if self.is_empty(one[0]) and self.__board.get_point(one[1]) == opponent.symbol():
                return from_here, one[0]
            elif self.is_empty(one[1]) and self.__board.get_point(one[0]) == opponent.symbol():
                return from_here, one[1]
            elif self.is_empty(two[0]) and self.__board.get_point(two[1]) == opponent.symbol():
                return from_here, two[0]
            elif self.is_empty(two[1]) and self.__board.get_point(two[0]) == opponent.symbol():
                return from_here, two[1]

        # if all pieces are separated, it chooses one and places it next to another
        keys = list(moves.keys())
        for key, value in moves.items():
            first = value[0]
            second = value[1]
            if self.is_empty(first[0]) and self.is_empty(first[1]):
                mv = choice(keys)
                while mv == key:
                    mv = choice(keys)
                return mv, first[0]
            elif self.is_empty(second[0]) and self.is_empty(second[1]):
                mv = choice(keys)
                while mv == key:
                    mv = choice(keys)
                return mv, second[0]

        # if none of the pieces have an empty line/col to themselves, choose one piece to move to an empty line
        board = self.__board.get_board()
        for key, value in board:
            if self.is_empty(key):
                first = value[0]
                second = value[1]
                if self.is_empty(first[0]) and self.is_empty(first[1]):
                    mv = choice(keys)
                    while mv == key:
                        mv = choice(keys)
                    return mv, key
                elif self.is_empty(second[0]) and self.is_empty(second[1]):
                    mv = choice(keys)
                    while mv == key:
                        mv = choice(keys)
                    return mv, key
