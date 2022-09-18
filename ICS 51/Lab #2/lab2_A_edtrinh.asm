# Eric Dechant Trinh
# edtrinh

.data
Invalid_Error: .asciiz " contains invalid characters\n"

.text
hex2bin:
	move $t9,$a0        # original address
	li $t7,0            # the binary output
	
	li $t0,0            # counter
LOOP1:	add $t1,$t9,$t0     # temporary address
	lb $t2,0($t1)       # loaded char
	beq $t2,$0,DONE1     # exit case
	
	li $t3,'A'
	beq $t2,$t3,A
	li $t3,'B'
	beq $t2,$t3,B
	li $t3,'C'
	beq $t2,$t3,C
	li $t3,'D'
	beq $t2,$t3,D
	li $t3,'E'
	beq $t2,$t3,E
	li $t3,'F'
	beq $t2,$t3,F
	li $t8,'0'          # the character zero
	bge $t2,$t8,DEFAULT

A:	li $t6,10
	j RESUME
B:	li $t6,11
	j RESUME
C:	li $t6,12
	j RESUME
D:	li $t6,13
	j RESUME
E:	li $t6,14
	j RESUME
F:	li $t6,15
	j RESUME
DEFAULT:
	li $t8,'9'          # the character nine
	bgt $t2,$t8,ERROR1
	li $t8,'0'          # the character zero
	sub $t6,$t2,$t8
	j RESUME
		
RESUME:	sll $t7,$t7,4
	add $t7,$t7,$t6
	addi $t0,$t0,1
	j LOOP1
ERROR1:
	li $v0,4
	la $a0,Invalid_Error
	syscall
	
	li $v0,10
	syscall
DONE1:
	move $v0,$t7
	jr $ra
