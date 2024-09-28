section .text
    global _start
_start:
    ;Write Luca Smith 
    mov edx,len
    mov ecx,name
    mov ebx,1
    mov eax,4
    int 0x80

    ;Switch Luna for John
    mov [name], dword 'John'

    ;Write John Smith
    mov edx,len
    mov ecx,name
    mov ebx,1
    mov eax,4
    int 0x80

    ;Exit
    mov eax,1
    mov ebx,0
    int 0x80

section .data
name db 'Loca Smith',0xa
len equ $ - name