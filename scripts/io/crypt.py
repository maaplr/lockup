from cryptography.fernet import Fernet

class Crypt:
    def __init__(self, key=None):
        self.generate_key = Fernet.generate_key()
        self.key = key.encode() if key else self.generate_key

    def encrypt(self, data):
        token = Fernet(self.key)
        return token.encrypt(data.encode())

    def decrypt(self, data):
        token = Fernet(self.key)
        return token.decrypt(data).decode()
