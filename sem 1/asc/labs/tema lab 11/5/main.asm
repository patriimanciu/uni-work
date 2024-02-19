bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf
extern compute
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

                          
; Read the signed numbers a, b and c on type byte; calculate and display a+b-c.
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 0
    a_str db "a = ", 0
    b db 0
    b_str db "b = ", 0
    c db 0
    c_str db "c = ", 0
    result dw 0
    res_str db "res = ", 0
    format db "%d", 0
    
    

; our code starts here
segment code use32 class=code
    start:
        push a_str
        call [printf]
        add esp, 4
        
        push a
        push format
        call [scanf]
        add esp, 4*2
        
        push b_str
        call [printf]
        add esp, 4
        
        push b
        push format
        call [scanf]
        add esp, 4*2
        
        push c_str
        call [printf]
        add esp, 4
        
        push c
        push format
        call [scanf]
        add esp, 4*2
        
        push dword[c]
        push dword[b]
        push dword[a]
        call compute ; store the result into eax
        mov [result], eax
        
        push res_str
        call [printf]
        add esp, 4
        
        push dword [result]
        push format
        call [printf]
        add esp, 4*2
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
