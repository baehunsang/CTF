flag = [17, 6, 37, 36, 8, 7, 37, 47, 29, 18, 1, 43, 27, 38, 61, 55, 8, 6, 33, 47, 29, 50, 1, 34, 24, 23, 13, 37, 13, 35, 16, 32, 29, 54, 61, 50, 26, 55, 12, 0]
for i in range(0, len(flag)):
    print(str(bin(flag[i])[2:]).zfill(6), end='')

