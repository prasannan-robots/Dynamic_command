import dyno

password = "shit"
message = "Blyat!"
encryp = dyno.dynos(password)

key = encryp.generate_key(encryp.generate_salt(10))

print(key)

encrypted_message = encryp.encrypt(message)
print(encrypted_message)

decrypted_messages  = encryp.decrypt(encrypted_message)
print(decrypted_messages)

encrypted_message = encryp.encrypt(decrypted_messages)
print(encrypted_message)

decrypted_messages  = encryp.decrypt(encrypted_message)
print(decrypted_messages)