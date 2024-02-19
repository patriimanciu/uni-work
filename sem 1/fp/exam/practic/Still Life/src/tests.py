from unittest import TestCase
from src.board import Board, BoardError
from src.game import Game, GameError


class TestLive(TestCase):
    def setUp(self):
        self.board = Board()
        self.game = Game(self.board)

    def test_place(self):
        # test load pattern
        self.game.load_patterns('blinker')
        self.assertEqual(self.game.get_pattern(), [[0, 0, 0], [1, 1, 1], [0, 0, 0]])
        self.board.place(self.game.get_pattern(), 1, 1)
        self.assertEqual(self.board.get_board(), [[0, 0, 0, 0, 0, 0, 0, 0],
                                                  [1, 1, 1, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0]])
        try:
            self.board.place(self.game.get_pattern(), 1, 1)
        except BoardError as e:
            assert str(e) == "You cannot overlap a live cell."

        try:
            self.board.place(self.game.get_pattern(), 8, 8)
        except BoardError as e:
            assert str(e) == "Live cell outside of board."

        try:
            self.game.place(['smmt', '4,4'])
        except GameError as e:
            assert str(e) == "Pattern doesn't exist."

        try:
            self.game.place(['blinker', '1'])
        except GameError as e:
            assert str(e) == "Not enough coord"

        try:
            self.game.place(['blinker', '1,a'])
        except GameError as e:
            assert str(e) == "Coord. should be integers"


    def test_tick(self):
        self.game.load_patterns('spaceship')
        self.board.place(self.game.get_pattern(), 1, 1)
        self.game.tick()
        self.assertEqual(self.board.get_board(), [[0, 0, 0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 0, 0, 0, 0, 0],
                                                  [0, 1, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(self.game.get_neighbours(2, 2, self.board.get_board()),  3)
