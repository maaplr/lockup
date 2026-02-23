from scripts.flags.parser import Parser
from scripts.io.crypt import Crypt
from scripts.io.file  import File

class Core:
    def __init__(self):
        self.file_data = None
        self.token = None
        self.key = None

        self.parser = Parser("lockup")
        self.crypt  = Crypt(self.key)

        self.file   = File(self.parser.path, self.parser.output)

    def file_data_read(self):
        self.file_data = self.file.read()

    def verbose(self):
        self.file.verbose(self.parser, self.crypt)

    def key_set(self):
        self.key = self.parser.key
        self.crypt.key = self.key

    def encrypting_data(self):
        self.token = self.crypt.encrypt(self.file_data).decode()

    def decrypting_data(self):
        self.token = self.crypt.decrypt(self.file_data) 

    def generating_key(self):
        print(f"Key= {self.crypt.generate_key.decode()}")

    def file_data_save(self):
        self.file.save(self.token)

    def file_data_save_auto(self):
        self.file.auto_save(path=self.parser.path, data=self.token, key=self.crypt.key)

    def run(self):
        # input 
        if self.parser.path:self.file_data_read()
        if self.parser.verbose:self.verbose()
        if self.parser.key:self.key_set()

        # process 
        if self.parser.encrypt:self.encrypting_data()
        if self.parser.decrypt:self.decrypting_data()
        if self.parser.generate_key:self.generating_key()

        # output
        if self.parser.output:self.file_data_save()
        if self.parser.auto:self.file_data_save_auto()

if __name__ == "__main__":
    Core().run()
