import argparse
import re


def get_state_and_movements(s: str) -> dict:
    """
    Parses a string like '(2, 3, E) LFRFF' into a dict with the initial state of the robot
    and the movement commands for the robot
    """
    pattern = "([0-9]*)\, ([0-9]*)\, ([NSEW])\) ([LRF]+)"
    m = re.search(pattern, s)
    try:
        return {
            "x": int(m.group(1)),
            "y": int(m.group(2)),
            "orientation": m.group(3),
            "movements": m.group(4),
        }
    except Exception:
        print(f"Invalid input {s} as it did not match regex:{pattern}")
        return None


def parse_inputs():
    parser = argparse.ArgumentParser(
        prog="MarsRover",
        description="Move robots on Mars",
    )

    parser.add_argument("x_size", type=int, help="width of the grid")
    parser.add_argument("y_size", type=int, help="height of the grid")
    parser.add_argument(
        "states_and_movements",
        type=str,
        nargs="+",
        help="Initial state, orientation and movement commands",
    )

    args = parser.parse_args()
    return {
        "x_size": args.x_size,
        "y_size": args.y_size,
        "states_and_movements": [
            get_state_and_movements(s) for s in args.states_and_movements
        ],
    }


def main():
    request = parse_inputs()
    print(request)


if __name__ == "__main__":
    main()
