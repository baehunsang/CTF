arr = [0x24, 0x27, 0x13, 0x0C6, 0x0C6, 0x13, 0x16, 0x0E6, 0x47, 0x0F5, 0x26, 0x96, 0x47, 0x0F5, 0x46, 0x27, 0x13, 0x26, 0x26, 0x0C6, 0x56, 0x0F5, 0x0C3, 0x0C3, 0x0F5, 0x0E3, 0x0E3, 0, 0, 0, 0, 0]

flag = ''
for k in range(0, 28):
    for i in range(0x0, 0xFF):
        if(16 * i & 0xf0 | (i >> 4) == arr[k]):
            flag += chr(i)
print flag