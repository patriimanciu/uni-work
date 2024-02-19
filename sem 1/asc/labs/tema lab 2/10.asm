bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 4h
    b db 3h
    c db 5h
    d db 7h 
    e dw 2h
    f dw 0bh
    g dw 8h
    h dw 0fh
    
segment code use32 class=code
    start:
        ; probleme inmultiri/impartiri a,b,c,d - byte, e,f,g,h - word
        ; (f*g-a*b*e)/(h+c*d)
        ; (11*8-4*3*2)/50
        ; 64 / 50
        mov AX, [f]
        mov DX, [g]
        mul DX ; DX:AX = f*g
        
        push DX
        push AX
        pop EBX ; EBX = f*g
        
        mov AL, [a]
        mul byte[b] ; AX = a*b
        mul word[e] ; DX:AX = a*b*e
        
        push DX
        push AX
        pop ECX ; ECX = a*b*e
        
        sub EBX, ECX ; EBX = f*g - a*b*e
        
        mov DX, 0 ; clear
        mov AX, 0 ; clear
        
        mov AL, [c]
        mul byte[d] ; AX = c*d
        add AX, [h] ; AX = h+c*d
        
        mov CX, AX ; CX = h+c*d
        
        ; EBX = f*g - a*b*e
        
        push EBX
        pop AX
        pop DX ; DX:AX = f*g - a*b*e
        
        div CX ; DX:AX = (f*g - a*b*e)/CX
        
        
        ; exit(0)
        push    dword 0
        call    [exit]