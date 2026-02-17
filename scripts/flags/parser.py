from .arguments import Arguments


class Parser:
    def __init__(self):
        self.args = Arguments().get()

    @property
    def path(self):
        return self.args.path

    @property
    def key(self):
        return self.args.key

    @property
    def save(self):
        return self.args.save

    @property
    def encrypt(self):
        return self.args.encrypt
    
    @property
    def decrypt(self):
        return self.args.decrypt

    @property
    def generate_key(self):
        return self.args.generate_key
        
