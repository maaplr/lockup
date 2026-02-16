from scripts.flags.parser import Parser
from scripts.io.reader import Reader
from scripts.io.crypt import Crypt
from scripts.io.writer import Writer

class Main:
    def __init__(self):
        self.parser = Parser()
        self.reader = Reader()
        self.crypt  = Crypt(self.parser.key if self.parser.key else None)
        self.writer = Writer()
        if self.parser.input:
            self.read_file = self.reader.run(self.parser.input)

    def enc(self):
        if self.parser.encrypt:
            token = self.crypt.encrypt(self.read_file).decode()
            if self.parser.output:
                self.writer.run(self.parser.output, token)
            print(f"Key: {self.crypt.get_key()}")
            print(f"Data:\n{token}")

    def dec(self):
        if self.parser.decrypt:
            token = self.crypt.decrypt(self.read_file) 
            if self.parser.output:
                self.writer.run(self.parser.output, token)
            print(f"Key:{self.crypt.get_key()}")
            print(f"Data:\n{token}")

    def gen(self):
        if self.parser.generate_key:
            print(self.crypt.generate_key().decode())

    def main(self):
        self.enc()
        self.dec()
        self.gen()

Main().main()
