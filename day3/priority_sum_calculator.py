def __item_in_both_compartments(rucksack: str):
    comp1 = rucksack[:len(rucksack)//2]
    comp2 = rucksack[len(rucksack)//2:]

    comp1_set = set(comp1)
    comp2_set = set(comp2)

    return list(comp1_set.intersection(comp2_set))[0]
    

def __common_badge(rucksacks: list):
    set_comp1 = set(rucksacks[0])
    set_comp2 = set(rucksacks[1])
    set_comp3 = set(rucksacks[2])
    return list((set_comp1.intersection(set_comp2)).intersection(set_comp3))[0]
    

def __priority(item: str) -> int:
    ascii = ord(item)
    
    if ascii >= 97:
        return ascii - 96
    else:
        return ascii - 65 + 27


def priorities_sum_part1(rucksack_list):
    sum = 0
    for rucksack in rucksack_list:
        duplicate_item = __item_in_both_compartments(rucksack)
        sum += __priority(duplicate_item)

    return sum


def priorities_sum_part2(rucksack_list):
    sum = 0
    for i in range(0, len(rucksack_list)-2, 3):
        badge = __common_badge(rucksack_list[i:i+3])
        sum += __priority(badge)

    return sum