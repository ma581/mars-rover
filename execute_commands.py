from typing import List, Tuple
from enum import Enum


class Orientation(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"  # Ordered clockwise

    def __str__(self):
        return str(self.value)


Command = Enum("Commands", ["F", "R", "L"])

# If you move Forward for each given orientation, this is your change in position
DELTA_BY_ORIENTATION = {
    Orientation.NORTH: (0, 1),
    Orientation.SOUTH: (0, -1),
    Orientation.EAST: (1, 0),
    Orientation.WEST: (-1, 0),
}


class RobotPosition:
    """
    X, Y coordinates and orientation of the robot
    """

    def __init__(self, x: int, y: int, orientation: Orientation) -> None:
        self.x = x
        self.y = y
        self.orientation = orientation

    def __eq__(self, other):
        return (
            isinstance(other, RobotPosition)
            and self.x == other.x
            and self.y == other.y
            and self.orientation == other.orientation
        )

    def __hash__(self):
        return hash(tuple(self.x, self.y, self.orientation))

    def __str__(self):
        return f"({self.x}, {self.y}, {self.orientation})"

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.orientation})"


def _execute_one_command(pos: RobotPosition, cmd: Command) -> RobotPosition:
    """Make a single movement or rotation"""
    x, y, orientation = pos.x, pos.y, pos.orientation
    if cmd == Command.F.name:
        delta = DELTA_BY_ORIENTATION[orientation]
        next_x, next_y = x + delta[0], y + delta[1]
        return RobotPosition(next_x, next_y, orientation)
    elif cmd in (Command.R.name, Command.L.name):
        return RobotPosition(x, y, _rotate(orientation, cmd))
    else:
        print(f"Invalid command {cmd} is not in {[c.name for c in Command]}")
        return pos


def _rotate(orientation: Orientation, cmd: Command) -> Orientation:
    clockwise_orientations = [o for o in Orientation]
    current_index = clockwise_orientations.index(orientation)
    if cmd == Command.R.name:
        next_index = (current_index + 1) % 4
    elif cmd == Command.L.name:
        next_index = (current_index - 1) % 4
    else:
        print(f"Invalid command {cmd} is not in {[o.name for o in Orientation]}")
        return orientation
    return clockwise_orientations[next_index]


def _is_outside_grid(pos: RobotPosition, grid_size: Tuple[int, int]) -> bool:
    (x, y) = pos.x, pos.y
    return x < 0 or x > grid_size[0] or y < 0 or y > grid_size[1]


def execute_commands(
    pos: RobotPosition,
    cmds: List[Command],
    grid_size: Tuple[int, int],
) -> Tuple[RobotPosition, str]:
    """
    Take a list of commands, initial state and grid limits and move the robot
    """
    if _is_outside_grid(pos, grid_size):
        return pos, "LOST"

    for cmd in cmds:
        next_pos = _execute_one_command(pos, cmd)
        if _is_outside_grid(next_pos, grid_size):
            return pos, "LOST"
        else:
            pos = next_pos
    return pos, ""
