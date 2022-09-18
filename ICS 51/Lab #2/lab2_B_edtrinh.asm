# Eric Dechant Trinh
# edtrinh

.data
err_string: .asciiz "Array does not contain any values\n"

.text
findStats:
	li $t0,0x0FFFFFFF   # initialize min
	li $t9,0x80000000   # initialize max
	
	move $t1,$a0        # address of array
	move $t8,$a1        # N - size
	
	blt $t8,1,ERROR2
	
	li $t3,0            # N counter
	li $t2,0            # increment
LOOP:	beq $t3,$t8,DONE2
	add $t5,$t1,$t2
	lw $t5,0($t5)
	blt $t5,$t0,MIN
R1:	bgt $t5,$t9,MAX
R2:	addi $t2,$t2,4
	addi $t3,$t3,1
	j LOOP
	
MIN:
	move $t0,$t5
	j R1

MAX:
	move $t9,$t5
	j R2
	
ERROR2:
	li $v0,4
	la $a0,err_string
	syscall
	
DONE2:	move $v0,$t0
	move $v1,$t9

	jr $ra
