import argparse
import unittest
from unittest import mock
from parse_inputs import _get_position_and_commands, parse_inputs
from execute_commands import Orientation, RobotPosition


class TestParseArgs(unittest.TestCase):
    def test_get_pos_and_cmds(self):
        args = "(0, 2, E) LRF"
        pos, cmds = _get_position_and_commands(args)
        self.assertEqual(RobotPosition(0, 2, Orientation.EAST), pos)
        self.assertEqual("LRF", cmds)

    def test_get_pos_and_cmds_extracts_valid_movements(self):
        args = "(0, 2, E) FXXXF"
        _, cmds = _get_position_and_commands(args)
        self.assertEqual("F", cmds)

    def test_get_pos_and_cmds_for_invalid_input(self):
        invalid_inputs = ["ABC", "0, 2, E) LRF"]
        for arg in invalid_inputs:
            pos, cmds = _get_position_and_commands(arg)
            self.assertIsNone(pos)
            self.assertIsNone(cmds)

    @mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(
            x_size=1,
            y_size=2,
            position_and_commands=["1 2 (0, 2, E) LRF"],
        ),
    )
    def test_parse_inputs(self, _):
        actual = parse_inputs()
        self.assertEquals((1, 2), actual["grid_size"])
        self.assertEquals(
            RobotPosition(0, 2, Orientation.EAST), actual["position_and_commands"][0][0]
        )
        self.assertEquals("LRF", actual["position_and_commands"][0][1])
