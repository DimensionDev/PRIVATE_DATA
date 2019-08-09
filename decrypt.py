# -*- coding: utf-8 -*-

import os
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=backend)
decryptor = cipher.decryptor()

# key and iv
print(b64encode(key).decode('utf-8'))
print(b64encode(iv).decode('utf-8'))

with open('./encrypted_actpwds.csv', 'r') as plain:
    # decrypt
    joined_ct = ''.join(plain.readlines())
    ct = b64decode(joined_ct)
    pt = decryptor.update(b64decode(joined_ct))

    # write
    decrypted = open('./actpwds.csv', 'w')
    decrypted.write(pt)
