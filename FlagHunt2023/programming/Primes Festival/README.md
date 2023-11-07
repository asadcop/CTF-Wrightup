# Problem
```#!/usr/local/bin/python
from Crypto.Util.number import getPrime, isPrime
from Crypto.Random.random import getrandbits

print('Welcome to yet another guess my favorite number chall!!!')

st = 1 << 20
primes = []

while len(primes) != 47:
  if isPrime(st):
    primes.append(st)
  st += 1

def ok(x):
  on = bin(x)[2:].count('1')
  return on >= 36

while True:
  secret = getrandbits(46)
  if ok(secret):
    break

hint = 1
for i in range(46):
  if (secret >> i) & 1:
    hint *= primes[i]

p = getPrime(512)
hint %= p

print('I will be generous to give you a hint :', hint, p)
  
num = int(input('Enter my favorite number: '))
if num == secret:
  print(open('flag.txt', 'r').read())
else:
  print("Nope, it's wrong!!")```
# solve
```
from pwn import *
from tqdm import tqdm
from Crypto.Util.number import isPrime

st = 1 << 20
primes = []
while len(primes) != 47:
  if isPrime(st):
    primes.append(st)
  st += 1
  
p1 = primes[:23]
p2 = primes[23:]

io = remote('127.0.0.1', 5000)
io.recvline()
io.recvuntil(b': ')

hint, p = map(int, io.recvline().decode().strip().split(' '))

vals1 = dict()
for mask in tqdm(range(1 << 23)):
  prod = 1
  for i in range(23):
    if (mask >> i) & 1:
      prod = (prod * p1[i]) % p
  vals1[prod] = mask

for mask in tqdm(range(1 << 23)):
  prod = 1
  for i in range(23):
    if (mask >> i) & 1:
      prod = (prod * p2[i]) % p
  need = (hint * pow(prod, -1, p)) % p

  if need in vals1:
    bits = vals1[need]
    ans = (mask << 23) + bits
    print('Secret num:', ans)
    break

io.recvuntil(b': ')
io.sendline(str(ans).encode())
io.interactive()

```
