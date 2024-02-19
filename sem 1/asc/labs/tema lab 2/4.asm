bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 5
    b db 3
    c db 10
    d db 1  
    
segment code use32 class=code
    start:
        ; probleme adunari 22
        ; (a+b+b)-(c+d)
        
        mov AL, [a]
        mov BL, [b]
        mov CL, [c]
        mov DL, [d]
        
        add BL, BL ; BL = b + b
        add AL, BL ; AL = a + b + b
        add CL, DL ; CL = c + d
        sub AL, CL ; AL = (a + b + b) - (c + d)
        
        ; exit(0)
        push    dword 0
        call    [exit]