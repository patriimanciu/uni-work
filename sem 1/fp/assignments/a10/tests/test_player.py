from unittest import TestCase

from domain.player import Player


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("X")

    def test_statics(self):
        self.assertEqual(self.player.get_adjacent('G7'), [("A7", "D7"), ("G1", "G4")])
        self.assertEqual(self.player.get_slide('G7'), ["D7", "G4"])

    def test_player(self):
        self.assertEqual(self.player.symbol(), "X")
        self.assertFalse(self.player.placed_all())
        self.player.dec_hand()
        self.assertEqual(self.player.get_hand(), 8)
        self.player.set_move('A1')
        self.assertEqual(len(self.player), 1)
        self.player.remove_move('A1')
        self.assertEqual(len(self.player.get_moves()), 0)
