# Eric Dechant Trinh
# edtrinh
.include "lab2_A_edtrinh.asm"
.include "lab2_B_edtrinh.asm"

.data
# Define  data items here
.align 2
array: .space 20
input: .space 9


prompt: .asciiz "Enter hex character string, without 0x (8 digit max): "

hex_str1: .asciiz "The hex value is "
hex_str2: .asciiz " in decimal"

min_str: .asciiz "The minimum value is "
max_str: .asciiz "The maximum value is "

endl: .asciiz "\n"

.globl main
.text
main:
	li $s5,0         # counter of 5
	li $s7,0         # counter of 8
	
OUTER:	beq $s5,5,CONTINUE

	li $v0,4
	la $a0,prompt
	syscall
	
	li $v0,8
	la $a0,input
	li $a1,9
	syscall
	move $s0,$a0

	li $v0,4
	la $a0,endl
	syscall

	j INNER
	
RETURN: li $s7,0
	
	li $v0,4
	la $a0,hex_str1
	syscall
	
	move $a0,$s0
	jal hex2bin
	move $s1,$v0
	
	la $s2,array
	sll $t1,$s5,2
	add $t1,$t1,$s2
	sw $s1,0($t1)
	
	
	li $v0,1
	move $a0,$s1
	syscall
	
	li $v0,4
	la $a0,hex_str2
	syscall
	
	li $v0,4
	la $a0,endl
	syscall

	addi $s5,$s5,1
	j OUTER
	
INNER:	beq $s7,8,RETURN
	add $s6,$s0,$s7
	lb $s6,0($s6)	
	li $s3,0x0A
	beq $s6,$s3,REPLACE
BACK:	addi $s7,$s7,1
	j INNER

REPLACE:
	li $s4,0
	add $s6,$s0,$s7
	sb $s4,0($s6)
	j BACK

CONTINUE:
	la $a0,array
	li $a1,5
	jal findStats
	
	move $s5,$v0
	move $s7,$v1
			
	li $v0,4
	la $a0,endl
	syscall
	
	li $v0,4
	la $a0,min_str
	syscall
	
	li $v0,1
	move $a0,$s5
	syscall
	
	li $v0,4
	la $a0,endl
	syscall
	
	li $v0,4
	la $a0,max_str
	syscall
	
	li $v0,1
	move $a0,$s7
	syscall
	
	li $v0,4
	la $a0,endl
	syscall
	
	li $v0,10
	syscall
