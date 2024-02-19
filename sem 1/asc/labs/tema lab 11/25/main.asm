;Read a string of signed numbers in base 10 from keyboard. 
;Determine the minimum value of the string and write it in the file min.txt (it will be created) in 16 base.
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf, fopen, fclose, fprintf
extern mini
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll 
import printf msvcrt.dll                  
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    format db "%d", 0
    format_hex db "%x", 0
    buffer resb 101
    filename db "min.txt", 0
    access_mode db "w", 0
    file_descriptor dd -1
    len dd 0
    input_len db "how many numbers: ", 13, 10, 0
    input_text db "Numbers: ",13,10,0
    result dd 0

; our code starts here
segment code use32 class=code
    start:
        ; how many numbers are read 
        push input_len
        call [printf]
        add esp, 4
        
        push len
        push format
        call [scanf]
        add esp, 4*2
        
        push input_text
        call [printf]
        add esp, 4

        mov ecx, [len]

        cmp ecx, 0
        jne continue
            jmp ending
        continue:
            ; the first number in the list is considered the minimum
            dec ecx
            push ecx
            
            push buffer
            push format
            call [scanf]
            add esp, 4*2
            mov ebx, [buffer]
            mov [result], ebx
            pop ecx
            
            cmp ecx, 0
            jne continue_further
                jmp almost_ending
            continue_further:
                reading:
                    push ecx
                    push buffer
                    push format
                    call [scanf]
                    add esp, 4*2
                    
                    push dword[result]
                    push dword[buffer]
                    call mini ; sores the minimum into eax and does ret 4*2
                    
                    mov [result], eax
                    pop ecx
                    loop reading
        
        ; push dword[buffer]
        ; push dword format
        ; call [printf]
        ; add esp, 4*2
        
        almost_ending:
            ; does the file handling stuff
            push dword access_mode
            push dword filename
            call [fopen]
            add esp, 4*2            

            mov [file_descriptor], eax  
            cmp eax, 0
            je ending
            
            push dword[result]
            push format_hex
            push dword[file_descriptor]
            call [fprintf]
            add esp, 4*3
            
            push dword [file_descriptor]
            call [fclose]
            add esp, 4
        
        ending:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
