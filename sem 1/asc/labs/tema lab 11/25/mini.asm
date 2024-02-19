bits 32
global mini
segment code use32 public code
    mini:
        ; esp - ret addr
        ; esp + 4 - buffer
        ; esp + 8 - result
        mov eax, [esp + 8]
        mov ebx, [esp + 4]
        cmp eax, ebx
        jl no_change
            mov eax, [esp + 4]
        no_change:
            ret 4*2