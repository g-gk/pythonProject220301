files = {}


class System:
    def add_directory(self, name):
        directories = name.split('/')
        while len(directories) != 1:
            if directories[0] in list(files.keys()):
                files[directories[0]].append(directories[1])
            else:
                files[directories[0]] = [directories[1]]
            del directories[0]
        files[directories[0]] = []

    def print_directory(self, name):
        print(files[name])


class File:
    def __init__(self):
        self.filecontents = {}

    def add_file_content(self, name, text):
        if name in list(self.filecontents.keys()):
            self.filecontents[name] = text
        else:
            road = name.split('/')
            files[road[-2]].append(road[-1])
            self.filecontents[name] = text

    def print_file_content(self, name):
        print(self.filecontents[name])