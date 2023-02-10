from movements import make_movements
from parse_inputs import parse_inputs


def main(request=None):
    if not request:  # Allows injection for unit testing
        request = parse_inputs()

    for state_and_cmds in request["states_and_commands"]:
        if state_and_cmds is not None:
            state = state_and_cmds["position"]
            cmds = state_and_cmds["commands"]
            grid_size = request["grid_size"]

            position, status = make_movements(state, cmds, grid_size)
            print(f"({position.x}, {position.y}, {position.orientation}) {status}")


if __name__ == "__main__":
    main()
