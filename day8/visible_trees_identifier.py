# returns the same grid, with 1 for visible and 0 for invisible
def identify_visible_trees(tree_heights: list[list[int]]) -> list[list[int]]:
    from visibility_grid_preparer import prepare_visibility_grid
    from visibility_checker import visible_from_bottom, visible_from_left, visible_from_right, visible_from_top

    visibility_grid = prepare_visibility_grid(tree_heights)

    for row_index in range(1, len(tree_heights)-1):
        row = tree_heights[row_index]

        for column_index in range(1, len(tree_heights[row_index])-1):
            
            column = [tree_heights[i][column_index] for i in range(len(tree_heights))]

            if visible_from_top(column, row_index) or visible_from_bottom(column, row_index):
                visibility_grid[row_index][column_index] = 1
                
            if visible_from_left(row, column_index) or visible_from_right(row, column_index):
                visibility_grid[row_index][column_index] = 1
                
        
    return visibility_grid
