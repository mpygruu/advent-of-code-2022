from path_finder import find_shortest_path

def find_shortest_trailing_path(heightmap: list[list[str]]):
    path_lengths = []

    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if heightmap[i][j] == 'a' or heightmap[i][j] == 'S':
                path_length = find_shortest_path(heightmap,(i, j))
                if path_length != -1:
                    path_lengths.append(path_length)
    
    return min(path_lengths)
