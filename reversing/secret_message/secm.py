with open('secretMessage.enc','rb') as f_in, open('secretMessage.raw', 'wb') as f_out:
    output=bytearray()
    byte=f_in.read(1)
    prev=byte[0]
    output.append(prev)
    while True:
        byte=f_in.read(1)
        if not byte:
            break
        cur=byte[0]
        output.append(cur)
        if prev==cur:
            count=f_in.read(1)
            count=count[0]
            for _ in range(count):
                output.append(cur)
            prev=-1
        else:
            prev=cur
    f_out.write(output)
    pass