def part1_solution():
    from input_reader import read_input
    from input_parser import parse_file_input
    from head_tail_simulation import perform_simulation
    from visited_positions_counter import count_visited_positions

    file_data = read_input()
    destinations, counts = parse_file_input(file_data)
    new_grid = perform_simulation(destinations, counts, 1)
    return count_visited_positions(new_grid)


def part2_solution():
    from input_reader import read_input
    from input_parser import parse_file_input
    from head_tail_simulation import perform_simulation
    from visited_positions_counter import count_visited_positions

    file_data = read_input()
    destinations, counts = parse_file_input(file_data)
    new_grid = perform_simulation(destinations, counts, 9)
    return count_visited_positions(new_grid)


def main():
    print("Part 1:", part1_solution())
    print("Part 2:", part2_solution())


main()