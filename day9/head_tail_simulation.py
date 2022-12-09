def perform_simulation(destinations: list[str], counts: list[int], tails_count: int) -> list[list[int]]:
    from grid_preparer import starting_indexes, prepare_grid
    from tail_mover import move_tail

    starting_index_row, starting_index_column = starting_indexes(destinations, counts)
    head_row_index, head_column_index = starting_index_row, starting_index_column

    tail_row_index = [starting_index_row for i in range(tails_count)]
    tail_column_index = [starting_index_column for i in range(tails_count)]

    grid = prepare_grid(destinations, counts)
    grid[starting_index_row][starting_index_column] = 1

    for i in range(len(destinations)):
        dest = destinations[i]

        # move head
        for count in range(counts[i]):
            if dest == 'L':
                head_column_index -= 1
            if dest == 'R':
                head_column_index += 1
            if dest == 'U':
                head_row_index -= 1
            if dest == 'D':
                head_row_index += 1

            # move tails
            if not __tail_nearby((head_row_index, head_column_index), (tail_row_index[0], tail_column_index[0])):
                tail_row_index, tail_column_index = move_tail(0, head_row_index, head_column_index, tail_row_index, tail_column_index)

            for j in range(1,tails_count):
                if not __tail_nearby((tail_row_index[j-1], tail_column_index[j-1]), (tail_row_index[j], tail_column_index[j])):
                    tail_row_index, tail_column_index = move_tail(j, tail_row_index[j-1], tail_column_index[j-1], tail_row_index, tail_column_index)

            grid[tail_row_index[tails_count-1]][tail_column_index[tails_count-1]] = 1

    return grid


def __tail_nearby(head_indexes, tail_indexes) -> bool:
    for i in range(head_indexes[0]-1, head_indexes[0]+2):
        for j in range(head_indexes[1]-1, head_indexes[1]+2):
            if tail_indexes[0] == i and tail_indexes[1] == j:
                return True
    
    return False