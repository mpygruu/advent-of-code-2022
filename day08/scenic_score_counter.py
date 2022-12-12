def calculate_scenic_scores(tree_heights: list[list[int]]) -> list[list[int]]:
    from scenic_score_trees_counter import trees_visible_left, trees_visible_right

    scenic_scores = [[0 for i in range(len(tree_heights))] for j in range(len(tree_heights[0]))]

    for row_index in range(1, len(tree_heights)-1):
        row = tree_heights[row_index]

        for column_index in range(1, len(tree_heights[row_index])-1):
            column = [tree_heights[i][column_index] for i in range(len(tree_heights))]

            scenic_scores[row_index][column_index] = trees_visible_left(row, column_index)
            scenic_scores[row_index][column_index] *= trees_visible_right(row, column_index)
            scenic_scores[row_index][column_index] *= trees_visible_left(column, row_index)
            scenic_scores[row_index][column_index] *= trees_visible_right(column, row_index)
    
    return scenic_scores
