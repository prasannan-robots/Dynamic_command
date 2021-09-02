Dynamic_enc is a package which uses rolling encryption key.

## Installation
```$ pip install dynamic_enc```

## How it works
Consider two keys and for our convenience let's consider them as previous key and current key<br><br>
The encrypter returns an encrypted string of three parameters
1. hashed Current key encrypted by previous key
1. New key encrypted by previous key
1. Data(needs to be sent) encrypted by New key

The whole string is encrypted in current key

eg . '1,2,3' (these 1 ,2, 3 are the above list)

## Methods
1. You have to initialize the module with your custom previous and current key  eg. ```object = dyno_encrpter(key) #(Key must be an array)```
1. You can later reassign keys with ```assign_key(keys)```
1. ```encrypt(data)``` This method is uses the method above to encrypt your data
1. ```decrypt(data)``` This method is uses the method above to decrypt your data
1. ```get_current_keys()``` Will return the current keys in use
1. ```generate_key()``` This method will help to generate keys( you can use it for initialization)

## Examples
```
from dynamic_enc import *

keys = dyno_encrypter.generate_keys()
encryption_object = dyno_encrypter(keys)

encrypted_data = encryption_object.encrypt("Hello")
decrypted_data = encryption_object.decrypt(encrypted_data)

current_keys = encryption_object.get_current_keys()

print(encrypted_data,decrypted_data,current_keys)
```

Enjoy!!!