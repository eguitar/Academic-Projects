.include "lab2_A_jwongma.asm"  # Change this to your file

.data
num: .asciiz  "AB157FCB"   # Modify this to test other cases
  
#endl: .asciiz "\n"
lead_string: .asciiz "The hex string value "
is_string: .asciiz " is "
decimal_string: .asciiz " in decimal\n"

.globl main
.text
main:

    # print string
    li $v0, 4
    la $a0, lead_string
    syscall

    # print string
    li $v0, 4
    la $a0, num
    syscall

    # load the argument registers
    la $a0, num
	
    # call the function
    jal hex2bin
	move $t0, $v0

    # print string
    li $v0, 4
    la $a0, is_string
    syscall
  
    # print return value
    move $a0, $t0
    li $v0, 1
    syscall

    # print string
    li $v0, 4
    la $a0, decimal_string
    syscall
    
    # Exit the program
    li $v0, 10
    syscall
