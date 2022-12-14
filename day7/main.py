from data import practice, full_data
from posixpath import join as path_join, dirname

class Folder():
    def __init__(self, location, name, *contents):
        self.path = path_join(location, name)
        self.location = location
        self.name = name
        self.contents = list(contents)

    def ls(self):
        print(self.contents)

    def __str__(self):
        return f"(path='{self.path}', size={self.getSize()})"

    def __repr__(self):
        return str(self)

    def getSize(self):
        size = 0
        for item in self.contents:
            size += item.getSize()
        return size

    def get_folders(self):
        return (directory for directory in self.contents if type(directory) is Folder)

    def get_all_folders(self):
        folders = [self]
        for folder in self.get_folders():
            folders += folder.get_all_folders()
        
        return folders

    def add_object(self, object):
        if self.path in f"/{object.location}":
            if self.path == object.location:
                self.contents.append(object)
            else:
                remaining_path = object.location[len(self.path):].strip("/")
                found_next_directory = False
                for folder in self.get_folders():
                    if found_next_directory := (folder.name == remaining_path.split("/")[0]):
                        folder.add_object(object)
                        break
                if not found_next_directory:
                    raise Exception(f"Cannot find path {remaining_path} in {self.path}")

        else:
            raise Exception(f"Cannot add object with path /{object.path} to {self.path}")

    def __getattribute__(self, idx):
        try:
            return super().__getattribute__(idx)
        except AttributeError:        
            for item in self.contents:
                if item.name == idx:
                    return item            

class File():
    def __init__(self,location, name, size):
        self.path = path_join(location, name)
        self.location = location
        self.name = name
        self.size = size

    def __str__(self):
        return f"file: (path={self.path}, size={self.size})"

    def __repr__(self):
        return str(self)

    def getSize(self):
        return self.size

def parse_terminal(raw_dataset):
    #history = [[command, [stdout]], ...]
    history = []
    current_command = []
    for line in raw_dataset.split("\n"):
        tokens = line.split(" ")
        if tokens[0] == "$":
            if tokens[1] == "cd":
                current_command = ["cd", tokens[2]]
                history.append(current_command)
            else:
                current_command = ["ls",[]]
                history.append(current_command)
        else:
            current_command[1].append(tokens)

    return history

def build_dir(dataset):
    parsed_terminal = parse_terminal(dataset)
    current_location = ""
    folder = None
    for [command, data] in parsed_terminal:
        if command == "cd":
            if data == "..":
                current_location = dirname(current_location)
            elif data == "/":
                current_location = "/"
                folder = Folder("","/")
            else:
                current_location = path_join(current_location, data)
        else:
            for [size_type, name] in data:
                if size_type == "dir":
                    folder.add_object(Folder(current_location, name))
                else:
                    size = int(size_type)
                    folder.add_object(File(current_location, name, size))
                
    return folder

def part_1(dataset=practice):
    top_dir = build_dir(dataset)
    counter = 0
    for dir in top_dir.get_all_folders():
        if (dir_size := dir.getSize()) <= 100000:
            counter += dir_size
    print(counter)
    
def part_2(dataset=practice):
    top_dir = build_dir(dataset)
    filesystem_size =   70000000
    space_needed =      30000000
    
    desired_space_left = filesystem_size-space_needed
    print(f"desired_space_left: {desired_space_left}")
    
    current_minimum = top_dir
    for dir in top_dir.get_all_folders():
        if top_dir.getSize() - dir.getSize() <= desired_space_left:
            if dir.getSize() < current_minimum.getSize():
                current_minimum = dir
                print(f"new low {dir}")
    
    print(f"final low {current_minimum} {current_minimum.getSize()}")
    return current_minimum.getSize()
    
        
if __name__ == "__main__":
    assert(part_2()==24933642)
    print(part_2(full_data))