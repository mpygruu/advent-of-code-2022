from file_parser import parse_file_data

# BFS
def find_shortest_path(heightmap: list[list[str]], start: tuple[int,int]):
    height_values = parse_file_data(heightmap)
    row, column = start[0]+1, start[1]+1
    step = 0
    visited = [(1,1)]
    queue = [(row, column, step)]
    
    while len(queue) > 0:
        row, column, step = queue.pop(0)

        if heightmap[row-1][column-1] == 'E':
            return step

        for i in range(-1,2):
            for j in range(-1,2):
                if i != j and i != -j:
                    if __can_visit(height_values, row+i, column+j, row, column, visited):
                        queue.append((row+i, column+j, step+1))
                        visited.append((row+i, column+j))
    
    return -1


def __can_visit(height_values, i, j, row, column, visited):
    if not (0 <= height_values[i][j] <= height_values[row][column]+1):
        return False
    
    if (i,j) in visited:
        return False
    
    return True


def start_x_y_part1(heightmap):
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if heightmap[i][j] == 'S':
                return i, j