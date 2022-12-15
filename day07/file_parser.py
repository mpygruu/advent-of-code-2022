from directory import Directory
from file import File

def get_directory_tree_from_file_data(file_data: list[str]) -> Directory:
    current_directory = Directory(path='/', previous_dir=None)

    for line in file_data[2:]:

        if line == '$ ls':
            continue

        elif line[:7] == '$ cd ..':
            current_directory = current_directory.previous_dir
            continue

        elif line[:4] == '$ cd':
            current_directory = current_directory.find_direct_directory(line[5:])
            continue

        if line[:3] == 'dir':
            current_directory.add_file_or_dir(Directory(line.split(' ')[1], current_directory))

        else:
            size = int(line.split(' ')[0])
            name = line.split(' ')[1]
            current_directory.add_file_or_dir(File(name, size))
    
    
    while current_directory.previous_dir != None:
        current_directory = current_directory.previous_dir

    return current_directory