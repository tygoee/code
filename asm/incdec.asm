SYS_EXIT equ 1
SYS_WRITE equ 4

STDOUT equ 1

section .text
    global _start

_start:
    mov eax,[value]
    inc eax
    mov [value],eax

    mov eax,SYS_WRITE
    mov ebx,STDOUT
    mov ecx,value
    mov edx,1
    int 0x80

    mov eax,[value]
    dec eax
    mov [value],eax

    mov eax,SYS_WRITE
    mov ebx,STDOUT
    mov ecx,value
    mov edx,1
    int 0x80

    mov eax,SYS_EXIT
    mov ebx,0
    int 0x80

section .data
    value db '0'+5