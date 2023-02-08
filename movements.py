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


def move(
    state: Tuple[int, int, Orientations], cmd: Commands
) -> Tuple[int, int, Orientations]:
    x, y, orientation = state
    if cmd == Commands.F.name:
        delta = delta_by_orientation[orientation]
        next_x, next_y = tuple(map(sum, zip((x, y), delta)))
        return (next_x, next_y, orientation)
    else:
        return (x, y, rotate(orientation, cmd))


def rotate(orientation: Orientations, cmd: Commands) -> Orientations:
    clockwise_orientations = [o for o in Orientations]
    current_index = clockwise_orientations.index(orientation)
    if cmd == Commands.R.name:
        next_index = (current_index + 1) % 4
    else:
        next_index = (current_index - 1) % 4

    return clockwise_orientations[next_index]


def make_movements(
    state: Tuple[int, int, Orientations],
    cmds: List[Commands],
    grid_size: Tuple[int, int],
) -> Tuple[Tuple[int, int, Orientations], str]:
    for cmd in cmds:
        next_state = move(state, cmd)
        if (
            next_state[0] < 0
            or next_state[0] > grid_size[0]
            or next_state[1] < 0
            or next_state[1] > grid_size[1]
        ):
            return state, "LOST"
        else:
            state = next_state

    return state, ""
