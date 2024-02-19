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
        ; probleme adunari byte 7
    
        mov AL, [a] ; incarca [a] in registrul AL
        mov BL, [b] ; incarca [b] -----||----- BL
        mov CL, [c] ; incarca [c] -----||----- CL
        mov DL, [d] ; incarca [d] -----||----- DL
        
        ; c-(d+d+d)+(a-b), byte
        ; 10 - (1 + 1 + 1) + (5 - 3) = 10 - 3 + 2 = 9
        
        add DL, [d]
        add DL, [d] ; aduna in DL, [d] de doua ori pentru a forma (d + d + d)
        sub AL, BL ; scade din AL = [a], BL = [b] pentru a calcula (a - b)
        
        sub CL, DL ; scade din CL = [c], DL = (d + d + d)
        add CL, AL ; scade din CL = c - (d + d + d), AL = (a - b)
        
        ; exit(0)
        push    dword 0
        call    [exit]