from __future__ import print_function
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC, SHA256
import time

key = get_random_bytes(16)
plaintext = b"I met aliens in UFO. Here is the map. You can use it for navigation purpose."

hmac=HMAC.new(key,plaintext,SHA256)
start=time.time()
digestvalue1=hmac.digest()
end=time.time()
elapsed=(end-start)*1000
print("\n Key:",key)
print("\n Plaintext:",plaintext)
print("\n Message digest:",digestvalue1)
digestvalue2=hmac.hexdigest()
print("\n Message digest in hex:",digestvalue2)
print("\n Size of the digest:",8*hmac.digest_size,"bits")
print("\n HMAC time:",elapsed)

h = SHA256.new(plaintext)
start=time.time()
digestvalue3=h.digest()
end=time.time()
elapsed=(end-start)*1000
print("\n SHA256 digest:",digestvalue3)
digestvalue4=h.hexdigest()
print("\n Digest in hex:",digestvalue4)
print("\n SHA256 time:",elapsed)
