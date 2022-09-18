.text
.globl main

main:
	li $t0,48
	
	
	li $v0,11
	move $a0,$t0
	syscall

.data
.align 2  # Align next items to word boundary
cells_array: .space 200

endl: .asciiz "\n"

