import os

class File:
    def read(self, path):
        if os.path.isfile(path):
            file = open(path)
            return file.read().strip()

    def write(self, path, content="This is the default message"):
        with open(path, "w") as file:
            file.write(content)
