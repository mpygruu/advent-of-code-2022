def perform_simulation(destinations: list[str], counts: list[int]) -> list[list[int]]:
    from grid_preparer import starting_indexes, prepare_grid

    starting_index_row, starting_index_column = starting_indexes(destinations, counts)
    head_row_index, head_column_index = starting_index_row, starting_index_column
    tail_row_index, tail_column_index = starting_index_row, starting_index_column

    grid = prepare_grid(destinations, counts)
    grid[starting_index_row][starting_index_column] = 1

    for i in range(len(destinations)):
        dest = destinations[i]
        for count in range(counts[i]):
            if dest == 'L':
                head_column_index -= 1
            if dest == 'R':
                head_column_index += 1
            if dest == 'U':
                head_row_index -= 1
            if dest == 'D':
                head_row_index += 1
            if not __tail_nearby((head_row_index, head_column_index), (tail_row_index, tail_column_index)):
                if dest == 'L':
                    tail_column_index = head_column_index + 1
                    tail_row_index = head_row_index
                if dest == 'R':
                    tail_column_index = head_column_index - 1
                    tail_row_index = head_row_index
                if dest == 'U':
                    tail_row_index = head_row_index + 1
                    tail_column_index = head_column_index
                if dest == 'D':
                    tail_row_index = head_row_index - 1
                    tail_column_index = head_column_index
                
                grid[tail_row_index][tail_column_index] = 1
    
    return grid


#def head_tail_same_column(head_indexes, tail_indexes):
#    return head_indexes[1] == tail_indexes[1]


#def head_tail_same_row(head_indexes, tail_indexes):
#    return head_indexes[0] == tail_indexes[0]

def __tail_nearby(head_indexes, tail_indexes) -> bool:
    for i in range(head_indexes[0]-1, head_indexes[0]+2):
        for j in range(head_indexes[1]-1, head_indexes[1]+2):
            if tail_indexes[0] == i and tail_indexes[1] == j:
                return True
    
    return False