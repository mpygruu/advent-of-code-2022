INPUT_PATH = "day13/input.txt"
EXAMPLE_INPUT_PATH = "day13/example_input.txt"

def load_input_data():
    with open(INPUT_PATH) as file:
        file_data = file.read().splitlines()

    return file_data


def decode_line(line: str):
    import json
    return json.loads(line)


def is_in_right_order(first_packet, second_packet) -> bool:
    # -1 -> brak decyzji
    # 0 -> False
    # 1 -> True
    result = -1

    for i in range(0, max(len(first_packet), len(second_packet))):
        if i >= len(first_packet):
            return True
        if i >= len(second_packet):
            return False

        if is_integer(first_packet[i]) and is_integer(second_packet[i]):
            if first_packet[i] != second_packet[i]:
                result = first_packet[i] < second_packet[i]
        
        if is_list(first_packet[i]) and is_list(second_packet[i]):
            result = is_in_right_order(first_packet[i], second_packet[i])

        if is_integer(first_packet[i]) and is_list(second_packet[i]):
            first_packet[i] = [first_packet[i]]
            result = is_in_right_order(first_packet[i], second_packet[i])

        if is_integer(second_packet[i]) and is_list(first_packet[i]):
            second_packet[i] = [second_packet[i]]
            result = is_in_right_order(first_packet[i], second_packet[i])
        
        if result != -1:
            return result
        
    return -1
        

is_integer = lambda value: isinstance(value, int)
is_list = lambda value: isinstance(value, list)


def count_pairs_in_right_order(data: list):
    sum = 0
    index = 1
    for i in range(0, len(data), 3):
        if is_in_right_order(decode_line(data[i]), decode_line(data[i+1])) == 1:
            sum += index
        index += 1

    return sum

def count_decoder_key(data: list):
    divider1 = 0
    divider2 = 0
    index = 1
    for i in range(0, len(data)):
        if len(data[i]) == 0:
            index += 1
            continue

        if is_in_right_order(decode_line(data[i]), [[2]]) == 1:
            divider1 += 1

        if is_in_right_order(decode_line(data[i]), [[6]]) == 1:
           divider2 += 1

        index += 1

    return (1+divider1)*(2+divider2)


file_data = load_input_data()
print("Part 1:", count_pairs_in_right_order(file_data))
print("Part 2:", count_decoder_key(file_data))