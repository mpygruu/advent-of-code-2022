def pair_overlaps(pair_data) -> bool:
    numbers = [int(char) for char in pair_data.replace(',', '-').split("-") if char.isdigit()]
    return (__right_overlaps_left(numbers) or __left_overlaps_right(numbers))


def __right_overlaps_left(numbers: list):
    if numbers[2] >= numbers[0] and numbers[2] <= numbers[1]:
        return True

    return False


def __left_overlaps_right(numbers: str):
    if numbers[0] >= numbers[2] and numbers[0] <= numbers[3]:
        return True

    return False


def count_overlaps(file_data):
    sum = 0
    for line in file_data:
        if pair_overlaps(line):
            sum += 1
    
    return sum