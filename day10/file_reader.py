EXAMPLE_INPUT_PATH = "day10/example_input.txt"
INPUT_PATH = "day10/input.txt"

def read_file():
    file = open(INPUT_PATH)
    file_data = file.read().splitlines()
    file.close()
    return file_data