def trees_visible_left(row: list[int], index: int) -> int:
    trees_visible = 0
    for i in range(index-1, -1, -1):    
        if row[i] < row[index]:              
            trees_visible += 1
        elif row[i] >= row[index]:
            trees_visible += 1
            break
        
    return trees_visible
         

def trees_visible_right(row: list[int], index: int) -> int:
    trees_visible = 0
    previous_max = 0
    for i in range(index+1, len(row)):
        if row[i] < row[index]:              
            trees_visible += 1
        elif row[i] >= row[index]:
            trees_visible += 1
            break
      

    return trees_visible