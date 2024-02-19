from unittest import TestCase

from domain.board import Board, BoardError
from service.board import BoardService


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board()
        self.service = BoardService(self.board)

    def test_get_board(self):
        self.assertEqual(self.board.get_board(), {
            'A1': ' ', 'A4': ' ', 'A7': ' ',
            'B2': ' ', 'B4': ' ', 'B6': ' ',
            'C3': ' ', 'C4': ' ', 'C5': ' ',
            'D1': ' ', 'D2': ' ', 'D3': ' ', 'D5': ' ', 'D6': ' ', 'D7': ' ',
            'E3': ' ', 'E4': ' ', 'E5': ' ',
            'F2': ' ', 'F4': ' ', 'F6': ' ',
            'G1': ' ', 'G4': ' ', 'G7': ' '
        })

    def test_set_space(self):
        self.board.set_space('A1', "X")
        self.board.set_space('G7', "O")
        self.assertEqual(self.board.get_point('A1'), "X")
        self.assertNotEqual(self.board.get_point('A1'), "O")
        self.assertEqual(self.board.get_point('G7'), "O")
        self.assertEqual(self.board.get_point('A4'), ' ')
        point = 'A2'
        with self.assertRaises(BoardError) as context:
            self.board.get_point(point)
        self.assertEqual(str(context.exception), f"Key {point} not found!")

    def test_service(self):
        self.assertTrue(self.service.is_valid_point('A1'))
        self.assertFalse(self.service.is_valid_point('A2'))
        self.assertTrue(self.service.is_empty('A1'))
        self.board.set_space('A1', "X")
        self.assertFalse(self.service.is_empty('A1'))

    def test_move(self):
        self.service.move('A1', "X")
        self.assertEqual(self.board.get_point('A1'), "X")
        point = 'A2'
        with self.assertRaises(BoardError) as context:
            self.service.move(point, "X")
        self.assertEqual(str(context.exception), "The point is not valid.")
        with self.assertRaises(BoardError) as context:
            self.service.move('A1', "O")
        self.assertEqual(str(context.exception), "The chosen point is not empty.")

