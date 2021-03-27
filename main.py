import hashlib
file = open('some', 'rb').read()
h = hashlib.md5(file).hexdigest()
print(h)