from pathlib import Path
import datetime
import random
import os

class File:
    def __init__(self, input_path, output_path, base_path=f"{Path.home()}/.lockup"):
        self.input_path = input_path
        self.output_path = output_path
        self.base_path = base_path
        self.date = datetime.datetime.now()
        self.ids = [] # only available when gen_id() func is called

    def listdir(self, path=None):
        # load up all of the ids 
        path = path if path != None else self.base_path
        for name in os.listdir(path):
            if "_" in name:
                self.ids.append(name[:name.index("_")])
    
    def gen_id(self):
        # this function generate a random number for the name and id of the file 
        # and then it will check if it is not already choosen then it would return 
        # if it is it would return None
        id = int(random.random() * 100000)
        self.listdir()
        return id if id not in self.ids else None

    def read(self):
        if os.path.isfile(self.input_path):
            file = open(self.input_path)
            return file.read()

    def save(self, content):
        with open(self.output_path, "w") as file:
            file.write(content)

    def auto_save(self, path, data, key.decode(), type="enc", ):
        # create a .lockup file in the home direcroty 
        # create a store and key.txt inside of it 
        # store data using the generated id by gen_id()
        # in the auto mode will check if it is a enc or dec
        store_path = os.path.join(self.base_path, "store")

        if not os.path.exists(self.base_path):
            os.mkdir(self.base_path)

        if not os.path.exists(store_path):
            os.mkdir(f"{self.base_path}/store")

        # if it needs a header 
        if not os.path.exists(f"{self.base_path}/keys.txt"):
            with open(f"{self.base_path}/keys.txt", "a") as keys_file:
                keys_file.write(f"date::time::id::key\n")

        if type == "enc":
            id = self.gen_id()
            date = self.date.strftime("%Y_%m_%d")
            time = self.date.strftime("%H_%M_%S")
            with open(f"{self.base_path}/keys.txt", "a") as keys_file:
                keys_file.write(f"{date}::{time}::{id}::{key}\n")

            with open(f"{self.base_path}/store/{id}_enc.txt", "w") as cipher_file:
                cipher_file.write(data)
        
        if type == "dec":
            if os.path.exists(path):
                pass

    def verbose(self, parser, crypt):
        # bug for gen key mode it should return nothing
        Mode = "Encryption" if parser.encrypt else "Decryption"
        From = parser.path
        To  = parser.output if not (parser.auto and parser.output) else ".lockup"
        Key = crypt.key 

        print(f"Mode : {Mode}")
        print(f"From : {From}")
        print(f"To   : {To}")
        print(f"Key  : {Key.decode()}")
