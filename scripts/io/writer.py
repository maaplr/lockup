import os


class Writer:
    def run(self, path, content="This is the default message"):
        with open(path, "w") as file:
            file.write(content)

Writer().run("/home/zero/this_is_fine")
