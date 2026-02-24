from scripts.flags.parser import Parser
from scripts.io.crypt import Crypt
from scripts.io.file  import File

from pathlib import Path

class Core:
    def __init__(self):
        self.home = f"{Path.home()}/.lockup"

        self.file_data = None
        self.token = None
        self.key = None

        self.parser = Parser("lockup")
        self.crypt  = Crypt(self.key)
        self.file   = File(self.parser.input, self.parser.output, self.home)

    def run(self):
        if self.parser.input:
            self.file_data = self.file.read_file_data()

        if self.parser.encrypt:
            if self.parser.key:
                self.crypt.key = self.parser.key

            self.token = self.crypt.encrypt(self.file_data).decode()

            if not self.parser.output:
                self.file.save_encrypted_data_auto(data=self.token, key=self.crypt.key)

        if self.parser.decrypt:
            if self.parser.key:
                self.token = self.crypt.decrypt(self.file_data) 

            if self.parser.decrypt != "":
                self.file.restore_encrypted_data(self.parser.decrypt, self.crypt)

        if self.parser.generate_key:
            print(f"Key= {self.crypt.generate_key.decode()}")

        if self.parser.output:
            self.file.save_encrypted_data(self.token)

        if self.parser.verbose:
            self.file.display_operation_details(self.crypt)

        if self.parser.show_ids:
            pass

if __name__ == "__main__":
    Core().run()
