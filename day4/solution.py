def get_file_data() -> list:
    file = open("day4/data.txt", "r")
    file_data = file.read().splitlines()
    file.close()
    return file_data


def main():
    from fully_containing_pairs_calculator import count_containing_other
    from overlap_pairs_calculator import count_overlaps
    file_data = get_file_data()
    print("Part 1:", count_containing_other(file_data))
    print("Part 2:", count_overlaps(file_data))



main()