from file_reader import read_file
from file_data_parser import parse_file_data_part1, parse_file_data_part2
import sand_simulator

file_data = read_file()
grid = parse_file_data_part1(file_data)
print("Part 1:", sand_simulator.simulate_falling_sand(grid))
