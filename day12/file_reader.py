INPUT_PATH = "day12/input.txt"
EXAMPLE_INPUT_PATH = "day12/example_input.txt"

def read_file() -> list[list[str]]:
    with open(INPUT_PATH) as file:
        file_data = file.read().splitlines()
    
    for i in range(len(file_data)):
        file_data[i] = [*file_data[i]]
    
    return file_data