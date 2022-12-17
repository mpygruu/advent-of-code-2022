INPUT_PATH = "day14/input.txt"
EXAMPLE_INPUT_PATH = "day14/example_input.txt"

def read_file():
    with open(EXAMPLE_INPUT_PATH) as file:
        file_data = file.read().splitlines()
    
    return file_data