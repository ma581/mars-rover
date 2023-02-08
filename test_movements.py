import unittest

from movements import _single_movement, Orientations, Commands, make_movements


class TestMovements(unittest.TestCase):
    # Test single movement
    single_movement_test_cases = [
        {
            "initial_state": (0, 0, Orientations.E),
            "command": "F",
            "expected_state": (1, 0, Orientations.E),
        },
        {
            "initial_state": (0, 0, Orientations.N),
            "command": "F",
            "expected_state": (0, 1, Orientations.N),
        },
        {
            "initial_state": (0, 0, Orientations.S),
            "command": "F",
            "expected_state": (0, -1, Orientations.S),
        },
        {
            "initial_state": (0, 0, Orientations.W),
            "command": "F",
            "expected_state": (-1, 0, Orientations.W),
        },
        {
            "initial_state": (0, 0, Orientations.N),
            "command": "R",
            "expected_state": (0, 0, Orientations.E),
        },
        {
            "initial_state": (0, 0, Orientations.N),
            "command": "L",
            "expected_state": (0, 0, Orientations.W),
        },
        {
            "initial_state": (0, 0, Orientations.E),
            "command": "R",
            "expected_state": (0, 0, Orientations.S),
        },
        {
            "initial_state": (0, 0, Orientations.E),
            "command": "L",
            "expected_state": (0, 0, Orientations.N),
        },
    ]

    def test_single_movement(self):
        for case in self.single_movement_test_cases:
            with self.subTest(msg=f'{case["initial_state"]}, {case["command"]}'):
                next_state = _single_movement(case["initial_state"], case["command"])
                self.assertEqual(case["expected_state"], next_state)

    # Test multiple movements
    multiple_movements_test_cases = [
        {
            "initial_state": (0, 0, Orientations.E),
            "commands": "FFF",
            "grid_size": (10, 10),
            "expected_state": (3, 0, Orientations.E),
            "expected_status": "",
        },
        {
            "initial_state": (0, 0, Orientations.E),
            "commands": "FFF",
            "grid_size": (1, 1),
            "expected_state": (1, 0, Orientations.E),
            "expected_status": "LOST",
        },
        {
            "initial_state": (2, 3, Orientations.N),
            "commands": "FLLFR",
            "grid_size": (4, 8),
            "expected_state": (2, 3, Orientations.W),
            "expected_status": "",
        },
        {
            "initial_state": (1, 0, Orientations.S),
            "commands": "FFRLF",
            "grid_size": (4, 8),
            "expected_state": (1, 0, Orientations.S),
            "expected_status": "LOST",
        },
        {
            "initial_state": (100, 100, Orientations.S), # Initial position is outside the grid!
            "commands": "F",
            "grid_size": (1, 1),
            "expected_state": (0, 0, Orientations.N),    # Return a valid default at (0,0) North
            "expected_status": "LOST",
        },
    ]

    def test_multiple_movements(self):
        for case in self.multiple_movements_test_cases:
            with self.subTest(
                msg=f'{case["initial_state"]}, {case["commands"]}, {case["grid_size"]}'
            ):
                next_state, status = make_movements(
                    case["initial_state"], case["commands"], case["grid_size"]
                )
                self.assertEqual(case["expected_state"], next_state)
                self.assertEqual(case["expected_status"], status)
