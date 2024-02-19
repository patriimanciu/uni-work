bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a dw 103h
    b dw 51Ah
    c dw 10Ah
    d dw 105h
    
segment code use32 class=code
    start:
        ; problema 22 adunari word
        ; (b-a)-(c+c+d)
        
        mov AX, [a]
        mov BX, [b]
        mov CX, [c]
        mov DX, [d]
        
        sub BX, AX ; BX = b - a
        add CX, CX ; CX = c + c
        add CX, DX ; CX = c + c + d
        sub BX, CX ; BX = (b - a) - (c + c + d)
        
        ; exit(0)
        push    dword 0
        call    [exit]