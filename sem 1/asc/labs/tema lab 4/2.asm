; Given the doublewords M and N, compute the doubleword P as follows.
; the bits 0-6 of P are the same as the bits 10-16 of M
; the bits 7-20 of P are the same as the bits 7-20 of (M AND N).
; the bits 21-31 of P are the same as the bits 1-11 of N.

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    m dd 01110111010101110111011101010111b
    n dd 10111110011101110101011110111110b
    p dd 00000000000000000000000000000000b
    result dd 01111011111101110101011101011101b
    

; our code starts here
segment code use32 class=code
    start:
        mov eax, [m]
        mov ebx, [n]
        and ebx, eax
        and eax, 00000000000000011111110000000000b
        mov cl, 10
        ror eax, cl
        
        and ebx, 00000000000111111111111110000000b
        or eax, ebx
        
        mov ebx, [n]
        and ebx, 00000000000000000000111111111110b
        mov cl, 20
        rol ebx, cl
        
        or eax, ebx
        
        mov [p], eax
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
