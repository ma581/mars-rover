import unittest

from movements import (
    RobotPosition,
    _single_movement,
    Orientation,
    make_movements,
)


class TestMovements(unittest.TestCase):
    # Test single movement
    single_movement_test_cases = [
        {
            "initial_state": RobotPosition(0, 0, Orientation.EAST),
            "command": "F",
            "expected_state": RobotPosition(1, 0, Orientation.EAST),
        },
        {
            "initial_state": RobotPosition(0, 0, Orientation.NORTH),
            "command": "F",
            "expected_state": RobotPosition(0, 1, Orientation.NORTH),
        },
        {
            "initial_state": RobotPosition(0, 0, Orientation.SOUTH),
            "command": "F",
            "expected_state": RobotPosition(0, -1, Orientation.SOUTH),
        },
        {
            "initial_state": RobotPosition(0, 0, Orientation.WEST),
            "command": "F",
            "expected_state": RobotPosition(-1, 0, Orientation.WEST),
        },
        {
            "initial_state": RobotPosition(0, 0, Orientation.NORTH),
            "command": "R",
            "expected_state": RobotPosition(0, 0, Orientation.EAST),
        },
        {
            "initial_state": RobotPosition(0, 0, Orientation.NORTH),
            "command": "L",
            "expected_state": RobotPosition(0, 0, Orientation.WEST),
        },
        {
            "initial_state": RobotPosition(0, 0, Orientation.EAST),
            "command": "R",
            "expected_state": RobotPosition(0, 0, Orientation.SOUTH),
        },
        {
            "initial_state": RobotPosition(0, 0, Orientation.EAST),
            "command": "L",
            "expected_state": RobotPosition(0, 0, Orientation.NORTH),
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
            "initial_state": RobotPosition(0, 0, Orientation.EAST),
            "commands": "FFF",
            "grid_size": (10, 10),
            "expected_state": RobotPosition(3, 0, Orientation.EAST),
            "expected_status": "",
        },
        {
            "initial_state": RobotPosition(0, 0, Orientation.EAST),
            "commands": "FXXXXFF",
            "grid_size": (10, 10),
            "expected_state": RobotPosition(3, 0, Orientation.EAST),
            "expected_status": "",
        },
        {
            "initial_state": RobotPosition(0, 0, Orientation.EAST),
            "commands": "FFF",
            "grid_size": (1, 1),
            "expected_state": RobotPosition(1, 0, Orientation.EAST),
            "expected_status": "LOST",
        },
        {
            "initial_state": RobotPosition(2, 3, Orientation.NORTH),
            "commands": "FLLFR",
            "grid_size": (4, 8),
            "expected_state": RobotPosition(2, 3, Orientation.WEST),
            "expected_status": "",
        },
        {
            "initial_state": RobotPosition(1, 0, Orientation.SOUTH),
            "commands": "FFRLF",
            "grid_size": (4, 8),
            "expected_state": RobotPosition(1, 0, Orientation.SOUTH),
            "expected_status": "LOST",
        },
        {
            "initial_state": RobotPosition(
                100,
                100,
                Orientation.SOUTH,
            ),  # Initial position is outside the grid!
            "commands": "F",
            "grid_size": (1, 1),
            "expected_state": RobotPosition(
                100,
                100,
                Orientation.SOUTH,
            ),  # Return initial position
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
