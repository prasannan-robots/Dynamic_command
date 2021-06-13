from cryptography.fernet import Fernet

def string_to_array(array):
   array = array[1:][:-1].split(',')
   print(array)

def write_file(file_name,data):
        file = open(file_name,"w")
        #file_data = string_to_array(data)
        for i in data:
            file.write(i.decode())
            file.write('\n')
        file.close()
        del file


def read_file(file_name):
        arr = []
        file = open(file_name,"rb")
        for i in file.readlines():
            arr.append(i)
        file.close()
        del file
        return arr

first_password = Fernet.generate_key()
second_password = Fernet.generate_key()
write_file("./server/.0903e3ddsda334d3.dasd234342.;sfaf'afafaf[a]]fasd.one",[first_password,second_password])
write_file("./client/.0903e3ddsda334d3.dasd234342.;sfaf'afafaf[a]]fasd.one",[first_password,second_password])
