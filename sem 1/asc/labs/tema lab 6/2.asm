bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; A string of bytes is given. Obtain the mirror image of the binary representation of this string of bytes.
; Example:
; given the byte string
; s DB 01011100b, 10001001b, 11100101b 
; obtain the string
; d DB 10100111b, 10010001b, 00111010b.


; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s db 01011100b, 10001001b, 11100101b 
    len equ $-s
    d times len db 0
    

; our code starts here
segment code use32 class=code
    start:
        mov esi, d
        mov edi, d
        cld
        mov ecx, len
        jecxz end
        
        repeat:
            dec esi
            lodsb ; AL = [esi], esi += 1
            dec esi
            
            xor bl, bl ; bl = 0
            push ecx ; save for later
            mov ecx, 8 ; iterate through all bits of a byte
            
            reverse_byte:
                rcr al, 1 ; rotate one bit at a time and save it into carry flag
                rcl bl, 1 ; move the bit into bl
            loop reverse_byte

            mov al, bl
            stosb 
            pop ecx
        
        loop repeat

        end:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
