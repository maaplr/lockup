from scripts.flags.parser import Parser
from scripts.io.file  import File
from scripts.io.crypt import Crypt

class Core:
    def __init__(self):
        self.key = None
        self.file_data = None

        self.parser = Parser("lockup")
        self.file   = File(self.parser.input, self.parser.output)
        self.crypt  = Crypt(self.key)

    def read_file_data(self):
        self.file_data = self.file.read()

    def save_file(self):
        self.file.save(self.token)

    def set_key(self):
        self.key = self.parser.key

    def save_file_auto(self):
        self.file.auto_save(data=self.token, key=self.crypt.key)

    def verbose(self):
        Mode = "Encryption" if self.parser.encrypt else "Decryption"
        From = self.parser.input
        To = self.parser.output if not (self.parser.auto and self.parser.output) else ".lockup"
        Key = self.crypt.key 

        print(f"Mode : {Mode}")
        print(f"From : {From}")
        print(f"To   : {To}")
        print(f"Key  : {Key.decode()}")

    def enc(self):
        self.token = self.crypt.encrypt(self.file_data).decode()

    def dec(self):
        self.token = self.crypt.decrypt(self.file_data) 

    def gen(self):
        print(f"Key: {self.crypt.generate_key.decode()}")
        

    def run(self):
        # -i
        if self.parser.input:
            self.read_file_data()

        # -o
        if self.parser.output:
            self.save_file()

        # -k
        if self.parser.key:
            self.set_key()

        # -a
        if self.parser.auto:
            self.save_file_auto()

        # -v
        if self.parser.verbose:
            self.verbose()

        # -e
        if self.parser.encrypt:
            self.enc()

        # -d
        if self.parser.decrypt:
            self.dec()

        # -g
        if self.parser.generate_key:
            self.gen()


if __name__ == "__main__":
    Core().run()
