class File:
    def __init__(self, name: str, size: int, path: str):
        self.name = name
        self.size = size
        self.path = path

    def __str__(self) -> str:
        return f"File with name: {self.name}, size: {self.size}, path: {self.path}"