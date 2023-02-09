import argparse
import re
from movements import Orientations


def _get_state_and_commands(s: str) -> dict:
    """
    Parses a string like '(2, 3, E) LFRFF' into a dict with the initial state of the robot
    and the movement commands for the robot
    """
    pattern = "([0-9]*)\, ([0-9]*)\, ([NSEW])\) ([LRF]+)"
    m = re.search(pattern, s)
    try:
        return {
            "state": (
                int(m.group(1)),  # x
                int(m.group(2)),  # y
                Orientations[m.group(3)],
            ),
            "commands": m.group(4),
        }
    except Exception:
        print(f"Invalid input '{s}' as it did not match regex:{pattern}")
        return None


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
        "states_and_commands",
        type=str,
        nargs="+",
        help="Initial state, orientation and movement commands",
    )

    args = parser.parse_args()
    return {
        "grid_size": (args.x_size, args.y_size),
        "states_and_commands": [
            _get_state_and_commands(s) for s in args.states_and_commands
        ],
    }
