def parse_file_data(heightmap: list[list[str]]) -> list[list[int]]:
    parsed_data = [[0 for i in range(len(heightmap[0])+2)] for j in range(len(heightmap)+2)]

    for i in range(len(parsed_data)):
        for j in range(len(parsed_data[0])):
            if i == 0 or i == len(parsed_data)-1 or j == 0 or j == len(parsed_data[0])-1:
                parsed_data[i][j] = -1
            elif heightmap[i-1][j-1] == 'S':
                parsed_data[i][j] = 1
            elif heightmap[i-1][j-1] == 'E':
                parsed_data[i][j] = ord('z')-96
            else:
                parsed_data[i][j] = ord(heightmap[i-1][j-1])-96

    return parsed_data