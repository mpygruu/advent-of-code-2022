def count_visible_trees(visibility_grid: list[list[int]]):
    sum = 0
    for row in visibility_grid: 
        for elem in row:
            if elem == 1:
                sum += 1
    
    return sum