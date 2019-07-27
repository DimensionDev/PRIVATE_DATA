# -*- coding: utf-8 -*-

import os
from base64 import b64encode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key =  os.urandom(32)
iv = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=backend)
encryptor = cipher.encryptor()

# key and iv
print(b64encode(key).decode('utf-8'))
print(b64encode(iv).decode('utf-8'))

with open('./actpwds.csv', 'r') as plain:
    # encrypt
    joined_plain = ''.join(plain.readlines())
    ct = encryptor.update(bytearray(joined_plain)) + encryptor.finalize()
    print(b64encode(ct).decode('utf-8'))

    # write
    encrypted = open('./encrypted_actpwds.csv','w')
    encrypted.write(b64encode(ct).decode('utf-8'))

    # validate
    decryptor = cipher.decryptor()
    pt = decryptor.update(ct)
    print(pt)
