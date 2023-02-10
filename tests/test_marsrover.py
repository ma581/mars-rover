import unittest
from marsrover import main
from unittest.mock import patch, call

from movements import Orientation, RobotPosition


class TestMarsRover(unittest.TestCase):
    @patch("builtins.print")
    def test_main_should_print_results(self, mock_print):
        request = {
            "states_and_commands": [
                {
                    "position": RobotPosition(2, 3, Orientation.NORTH),
                    "commands": "FLLFR",
                },
                {
                    "position": RobotPosition(1, 0, Orientation.SOUTH),
                    "commands": "FFRLF",
                },
            ],
            "grid_size": (4, 8),
        }

        main(request)

        expected_calls = [call("(2, 3, W) "), call("(1, 0, S) LOST")]
        mock_print.assert_has_calls(expected_calls)
