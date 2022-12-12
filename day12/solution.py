from file_reader import read_file
from file_parser import parse_file_data
from path_finder import find_shortest_path, start_x_y_part1
from trailing_path_finder import find_shortest_trailing_path


def part1_solution():
    data = read_file()
    return find_shortest_path(data, start_x_y_part1(data))


def part2_solution():
    data = read_file()
    return find_shortest_trailing_path(data)


print("Part 1:", part1_solution())
print("Part 2:", part2_solution())