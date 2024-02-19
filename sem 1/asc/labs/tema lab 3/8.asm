; (a*a+b+x)/(b+b)+c*c; a-word; b-byte; c-doubleword; x-qword
; signed

bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a dw 2
    b db 15
    c dd 125
    x dq 300
    twoB dd 0
    
segment code use32 class=code
    start:
    mov ax, [a]
    imul ax
    ; dx:ax = a*a
    push dx
    push ax
    pop ebx
    ; ebx = a*a
    mov al, [b]
    cbw
    cwde
    add ebx, eax
    ; ebx = a*a + b
    
    mov eax, [x]
    mov edx, [x + 4]
    ; edx:eax = x
    
    add ebx, eax
    adc edx, 0
    ; edx:ebx = a*a+b+x
    
    
    mov al, [b]
    add al, [b]
    
    cbw
    cwde
    ; eax = b + b
    
    mov [twoB], eax
    mov eax, ebx
    idiv dword[twoB]
    ; eax = (a*a+b+x)/(b+b)
    ; edx = (a*a+b+x)%(b+b)
    
    mov ebx, eax
    mov ecx, edx
    
    mov eax, [c]
    imul dword[c]
    
    add eax, ebx
    adc edx, ecx 
    
    
    push   dword 0 
    call   [exit]