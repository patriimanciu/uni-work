bits 32

global start

extern exit, printf, scanf
extern substring
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll

section data use32 class=data
    str_format db "%s", 0
    first_str resb 101
    buffer resb 101
    len dd 0
    input_len db "how many words: ", 13, 10, 0
    input_text db "Words: ",13,10,0
    first_word db "first word: ", 13, 10, 0
    not_cnt dd 0
    message_not db "The first string does NOT appear as a subsequence in each of the others", 0
    message db "The first string does appear as a subsequence in each of the others", 0

section code use32 class=code
    start:
        push first_word
        call [printf]
        add esp, 4
    
        push dword first_str
        push dword str_format
        call [scanf]
        add esp, 4*2
    
        push input_len
        call [printf]
        add esp, 4
        
        push len
        push str_format
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
        
        reading:
            push ecx
            push buffer
            push str_format
            call [scanf]
            add esp, 4*2
            
            push dword first_str
            push dword buffer
            call substring ; puts into eax 0 if the first string is not a substring of the current string, 1 otherwise
            cmp eax, 0
            jne substrings
               mov dword[not_cnt], 1
            substrings:
            loop reading
        
        cmp dword[not_cnt], 0
        jne not_substrings
            push dword message
            call [printf]
            add esp, 4
            jmp ending
        
        not_substrings:
            push dword message_not
            call [printf]
            add esp, 4
        ending:  
        push dword 0
        call [exit]
