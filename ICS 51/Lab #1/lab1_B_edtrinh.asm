# Eric Dechant Trinh
# edtrinh

.data
endl: .asciiz "\n"   # a string

.globl main
.text
main:

# Your code goes here
	li $t0,0x01234567     #1
	li $v0, 35
	add $a0,$t0,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	li $t1,0xFF           #2
	and $t2,$t0,$t1
	li $v0, 35
	add $a0,$t2,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	sll $t1,$t1,10        #3
	and $t2,$t0,$t1
	li $v0, 35
	add $a0,$t2,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	li $t3, 7             #4
	sll $t3,$t3,1
	li $v0, 1
	add $a0,$t3,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	ror $t3,$t3,4         #5
	li $v0, 1
	add $a0,$t3,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	sra $t3,$t3,1         #6
	li $v0, 1
	add $a0,$t3,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	srl $t3,$t3,1         #7
	li $v0, 1
	add $a0,$t3,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	li $v0, 10            #8
	syscall