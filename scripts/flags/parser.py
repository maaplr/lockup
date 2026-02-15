from .arguments import Arguments


class Parser:
    def __init__(self):
        self.args = Arguments().get()

    @property
    def path(self):
        return self.args.path

    @property
    def encrypt(self):
        return self.args.encrypt
    
    @property
    def decrypt(self):
        return self.args.decrypt

    @property
    def output(self):
        return self.args.output

