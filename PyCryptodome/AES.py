from __future__ import print_function
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import time


key = get_random_bytes(16)
plaintext = b"I met aliens in UFO. Here is the map. You can use it for navigation purpose."
cipher = AES.new(key, AES.MODE_CBC) # Create a AES cipher object with the key using the mode CBC
start=time.time()
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size)) # Pad the input data and then encrypt
end=time.time()
elapsed=(end-start)*1000


with open('cipher_file','wb') as c_file:
    c_file.write(cipher.iv)	
    c_file.write(ciphertext)

print("\n Plaintext is: ",plaintext)
print("\n Ciphertext is (with padding CBC mode): ",ciphertext)
print("\n Average AES128 Encryption time: ", elapsed, "ms")




with open('cipher_file','rb') as c_file:
    iv=c_file.read(16)	
    ciphertext=c_file.read()

cipher1 = AES.new(key, AES.MODE_CBC, iv)
start=time.time()
plaintext = unpad(cipher1.decrypt(ciphertext), AES.block_size) # unpad the input data and then encrypt
end=time.time()
elapsed=(end-start)*1000

print("\n Plaintext is: ",plaintext)
print("\n Average AES128 Decryption time:",elapsed,"ms")

