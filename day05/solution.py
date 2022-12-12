def part1_solution():
    from crate_rearrange import crates_on_top_part_1
    from file_data_getter import get_commands_from_file, get_data_from_file
    file_data = get_data_from_file()
    commands_data = get_commands_from_file()
    return crates_on_top_part_1(file_data, commands_data)


def part2_solution():
    from crate_rearrange import crates_on_top_part_2
    from file_data_getter import get_commands_from_file, get_data_from_file
    file_data = get_data_from_file()
    commands_data = get_commands_from_file()
    return crates_on_top_part_2(file_data, commands_data)


def main():
    print("Part 1:", part1_solution())
    print("Part 2:", part2_solution())


main()