bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a dw 101h
    b dw 103h
    c dw 10Ah
    d dw 105h
    
segment code use32 class=code
    start:
        ; problema 7 adunari word
        ; (c+c+c)-b+(d-a)
        
        mov AX, [a]
        mov BX, [b]
        mov CX, [c]
        mov DX, [d]
        
        add CX, CX
        add CX, [c] ; CX = c + c + c
        
        sub DX, AX ; DX = d - a
        
        sub CX, BX ; CX = (c + c + c) - b
        add CX, DX ; CX = (c + c + c) - b + (d - a)
        
        ; exit(0)
        push    dword 0
        call    [exit]