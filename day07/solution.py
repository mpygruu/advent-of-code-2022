from file import File


def part1_solution():
    from file_parser import get_files_from_input
    from file_reader import read_commands
    files = get_files_from_input()
    dirs_sizes = directories_sizes(files)
    return size_sum_part_1(total_sizes(dirs_sizes))
    
# sizes of directories without children directories
def directories_sizes(files: list[File]):
    dirs_sizes = dict()

    for file in files:
        if file.path in dirs_sizes:
            dirs_sizes[file.path] += file.size
        else:
            dirs_sizes[file.path] = file.size


    return dirs_sizes


def total_sizes(dirs_sizes):
    total_dirs_sizes = dirs_sizes
    for path in dirs_sizes:
        for smaller_path in dirs_sizes:
            if path[:len(smaller_path)] == smaller_path:
                total_dirs_sizes[path] += dirs_sizes[smaller_path]
    
    return total_dirs_sizes


# directories with of at most 100000
def size_sum_part_1(dirs_sizes: dict) -> int:
    sum = 0
    for path in dirs_sizes:
        if dirs_sizes[path] <= 100000:
            sum += dirs_sizes[path]
    
    return sum


def main():
    print("Part 1:", part1_solution())


main()