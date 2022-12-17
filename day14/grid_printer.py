def print_grid(grid):
    for i in range(len(grid)):
        print(i, end="")
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print()