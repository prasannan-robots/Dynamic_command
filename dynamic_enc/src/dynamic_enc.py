# Code is written by prasannan-robots

from cryptography.fernet import Fernet
from hashlib import sha256

# This is the class for dyno Encryptor
class dyno_encrypter:
    
    # Initializes class
    def __init__(self,keys):
        self.previous_password = keys[0]
        self.current_password = keys[1]
        self.current_password_send = keys[1]
        self.previous_password_send = keys[0]
    
    # Useful for assigning keys later
    def assign_key(self,keys):
        self.previous_password = keys[0]
        self.current_password = keys[1]
        self.current_password_send = keys[0]
        self.previous_password_send = keys[1]
    
    # to change keys for decryptor
    def key_changer(self,current_password,new_key):
        self.current_password = new_key
        self.previous_password = current_password

    # to change keys for encrptor
    def key_changer_send(self,current_password,new_key):
        self.current_password_send = new_key
        self.previous_password_send = current_password
    
    # Encryption function takes data in
    def encrypt(self,data):
        def cur_pass_pre_en():
            previous_password = self.previous_password_send
            current_password = self.current_password_send
            key = Fernet(previous_password)
            current_password = sha256(current_password).hexdigest()
            data = key.encrypt(current_password.encode())
            del key
            return data

        def new_pass_pre_en():
            previous_password = self.previous_password_send
            current_password = self.current_password_send
            key = Fernet(previous_password)
            new_key = Fernet.generate_key()
            data = key.encrypt(new_key)
            del key
            return data,new_key
        
        
        def sender_head(data):
            previous_password = self.previous_password_send
            current_password = self.current_password_send
            en_key,new_key = new_pass_pre_en()
            da_encry = Fernet(new_key)
            en_con = da_encry.encrypt(data.encode())
            sign = cur_pass_pre_en()
            new_key = new_key.decode()
            self.key_changer_send(current_password,new_key)
            data_cap = f"{sign.decode()},{en_key.decode()},{en_con.decode()}"
            
            data_cap_encrp = Fernet(current_password)
            data_cap_en = data_cap_encrp.encrypt(data_cap.encode())
            return data_cap_en
        data = sender_head(data)
        return data
        
    def decrypt(self,data_k):
       
        def receiver_head(data):
            previous_password = self.previous_password
            current_password = self.current_password
            new_encrypter = Fernet(current_password)
            data = new_encrypter.decrypt(data).decode()
            data = data.split(",")
            key = Fernet(previous_password)
            
            if key.decrypt(data[0].encode()).decode() == sha256(current_password).hexdigest():
                del new_encrypter,key
                keys = Fernet(previous_password)
                new_key = keys.decrypt(data[1].encode()).decode()
                del keys
                self.key_changer(current_password,new_key)
                data_dec = Fernet(new_key)
                datas = data_dec.decrypt(data[2].encode())
                del data_dec               
                return datas.decode()
            else:
                raise Exception("Password mismatch Current password doesn't meet the input")
        return receiver_head(data_k)
    
    def get_current_keys(self):
        return self.previous_password, self.current_password
    
    def generate_keys():
        first_password = Fernet.generate_key()
        second_password = Fernet.generate_key()
        key = [first_password,second_password]
        return key
