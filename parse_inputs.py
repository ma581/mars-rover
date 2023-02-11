import argparse
import re
from typing import List, Tuple
from execute_commands import Orientation, RobotPosition, Command


def _get_position_and_commands(s: str) -> Tuple[RobotPosition, List[Command]]:
    """
    Parses a string like '(2, 3, E) LFRFF' into the initial position of the robot
    and the commands for the robot
    """
    pattern = "\(([0-9]*)\, ([0-9]*)\, ([NSEW])\) ([LRF]+)"
    m = re.search(pattern, s)
    try:
        return (
            RobotPosition(
                int(m.group(1)),
                int(m.group(2)),
                Orientation(m.group(3)),
            ),
            m.group(4),
        )
    except Exception as e:
        print(f"Invalid input '{s}' as it did not match regex:{pattern}. {e}")
        return None, None


def parse_inputs() -> dict:
    """
    Parses CLI inputs and returns a dict
    """
    parser = argparse.ArgumentParser(
        prog="MarsRover",
        description="Move robots on Mars",
    )

    parser.add_argument("x_size", type=int, help="width of the grid")
    parser.add_argument("y_size", type=int, help="height of the grid")
    parser.add_argument(
        "position_and_commands",
        type=str,
        nargs="+",
        help="Initial state, orientation and movement commands",
    )

    args = parser.parse_args()
    if args.x_size < 0 or args.y_size < 0:
        raise ValueError(f"'{(args.x_size, args.y_size)} is less than 0")

    return {
        "grid_size": (args.x_size, args.y_size),
        "position_and_commands": [
            _get_position_and_commands(p) for p in args.position_and_commands
        ],
    }
