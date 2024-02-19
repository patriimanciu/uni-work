bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 4h
    b db 3h
    c db 5h
    d db 0ah
    
segment code use32 class=code
    start:
        ; probleme inmultiri/impartiri a,b,c,d - byte, e,f,g,h - word
        ; (a+b)*(c+d)
        ; (4+3)*(5+10) = 7 * 15 = 105
        mov AL, 0
        mov BL, 0 ; clear
        
        mov AL, [a]
        add AL, [b] ; AL = a + b
        
        mov BL, [c]
        add BL, [d] ; BL = c + d
        
        mul BL ; AX = (a+b)*(c+d)
        
        ; exit(0)
        push    dword 0
        call    [exit]