.include "lab3_A_edtrinh.asm"
.data 
str: .asciiz "Oh 0h my" # "00 Run Sonic 00"            # Change to test! try "Oh 0h my"
ring_str: .asciiz "oO0"   # lower case o, upper case O, and zero 
enemy_str: .asciiz "ENEMYenemy"

num_lives: .asciiz "numLives: "
num_rings: .asciiz "numRings: "
lose_str: .asciiz "Sonic Died!"
newline: .asciiz "\n"

.globl main
.text
main:
    la $a0, str
	la $a1, ring_str
	la $a2, enemy_str
	li $a3, 0
    addi $sp, $sp, -8
    sw $0,  4($sp) 
    li $t0, 100
    sw $t0, 0($sp) 
	jal sonicRun

    addi $sp, $sp, 8
	move $t9, $v0
	move $t8, $v1

	bltz $t9, lost

	li $v0, 4
	la $a0, num_lives
	syscall

	li $v0, 1
	move $a0, $t9
	syscall

    li $v0, 4
    la $a0, newline
    syscall

	li $v0, 4
	la $a0, num_rings
	syscall

	li $v0, 1
	move $a0, $t8
	syscall

    li $v0, 4
    la $a0, newline
    syscall
	j end

lost:

    li $v0, 4
    la $a0, lose_str
    syscall
end:
	li $v0, 10
	syscall


.include "lab3_functions.asm"
