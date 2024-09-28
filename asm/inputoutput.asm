section .data
   question db 'Enter a number: '
   qlen equ $ - question
   answer db 'You have entered: '
   alen equ $ - answer

section .bss
   num resb 5

section .text
   global _start

_start:
   ;Ask question
   mov eax,4
   mov ebx,1
   mov ecx,question
   mov edx,qlen
   int 0x80

   ;Read question
   mov eax,3
   mov ebx,0
   mov ecx,num
   mov edx,5
   int 0x80

   ;Output message
   mov eax,4
   mov ebx,1
   mov ecx,answer
   mov edx,alen
   int 0x80

   ;Output num
   mov eax,4
   mov ebx,1
   mov ecx,num
   mov edx,5
   int 0x80

   ;Exit
   mov eax,1
   mov ebx,0
   int 0x80