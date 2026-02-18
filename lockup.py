from scripts.flags.parser import Parser
from scripts.io.file  import File
from scripts.io.crypt import Crypt
from pathlib import Path

import os

class Core:
    def __init__(self):
        self.parser = Parser(
            "lockup",
        )
        self.file   = File(
            self.parser.path or None,
            self.parser.save or None
        )
        self.crypt  = Crypt(
            self.parser.key or None,
        )

        # HOME
        self.base_path = f"{Path.home()}/.lockup"
        # -p
        if self.parser.path:
            self.read_file = self.file.read()
        
    ### Flags functionality

    def crypting(self):
        # -e |  encrypt data using a key
        if self.parser.encrypt:
            self.token = self.crypt.encrypt(self.read_file).decode()
        
        # -d | decrypt data using a key as input
        if self.parser.decrypt:
            self.token = self.crypt.decrypt(self.read_file) 

        # -g | generate random key and prints it
        if self.parser.generate_key:
            print(f"Key: {self.crypt.generate_key.decode()}")

    def storing(self):
        # manual saving both for keys and file
        # -s
        if self.parser.save:
            self.file.save(self.token)
            self.showing()

        # -as | auto saving 
        if self.parser.auto_save:
            if not os.path.exists(self.base_path):
                os.mkdir(self.base_path)

            if not os.path.exists(f"{self.base_path}/store"):
                os.mkdir(self.base_path)

            # keys
            keys_file = open(f"{self.base_path}/keys.txt", "a")
            keys_file.write(f"[{self.parser.save}] => encryption key => {self.crypt.enc_key}\n")
            self.showing()


    def showing(self):
        Mode = "Encryption" if self.parser.encrypt else "Decryption"
        From = self.parser.path
        To = self.parser.save
        Key = self.crypt.key 

        print(f"Mode : {Mode}")
        print(f"From : {From}")
        print(f"To   : {To}")
        print(f"Key  : {Key.decode()}")

    def run(self):
        self.crypting()
        self.storing()

if __name__ == "__main__":
    Core().run()
