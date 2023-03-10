import unittest
from marsrover import main
from unittest.mock import patch, call

from execute_commands import Orientation, RobotPosition


class TestMarsRover(unittest.TestCase):
    @patch("builtins.print")
    def test_main_should_print_results(self, mock_print):
        request = {
            "position_and_commands": [
                (RobotPosition(2, 3, Orientation.NORTH), "FLLFR"),
                (RobotPosition(1, 0, Orientation.SOUTH), "FFRLF"),
            ],
            "grid_size": (4, 8),
        }

        main(request)

        expected_calls = [call("(2, 3, W) "), call("(1, 0, S) LOST")]
        mock_print.assert_has_calls(expected_calls)
