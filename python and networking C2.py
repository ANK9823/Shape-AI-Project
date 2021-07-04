import hashlib
#print(hashlib.algorithms_available)

msg = "This is my second challenge under Python and Network security bootcamp".encode()

print("BLAKE2c:", hashlib.blake2b(msg).hexdigest())

print("SHA-3-256:", hashlib.sha3_256(msg).hexdigest())

print("SHA-3-512:", hashlib.sha3_512(msg).hexdigest())

