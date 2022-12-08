def part1_solution():
    from file_reader import read_tree_heights
    from visible_trees_identifier import identify_visible_trees
    from visible_trees_counter import count_visible_trees

    file_data = read_tree_heights()
    visibility_grid = identify_visible_trees(file_data)

    return count_visible_trees(visibility_grid)
    


def main():
    print("Part 1:", part1_solution())


main()