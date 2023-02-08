import unittest

from movements import move, Orientations, make_movements


class TestMovements(unittest.TestCase):
    # Test single movement
    def test_move_east(self):
        next_state = move((0, 0, Orientations.E), "F")
        self.assertEqual((1, 0, Orientations.E), next_state)

    def test_move_north(self):
        next_state = move((0, 0, Orientations.N), "F")
        self.assertEqual((0, 1, Orientations.N), next_state)

    def test_move_south(self):
        next_state = move((0, 0, Orientations.S), "F")
        self.assertEqual((0, -1, Orientations.S), next_state)

    def test_move_west(self):
        next_state = move((0, 0, Orientations.W), "F")
        self.assertEqual((-1, 0, Orientations.W), next_state)

    def test_turn_right_from_north(self):
        next_state = move((0, 0, Orientations.N), "R")
        self.assertEqual((0, 0, Orientations.E), next_state)

    def test_turn_left_from_north(self):
        next_state = move((0, 0, Orientations.N), "L")
        self.assertEqual((0, 0, Orientations.W), next_state)

    def test_turn_right_from_east(self):
        next_state = move((0, 0, Orientations.E), "R")
        self.assertEqual((0, 0, Orientations.S), next_state)

    def test_turn_left_from_east(self):
        next_state = move((0, 0, Orientations.E), "L")
        self.assertEqual((0, 0, Orientations.N), next_state)

    # Test multiple movements
    def test_make_movements_east(self):
        state, status = make_movements((0, 0, Orientations.E), "FFF", (10, 10))
        self.assertEqual((3, 0, Orientations.E), state)
        self.assertEqual("", status)

    def test_move_outside_grid(self):
        state, status = make_movements((0, 0, Orientations.E), "FFF", (1, 1))
        self.assertEqual((1, 0, Orientations.E), state)
        self.assertEqual("LOST", status)

    def test_move_inside_grid_two(self):
        state, status = make_movements((2, 3, Orientations.N), "FLLFR", (4, 8))
        self.assertEqual((2, 3, Orientations.W), state)
        self.assertEqual("", status)

    def test_move_outside_grid_two(self):
        state, status = make_movements((1, 0, Orientations.S), "FFRLF", (4, 8))
        self.assertEqual((1, 0, Orientations.S), state)
        self.assertEqual("LOST", status)
