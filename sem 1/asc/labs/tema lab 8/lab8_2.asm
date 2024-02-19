; Read two numbers a and b (in base 10) from the keyboard and determine the order relation between them (either a < b, or a = b, or a > b). Display the result in the following format: "<a> < <b>, <a> = <b> or <a> > <b>".
bits 32
global start

extern exit, printf, scanf
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll

segment data use32 class=data
    a dd 0
    b dd 0
    format db "%d", 0
    message_a db "a = ", 0
    message_b db "b = ", 0
    
    message_greater db "%d > %d", 0
    message_equal db "%d = %d", 0
    message_less db "%d < %d", 0
    
    
segment code use32 class=code
    start:
        ; print the message for a  
        push dword message_a
        call [printf]
        add esp, 4 * 1
        
        ; read the number a from console
        push dword a       
        push dword format
        call [scanf]       
        add esp, 4 * 2
        
        ; print the message for b 
        push dword message_b
        call [printf]
        add esp, 4 * 1
        
        ; read the number b from console
        push dword b       
        push dword format
        call [scanf]       
        add esp, 4 * 2
        
        mov eax, [a]
        mov ebx, [b]
        cmp eax, ebx
        
        jg greater
            jl less
                push dword [b]
                push dword [a]
                push dword message_equal
                call [printf]
                add esp, 4 * 3
                jmp end
            
            less:
                push dword [b]
                push dword [a]
                push dword message_less
                call [printf]
                add esp, 4 * 3
                jmp end
        
        greater:
            push dword [b]
            push dword [a]
            push dword message_greater
            call [printf]
            add esp, 4 * 3
        end:
        
        push dword[0]
        call [exit]