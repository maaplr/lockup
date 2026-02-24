from .arguments import Arguments

class Parser:
    def __init__(self, name):
        self.args = Arguments(name).get()

    def __getattr__(self, name):
        if hasattr(self.args, name):
            return getattr(self.args, name)
