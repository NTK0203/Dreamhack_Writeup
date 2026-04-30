from pwn import *
import re
p=remote("host8.dreamhack.games",23140)
#p=process("./prob")

for i in range(10):
    p.recvuntil(b"[INFO] ")
    stat_line=p.recvline().decode()
    stats=re.findall(r'\d+',stat_line)
    hp, str_val, agi, vit, int_val, end_val, dex_val = [int(s) for s in stats]

    b0 = p8(str_val)
    b1 = p8(agi)
    b2 = p8(vit)
    b3 = p8(int_val)
    b4 = p8(end_val)
    b5 = p8(dex_val)
    b6b7 = p16(hp)

    ptr_bytes=b0+b1+b2+b3+b4+b5+b6b7
    ptr_value=u64(ptr_bytes)
    input_list=[]
    while ptr_value>0:
        if ptr_value%2==0:
            ptr_value//=2
            input_list.append('B')
        else:
            ptr_value-=1
            input_list.append('A')
    input_list.reverse()
    input="".join(input_list)
    p.sendlineafter(b'Cast your spell!: ',input.encode())

    #log.info(f"Stage {i+1} spell sent. Waiting for clear confirmation...")
    #p.recvuntil(b"cleared!")
    #log.success(f"Stage {i+1} cleared confirmation received.")

p.recvuntil(b'Take the flag: ')
flag=p.recvline().decode().strip()

log.success(f"flag: {flag}")

p.close()