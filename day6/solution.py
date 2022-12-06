def part1_solution():
    from packet_marker_finder import characters_before_start_of_packet
    from file_reader import get_signal_from_file

    signal = get_signal_from_file()
    return characters_before_start_of_packet(signal)


def part2_solution():
    from packet_marker_finder import characters_before_start_of_message
    from file_reader import get_signal_from_file
    
    signal = get_signal_from_file()
    return characters_before_start_of_message(signal)


def main():
    print("Part 1:", part1_solution())
    print("Part 2:", part2_solution())


main()