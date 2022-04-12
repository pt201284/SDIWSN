from __future__ import print_function
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time

key = RSA.generate(3072)
private_key = key.export_key()
file_out = open('private.pem', 'wb')
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open('receiver.pem', 'wb')
file_out.write(public_key)
file_out.close()

plaintext = b"I met aliens in UFO. Here is the map. You can use it for navigation purpose."

start=time.time()
encryption_key = RSA.import_key(open("receiver.pem").read())
cipher_rsa = PKCS1_OAEP.new(encryption_key)
ciphertext = cipher_rsa.encrypt(plaintext)
end=time.time()
elapsed=(end-start)*1000

print("\n Plaintext is: ",plaintext)
print("\n Ciphertext is: ",ciphertext)
print("\n RSA Encryption time: ", elapsed, "ms")


start=time.time()
decryption_key = RSA.import_key(open("private.pem").read())
cipher_rsa1 = PKCS1_OAEP.new(decryption_key)
plaintext = cipher_rsa1.decrypt(ciphertext)
end=time.time()
elapsed=(end-start)*1000

print("\n Plaintext is: ",plaintext)
print("\n RSA Decryption time: ", elapsed, "ms")

