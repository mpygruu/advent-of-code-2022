cycle = 1
register_x = 1
signal_strength = 0
CRT = [['' for i in range(40)] for i in range(6)]
CRT_column = 0

def execute_program(file_data):
    global cycle
    global register_x
    global signal_strength
    global CRT
    global CRT_column

    for line in file_data:
        instruction = line[:4]
        number = int(line[5:]) if instruction == 'addx' else 0

        if instruction == 'noop':
            if CRT_column < 6:
                update_CRT()

            cycle += 1

            if is_interesting_cycle():
                signal_strength += cycle*register_x
            
            if cycle % 40 == 0:
                CRT_column += 1

        elif instruction == 'addx':
            for i in range(2):
                if CRT_column < 6:
                    update_CRT()

                cycle += 1

                if i == 1: 
                    register_x += number

                if is_interesting_cycle():
                    signal_strength += cycle*register_x
                
                if cycle % 40 == 0:
                    CRT_column += 1

    return signal_strength, CRT


def is_interesting_cycle() -> bool:
    return True if (cycle-20)%40 == 0 else False


def update_CRT():
    index = (cycle-1)%40
    if index >= register_x - 1 and index <= register_x +1:
        CRT[CRT_column][index] = '#'
    else:
        CRT[CRT_column][index] += '.'


def print_CRT():
    for list in CRT:
        for item in list:
            print(item, end="")
        print()


def main():
    from file_reader import read_file

    file_data = read_file()
    signal_strength, CRT = execute_program(file_data)
    print("Part 1:", signal_strength)
    print("Part 2:")
    print_CRT()


main()