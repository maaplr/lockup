from scripts.flags.parser import Parser
from scripts.io.file  import File
from scripts.io.crypt import Crypt

from pathlib import Path

import datetime
import random
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

        # -p
        if self.parser.path:
            self.read_file = self.file.read()

        self.date = datetime.datetime.now()
        self.id = random.randint(99999,999999)

    def enc(self):
        # -enc |  encrypt data using a key
        if self.parser.encrypt:
            self.token = self.crypt.encrypt(self.read_file).decode()
            # manual saving both for keys and file
            # -s
            if self.parser.save:
                self.file.save(self.token)
                self.showing()

            # -auto | auto saving 
            if self.parser.auto_save:
                self.base_path = f"{Path.home()}/.lockup"
                if not os.path.exists(self.base_path):
                    os.mkdir(self.base_path)

                if not os.path.exists(f"{self.base_path}/store"):
                    os.mkdir(f"{self.base_path}/store")

                # keys
                keys_file = open(f"{self.base_path}/keys.txt", "a")
                keys_file.write(f"{self.date.strftime("%Y_%m_%d")}::{self.date.strftime("%H_%M_%S")}::{self.id}::{self.crypt.key.decode()}\n")

                data_file = open(f"{self.base_path}/store/{self.id}.txt", "w")
                data_file.write(self.token)
                self.showing()

    def dec(self):
        # -dec | decrypt data using a key as input
        if self.parser.decrypt:
            self.token = self.crypt.decrypt(self.read_file) 

            # -s
            if self.parser.save:
                self.file.save(self.token)
                self.showing()

    def gen(self):
        # -gen | generate random key and prints it
        if self.parser.generate_key:
            print(f"Key: {self.crypt.generate_key.decode()}")
        
    def showing(self):
        Mode = "Encryption" if self.parser.encrypt else "Decryption"
        From = self.parser.path
        To = self.parser.save if not self.parser.auto_save else ".lockup"
        Key = self.crypt.key 

        print(f"Mode : {Mode}")
        print(f"From : {From}")
        print(f"To   : {To}")
        print(f"Key  : {Key.decode()}")

    def run(self):
        # Modes
        self.enc()
        self.dec()
        self.gen()


if __name__ == "__main__":
    Core().run()
