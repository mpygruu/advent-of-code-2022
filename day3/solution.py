def read_file_data() -> list:
    file = open("day3/data.txt", "r")
    file_data = file.read().splitlines()
    file.close()
    return file_data


def item_in_both_compartments(rucksack: str):
    comp1 = rucksack[:len(rucksack)//2]
    comp2 = rucksack[len(rucksack)//2:]

    comp1_set = set(comp1)
    comp2_set = set(comp2)

    return list(comp1_set.intersection(comp2_set))[0]
    

def priority(item: str) -> int:
    print(item)
    ascii = ord(item)
    
    if ascii >= 97:
        return ascii - 96
    else:
        return ascii - 65 + 27


def priorities_sum(rucksack_list):
    sum = 0
    for rucksack in rucksack_list:
        duplicate_item = item_in_both_compartments(rucksack)
        sum += priority(duplicate_item)

    return sum



def main():
    rucksack_list = read_file_data()
    print("Part 1:", priorities_sum(rucksack_list))

main()