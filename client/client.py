import socket
from cryptography.fernet import Fernet
from hashlib import sha256
import subprocess
import sys
def data_loader():
    arr = []
    file = open(".0903e3ddsda334d3.dasd234342.;sfaf'afafaf[a]]fasd.one","r")
    for i in file.readlines():
        i = i.replace("\n","")
        if i=="\n":
            pass
        else:
            arr.append(i)
    file.close()
    del file
    return arr[0],arr[1]

def literal_eval(array): 
   return array[1:][:-1].split(',')

def create_socket():
    try:
        s = socket.socket()
        return s
    except:
        del s
        create_socket()

def key_changer(previous_passwords,current_passwords):
    file=open(".0903e3ddsda334d3.dasd234342.;sfaf'afafaf[a]]fasd.one","w")
    file.write(previous_passwords)
    file.write("\n")
    file.write(current_passwords)
    file.close()
    del file



def secure_acceptor(s,host,port):
    def validate_socket(s):
        previous_password,current_password = data_loader()
        new_encrypter = Fernet(current_password)
        prev_encrypter = Fernet(previous_password)
        validation_data = sha256(previous_password.encode()).hexdigest()
        s.send(new_encrypter.encrypt(validation_data.encode()))
        sec_val = s.recv(10000)
        if prev_encrypter.decrypt(sec_val).decode() == sha256(current_password.encode()).hexdigest():
            del new_encrypter,prev_encrypter
            return True
        else:
            s.close()
            del s
            return False
            

    def socket_accept(s,host,port):
        while True:
            #try:
                
                s.connect((host,port))
                validataion_s = validate_socket(s)
                if validataion_s == True:
                    data_processing(s)
                    break
                else:
                    break
            #except Exception as e:
             #   print("socket_accept",e)
             #   break
    socket_accept(s,host,port)
def data_processing(conn):
    previous_password,current_password = data_loader()

    def sender(conn,data):
         
        def cur_pass_pre_en():
            previous_password,current_password = data_loader()
            key = Fernet(previous_password)
            current_password = sha256(current_password.encode()).hexdigest()
            data = key.encrypt(current_password.encode())
            del key
            return data

        def new_pass_pre_en():
            previous_password,current_password = data_loader()
            key = Fernet(previous_password)
            new_key = Fernet.generate_key()
            data = key.encrypt(new_key)
            del key
            return data,new_key
        
        
        def sender_head(data):
            previous_password,current_password = data_loader()
            en_key,new_key = new_pass_pre_en()
            da_encry = Fernet(new_key)
            en_con = da_encry.encrypt(data.encode())
            sign = cur_pass_pre_en()
            new_key = new_key.decode()
            key_changer(current_password,new_key)
            data_cap = f"{sign.decode()},{en_key.decode()},{en_con.decode()}"
            
            data_cap_encrp = Fernet(current_password.encode())
            data_cap_en = data_cap_encrp.encrypt(data_cap.encode())
            conn.send(data_cap_encrp.encrypt(str(sys.getsizeof(str(data_cap_en))).encode()))
            conn.send(data_cap_en)
            del data_cap_encrp,da_encry
        sender_head(data)
    def receiver(conn):
        def receiver_head():
            
            previous_password,current_password = data_loader()
            data_k = Fernet(current_password)
            data = str(conn.recv(2048),"utf-8")
            data_length = int(data_k.decrypt(data.encode()).decode())
            data = str(conn.recv(data_length),"utf-8")
            del data_k
            return receiver_data(conn,data)
        def receiver_data(conn,data):
            
            previous_password,current_password = data_loader()
            new_encrypter = Fernet(current_password)
            data = new_encrypter.decrypt(data.encode()).decode()
            data = data.split(",")
            key = Fernet(previous_password)
            
            if key.decrypt(data[0].encode()).decode() == sha256(current_password.encode()).hexdigest():
                del new_encrypter,key
                keys = Fernet(previous_password)
                new_key = keys.decrypt(data[1].encode()).decode()
                del keys
                key_changer(current_password,new_key)
                data_dec = Fernet(new_key)
                datas = data_dec.decrypt(data[2].encode())
                del data_dec               
                return datas 
            else:
                conn.close()
                del s20482048
                s = create_socket(7867)
                socket_accept(s)
        return receiver_head()
    def read_file(file_name):
        arr = []
        file = open(file_name,"r")
        for i in file.readlines():
            arr.append(i)
        file.close()
        del file
        return arr
    def write_file(file_name,data):
        file = open(file_name,"wb")
        file_data = literal_eval(data)
        for i in file_data:
            file.write(i)
        file.close()
        del file
    while True:
        data_to_send = input()
        sender(s,data_to_send)
        print(receiver(conn).decode(),end="")
ip_ad = '127.0.0.1'
s = create_socket()
secure_acceptor(s,ip_ad,7867)