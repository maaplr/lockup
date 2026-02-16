from .arguments import Arguments


class Parser:
    def __init__(self):
        self.args = Arguments().get()

    @property
    def input(self):
        return self.args.input

    @property
    def key(self):
        return self.args.key

    @property
    def output(self):
        return self.args.output

    @property
    def encrypt(self):
        return self.args.encrypt
    
    @property
    def decrypt(self):
        return self.args.decrypt

    @property
    def generate_key(self):
        return self.args.generate_key
        
