from unittest import TestCase

from domain.game import Game, GameError
from service.game import ServiceError


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def test_add_move(self):
        self.game.add_move('A1')
        self.assertEqual(list(self.game.computer.get_moves().keys()), ['A1'])
        self.game.add_move('A4', "X")
        self.assertEqual(list(self.game.human.get_moves().keys()), ['A4'])

    def test_move(self):
        self.game.move('B2')
        self.assertEqual(list(self.game.computer.get_moves().keys()), ['B2'])

    def test_mill_and_strategy_and_remove(self):
        self.game.move('A1', "X")
        self.assertTrue(self.game.mill('A7', self.game.human))
        self.game.move('A4', "X")
        formed, where, player = self.game.mill('A7', self.game.human)
        self.assertTrue(formed)
        self.assertEqual(where, ("A1", "A4"))
        self.assertEqual(player, "X")
        self.game.move('A7', "X")
        self.assertTrue(self.game.mill('A1', self.game.human))
        self.game.move('D1')
        self.game.move('G1')
        self.game.strategy('A7')
        self.assertEqual(self.game.best_remove(), 'A1')

    def test_successful_remove(self):
        self.game.move('A1', "X")
        self.game.move('B2', "X")
        self.game.remove("A1", self.game.computer, self.game.human)
        self.assertEqual(list(self.game.human.get_moves().keys()), ["B2"])

        self.game.move('A4')
        self.game.remove('A4', self.game.human, self.game.computer)
        self.assertEqual(list(self.game.computer.get_moves().keys()), [])

    def test_failed_remove(self):
        self.game.move('A1', "X")
        self.game.remove("A1", self.game.computer, self.game.human)
        with self.assertRaises(GameError) as context:
            self.game.remove("A1", self.game.computer, self.game.human)
        self.assertEqual(str(context.exception), "That space is empty, remove something else.")

    def test_successful_slide(self):
        self.game.move('A1', "X")
        self.game.slide(self.game.human, "A1", "A4")
        self.assertEqual(list(self.game.human.get_moves().keys()), ['A4'])

    def test_failed_slide(self):
        self.game.move('A1', "X")
        with self.assertRaises(GameError) as context:
            self.game.slide(self.game.human, "A1", "B2")
        self.assertEqual(str(context.exception), "The place you want to slide into is not adjacent to your original piece. A1 B2")

    def test_successful_fly(self):
        self.game.move("A1", "O")
        self.game.fly(self.game.computer, "A1", "B2")
        self.assertEqual(list(self.game.computer.get_moves().keys()), ["B2"])

    def test_failed_fly(self):
        self.game.move("A1", "X")
        with self.assertRaises(GameError) as context:
            self.game.fly(self.game.computer, "A1", "B2")
        self.assertEqual(str(context.exception), "You can slide only your own pieces.")
        self.game.move("B2", "O")
        with self.assertRaises(GameError) as context:
            self.game.fly(self.game.human, "A1", "B2")
        self.assertEqual(str(context.exception), "You can only slide into an empty spot.")

    def test_blocked(self):
        pass
