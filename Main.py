from scripts.argument_parser.parse import Parse
from scripts.io_handling.reader import Reader
from scripts.io_handling.crypt import Crypt


class Main:
    def __init__(self):
        self.parsed = Parse()
        self.reader = Reader()
        self.crypt  = Crypt()

    def main(self):
        # parsing the path from the command line then read the file and then encrypt it
        token = self.crypt.encrypt(self.reader.run(self.parsed.path))
        key = self.crypt.get_key(type="encode")

        # encrypted
        print(token)

        print("\n")

        # decrypted
        print(self.crypt.decrypt(token,key)) 




Main().main()
