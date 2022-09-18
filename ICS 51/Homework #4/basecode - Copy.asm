.text
.globl main

main:
	li $t0,-1

OUTE:	addi $t0,$t0,1
	beq $t0,10,EXITE
	
		
	li $t1,0
	j INE
	
	
INE:	beq $t1,10,OUTE

	########
	li $v0,1
	move $a0,$t0
	syscall
	
	li $v0,1
	move $a0,$t1
	syscall
	
	li $v0,4
	la $a0,endl
	syscall
	
	addi $t1,$t1,1
	j INE

EXITE:

.data
.align 2  # Align next items to word boundary
cells_array: .space 200

endl: .asciiz "\n"

