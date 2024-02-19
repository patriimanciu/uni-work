; Write a program in assembly language which computes one of the following arithmetic expressions, considering the following domains for the variables: 
; a - byte, b - word, c - double word, d - qword - Unsigned representation
;     (a + b + c) - (d + d) + (b + c)

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
        
        add ax, [b]
        mov dx, 0
        
        push dx
        push ax
        pop eax
        
        add eax, [c]
        ; eax = (a + b + c)
        
        mov edx, 0 
        ; unsigned conversion from dword to qword
        
        mov ebx, dword[d]
        mov ecx, dword[d + 4]
        
        add ebx, ebx
        adc ecx, ecx
        ; ecx:ebx = d + d
        
        sub eax, ebx
        sbb edx, ecx
        ; edx:eax = (a + b + c) - (d + d)
        
        mov bx, [b]
        mov cx, 0
        push cx
        push bx
        pop ebx
        add ebx, [c]
        
        add eax, ebx
        adc edx, 0
       
        
        push   dword 0 
        call   [exit]