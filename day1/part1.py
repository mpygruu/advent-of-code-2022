def get_calories_from_file() -> list:
    file_path = "day1/data.txt"
    file = open(file_path)
    file_data =  file.read().splitlines()
    file.close()
    return file_data


def calories_per_elf(calories_list) -> list:
    elves_calories = []
    elf_index = 0

    for calories in calories_list:
        if calories == '':
            elf_index+=1
        else:
            if len(elves_calories) == elf_index:
                elves_calories.append(int(calories))
            else:
                elves_calories[elf_index] += int(calories)
    
    return elves_calories


def part1_solution():
    calories_list = get_calories_from_file()
    elves_calories = calories_per_elf(calories_list)
    return max(elves_calories)


def main():
    max_elf_calories = part1_solution()
    print(max_elf_calories)


main()