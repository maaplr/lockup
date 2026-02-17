from cryptography.fernet import Fernet

class Crypt:
    def __init__(self, key=None) -> None:
        self.generate_key = Fernet.generate_key()
        self.key = key.encode() if key else self.generate_key
        self.token = Fernet(self.key)

    def encrypt(self, data):
        return self.token.encrypt(data.encode())

    def decrypt(self, data):
        return self.token.decrypt(data).decode()

    def get_key(self, type=None):
        return self.key if type == "encode" else self.key.decode()
