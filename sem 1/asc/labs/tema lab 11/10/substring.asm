bits 32

global substring

extern printf
import printf msvcrt.dll

segment data use32 class=data
    message db "The first read string appears as a subsequence in each of the substrings read afterwards"
    
segment code use32 public code
    substring:
        ; find the length of the first string
        mov esi, [esp+8]
        mov edi, [esp+4]
        
        mov ecx, 0
        find_length:
            cmp byte [esi+ecx], 0
            jz found_length
            inc ecx
            jmp find_length
           
        found_length:
        cmp ecx, 0
        je found_substring
        
        mov edx, ecx
        mov ecx, 0
        
        search_string:
            cmp byte[edi+ecx], 0 ; chack if it ended
            je not_found
            mov al, [edi + ecx]   ; load character from main string
            cmp al, [esi + ecx]   ; compare with substring character
            jne not_match

            inc ecx               ; move to the next character
            cmp ecx, edx          ; check if the entire substring has been matched
            je  found_substring   ; if yes, substring is found
            jmp search_string  ; continue searching

        not_match:
            inc esi               ; move to the next position in the main string
            mov ecx, 0           ; reset the counter for the next iteration
            jmp search_string
        
        not_found:
            mov eax, 0
        
        found_substring:
        ret 4*2
