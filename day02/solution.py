def read_file_data() -> list:
    file_path = "day2/data.txt"
    file = open(file_path, "r")
    file_data = file.read().splitlines()
    file.close()
    return file_data


def part1_solution():
    from score_calculator import calculate_score

    game_data = read_file_data()
    return calculate_score(game_data)


def part2_solution():
    from score_calculator_part_2 import calculate_score

    game_data = read_file_data()
    return calculate_score(game_data)


def main():
    print("Part 1:", part1_solution())
    print("Part 2:", part2_solution())

main()