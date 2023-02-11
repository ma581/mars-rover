from execute_commands import execute_commands
from parse_inputs import parse_inputs


def main(request=None):
    if not request:  # Allows injection for unit testing
        try:
            request = parse_inputs()
        except Exception as e:
            print(f"{e}")
            return

    for pos, cmds in request["position_and_commands"]:
        if pos is not None:
            grid_size = request["grid_size"]

            position, status = execute_commands(pos, cmds, grid_size)
            print(f"({position.x}, {position.y}, {position.orientation}) {status}")


if __name__ == "__main__":
    main()
