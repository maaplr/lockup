import argparse


class Arguments:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
                prog="lockup",
        )

    def arguments(self) -> None:
        self.parser.add_argument(
                "-p", "--path",
                help="path for the file/folder", 
                metavar="", 
        )
        self.parser.add_argument(
                "-enc", "--encrypt",
                help="encrypt the given data if used", 
                action="store_true",
        )
        self.parser.add_argument(
                "-dec", "--decrypt",
                help="decrypt the given data using a key", 
                action="store_true",
        )
        self.parser.add_argument(
                "-o", "--output",
                help="path for the file/folder", 
                metavar="", 
        )

    def get(self):
        self.arguments()
        return self.parser.parse_args()
