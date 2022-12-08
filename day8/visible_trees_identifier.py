# returns the same grid, with 1 for visible and 0 for invisible
def identify_visible_trees(tree_heights: list[list[int]]) -> list[list[int]]:
    from visibility_grid_preparer import prepare_visibility_grid

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



def visible_from_left(row: list[int], index: int) -> bool:
    for i in range(index):
        if row[i] >= row[index]:
            return False
    
    return True


def visible_from_right(row: list[int], index: int) -> bool:
    for i in range(index+1, len(row)):
        if row[i] >= row[index]:
            return False
    
    return True


def visible_from_top(column: list[int], index: int) -> bool:
    for i in range(index):
        if column[i] >= column[index]:
            return False
    
    return True


def visible_from_bottom(column: list[int], index: int) -> bool:
    for i in range(index+1, len(column)):
        if column[i] >= column[index]:
            return False
    
    return True