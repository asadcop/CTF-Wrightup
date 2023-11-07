from random import randint
import hashlib
from string import ascii_letters, digits

opts = ascii_letters + digits + '!@#$%&_-+=<>.,?;:[]'

# def get_flag(sz):
#     core = ''.join(opts[randint(0, len(opts) - 1)] for i in range(sz))
#     flag = 'CTF_BD{' + core + '}'
#     with open('flag.txt', 'w') as f:
#         f.write(flag)
# #This function was used to produce the flag
# get_flag(30)

flag = open('flag.txt', 'rb').read()
xored = []

for itr in range(650):
    xor = []
    for c in flag:
        c ^= randint(1, 127)
        xor.append(c)
    xored.append(bytes(xor))

hash = hashlib.sha256(flag).hexdigest()
with open('out.txt', 'w') as f:
    for xor in xored:
        f.write(xor.hex() + '\n')
    f.write(hash)
