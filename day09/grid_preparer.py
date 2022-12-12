# left, right, top, bottom
def max_destination_counts(destinations: list[str], counts: list[int]) -> tuple[int,int,int,int]:
    right, bottom = 0,0
    left_max, right_max, top_max, bottom_max = 0,0,0,0
    
    for i in range(len(counts)):
        if destinations[i] == 'L':
            right -= counts[i]
            if left_max < -right and right < 0:
                left_max = -right
        if destinations[i] == 'R':
            right += counts[i]
            if right_max < right:
                right_max = right
        if destinations[i] == 'U':
            bottom -= counts[i]
            if(top_max < -bottom) and bottom < 0:
                top_max = -bottom
        if destinations[i] == 'D':
            bottom += counts[i]
            if(bottom_max < bottom):
                bottom_max = bottom

    return (left_max, right_max, top_max, bottom_max)
    

def grid_size(destinations: list[str], counts: list[int]) -> tuple[int, int]:
    left_max, right_max, top_max, bottom_max = max_destination_counts(destinations, counts)
    return (top_max + bottom_max + 1, left_max + right_max + 1)


def starting_indexes(destinations: list[str], counts: list[int]) -> tuple[int, int]:
    left_max, right_max, top_max, bottom_max = max_destination_counts(destinations, counts)
    return (top_max, left_max)


def prepare_grid(destinations: list[str], counts: list[int]) -> list[int, int]:
    grid_size_rows, grid_size_columns = grid_size(destinations, counts)
    return [[0 for i in range(grid_size_columns)] for j in range(grid_size_rows)]