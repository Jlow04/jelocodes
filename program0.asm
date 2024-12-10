; -- header --
          bits 64
          deafult rel
          ; -- variables --
          section.bss
          ; -- contants --
          section.data
          ; -- Entry Point --
          section .text
          global main
          extern ExitProcess
          extern printf
          extern scanf


          main:
          	PUSH rbp
          	MOV rbp,rsp
          	SUB rsp,32
          ; -- PUSH 10 ---
	PUSH 10
; -- PUSH 7 ---
	PUSH 7
; -- ADD ---
	POP rax
	ADD qword[rsp], rax
; -- SUB ---
; -- PRINT ---
; NOT IMPLEMENTED
; -- HALT ---
	 JMP EXIT_LABEL
EXIT_LABEL:
	XOR rax, rax
	CALL ExitProcess
