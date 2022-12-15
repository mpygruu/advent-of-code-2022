from file import File

class Directory:
    def __init__(self, path: str, previous_dir = None) -> None:
        self.path = path
        self.files = []
        self.previous_dir = previous_dir
        self.size = None
    
    def add_file_or_dir(self, file_or_dir):
        self.files.append(file_or_dir)

    
    def find_direct_directory(self, path) -> int:
        for i in range(len(self.files)):
            if isinstance(self.files[i], Directory) and self.files[i].path == path:
                return self.files[i]
    

    def calculate_size(self):
        size = 0
        for obj in self.files:
            if isinstance(obj, File):
                size += obj.size
            else:
                size += obj.calculate_size()

        self.size = size
        return size


    def __dir_str(self, nest_level):
        dir_str = '\n'
        dir_str += '  '*nest_level
        dir_str += f'- {self.path} (dir) -> size: {self.size}'

        for file_or_dir in self.files:
            if isinstance(file_or_dir, File):
                dir_str += '\n'
                dir_str += '  '*(nest_level+1)
                dir_str +=f'- {file_or_dir.name} (file, size={file_or_dir.size})'
            elif isinstance(file_or_dir, Directory):
                dir_str += '  '*(nest_level+1)
                dir_str += self.find_direct_directory(file_or_dir.path).__dir_str(nest_level+1)
        

        return dir_str


    def __str__(self) -> str:
        return self.__dir_str(0)