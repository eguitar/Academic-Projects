.include "lab2_B_netid.asm"  # Change this to your file

.data
array: .word  55,0,-1,105,77,10,200,-6   # Modify these values to test different cases

return_string: .asciiz "The return value is ("
comma_string: .asciiz ", "
end_string: .asciiz ")\n"

.globl main
.text
main:

	la $a0, array	
    li $a1, 8       # Modify this value for the size of the array
	jal findStats

    li $t0, 0x0FFFFFFF
	beq $v0, $t0, main_done

    move $t0, $v0
    move $t1, $v1

	la $a0, return_string
	li $v0, 4
	syscall

    move $a0, $t0
    li $v0, 1
    syscall

	la $a0, comma_string
	li $v0, 4
	syscall

    move $a0, $t1
    li $v0, 1
    syscall

	la $a0, end_string
	li $v0, 4
	syscall

main_done:
	li $v0, 10
	syscall
