# Homework 1
# Name: MY_FIRSTNAME MY_LASTNAME (e.g., John Doe)
# Net ID: MY_NET_ID (e.g., jdoe)
.globl main

.data
newline: .asciiz "\n"
err_string: .asciiz "INPUT ERROR"

prompt_type: .asciiz "Number (n/N) or ASCII String (a/A)? "
prompt_ascii: .asciiz "Enter a ASCII string (max 100 characters): "
prompt_find: .asciiz "Enter the find character: "
prompt_replace: .asciiz "Enter the replace character: "
prompt_number: .asciiz "Enter the number: "

number_even: .asciiz "The number is Even\n"
number_power: .asciiz "The number is a power of 2\n"
number_mult: .asciiz "The number is a multiple of 16\n"
number_binary1: .asciiz "There are "
number_binary2: .asciiz " 1's in the binary representation\n"
number_div4: .asciiz "The value/4 is "

ascii_length: .asciiz "Length of string: "
ascii_space: .asciiz "# of space characters: "
ascii_upper: .asciiz "# of uppercase letters: "
ascii_symbols: .asciiz "# of symbols: "

.text

main:
	# Your code goes here
	li $v0,4
	la $a0,prompt_type
	syscall
	
	li $v0,12
	syscall
	move $t9,$v0
	li $v0,4
	la $a0,newline
	syscall
	
	li $t0,'a'
	li $t1,'A'
	li $t2,'n'
	li $t3,'N'
	
	beq $t9,$t0,CHARACTER
	beq $t9,$t1,CHARACTER
	beq $t9,$t2,NUMBER
	beq $t9,$t3,NUMBER
	j ERROR
	
CHARACTER:
	li $v0,4
	la $a0,prompt_ascii
	syscall
	
	li $v0,8
	li $a0,0x100101e0
	li $a1,100
	syscall

	li $v0,4
	la $a0,prompt_find
	syscall
	
	li $v0,12
	move $t0,$v0
	syscall
	
	li $v0,4
	la $a0,newline
	syscall
	
	li $v0,4
	la $a0,prompt_replace
	syscall
	
	li $v0,12
	move $t1,$v0
	syscall
	
	li $v0,12
	li $a0,63
	syscall
	
	
	
LOOP:	#beq ?,?,END
	
	j LOOP
	
END:
	
	
	
	
	j DONE
	

	
	
NUMBER:
	li $v0,4
	la $a0,prompt_number
	syscall
	li $v0,5
	syscall
	move $s0,$v0
	
	andi $t9,$s0,1
	beq $t9,0,EVEN
R1:	move $t9,$s0
	
	
	
	
	
	
	j DONE

EVEN:
	li $v0,4
	la $a0,number_even
	syscall
	j R1
		
POWER:







MULTIPLE:
	
		

	#li $v0,35
	#move $a0,$t9
	#syscall
	
	
	
ERROR:
	li $v0,4
	la $a0,err_string
	syscall
	li $v0,10
	syscall
	
DONE:
	li $v0,10
	syscall

