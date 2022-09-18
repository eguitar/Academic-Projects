# Homework 1
# Name: Eric Trinh
# Net ID: edtrinh
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

output_string: .space 101
find_char: .byte ' '
replace_char: .byte ' '

.text

main:
	# print prompt
	li $v0,4
	la $a0,prompt_type
	syscall
	# read character
	li $v0,12
	syscall
	move $t9,$v0
	# print newline
	li $v0,4
	la $a0,newline
	syscall
	# possible options
	li $t0,'a'
	li $t1,'A'
	li $t2,'n'
	li $t3,'N'
	# branches
	beq $t9,$t0,CHARACTER
	beq $t9,$t1,CHARACTER
	beq $t9,$t2,NUMBER
	beq $t9,$t3,NUMBER
	j ERROR
CHARACTER:
	# print prompt
	li $v0,4
	la $a0,prompt_ascii
	syscall
	# read string
	li $v0,8
	la $a0,output_string
	li $a1,101
	syscall
	move $s0,$a0       #address of string
	# print prompt
	li $v0,4
	la $a0,prompt_find
	syscall
	# read find character
	la $s7,find_char
	li $v0,12
	syscall
	sb $v0,0($s7)      #find char
	# print newline
	li $v0,4
	la $a0,newline
	syscall
	# print prompt
	li $v0,4
	la $a0,prompt_replace
	syscall
	# read replace character
	la $t6,replace_char
	li $v0,12
	syscall
	sb $v0,0($t6)      #replace char
	# print newline
	li $v0,4
	la $a0,newline
	syscall
	# load string
	la $s0, output_string
	li $t0,0    #counter (or shifting amount)
	
	li $t6,-1   # counter for length
	li $t7,0   # counter for space
	li $t8,0   # counter for upper
	li $t9,0   # counter for symbol
	
	la $t2,find_char       #find character address
	lb $s6,0($t2)		#find character
	la $t3,replace_char    #replace character address
	lb $s7,0($t3)		#replace character

LOOP1:	add $t1,$s0,$t0
	
	#loading char
	lb $s1,0($t1)
	beq $s1,$0,EXIT
	j LEN

S1:	beq $s1,0x20,SPA
S2:	bge $s1,0x41,UPP
S3:	bge $s1,0x21,SYM1
S41:	bge $s1,0x3A,SYM2
S42:	bge $s1,0x5B,SYM3
S43:	bge $s1,0x7B,SYM4
S44:	beq $s1,$s6,REPLACE
S5:	#shifting counter
	addi $t0,$t0,1
	j LOOP1
REPLACE:
	sb $s7,0($t1)
	j S5
LEN:
	addi $t6,$t6,1
	j S1
SPA:
	addi $t7,$t7,1
	j S2
UPP:	
	bge $s1,0x5B,S3
	addi $t8,$t8,1
	j S3
SYM1:
	bge $s1,0x30,S41
	addi $t9,$t9,1
	j S41
SYM2:
	bge $s1,0x41,S42
	addi $t9,$t9,1
	j S42
SYM3:
	bge $s1,0x61,S43
	addi $t9,$t9,1
	j S43
SYM4:
	bge $s1,0x7F,S44
	addi $t9,$t9,1
	j S44
		
EXIT:	li $v0,4
	la $a0,ascii_length
	syscall
	li $v0,1
	move $a0,$t6
	syscall
	li $v0,4
	la $a0,newline
	syscall
	
	li $v0,4
	la $a0,ascii_space
	syscall
	li $v0,1
	move $a0,$t7
	syscall
	li $v0,4
	la $a0,newline
	syscall
	
	li $v0,4
	la $a0,ascii_upper
	syscall
	li $v0,1
	move $a0,$t8
	syscall
	li $v0,4
	la $a0,newline
	syscall
	
	li $v0,4
	la $a0,ascii_symbols
	syscall
	li $v0,1
	move $a0,$t9
	syscall
	li $v0,4
	la $a0,newline
	syscall

	li $v0,4
	la $a0,output_string
	syscall

	j DONE
NUMBER:
	# print prompt
	li $v0,4
	la $a0,prompt_number
	syscall
	# read integer
	li $v0,5
	syscall
	move $s0,$v0	
	# testing for even
	andi $t9,$s0,1
	beq $t9,0,EVEN	    # if even
N1:	beq $s0,0,N2       # if zero then is not power of 2
	addi $t0,$s0,-1
	and $t0,$t0,$s0
	beq $t0,0,POWER    # if power of two
N2:	li $t0,16
	div $s0,$t0
	mfhi $t0
	beq $t0,0,MULTIPLE # if multiple
N3:	# counting 1s in binary
	add $s1,$0,$0      #counter
	li $t0,1           #position
	li $t1,0           #index
	li $t9,32
	# while loop
LOOP2:	bge $t1,$t9,BREAK2 
	and $s2,$s0,$t0
	
	beqz $s2,IF
		addi $s1,$s1,1

IF:	sll $t0,$t0,1
	addi $t1,$t1,1
	j LOOP2

BREAK2:	# print stats
	li $v0,4
	la $a0,number_binary1
	syscall
	li $v0,1
	move $a0,$s1
	syscall
	li $v0,4
	la $a0,number_binary2
	syscall
	# print stats
	li $v0,4
	la $a0,number_div4
	syscall
	li $v0,1
	li $t0,4
	div $s0,$t0
	mflo $a0
	syscall
	j DONE
EVEN:
	li $v0,4
	la $a0,number_even
	syscall
	j N1
POWER:
	li $v0,4
	la $a0,number_power
	syscall
	j N2
MULTIPLE:
	li $v0,4
	la $a0,number_mult
	syscall
	j N3
ERROR:
	li $v0,4
	la $a0,err_string
	syscall
	j DONE
DONE:
	li $v0,10
	syscall	
	