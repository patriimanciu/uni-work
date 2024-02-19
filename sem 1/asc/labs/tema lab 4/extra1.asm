; Se dau cuvintele A, B si C. Sa se obtina octetul D ca suma a numerelor reprezentate de:
; biţii de pe poziţiile 0-4 ai lui A
; biţii de pe poziţiile 5-9 ai lui B
; Octetul E este numarul reprezentat de bitii 10-14 ai lui C. Sa se obtina octetul F ca rezultatul scaderii D-E.

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw 0111011101010111b
    b dw 1011101111101110b
    c dw 1110101101010100b
    d db 0b
    e db 0b
    f db 0b

; our code starts here
segment code use32 class=code
    start:
        mov ax, [a]
        mov bx, [b]
        
        and ax, 0000000000011111b
        and bx, 0000001111100000b
        mov cl, 5
        ror bx, cl
        add ax, bx
        mov [d], ax
        
        mov ax, [c]
        and ax, 0111110000000000b
        mov cl, 10
        ror ax, cl
        mov [e], ax
        
        mov bl, byte[d]
        sub bl, byte[e]
        mov [f], bx
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
