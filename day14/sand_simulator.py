def simulate_falling_sand(grid):
    start_x = find_source_x(grid)
    grains_placed = 0

    while not falling_into_abyss(grid, start_x, last_free_index(grid, start_x, 0)):
        x, y = start_x, last_free_index(grid, start_x, 0)
        grid = spawn_sand_grain(grid, x, y)

        grains_placed+=1
        print(grains_placed)

    return grains_placed


def find_source_x(grid):
    for i in range(len(grid[0])):
        if grid[0][i] == '+':
            return i


def last_free_index(grid, start_x, y):
    for i in range(y, len(grid)):
        if grid[i][start_x] in {'#', 'o'}:
            return i-1
    

def spawn_sand_grain(grid,x,y):
    # go down left
    if grid[y+1][x-1] == '.':
        spawn_sand_grain(grid,x-1,last_free_index(grid, x-1, y+1))
    # go down right
    elif grid[y+1][x+1] == '.':
        spawn_sand_grain(grid,x+1,last_free_index(grid, x+1, y+1))
    # rest in place
    else:
        grid[y][x] = 'o'
    
    return grid


def falling_into_abyss(grid,x,y): 
    if x <= 0 or y >= len(grid)-2:
        return True

    # go down left
    if grid[y+1][x-1] == '.':
        falling_into_abyss(grid,x-1,last_free_index(grid, x-1, y+1))
    # go down right
    elif grid[y+1][x+1] == '.':
        falling_into_abyss(grid,x-1,last_free_index(grid, x+1, y+1))
    else:
        return False