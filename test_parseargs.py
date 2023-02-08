import unittest

from marsrover import get_state_and_commands
from movements import Orientations


class TestParseArgs(unittest.TestCase):
    def test_get_state_and_movements(self):
        args = "(0, 2, E) LRF"
        actual = get_state_and_commands(args)
        self.assertEqual((0, 2, Orientations.E), actual["state"])
        self.assertEqual("LRF", actual["commands"])

    def test_get_state_and_movements_extracts_valid_movements(self):
        args = "(0, 2, E) FXXXF"
        actual = get_state_and_commands(args)
        self.assertEqual("F", actual["commands"])

    def test_get_state_and_movements_for_invalid_input(self):
        args = "ABC"
        actual = get_state_and_commands(args)
        self.assertIsNone(actual)
