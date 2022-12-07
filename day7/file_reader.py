def read_commands() -> list[str]:
    file = open("day7/data.txt")
    commands_list = file.read().splitlines()
    file.close()
    return commands_list