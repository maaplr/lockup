import argparse


class Arguments:
    def __init__(self,name):
        self.parser = argparse.ArgumentParser(
                prog=name,
                formatter_class=argparse.RawDescriptionHelpFormatter,
                epilog="Example: lockup -enc -as -i file.txt"
        )
        self.io = self.parser.add_argument_group("Input/Output")
        self.mode = self.parser.add_argument_group("Modes")

    def arguments(self):
        self.parser.add_argument(
                "-i", "--input",
                help="path for the file", 
                metavar="FILE",
                type=str,
                required=False
        )
        self.io.add_argument(
                "-o", "--output",
                help="output file path", 
                metavar="FILE",
                type=str,
                required=False
        )
        self.io.add_argument(
                "-k", "--key",
                help="encryption/decryption key (if not provided, will be generated)", 
                metavar="KEY", 
                type=str,
                required=False
        )
        self.io.add_argument(
                "-v", "--verbose",
                help="show detailed information about the operation", 
                action="store_true",
                required=False
        )
        self.mode.add_argument(
                "-enc", "--encrypt",
                help="encrypt the given data", 
                action="store_true",
                required=False
        )
        self.mode.add_argument(
                "-dec", "--decrypt",
                help="decrypt the given data using a key", 
                metavar="ID",
                required=False
        )
        self.mode.add_argument(
                "-ids", "--show-ids",
                help="shows all of the ids in .lockup folder and their original path",
                action="store_true",
                required=False,
        )
        self.mode.add_argument(
                "-gen", "--generate-key",
                help="generate a new decoded 32-byte encryption key (base64-url-safe format)",
                action="store_true",
                required=False
        )

    def get(self):
        self.arguments()
        return self.parser.parse_args()
