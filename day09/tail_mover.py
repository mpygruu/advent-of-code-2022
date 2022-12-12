def move_tail(index, prev_row_index, prev_column_index, tail_row, tail_column):
    possibilities_row = []
    possibilities_column = []
    for i in range(prev_row_index-1, prev_row_index+2):
        for j in range(prev_column_index-1, prev_column_index+2):
            for k in range(tail_row[index]-1, tail_row[index]+2):
                for l in range(tail_column[index]-1, tail_column[index]+2):
                    if i == k and j == l:
                        possibilities_row.append(i)
                        possibilities_column.append(j)
    
    if len(possibilities_row) == 3:
        tail_row[index] = possibilities_row[1]
        tail_column[index] = possibilities_column[1]
    elif len(possibilities_row) == 2:
        if possibilities_row[0] != prev_row_index and possibilities_column[0] != prev_column_index:
            tail_row[index] = possibilities_row[1]
            tail_column[index] = possibilities_column[1]
        else:
            tail_row[index] = possibilities_row[0]
            tail_column[index] = possibilities_column[0]
    else:
        tail_row[index] = possibilities_row[0]
        tail_column[index] = possibilities_column[0]
                
    return tail_row, tail_column