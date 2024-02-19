bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 4h
    b db 3h
    c db 5h
    d dw 0bh
    
segment code use32 class=code
    start:
        ; probleme inmultiri/impartiri a, b, c - byte, d - word
        ; [(10+d)-(a*a-2*b)]/c
        ; [(10+10)-(4*4-2*3)]/5 = [21-(16-6)]/5 = 11 / 5 = 2 -> 11 % 5 = 1
        add word [d], 10 ; [d] = d + 10
        mov DX, [d] ; DX = d
        
        mov AL, [b]
        mov CL, 2
        mul CL ; AX = b * 2
        mov BX, AX ; save the data from AX => BX = b * 2
        mov AX, 0 ; clear AX
        
        mov AL, [a]
        mul AL ; AX = a * a
        sub AX, BX ; AX = a*a-2*b
        
        sub DX, AX ; DX = (10+d)-(a*a-2*b)
        mov AX, DX ; pentru division
        
        mov CL, [c]
        
        div CL ; AL = AX / CL = 2, AH = AX % CL = 1
        
        ; exit(0)
        push    dword 0
        call    [exit]