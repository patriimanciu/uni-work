bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    
segment code use32 class=code
    start:
        ; problema 7 simpla -> 256/1
        
        mov DX, 0 ; ne asiguram ca pe DX avem liber
        mov AX, 100h ; pe AL intra pana la 255
        mov BL, 1h ; divident
        div BX ; ca sa incapa 256
        
        
        ; exit(0)
        push    dword 0
        call    [exit]