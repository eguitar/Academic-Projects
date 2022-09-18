# Eric Dechant Trinh
# edtrinh

.text
sumArray:
	# $a0 - address of array
	# $a1 - numRow
	# $a2 - numCol
	li $t9,0          # sum
	
	li $t0,-1          # i counter
	move $t1,$a2       # column offset
	addi $t1,$t1,-1
	sll $t1,$t1,2
	
SUM_L:	addi $t0,$t0,1
	beq $t0,$a1,SUM_D

	mul $t5,$t0,$a2
	sll $t5,$t5,2
	
	add $t5,$t1,$t5
	add $t8,$t5,$a0
	lw $t8,0($t8)
			
	add $t9,$t9,$t8
			
	j SUM_L	
	
SUM_D:	move $v0,$t9
	jr $ra
	
#####################################################################
initArray:
	# $a0 - address of array
	# $a1 - numRow
	# $a2 - numCol
	li $t9,0          # zero
	
	li $t0,-1          # i counter
	move $t1,$a2       # column offset
	addi $t1,$t1,-1
	sll $t1,$t1,2
	
INIT_L:	addi $t0,$t0,1
	beq $t0,$a1,SUM_D

	mul $t5,$t0,$a2
	sll $t5,$t5,2
	
	add $t5,$t1,$t5
	add $t8,$t5,$a0
	sw $t9,0($t8)
			
	j INIT_L	
	
INIT_D:	move $v0,$t9
	jr $ra