from scripts.flags.parser import Parser
from scripts.io.file import File
from scripts.io.crypt import Crypt

class Lockup:
    def __init__(self):
        self.parser = Parser()
        self.file   = File()
        self.crypt  = Crypt(self.parser.key if self.parser.key else None)

        if self.parser.path:
            self.read_file = self.file.read(self.parser.path)

    # Modes 1.
    def enc(self):
        if self.parser.encrypt:
            token = self.crypt.encrypt(self.read_file).decode()
            if self.parser.save:
                self.file.write(self.parser.save, token)
            print(f"Key: {self.crypt.get_key()}")

    # Modes 2.
    def dec(self):
        if self.parser.decrypt:
            token = self.crypt.decrypt(self.read_file) 
            if self.parser.save:
                self.file.write(self.parser.save, token)
            print(f"Key:{self.crypt.get_key()}")

    # Modes 3.
    def gen(self):
        if self.parser.generate_key:
            print(f"Key: {self.crypt.generate_key.decode()}")

    def run(self):
        self.enc()
        self.dec()
        self.gen()

if __name__ == "__main__":
    Lockup().run()
