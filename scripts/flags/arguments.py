import argparse


class Arguments:
    def __init__(self,name):
        self.parser = argparse.ArgumentParser(
                prog=name,
        )
        self.io = self.parser.add_argument_group("Input/Output")
        self.mode = self.parser.add_argument_group("Modes")

    def arguments(self):
        self.io.add_argument(
                "-p", "--path",
                help="path for the file/folder", 
                metavar="", 
        )
        self.io.add_argument(
                "-s", "--save",
                help="where to save file/folder", 
                metavar="", 
        )
        self.io.add_argument(
                "-k", "--key",
                help="use a custom key", 
                metavar="", 
        )
        self.io.add_argument(
                "-as", "--auto-save",
                help="after running if included will save the data to the .lockup file",
                action="store_true",
        )
        self.mode.add_argument(
                "-e", "--encrypt",
                help="encrypt the given data if used", 
                action="store_true",
        )
        self.mode.add_argument(
                "-d", "--decrypt",
                help="decrypt the given data using a key", 
                action="store_true",
        )
        self.mode.add_argument(
                "-g", "--generate-key",
                help="generates a 32 url-safe base64-encoded bytes key",
                action="store_true",
        )

    def get(self):
        self.arguments()
        return self.parser.parse_args()
