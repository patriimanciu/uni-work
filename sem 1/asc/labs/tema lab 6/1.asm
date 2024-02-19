bits 32 ; assembling for the 32 bits architecture

; Given an array A of words, build two arrays of bytes:  
; - array B1 contains as elements the higher part of the words from A
; - array B2 contains as elements the lower part of the words from A

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    array dw 1432h, 8675h, 0ADBCh, 0702h, 090Ah, 0B0Ch, 0304h, 0506h, 0108h 
    len equ ($-array)/2
    b1 times len db 0
    b2 times len db 0
    index db 0

; our code starts here
segment code use32 class=code
    start:
        mov esi, array
        cld
        mov edi, b1
        mov ecx, len
        jecxz end
        
        move_lower:
            lodsb ; AL = lower part of the word
                  ; inc ESI
            stosb ; [edi] = AL
                  ; inc EDI
            lodsb
        loop move_lower
        
        mov edi, b2
        mov esi, array
        
        mov ecx, len
        jecxz end
        
        move_higher:
            lodsb
            lodsb
            stosb
        loop move_higher
        
        end:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
