; Write a program in assembly language which computes one of the following arithmetic expressions, considering the following domains for the variables: 
; a - byte, b - word, c - double word, d - qword - Unsigned representation
;     (a + d + d) - c + (b + b)

bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 10
    b dw 2000
    c dd 400000
    d dq 50000000
    
segment code use32 class=code
    start:
        mov al, [a]
        mov ah, 0 ; unsigned conversion from byte to word into AX
        
        mov bx, 0
        
        push bx
        push ax
        pop eax ; unsigned conversion from word into double word
        
        mov edx, 0 ; conversion to quad -> edx:eax = [a]
        
        add eax, [d]
        adc edx, [d + 4]
        
        add eax, [d]
        adc edx, [d + 4]
        
        ; edx:eax = (a + d + d)
        
        mov ebx, [c]
        mov ecx, 0
        
        sub eax, ebx
        sbb edx, ecx
        
        ; edx:eax = (a + d + d) - c
        
        mov bx, [b]
        mov cx, 0
        
        push cx
        push bx
        pop ebx
        
        mov ecx, 0
        
        add eax, ebx
        adc edx, ecx
        
        add eax, ebx
        adc edx, ecx
        
        push   dword 0 
        call   [exit]