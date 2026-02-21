from .arguments import Arguments

class Parser:
    def __init__(self, name):
        self.args = Arguments(name).get()

    @property
    def input(self):return self.args.input

    @property
    def output(self):return self.args.output

    @property
    def key(self):return self.args.key

    @property
    def auto(self):return self.args.auto

    @property
    def verbose(self):return self.args.verbose

    @property
    def encrypt(self):return self.args.encrypt
    
    @property
    def decrypt(self):return self.args.decrypt

    @property
    def generate_key(self):return self.args.generate_key

