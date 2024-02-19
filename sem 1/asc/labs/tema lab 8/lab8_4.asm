; A file name and a text (defined in data segment) are given. The text contains lowercase letters, uppercase letters, digits and special characters. Replace all spaces from the text with character 'S'. Create a file with the given name and write the generated text to file.
bits 32
global start

extern exit, printf, scanf, fopen, fprintf, fclose
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll

segment data use32 class=data
    file_name db "lab8_4.txt", 0
    format db "%s", 0
    access_mode db "w", 0
    file_descriptor dd -1
    text db "TexTul PENtru 3XemP1u ", 0
    len equ $-text
    modified_text resb len 
    
    
segment code use32 class=code
    start:
        ; create the file
        push dword access_mode     
        push dword file_name
        call [fopen]
        add esp, 4 * 2
        
        mov [file_descriptor], eax ; store the file descriptor returned by fopen
        cmp eax, 0
        je final
        
        lea esi, [text]
        lea edi, [modified_text]
        
        replace:
            mov al, [esi]
            cmp al, 0
            je done
            
            cmp al, ' '
            je replace_s
            
            mov [edi], al
            inc esi
            inc edi
            jmp replace
            
            replace_s:
                mov byte[edi], 'S'
                inc esi
                inc edi
                jmp replace
        
        done:           
        push dword modified_text
        push dword [file_descriptor]
        call [fprintf]
        add esp, 4 * 2
        
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
        final:
        push dword[0]
        call [exit]