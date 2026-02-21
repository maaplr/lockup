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
                "-i", "--input",
                help="input file path", 
                metavar="", 
        )
        self.io.add_argument(
                "-o", "--output",
                help="output file path", 
                metavar="", 
        )
        self.io.add_argument(
                "-k", "--key",
                help="use a custom key", 
                metavar="", 
        )
        self.io.add_argument(
                "-a", "--auto",
                help="auto-save key and data to .lockup",
                action="store_true",
        )
        self.io.add_argument(
                "-v", "--verbose",
                help="show detailed information about the operation", 
                action="store_true",
        )

        self.mode.add_argument(
                "-e", "--encrypt",
                help="encrypt the given data", 
                action="store_true",
        )
        self.mode.add_argument(
                "-d", "--decrypt",
                help="decrypt the given data using a key", 
                action="store_true",
        )
        self.mode.add_argument(
                "-g", "--generate-key",
                help="generate a new decoded 32-byte encryption key (base64-url-safe format)",
                action="store_true",
        )

    def get(self):
        self.arguments()
        return self.parser.parse_args()
