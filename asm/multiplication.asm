SYS_EXIT equ 1
SYS_READ equ 3
SYS_WRITE equ 4
STDIN equ 0
STDOUT equ 1

section .data
    msg1 db "Enter first number: "
    msg1len equ $-msg1

    msg2 db "Enter second number: "
    msg2len equ $-msg2

    msg3 db "The multiplication is "
    msg3len equ $-msg3

    newline db 0xa

section .bss
    num1 resb 2
    num2 resb 2
    result resb 1

section .text
    global _start

_start:
    mov eax,SYS_WRITE
    mov ebx,STDOUT
    mov ecx,msg1
    mov edx,msg1len
    int 0x80

    mov eax,SYS_READ
    mov ebx,STDIN
    mov ecx,num1
    mov edx,2
    int 0x80

    mov eax,SYS_WRITE
    mov ebx,STDOUT
    mov ecx,msg2
    mov edx,msg2len
    int 0x80

    mov eax,SYS_READ
    mov ebx,STDIN
    mov ecx,num2
    mov edx,2
    int 0x80

    mov al,[num1]
    sub al,'0' 
    mov dl,[num2]
    sub dl,'0'
    
    mul dl
    add al,'0'
    mov [result],al

    mov eax,SYS_WRITE
    mov ebx,STDOUT
    mov ecx,msg3
    mov edx,msg3len
    int 0x80

    mov eax,SYS_WRITE
    mov ebx,STDOUT
    mov ecx,result
    mov edx,1
    int 0x80

    mov eax,SYS_WRITE
    mov ebx,STDOUT
    mov ecx,newline
    mov edx,1
    int 0x80

    mov eax,SYS_EXIT
    xor ebx,ebx
    int 0x80