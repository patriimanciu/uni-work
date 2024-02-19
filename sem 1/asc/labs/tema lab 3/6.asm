; d-(7-a*b+c)/a-6+x/2; a,c-byte; b-word; d-doubleword; x-qword
; signed

bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 2
    b dw 15
    c db 125
    d dd 80
    x dq 300
    two dd 2
    
segment code use32 class=code
    start:
    mov al, [a]
    cbw
    imul word[b]
    mov bx, ax
    mov ax, 7
    sub ax, bx
    add al, byte[c]
    adc ah, 0
    ; ax = 7-a*b+c
    idiv byte[a]
    
    mov bx, ax
    ; bx = (7-a*b+c) / a
    mov cx, dx
    ; cx = (7-a*b+c) % a
    
    mov eax, [x]
    mov edx, [x + 4]
    idiv dword[two]
    ; eax = x / 2
    ; edx = x % 2
    
    add eax, [d]
    sub ax, bx
    sbb dx, cx
    sub eax, 6
    
    push   dword 0 
    call   [exit]