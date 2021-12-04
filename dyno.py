import base64
import os
import random
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class dynos:
    # To store password and salt by the initiation of the class
    def __init__(self,password=None, salt=None, length=None, iterations=None):

        # To store password for generate_key
        if password != None:
            self.password = password

        # To store salt for generate_key
        if salt != None:
            self.salt = salt
        
        # To store length for generate_key
        if length != None:
            self.length = length
        else:
            self.length = 32

         # To store iterations for generate_key
        if iterations != None:
            self.iterations = iterations
        else:
            self.iterations = 390000


    # To generate salt 
    def generate_salt(self, random_no=random.randrange(20, 50, 3)):
        salt = os.urandom(random_no)
        self.salt = salt
        self.random = random_no
        return salt


    # To generate_key
    def generate_key(self, password=None, length=32, iterations=390000, salt=None):
        try:
            if password == None:
                password = self.password
        except AttributeError:
            raise Exception("password not found! Give a password")
        try:        
            if salt == None:
                salt = self.salt
        except AttributeError:
            raise Exception("salt not found! try calling generate_salt before :(")
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=length,
            salt=salt,
            iterations=iterations,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        self.key = key
        return key
    
    # To encrypt message
    def encrypt(self, message, key=None, future_salt=None):
        if key == None:
            key = self.key
        if future_salt == None:
            if "future_salt" in self.__dict__:
                future_salt = self.future_salt
            else:
                future_salt = self.generate_salt()
                self.future_salt = future_salt
            
        combined_messages = f"{future_salt},{message}" # We are combining future salt and message and encrypting it in current salt :0
        fernet_object = Fernet(key)
        encrypted_combined_message = fernet_object.encrypt(combined_messages.encode())
        return encrypted_combined_message
    
    # To decrypt message
    def decrypt(self, encrypted_message, key=None):
        if key == None:
            key = self.key
        fernet_object = Fernet(key)
        decrypted_message = fernet_object.decrypt(encrypted_message).decode()
        decrypted_message = decrypted_message.split(',')#As they are in string seperated by commas"/sad/xs, Secret message"
        future_salt = decrypted_message[0]
        message = decrypted_message[1]
        self.future_salt = future_salt
        return message