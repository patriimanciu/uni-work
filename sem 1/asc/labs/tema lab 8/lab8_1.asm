; Read a number in base 10 from the keyboard and display the value of that number in base 16 Example: Read: 28; display: 1C
bits 32
global start

extern exit, printf, scanf
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll

segment data use32 class=data
    n dd 0
    message db "The number read from console n = ", 0
    message2 db "The number in hex is n = %x", 0
    format  db "%d", 0
    
    
segment code use32 class=code
    start:
        ; print the message   
        push dword message
        call [printf]
        add esp, 4 * 1
        
        ; read the number from console
        push dword n       
        push dword format
        call [scanf]       
        add esp, 4 * 2
        
        ; print message2 with the hex representation
        push dword [n]
        push dword message2
        call [printf]
        add esp, 4 * 2
        
        push dword[0]
        call [exit]