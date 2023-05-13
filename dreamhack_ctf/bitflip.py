addr =    0x7f7f6629ad90

for i in range(0, 8):
    print(hex(addr ^ (1 << i)))

