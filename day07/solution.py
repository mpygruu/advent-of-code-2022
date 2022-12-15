from directory import Directory
from file import File
from file_parser import get_directory_tree_from_file_data


INPUT_PATH = "day07/input.txt"
EXAMPLE_INPUT_PATH = "day07/example_input.txt"


def read_file() -> list[str]:
    with open(INPUT_PATH) as file:
        file_data = file.read().splitlines()

    return file_data


def dir_size_sum(root_dir: Directory, limit: int = None) -> int:
    sum = 0
    for dir in root_dir.files:
        if not isinstance(dir, Directory):
            continue

        if dir.size <= limit:
            sum += dir.size

        sum += dir_size_sum(dir, limit)
    
    return sum


def smallest_dir_size_to_delete(root_dir: Directory, required_space: int, min: int):
    for dir in root_dir.files:
        if not isinstance(dir, Directory):
            continue

        if dir.size > required_space and dir.size < min:
            min = dir.size
        
        min = smallest_dir_size_to_delete(dir, required_space, min)

    return min



file_data = read_file()
root_dir = get_directory_tree_from_file_data(file_data)
root_dir.calculate_size()

print("Part 1:", dir_size_sum(root_dir, 100000))
print("Part 2:", smallest_dir_size_to_delete(root_dir, 30000000-(70000000-root_dir.size), root_dir.size))