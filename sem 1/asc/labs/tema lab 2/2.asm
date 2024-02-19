bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data  
    
segment code use32 class=code
    start:
        ; problema 22 simpla -> 16/4
        
        mov AX, 16
        mov BL, 4
        div BL
        
        ; exit(0)
        push    dword 0
        call    [exit]