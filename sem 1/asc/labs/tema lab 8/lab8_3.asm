; Read a file name and a text from the keyboard. Create a file with that name in the current folder and write the text that has been read to file. Observations: The file name has maximum 30 characters. The text has maximum 120 characters.
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
    file_name resb 100
    format db "%s", 0
    message_filename db "filename: ", 0
    access_mode db "w", 0
    file_descriptor dd -1
    message_text db "write a text of maximum 120 characters: ", 0
    text resb 120
    len equ 120
    
    
segment code use32 class=code
    start:
        ; print the message for filename input  
        push dword message_filename
        call [printf]
        add esp, 4 * 1
    
        ; read input
        push dword file_name
        push dword format
        call [scanf]
        add esp, 4 * 2
        
        
        ; create the file
        push dword access_mode     
        push dword file_name
        call [fopen]
        add esp, 4 * 2
        
        mov [file_descriptor], eax ; store the file descriptor returned by fopen
        cmp eax, 0
        je final
        
        ; print message for text input
        push dword message_text
        call [printf]
        add esp, 4 * 1
        
        ; read text
        push dword text
        push dword format
        call [scanf]
        add esp, 4 * 2
        
        ; imi ia doar pana la primul spatiu
        push dword text
        push dword [file_descriptor]
        call [fprintf]
        add esp, 4 * 2
        
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
        final:
        
        push dword[0]
        call [exit]