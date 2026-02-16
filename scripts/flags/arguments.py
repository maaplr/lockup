import argparse


class Arguments:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
                prog="lockup",
        )
        self.io = self.parser.add_argument_group("input/output")
        self.mode = self.parser.add_argument_group("Mode")

    def arguments(self) -> None:
        self.io.add_argument(
                "-i", "--input",
                help="path for the file/folder", 
                metavar="", 
        )
        self.io.add_argument(
                "-k", "--key",
                help="set key for decryption/encryption", 
                metavar="", 
        )
        self.io.add_argument(
                "-o", "--output",
                help="path for the file/folder", 
                metavar="", 
        )
        self.mode.add_argument(
                "-enc", "--encrypt",
                help="encrypt the given data if used", 
                action="store_true",
        )
        self.mode.add_argument(
                "-dec", "--decrypt",
                help="decrypt the given data using a key", 
                action="store_true",
        )
        self.mode.add_argument(
                "-gen", "--generate_key",
                help="generates a 32 url-safe base64-encoded bytes key",
                action="store_true",
        )

    def get(self):
        self.arguments()
        return self.parser.parse_args()
