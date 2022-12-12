def prepare_visibility_grid(tree_heights: list[list[int]]):
    visibility_grid = [[0 for i in range(len(tree_heights))] for j in range(len(tree_heights[0]))]
    for i in range(len(visibility_grid)):
        if i==0 or i==len(visibility_grid)-1:
            visibility_grid[i] = [1 for i in range(len(tree_heights))]
        else:
            visibility_grid[i][0] = 1
            visibility_grid[i][len(visibility_grid)-1] = 1
    
    return visibility_grid