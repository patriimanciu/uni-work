bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    d dw 2h
    
segment code use32 class=code
    start:
        ; probleme inmultiri/impartiri a, b, c - byte, d - word
        ; [100*(d+3)-10]/d
       
        mov AX, 100
        mov DX, [d] ; DX = d
        add DX, 3 ; DX = d + 3
        mul DX ; DX:AX = AX * DX = 100 * (d + 3)
        sub AX, 10
       
        mov BX, [d] ; BX = d
        
        div BX ; AX ← DX:AX / BX, DX ← DX:AX % BX
        
        ; exit(0)
        push    dword 0
        call    [exit]