def visible_from_left(row: list[int], index: int) -> bool:
    for i in range(index):
        if row[i] >= row[index]:
            return False
    
    return True


def visible_from_right(row: list[int], index: int) -> bool:
    for i in range(index+1, len(row)):
        if row[i] >= row[index]:
            return False
    
    return True


def visible_from_top(column: list[int], index: int) -> bool:
    for i in range(index):
        if column[i] >= column[index]:
            return False
    
    return True


def visible_from_bottom(column: list[int], index: int) -> bool:
    for i in range(index+1, len(column)):
        if column[i] >= column[index]:
            return False
    
    return True