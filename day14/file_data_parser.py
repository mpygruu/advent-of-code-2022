# returns grid with filled lines as #
def parse_file_data_part1(file_data: list[str]) -> list[list[str]]:
    min_x = find_min_x(file_data)
    max_x, max_y = max_x_y(file_data)

    grid = [['.' for i in range((max_x-min_x+1))] for j in range(max_y+1)]
    grid[0][500-min_x] = '+'
    
    for line in file_data:       
        points_x, points_y = get_points_from_line(line)
        
        for i in range(len(points_x)-1):
            if points_x[i] == points_x[i+1]:
                grid = draw_line_y(grid, points_x[i]-min_x, points_y[i], points_y[i+1])
            else:
                grid = draw_line_x(grid, points_y[i], points_x[i]-min_x, points_x[i+1]-min_x)


    return grid


def parse_file_data_part2(file_data: list[str]) -> list[list[str]]:
    min_x = find_min_x(file_data)
    max_x, max_y = max_x_y(file_data)

    grid = [['.' for i in range((max_x-min_x+31))] for j in range(max_y+3)]
    grid[0][500-min_x+15] = '+'
    
    for line in file_data:       
        points_x, points_y = get_points_from_line(line)
        
        for i in range(len(points_x)-1):
            if points_x[i] == points_x[i+1]:
                grid = draw_line_y(grid, points_x[i]-min_x+15, points_y[i], points_y[i+1])
            else:
                grid = draw_line_x(grid, points_y[i], points_x[i]-min_x+15, points_x[i+1]-min_x+15)

    for i in range(len(grid[0])):
        grid[2+max_y][i] = '#'

    return grid


def find_min_x(file_data):
    min_x = 1000
    for line in file_data:
        points_data = line.replace(' -> ', ',')

        ind = 0
        for number in points_data.split(','):
            if ind%2==0 and int(number) < min_x:
                min_x = int(number)

            ind+=1

    return min_x


def max_x_y(file_data):
    max_x, max_y = 0, 0
    for line in file_data:
        points_data = line.replace(' -> ', ',')

        ind = 0
        for number in points_data.split(','):
            if ind%2==0 and int(number) > max_x:
                max_x = int(number)
            elif ind%2==1 and int(number) > max_y:
                max_y = int(number)

            ind+=1

    return max_x, max_y


def get_points_from_line(line):
    points_data = line.replace(' -> ', ',')
    points_x, points_y = [], []
    ind = 0
    for number in points_data.split(','):
        if ind%2==0:
            points_x.append(int(number))
        else:
            points_y.append(int(number))
        ind+=1

    return points_x, points_y


def draw_line_x(grid, y, start, end):
    if start > end:
        start, end = end, start

    for i in range(start, end+1):
        grid[y][i] = '#'
    
    return grid


def draw_line_y(grid, x, start, end):
    if start > end:
        start, end = end, start

    for i in range(start, end+1):
        grid[i][x] = '#'

    return grid