from cryptography.fernet import Fernet


class Crypt:
    def __init__(self, key=None) -> None:
        self.key = key.encode() if key else Fernet.generate_key()
        self.token = Fernet(self.key)

    def get_key(self, type=None):
        return self.key if type == "encode" else self.key.decode()

    def encrypt(self, token):
        return self.token.encrypt(token.encode())

    def decrypt(self, token):
        return self.token.decrypt(token).decode()

    def generate_key(self):
        return Fernet.generate_key()
