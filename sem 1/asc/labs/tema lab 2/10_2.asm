bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 4h
    b db 5h
    c db 3h
    
segment code use32 class=code
    start:
        ; probleme inmultiri/impartiri a,b,c,d - byte, e,f,g,h - word
        ; (a+(b-c))*3
        ; (4+(5-3))*3
        
        mov AL, [a]
        mov BL, [b]
        sub BL, [c]
        add AL, BL
        mov CL, 3
        mul CL ; AX = AL * 3
        
        
        ; exit(0)
        push    dword 0
        call    [exit]