def get_data_from_file() -> list:
    file_data = []
    file = open("day5/crate_stacks_input.txt", "r")

    for line in file:
        line_chars = []
        for i in range(0, len(line)):
            if (i%4-1)==0:
                line_chars.append(line[i])
        file_data.append(line_chars)
    
    file.close()
    return file_data


def get_commands_from_file() -> list:
    file_data = []
    file = open("day5/rearrangement_commands.txt", "r")

    for line in file:
        numbers = [int(char) for char in line.replace('move ', '').replace('from ', '').replace('to ', '').split() if char.isdigit()]
        file_data.append(numbers)
    
    file.close()
    return file_data