#problem
```
#!/usr/local/bin/python
from random import getrandbits

p = 2**521 - 1
a = getrandbits(521)
b = getrandbits(521)
print("a =", a)
print("b =", b)

try:
    x = int(input("enter your starting point: "))
    y = int(input("alright, what's your guess? "))
except:
    print("?")
    exit(-1)

r = getrandbits(20)
for _ in range(r):
    x = (x * a + b) % p

if x == y:
    print("wow, you are truly psychic! here, have a flag:", open("flag.txt").read())
else:
    print("sorry, you are not a true psychic... better luck next time")
```
#solve 
```
from pwn import *

conn = remote('be.ax', 31800)

p = 2**521 - 1
a = int(conn.recvline().decode().strip().split('a = ')[1])
b = int(conn.recvline().decode().strip().split('b = ')[1])
x = y = -b * pow(a - 1, -1, p) % p
conn.sendlineafter(b'starting point: ', str(x).encode())
conn.sendlineafter(b'guess? ', str(y).encode())

print(conn.recvline().decode())
```
