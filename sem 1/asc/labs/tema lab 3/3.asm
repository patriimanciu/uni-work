; Write a program in assembly language which computes one of the following arithmetic expressions, considering the following domains for the variables: 
; a - byte, b - word, c - double word, d - qword - Interpretare cu semn
;     b+c+d+a-(d+c)

bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 2
    b dw 15
    c dd 125
    d dq 80
    
segment code use32 class=codes
    start:
        mov al, [a]
        cbw 
        add ax, [b]
        cwd ; dx:ax = b
        add ax, word[c]
        adc dx, word[c + 2]
        
        push dx
        push ax
        pop eax
        
        cdq ; eax -> edx:eax
        
        add eax, dword[d]
        adc edx, dword[d + 4]
        ; edx:eax = b+c+d+a
        
        mov ebx, [d]
        mov ecx, [d + 4]
        
        add ebx, [c]
        adc ecx, 0
        
        sub eax, ebx
        sbb edx, ecx
        
        
        
        push   dword 0 
        call   [exit]