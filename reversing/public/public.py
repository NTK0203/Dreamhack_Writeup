p=65287
q=65419
n=4271010253
e=201326609

phi_n=(p-1)*(q-1)
d=pow(e,-1,phi_n)
flag=b''

with open('out.bin','rb') as f_in:
    while True:
        chunk=f_in.read(8)
        if not chunk:
            break
        c=int.from_bytes(chunk,'little')
        m=pow(c,d,n)
        flag += m.to_bytes(4, 'little')

print(flag)