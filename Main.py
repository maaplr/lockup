from scripts.flags.parser import Parser
from scripts.io.reader import Reader
from scripts.io.crypt import Crypt
from scripts.io.writer import Writer

class Main:
    def __init__(self):
        self.parser = Parser()
        self.reader = Reader()
        self.crypt  = Crypt()
        self.writer = Writer()

    def enc(self):
        if self.parser.encrypt:
            # parsing the path from the command line
            # then read the file and then encrypt it
            token = self.crypt.encrypt(self.reader.run(self.parser.path))
            encrypted = token.decode()
            if self.parser.output:
                self.writer.run(self.parser.output, encrypted)

    def dec(self):
        if self.parser.decrypt:
            token = self.crypt.encrypt(self.reader.run(self.parser.path))
            key = self.crypt.get_key(type="encode")
            decrypted = self.crypt.decrypt(token, key) 
            if self.parser.output:
                self.writer.run(self.parser.output, decrypted)

    def main(self):
        self.enc()
        self.dec()

Main().main()
