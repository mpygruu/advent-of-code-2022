INPUT_PATH = "day9/input.txt"
EXAMPLE_INPUT_PATH = "day9/example_input.txt"

def read_input():
    file = open(INPUT_PATH)
    file_data = file.read().splitlines()
    file.close()
    return file_data