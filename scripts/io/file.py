import os

class File:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def read(self):
        if os.path.isfile(self.input_path):
            file = open(self.input_path)
            return file.read()

    def save(self, content):
        with open(self.output_path, "w") as file:
            file.write(content)
