# Eric Dechant Trinh
# edtrinh
.data
endl: .asciiz "\n"


.text
printHist:
	# epilogue
	addi $sp,$sp,-16
	sw $ra,0($sp)
	sw $s0,4($sp)
	sw $s1,8($sp)
	sw $s2,12($sp)
	
	move $s0,$a0
	move $s1,$a1
	
	# body
	li $s2,-1          # i counter
	
PRINT_L:	
	addi $s2,$s2,1
	beq $s2,$s1,PRINT_D
	
	sll $t5,$s2,1       # take i multiply by 2 which is column
	sll $t5,$t5,2       # multiply by 4 and add to base address
	add $t5,$t5,$s0
	
	addi $a0,$t5,0   # [row][0]
	lb $a0,0($a0)
	addi $a1,$t5,4   # [row][1]
	lw $a1,0($a1)
	jal printHistRow
	
	li $v0,4
	la $a0,endl
	syscall
	j PRINT_L
	
PRINT_D:	# prologue
	lw $ra,0($sp)
	lw $s0,4($sp)
	lw $s1,8($sp)
	lw $s2,12($sp)
	addi $sp,$sp,16
	jr $ra

#########################################################
countHist:
   	# epilogue
	addi $sp,$sp,-20
	sw $ra,0($sp)
	sw $s0,4($sp)
	sw $s1,8($sp)
	sw $s2,12($sp)
	sw $s3,16($sp)
	
	move $s0,$a0      # address array
	move $s1,$a1      # numRows
	move $s2,$a2      # mystr
	
	# body
	li $s3,-1          # i counter
	
COUNT_L:	
	addi $s3,$s3,1
	beq $s3,$s1,COUNT_D
	
	sll $t5,$s3,1
	sll $t5,$t5,2
	add $t5,$t5,$s0
	lb $a1,0($t5)     # [row][0]
	move $a0,$s2
	jal countChars
	
	sll $t5,$s3,1
	sll $t5,$t5,2
	add $t5,$t5,$s0
	lw $t0,4($t5)
	add $t0,$t0,$v0
	sw $t0,4($t5)     # [row][1]
		
	j COUNT_L
	
COUNT_D:	# prologue
	lw $ra,0($sp)
	lw $s0,4($sp)
	lw $s1,8($sp)
	lw $s2,12($sp)
	lw $s3,16($sp)
	addi $sp,$sp,20
	jr $ra
