; Two character strings S1 and S2 are given. Obtain the string D which contains all the elements of S1 that do not appear in S2.
; Example:
; S1: '+', '4', '2', 'a', '8', '4', 'X', '5'
; S2: 'a', '4', '5'
; D: '+', '2', '8', 'X'
bits 32 ; assembling for the 32 bits architecture

global start        

extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s1 db '+', '4', '2', 'a', '8', '4', 'X', '5'
    len_s1 equ $-s1
    s2 db 'a', '4', '5'
    len_s2 equ $-s2
    d times len_s1 db 0 ; at most, all elements in s1 do not appear in s2

; our code starts here
segment code use32 class=code
    start:
        mov esi, 0
        mov edi, d
        mov ecx, len_s1
        
        jecxz end
        
        check_char:
            mov al, [s1 + esi]
            mov ebx, 0
            mov edx, s2
            
            in_s2:
                cmp al, [edx]
                je found
                inc edx
                inc ebx
                
                cmp byte[edx], 0 ; checks if we went through all numbers in s2
                jne in_s2
                jmp not_found
            
            found:
                ; don't add it and move to the next element in s1
                inc esi
                jmp check_char
                
            not_found:
                mov [edi], al
                inc edi
        
        loop check_char
        
        
        end:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
