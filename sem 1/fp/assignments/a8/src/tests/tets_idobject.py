from unittest import TestCase
from src.domain.idobject import IdObject


class TestId(TestCase):
    def test_id(self):
        with self.assertRaises(TypeError):
            _id = IdObject("yes")
