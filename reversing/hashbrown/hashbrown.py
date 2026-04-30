from hashlib import md5
from pwn import *
# C 코드의 v8 배열에 있던 64비트 정수 값들
# 이 값들을 리틀 엔디안 바이트로 변환하여 목표 해시 생성
v8_values = [
    0xFE5D3A093968D02B, 0xBA0AA367C2862EAE,  # Chunk 1
    0x8BEA2ADA9E26604F, 0x2E6F41C96DCF5224,  # Chunk 2
    0x7FD91BD2949B75F3, 0x05B1ED8E6072F3A6,  # Chunk 3
    0xC94045C6D4887611, 0x9D43DF6DF6B94D95,  # Chunk 4
    0xB9A8A83C8AC08D80, 0x6D78E80376518464,  # Chunk 5
    0x0E81A20F2023C2D0, 0x2E41EAE69D89F186,  # Chunk 6
    0x425C831DD2A3E5FD, 0x82788DBBDC4100EC,  # Chunk 7
    0x6D0FEE8D3901DD20, 0xEBE82A0A41E5D783,  # Chunk 8
    0x2AFA26414B72E506, 0xD1848E9C21D114D,   # Chunk 9
]

chars = range(32,127)
flag=''
for i in range(9):
    hash=p64(v8_values[i*2])+p64(v8_values[i*2+1])
    for j in chars:
        for k in chars:
            for l in chars:
                temp=chr(j)+chr(k)+chr(l)
                if hash == md5(temp.encode()).digest():
                    flag+=temp
print(flag)