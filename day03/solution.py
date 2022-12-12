def read_file_data() -> list:
    file = open("day3/data.txt", "r")
    file_data = file.read().splitlines()
    file.close()
    return file_data


def part1_solution():
    from priority_sum_calculator import priorities_sum_part1
    rucksack_list = read_file_data()
    return priorities_sum_part1(rucksack_list)


def part2_solution():
    from priority_sum_calculator import priorities_sum_part2
    rucksack_list = read_file_data()
    return priorities_sum_part2(rucksack_list)


def main():
    print("Part 1:", part1_solution())
    print("Part 2:", part2_solution())


main()