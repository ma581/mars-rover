from typing import List, Tuple
from enum import Enum


class Orientations(Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"  # Ordered clockwise

    def __str__(self):
        return str(self.value)


Commands = Enum("Commands", ["F", "R", "L"])

delta_by_orientation = {
    Orientations.N: (0, 1),
    Orientations.S: (0, -1),
    Orientations.E: (1, 0),
    Orientations.W: (-1, 0),
}


def _single_movement(
    state: Tuple[int, int, Orientations], cmd: Commands
) -> Tuple[int, int, Orientations]:
    """Make a single movement or rotation"""
    x, y, orientation = state
    if cmd == Commands.F.name:
        delta = delta_by_orientation[orientation]
        next_x, next_y = tuple(map(sum, zip((x, y), delta)))
        return (next_x, next_y, orientation)
    else:
        return (x, y, _rotate(orientation, cmd))


def _rotate(orientation: Orientations, cmd: Commands) -> Orientations:
    clockwise_orientations = [o for o in Orientations]
    current_index = clockwise_orientations.index(orientation)
    if cmd == Commands.R.name:
        next_index = (current_index + 1) % 4
    else:
        next_index = (current_index - 1) % 4

    return clockwise_orientations[next_index]


def _is_outside_grid(
    state: Tuple[int, int, Orientations], grid_size: Tuple[int, int]
) -> bool:
    (x, y, _) = state
    return x < 0 or x > grid_size[0] or y < 0 or y > grid_size[1]


valid_default_state = (0, 0, Orientations.N)


def make_movements(
    state: Tuple[int, int, Orientations],
    cmds: List[Commands],
    grid_size: Tuple[int, int],
) -> Tuple[Tuple[int, int, Orientations], str]:
    """
    Take a list of commands, initial state and grid limits and move the robot
    """
    for cmd in cmds:

        if _is_outside_grid(state, grid_size):
            print(
                f"Initial state {state} is outside the grid: {grid_size}. Returning a default valid state"
            )
            return valid_default_state, "LOST"

        next_state = _single_movement(state, cmd)
        if _is_outside_grid(next_state, grid_size):
            return state, "LOST"
        else:
            state = next_state

    return state, ""
