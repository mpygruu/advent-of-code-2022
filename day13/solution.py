INPUT_PATH = "day13/input.txt"
EXAMPLE_INPUT_PATH = "day13/example_input.txt"

def load_input_data():
    with open(EXAMPLE_INPUT_PATH) as file:
        file_data = file.read().splitlines()

    return file_data


def decode_line(line: str):
    import json
    return json.loads(line)


def is_in_right_order(first, second) -> bool:
    for i in range(min(len(first), len(second))):

        if isinstance(first[i], int) and isinstance(second[i], int):       
            if first[i] == second[i]:
                continue
            else:
                return (first < second)

        if isinstance(first[i], list) and isinstance(second[i], list):       
            return is_in_right_order(first[i], second[i])

        if isinstance(first[i], int) and isinstance(second[i], list):  
            temp = [first[i]]    
            return is_in_right_order(temp, second[i])

        if isinstance(first[i], list) and isinstance(second[i], int):  
            temp = [second[i]]    
            return is_in_right_order(temp, second[i])
    
    return len(first) < len(second)


def count_pairs_in_right_order(data: list):
    sum = 0

    for i in range(0, len(data)-2, 3):
        if is_in_right_order(decode_line(data[i]), decode_line(data[i+1])):
            sum += 1

    return sum



file_data = load_input_data()
print("Part 1:", count_pairs_in_right_order(file_data))