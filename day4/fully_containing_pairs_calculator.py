def __contains_the_other(pair_data: str) -> bool:
    numbers = [int(char) for char in pair_data.replace(',', '-').split("-") if char.isdigit()]
    return (__right_fully_contains_left(numbers) or __left_fully_contains_right(numbers))


def __right_fully_contains_left(numbers: list):
    if numbers[0] >= numbers[2] and numbers[1] <= numbers[3]:
        return True

    return False


def __left_fully_contains_right(numbers: str):
    if numbers[2] >= numbers[0] and numbers[3] <= numbers[1]:
        return True

    return False


def count_containing_other(file_data):
    sum = 0
    for line in file_data:
        if(__contains_the_other(line)):
            sum += 1
    
    return sum