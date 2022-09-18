.text
.globl main

main:
# Code & Instructions defined here
	#li $v0,12
	#syscall
	#la $s7,find_char
	#sb $v0,0($s7)      #find char
	
	#lb $s7,0($s7)
	
	#la $t9,char
	#lb $t9,0($t9)
	
	#beq $s7,$t9,PRINT
	#li $v0,10
	#syscall
	
#PRINT:	
	#li $v0,1
	#li $a0,1
	#syscall
	
	
	li $t8,'a'
	li $t9,'b'
	
	la $t0,find_char
	sb $t8,0($t0)
	
	la $t1,replace_char
	sb $t9,0($t1)
	
.data
# Global Variables defined here
output_string: .space 101
find_char: .byte '6'
replace_char: .byte 'f'
char: .byte 'k'


