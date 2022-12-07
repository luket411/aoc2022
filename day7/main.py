from data import practice, full_data
from os.path import join as path_join, dirname

class Folder():
    def __init__(self, location, name, *contents):
        self.path = path_join(location, name)
        self.location = location
        self.name = name
        self.contents = list(contents)

    def ls(self):
        print(self.contents)

    def __str__(self):
        return f"dir:'{self.path}'"

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
        print(self)
        for folder in self.get_folders():
            folders += folder.get_all_folders()

    def add_object(self, object):
        if self.path in object.location:
            if self.path == object.location:
                self.contents.append(object)
            else:
                remaning_path = object.location.strip(self.path)
                found_next_directory = False
                for folder in self.get_folders():
                    if found_next_directory := (folder.name == remaning_path.split("/")[0]):
                        folder.add_object(object)
                        break
                if not found_next_directory:
                    raise Exception(f"Cannot find path {remaning_path} in {self.path}")

        else:
            raise Exception(f"Cannot add object with path {object.path} to {self.path}")


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

def build_dir(dataset=practice):
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


if __name__ == "__main__":
    top_dir = build_dir()
    top_dir.ls()
    print(list(top_dir.get_folders()))
    # print(top_dir.get_all_folders())
