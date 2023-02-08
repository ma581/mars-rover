import unittest

from marsrover import get_state_and_movements


class TestParseArgs(unittest.TestCase):
    def test_get_state_and_movements(self):
        args = "(0, 2, E) LRF"
        actual = get_state_and_movements(args)
        self.assertEqual(0, actual["x"])
        self.assertEqual(2, actual["y"])
        self.assertEqual("E", actual["orientation"])
        self.assertEqual("LRF", actual["movements"])

    def test_get_state_and_movements_extracts_valid_movements(self):
        args = "(0, 2, E) FXXXF"
        actual = get_state_and_movements(args)
        self.assertEqual("F", actual["movements"])

    def test_get_state_and_movements_for_invalid_input(self):
        args = "ABC"
        actual = get_state_and_movements(args)
        self.assertIsNone(actual)
