from scripts.flags.parser import Parser
from scripts.io.reader import Reader
from scripts.io.crypt import Crypt

class Main:
    def __init__(self):
        self.parser = Parser()
        self.reader = Reader()
        self.crypt  = Crypt()

    def main(self):
        if self.parser.encrypt:
            # parsing the path from the command line
            # then read the file and then encrypt it
            token = self.crypt.encrypt(self.reader.run(self.parser.path))
            print(token.decode())

        if self.parser.decrypt:
            token = self.crypt.encrypt(self.reader.run(self.parser.path))
            key = self.crypt.get_key(type="encode")
            print(self.crypt.decrypt(token, key)) 

Main().main()
