from file import File


def get_files_from_input() -> list[File]:
    from file_reader import read_commands
    commands = read_commands()

    file_list = []
    path = ""
    for line in commands:
        if line[0] == '$':
            if line[2:4] == 'cd':
                path = __updated_path(path, line[5:])
        else:
            if __is_file(line): 
                file_list.append(get_file_from_line(line, path))

    return file_list


def __updated_path(path: str, content: str) -> str:
    if content == '/':
        return content

    if content == '..':
        ind = path.rfind('/', 0, len(path)-2)
        return path[:ind+1]

    return path + content + '/'
 

def __is_file(line) -> bool:
    if line[0:3] == 'dir':
        return False
    
    return True


def get_file_from_line(line: str, path) -> File:
    file_data = line.split()
    return File(file_data[1], int(file_data[0]), path)