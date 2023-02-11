import unittest

from execute_commands import (
    RobotPosition,
    _execute_one_command,
    Orientation,
    execute_commands,
)


class TestExecuteCommands(unittest.TestCase):
    single_command_test_cases = [
        {
            "initial_position": RobotPosition(0, 0, Orientation.EAST),
            "command": "F",
            "expected_position": RobotPosition(1, 0, Orientation.EAST),
        },
        {
            "initial_position": RobotPosition(0, 0, Orientation.NORTH),
            "command": "F",
            "expected_position": RobotPosition(0, 1, Orientation.NORTH),
        },
        {
            "initial_position": RobotPosition(0, 0, Orientation.SOUTH),
            "command": "F",
            "expected_position": RobotPosition(0, -1, Orientation.SOUTH),
        },
        {
            "initial_position": RobotPosition(0, 0, Orientation.WEST),
            "command": "F",
            "expected_position": RobotPosition(-1, 0, Orientation.WEST),
        },
        {
            "initial_position": RobotPosition(0, 0, Orientation.NORTH),
            "command": "R",
            "expected_position": RobotPosition(0, 0, Orientation.EAST),
        },
        {
            "initial_position": RobotPosition(0, 0, Orientation.NORTH),
            "command": "L",
            "expected_position": RobotPosition(0, 0, Orientation.WEST),
        },
        {
            "initial_position": RobotPosition(0, 0, Orientation.EAST),
            "command": "R",
            "expected_position": RobotPosition(0, 0, Orientation.SOUTH),
        },
        {
            "initial_position": RobotPosition(0, 0, Orientation.EAST),
            "command": "L",
            "expected_position": RobotPosition(0, 0, Orientation.NORTH),
        },
    ]

    def test_execute_one_command(self):
        for case in self.single_command_test_cases:
            with self.subTest(msg=f'{case["initial_position"]}, {case["command"]}'):
                next_position = _execute_one_command(
                    case["initial_position"], case["command"]
                )
                self.assertEqual(case["expected_position"], next_position)

    multiple_commands_test_cases = [
        {
            "initial_position": RobotPosition(0, 0, Orientation.EAST),
            "commands": "FFF",
            "grid_size": (10, 10),
            "expected_position": RobotPosition(3, 0, Orientation.EAST),
            "expected_status": "",
        },
        {
            "initial_position": RobotPosition(0, 0, Orientation.EAST),
            "commands": "FXXXXFF",
            "grid_size": (10, 10),
            "expected_position": RobotPosition(3, 0, Orientation.EAST),
            "expected_status": "",
        },
        {
            "initial_position": RobotPosition(0, 0, Orientation.EAST),
            "commands": "FFF",
            "grid_size": (1, 1),
            "expected_position": RobotPosition(1, 0, Orientation.EAST),
            "expected_status": "LOST",
        },
        {
            "initial_position": RobotPosition(2, 3, Orientation.NORTH),
            "commands": "FLLFR",
            "grid_size": (4, 8),
            "expected_position": RobotPosition(2, 3, Orientation.WEST),
            "expected_status": "",
        },
        {
            "initial_position": RobotPosition(1, 0, Orientation.SOUTH),
            "commands": "FFRLF",
            "grid_size": (4, 8),
            "expected_position": RobotPosition(1, 0, Orientation.SOUTH),
            "expected_status": "LOST",
        },
        {
            "initial_position": RobotPosition(
                0,
                2,
                Orientation.SOUTH,
            ),  # Initial position is outside the grid!
            "commands": "F",
            "grid_size": (1, 1), # Move inside grid
            "expected_position": RobotPosition(
                0,
                2,
                Orientation.SOUTH,
            ),  # Return initial position
            "expected_status": "LOST",
        },
    ]

    def test_execute_commands(self):
        for case in self.multiple_commands_test_cases:
            with self.subTest(
                msg=f'{case["initial_position"]}, {case["commands"]}, {case["grid_size"]}'
            ):
                next_position, status = execute_commands(
                    case["initial_position"], case["commands"], case["grid_size"]
                )
                self.assertEqual(case["expected_position"], next_position)
                self.assertEqual(case["expected_status"], status)
