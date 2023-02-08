import argparse
import re

from movements import Orientations, make_movements


def get_state_and_commands(s: str) -> dict:
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
            get_state_and_commands(s) for s in args.states_and_commands
        ],
    }


def main():
    request = parse_inputs()

    for state_and_cmds in request["states_and_commands"]:
        if state_and_cmds is not None:
            state = state_and_cmds["state"]
            cmds = state_and_cmds["commands"]
            grid_size = request["grid_size"]
            (final_x, final_y, final_o), status = make_movements(state, cmds, grid_size)
            print(f"({final_x}, {final_y}, {final_o}) {status}")


if __name__ == "__main__":
    main()
