from dyno import dyno_encrypter as dyno

keys = dyno.generate_key()

enc_obj = dyno(keys)

encrypted_text = enc_obj.encrypt("Hi")
print(enc_obj.get_current_keys())
decrypted_text = enc_obj.decrypt(encrypted_text)
print(enc_obj.get_current_keys())
print(decrypted_text)