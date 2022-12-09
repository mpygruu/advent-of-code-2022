def count_visited_positions(grid: list[list[int]]):
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == 1):
                sum += 1
    
    return sum