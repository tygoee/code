section .text
    global _start

_start:
    ;write[4](stdout[1], msg, len)
    mov edx,len
    mov ecx,msg
    mov ebx,1
    mov eax,4
    int 0x80

    ;exit[1](0)
    mov eax,1
    mov ebx,0
    int 0x80

section .data
msg db 'Hello world',0xa
len equ $ - msg