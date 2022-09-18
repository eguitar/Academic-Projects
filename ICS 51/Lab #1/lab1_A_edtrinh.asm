# Eric Dechant Trinh
# edtrinh

.data
endl: .asciiz "\n"   # a string
myNum: .word 0xAABBCCDD

.globl main
.text
main:	la $t0,myNum      #1
	li $v0, 34        #2
	add $a0,$t0,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	lw $t1,0($t0)     #3
	li $v0, 1         #4
	add $a0,$t1,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	lb $t2,0($t0)     #5
	li $v0, 34
	add $a0,$t2,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	lb $t3,2($t0)     #6
	li $v0, 34
	add $a0,$t3,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	lbu $t3,2($t0)    #7
	li $v0, 34
	add $a0,$t3,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	lh $t4,0($t0)     #8
	li $v0, 1
	add $a0,$t4,$0
	syscall
	li $a0, 32
	li $v0, 11
	syscall
	li $v0, 34
	add $a0,$t4,$0
	syscall
	li $v0, 4
	la $a0,endl
	syscall	
	li $t5,0xFF       #9
	la $t0, myNum
	sb $t5,3($t0)
	lw $a0,0($t0)     #10
	li $v0, 34
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	li $v0, 10        #11
	syscall