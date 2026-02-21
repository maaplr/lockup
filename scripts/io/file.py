from pathlib import Path
import datetime
import random
import os

class File:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.date = datetime.datetime.now()
        self.id = int(random.random() * 1000000)

    def gen_id(self):
        pass

    def read(self):
        if os.path.isfile(self.input_path):
            file = open(self.input_path)
            return file.read()

    def save(self, content):
        with open(self.output_path, "w") as file:
            file.write(content)

    def auto_save(self, data, key, type="enc", base_path=f"{Path.home()}/.lockup"):
        store_path = os.path.join(base_path, "store")

        if not os.path.exists(base_path):
            os.mkdir(base_path)

        if not os.path.exists(store_path):
            os.mkdir(f"{base_path}/store")

        if type == "enc":
            keys_file = open(f"{base_path}/keys.txt", "a")
            keys_file.write(f"{self.date.strftime("%Y_%m_%d")}::{self.date.strftime("%H_%M_%S")}::{self.id}::{key.decode()}\n")

            data_file = open(f"{base_path}/store/{self.id}_enc.txt", "w")
            data_file.write(data)
        
        if type == "dec":
            data_file = open(f"{base_path}/store/{self.id}_dec.txt", "w")
            data_file.write(data)
