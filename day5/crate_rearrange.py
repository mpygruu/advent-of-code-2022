def __get_stacks(file_data: list) -> list:
    stacks = []

    for i in range(len(file_data[0])):
        stack = []
        for line in file_data:
            if line[i] != ' ':
                stack.append(line[i])
        stacks.append(list(reversed(stack)))
            
    return stacks


def __do_commands_on_stacks_cratemover_9000(stacks: list, commands: list):
    for command in commands:
        move, frm, to = command[0], command[1]-1, command[2]-1
        for i in range(0, move):
            temp = stacks[frm][-1]
            stacks[frm].pop()
            stacks[to].append(temp)
        
    return stacks


def __do_commands_on_stacks_cratemover_9001(stacks: list, commands: list):
    for command in commands:
        move, frm, to = command[0], command[1]-1, command[2]-1
        temp = stacks[frm][-move:]

        for i in range(move):
            del stacks[frm][-1]
            stacks[to].append(temp[i])
        
    return stacks


def __crates_on_top_as_str(stacks):
    top = ''
    for stack in stacks:
        top += stack[-1]
    return top


def crates_on_top_part_1(file_data, commands_data):
    stacks = __get_stacks(file_data)
    new_stacks = __do_commands_on_stacks_cratemover_9000(stacks, commands_data)
    return __crates_on_top_as_str(new_stacks)


def crates_on_top_part_2(file_data, commands_data):
    stacks = __get_stacks(file_data)
    new_stacks = __do_commands_on_stacks_cratemover_9001(stacks, commands_data)
    return __crates_on_top_as_str(new_stacks)