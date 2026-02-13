import argparse


class Arguments:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
                prog="lockup",
        )

    def arguments(self):
        self.parser.add_argument(
                "-p", "--path",
                help="path for the file/folder", 
                metavar="", 
                required=True,
        )

    def get(self):
        self.arguments()
        return self.parser.parse_args()
