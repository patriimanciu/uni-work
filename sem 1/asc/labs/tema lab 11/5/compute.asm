bits 32
global compute
segment code use32 public code
    compute:
        ; a = [esp + 4]
        ; b = [esp + 8]
        ; c = [esp + 12]
        mov eax, [esp + 4]
        add eax, [esp + 8]
        sub eax, [esp + 12]
        ret 4*3