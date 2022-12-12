def find_max_scenic_score(scenic_scores: list[list[int]]) -> int:
    max_scenic_score = 0

    for row in scenic_scores:    
        if max(row) > max_scenic_score:
            max_scenic_score = max(row)
    
    return max_scenic_score