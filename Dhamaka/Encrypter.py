import os
from cryptography.fernet import Fernet


class Encrypter:
    def __init__(self):
        self.files = self.files
        self.key = self.key

    def encrypt(self):

        self.files = []

        for file in os.listdir():
            if file == 'key.key' or os.path.basename(__file__):
                continue
            if os.path.isfile(file):
                self.files.append(file)

        print(self.files)
        print('*Note: Do not delete the key.key!! or else the files can never be decrypted!*')

        self.key = Fernet.generate_key()

        with open('key.key', 'wb') as thekey:
            thekey.write(self.key)

        for file in self.files:
            with open(file, 'rb') as thefile:
                contents = thefile.read()
                contents_encrypted = Fernet(self.key).encrypt(contents)
            with open(file, 'wb') as thefile:
                thefile.write(contents_encrypted)

    def decrypt(self):
        self.files = []

        for file in os.listdir():
            if file == 'key.key' or os.path.basename(__file__):
                continue
            if os.path.isfile(file):
                self.files.append(file)

        print(self.files)

        with open('key.key', 'rb') as thekey:
            key = thekey.read()

        for file in self.files:
            with open(file, 'rb') as thefile:
                contents = thefile.read()
                contents_decrypted = Fernet(key).decrypt(contents)
            with open(file, 'wb') as thefile:
                thefile.write(contents_decrypted)
