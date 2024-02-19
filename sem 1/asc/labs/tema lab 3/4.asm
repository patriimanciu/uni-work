; Write a program in assembly language which computes one of the following arithmetic expressions, considering the following domains for the variables: 
; a - byte, b - word, c - double word, d - qword - Interpretare cu semn
;     (a + b - c) + (a + b + d) - (a + b)

bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 2
    b dw 15
    c dd 125
    d dq 80
    
segment code use32 class=code
    start:
        mov al, [a]
        cbw
        add ax, [b]
        cwd
        ; doubled the value
        sub ax, word[c]
        sbb dx, word[c + 2]
        push dx
        push ax
        pop ebx
        ; ebx = a + b - c
        mov al, [a]
        cbw
        add ax, [b]
        cwd
        push dx
        push ax
        pop eax
        cdq
        add eax, dword[d]
        adc edx, dword[d + 4]
        
        add eax, ebx
        adc edx, 0
        
        ; edx:eax = (a + b - c) + (a + b + d)
        mov ebx, eax
        mov ecx, edx
        ; ecx:ebx = (a + b - c) + (a + b + d)
        
        mov al, [a]
        cbw
        add ax, [b]
        cwd
        push dx
        push ax
        mov eax, ebx
        pop ebx
        mov edx, ecx
        add eax, ebx
        adc edx, 0
        
        push   dword 0 
        call   [exit]