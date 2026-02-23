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
    
    def gen_id(self):
        # this function generate a random number for the name and id of the file 
        # and then it will check if it is not already choosen then it would return 
        # if it is it would return None
        self.id = int(random.random() * 100000)

        # load up all of the ids 
        for name in os.listdir(self.base_path):
            if "_" in name:
                self.ids.append(name[:name.index("_")])

        return self.id if self.id not in self.ids else None

    def read(self):
        if os.path.isfile(self.input_path):
            file = open(self.input_path)
            return file.read()

    def save(self, content):
        with open(self.output_path, "w") as file:
            file.write(content)

    def auto_save(self, data, key, type="enc", ):
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
            with open(f"{self.base_path}/keys.txt", "a") as keys_file:
                keys_file.write(f"{self.date.strftime("%Y_%m_%d")}::{self.date.strftime("%H_%M_%S")}::{self.gen_id()}::{key.decode()}\n")

            with open(f"{self.base_path}/store/{self.gen_id()}_enc.txt", "w") as cipher_file:
                cipher_file.write(data)
        
        if type == "dec":
            with open(f"{self.base_path}/store/{self.gen_id()}_dec.txt", "w") as data_file:
                data_file.write(data)
