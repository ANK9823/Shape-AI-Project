import hashlib

txt = "This is my first challenge under Python and Network security bootcamp"
hash_obt = hashlib.md5(txt.encode())
md5_hash = hash_obt.hexdigest()

print(md5_hash)