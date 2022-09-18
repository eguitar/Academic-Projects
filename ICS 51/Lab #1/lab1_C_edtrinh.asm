# Eric Dechant Trinh
# edtrinh

.globl main
.text
main:

# Your code goes here
	
	la $t0,num
	li $v0,4
	move $a0,$t0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	li $v0, 4
	la $a0,prompt
	syscall
	li $v0,12
	syscall
	move $s0,$v0
	sb $s0,0($t0)
	li $v0, 4
	la $a0,endl
	syscall
	li $v0,4
	move $a0,$t0
	syscall
	lb $t9,2($t0)
	addi $t9,$t9,32
	sb $t9,2($t0)
	li $v0, 4
	la $a0,endl
	syscall
	li $v0,4
	move $a0,$t0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	
	lw $t8,0($t0)
	srl $t8,$t8,8
	
	sll $t9,$t9,24
	add $t1,$t8,$t9
	sw $t1,0($t0)
	
	li $v0,4
	move $a0,$t0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	
	sb $0,4($t0)
	li $v0,4
	move $a0,$t0
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	
	lw $t2,0($t0)
	ror $t2,$t2,4
	li $v0,4
	la $a0,num
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	
	sw $t2,0($t0)
	li $v0,4
	la $a0,num
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	
	lw $t2,0($t0)
	ror $t2,$t2,4
	sw $t2,0($t0)
	li $v0,4
	la $a0,num
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	
	li $v0,4
	la $a0,myspace
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	
	la $t5,myspace
	lw $t5,0($t5)
	add $t5,$t5,$s0
	la $t0,myspace
	sw $t5,0($t0)
	li $v0,4
	la $a0,myspace
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	
	addi $t5,$t5,1
	sb $t5,1($t0)
	li $v0,4
	la $a0,myspace
	syscall
	li $v0, 4
	la $a0,endl
	syscall
	
	li $v0,10
	syscall
	

.data
prompt: .asciiz "Enter a lowercase letter: "
endl: .asciiz "\n"
.align 2
num: .word 0x44434241
myspace: .byte '#', 0x00, '@', '%' 
stop: .byte 0x00

