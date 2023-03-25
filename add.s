.intel_syntax noprefix

.global _start

.data

pos_str:
    .ascii "Result is positive.\n"
pos_str_len = . - pos_str

neg_str:
    .ascii "Result is negative.\n"
neg_str_len = . - neg_str

.text

_start:
    # 산술 연산 (a + b) a는 rax, b는 rdx에 저장할것
    ??? # a = 5
    ??? # b = -3
    ??? # c = a + b

    ??? # 분기 연산 (c >= 0 ? positive : negative)
    ??? # if (c >= 0) goto is_positive

is_negative:
    # sys_write (1) system call: Write negative message
    mov rax, 1
    mov rdi, 1
    lea rsi, [rip + neg_str]
    mov rdx, neg_str_len
    syscall

    jmp exit

is_positive:
    # sys_write (1) system call: Write positive message
    mov rax, 1
    mov rdi, 1
    lea rsi, [rip + pos_str]
    mov rdx, pos_str_len
    syscall

exit:
    # sys_exit (60) system call
    mov rax, 60
    xor rdi, rdi
    syscall
