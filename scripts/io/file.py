import datetime
import random
import os

class File:
    def __init__(self, input_path, output_path, home):
        self.input_path = input_path
        self.output_path = output_path

        self.home = home
        self.store = os.path.join(self.home, "store")

        self.date = datetime.datetime.now()
        self.dt = self.date.strftime("%Y_%m_%d_%H_%M_%S")

        if self.input_path:
            self.name = os.path.basename(self.input_path)

        self.ids = []

    def _load_existing_ids(self, path=None):
        # load up all of the ids 
        path = path if path != None else self.store
        for name in os.listdir(path):
            if "." in name:
                self.ids.append(name[:name.index(".")])

    def _generate_uniq_id(self):
        # this function generate a random number for the name and id of the file 
        # and then it will check if it is not already choosen then it would return 
        # if it is it would return None
        id = random.randint(1,100000)
        self._load_existing_ids()
        return id if id not in self.ids else None

    def read_file_data(self):
        if os.path.isfile(self.input_path):
            with open(self.input_path) as file:
                return file.read()

    def save_encrypted_data(self, content):
        with open(self.output_path, "w") as file:
            file.write(content)

    def save_encrypted_data_auto(self, data, key):
        # create a .lockup file in the home direcroty 
        # create a store and key.txt inside of it 
        # store data using the generated id by gen_id()
        if not os.path.exists(self.home):
            os.mkdir(self.home)

        if not os.path.exists(self.store):
            os.mkdir(f"{self.home}/store")

        id = self._generate_uniq_id()

        # if it needs a header 
        if not os.path.exists(f"{self.home}/keys.txt"):
            with open(f"{self.home}/keys.txt", "a") as keys_file:
                keys_file.write(f"id::name::date_time::key\n")

        with open(f"{self.home}/keys.txt", "a") as keys_file:
            keys_file.write(f"{id}::{self.name}::{self.dt}::{key.strip()}\n")

        with open(f"{self.home}/store/{id}.txt", "w") as cipher_file:
            cipher_file.write(data)
    
    def restore_encrypted_data(self, id, crypt):
        self._load_existing_ids()

        if id in self.ids:
            with open(f"{self.home}/keys.txt") as keys_file:
                for line in keys_file:
                    if id in line:
                        self.dec_key = line.split("::")[-1]

            with open(f"{self.store}/{id}.txt") as file:
                print(self.dec_key)
                print(crypt.decrypt(file, self.dec_key))

    def display_operation_details(self, crypt):
        # bug for gen key mode it should return nothing
        From = self.input_path
        To  = self.output_path
        Key = crypt.key 

        print(f"From : {From}")
        print(f"To   : {To}")
        print(f"Key  : {Key.decode()}")
