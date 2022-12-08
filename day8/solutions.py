def part1_solution():
    from file_reader import read_tree_heights
    from visible_trees_identifier import identify_visible_trees
    from visible_trees_counter import count_visible_trees

    file_data = read_tree_heights()
    visibility_grid = identify_visible_trees(file_data)

    return count_visible_trees(visibility_grid)
    
def part2_solution():
    from file_reader import read_tree_heights
    from scenic_score_counter import calculate_scenic_scores
    from max_scenic_score_finder import find_max_scenic_score

    file_data = read_tree_heights()
    scenic_scores = calculate_scenic_scores(file_data)
    print(scenic_scores)
    max_scenic_score = find_max_scenic_score(scenic_scores)
    
    return max_scenic_score
    

def main():
    print("Part 1:", part1_solution())
    print("Part 2:", part2_solution())


main()