from pwn import *
table=[None]*64
#테이블 복원
with open('text_in.txt', 'rb') as f_in, open('text_out.txt','rb') as f_out:
    while True:
        v11=f_in.read(3)
        idx=[]
        if not v11:
            break
        if len(v11)==3:
            v8=f_out.read(4)
            idx.append(v11[0]>>2)
            idx.append(((v11[0]<<4)&0x30)|(v11[1]>>4))
            idx.append(((v11[1]<<2)&0x3C)|(v11[2]>>6))
            idx.append(v11[2]&0x3F)
            for i in range(4):
                table[idx[i]]=v8[i]
        elif len(v11)==2:
            v8=f_out.read(3)
            idx.append(v11[0]>>2)
            idx.append(((v11[0]<<4)&0x30)|(v11[1]>>4))
            idx.append(((v11[1]<<2)&0x3C))
            for i in range(3):
                table[idx[i]]=v8[i]
        elif len(v11)==1:
            v8=f_out.read(2)
            idx.append(v11[0]>>2)
            idx.append(((v11[0]<<4)&0x30))
            for i in range(2):
                table[idx[i]]=v8[i]

print(table)
char_table="".join([chr(c) for c in table if c is not None])
print(char_table)

#플래그 디코딩
reverse_table={chr(value): index for index, value in enumerate(table) if value is not None}
reverse_table['=']=0
flag=bytearray()
with open('flag_out.txt','r') as f:
    flag_out=f.read().strip()

for i in range(0,len(flag_out),4):
    chunk=flag_out[i:i+4]

    idx1=reverse_table[chunk[0]]
    idx2=reverse_table[chunk[1]]

    flag.append(((idx1<<2)|idx2>>4))

    if chunk[2] != '=':
        idx3=reverse_table[chunk[2]]
        flag.append((((idx2&0b1111)<<4)|idx3>>2))

    if chunk[3] != '=':
        idx4=reverse_table[chunk[3]]
        flag.append((((idx3&0b11)<<6)|idx4))

print(flag.decode())