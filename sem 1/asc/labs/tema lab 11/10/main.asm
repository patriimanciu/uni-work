; Multiple strings of characters are being read.
; Determine whether the first appears as a subsequence in each of the others and give an appropriate message.

bits 32

global start

extern exit, printf, scanf
extern substring
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll

segment data use32 class=data
    str_format db "%s", 0
    first_str resb 101
    current_str resb 101
    message_first db "The first string read was %s", 0
    not_cnt db 0
    message_not db "The first string does NOT appear as a subsequence in each of the others", 0
    message db "The first string does appear as a subsequence in each of the others", 0
    
    
segment code use32 class=code
    start:
        ; read the first string
        push dword first_str
        push dword str_format
        call [scanf]
        add esp, 4*2

        read_loop:
            push dword current_str
            push str_format
            call [scanf]
            add esp, 4*2
            cmp byte[current_str], '0'
            je end_read
            push first_str
            push current_str
            call substring ; puts into eax 0 if the first string is not a substring of the current string, 1 otherwise
            cmp eax, 0
            jne substrings
               mov dword[not_cnt], 1
            substrings:
                jmp read_loop
        end_read:
        
        cmp dword[not_cnt], 0
        jne not_substrings
            push dword message
            call [printf]
            add esp, 4
        
        not_substrings:
            push dword message_not
            call [printf]
            add esp, 4
        push dword 0
        call [exit]