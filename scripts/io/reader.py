import os


class Reader:
    def run(self, path):
        if os.path.isfile(path):
            file = open(path).read()
            return file.strip()
