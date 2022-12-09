def parse_file_input(file_data: list[str]) -> tuple[list[str], list[int]]:
    directions = []
    counts = []

    for line in file_data:
        directions.append(line[0])
        counts.append(int(line[2:]))
    
    return (directions, counts)