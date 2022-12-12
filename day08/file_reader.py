FILE_PATH = "day8/data.txt"
EXAMPLE_FILE_PATH = "day8/example_data.txt"


def read_tree_heights():
    file_data = []
    file = open(FILE_PATH)
    for row in file:
        row_list = []
        for char in row:
            if(char != '\n'):
                row_list.append(int(char))

        file_data.append(row_list)
    
    file.close()
    return file_data