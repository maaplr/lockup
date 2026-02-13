from .arguments import Arguments


class Parse:
    def __init__(self):
        self.args = Arguments()

    @property
    def path(self):
        return self.args.get().path
