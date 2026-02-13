from cryptography.fernet import Fernet


class Crypt:
    def __init__(self, key=None) -> None:
        self.key = key.encode() if key else Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def get_key(self, type=None):
        return self.key if type == "encode" else self.key.decode()

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt(self, token, key):
        return Fernet(key).decrypt(token).decode()
