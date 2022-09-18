# Eric Dechant Trinh
# edtrinh

.data
str_rings: .asciiz " RINGS!\n"
str_enemy: .asciiz "Hit Enemy "
str_gone: .asciiz " Rings gone.\n"
str_life: .asciiz " No Rings, lost life.\n"
str_ran: .asciiz "Ran through "
endl: .asciiz "\n"
.text

sonicRun:
	
	lw $t0,0($sp)      # ringsPerLife    - stack
	lw $t1,4($sp)      # numRings        - $s

	# prologue
	addi $sp,$sp,-40
	sw $ra,0($sp)
	sw $a0,4($sp)      # str             - stack   (original)
	sw $a1,8($sp)      # ringStr         - stack
	sw $a2,12($sp)     # enemyStr        - stack
	sw $t0,16($sp)     # ringsPerLife    - stack
	
	# save old s registers
	sw $s0,20($sp)
	sw,$s1,24($sp)
	sw $s2,28($sp)
	sw,$s3,32($sp)
	sw $s4,36($sp)
	
	# pre-body
	move $s0,$a0       # str             - $s / stack	
	move $s1,$a3       # numLives        - $s
	move $s2,$t1       # numRings        - $s
	
	# body
LOOP:	lb $s3,0($s0)
	li $t0,0x00
	beq $s3,$t0,EXIT
	
	# print
	li $v0,4
	la $a0,str_ran
	syscall
	li $v0,11
	move $a0,$s3
	syscall
	li $v0,4
	la $a0,endl
	syscall
	
	# inString function call
	move $a0,$s3
	lw $a1,12($sp)
	jal inString
	move $s4,$v0         # hitEnemy

	# indexString function call	
	move $a0,$s3
	lw $a1,8($sp)
	jal indexString
	move $t0,$v0
	
	bgez $t0,RING
	beq $s4,1,ENEM1
R1:	beq $s4,1,ENEM2
RETURN:	addi $s0,$s0,1
	j LOOP
	
	
EXIT:	# epilogue
	move $v0,$s1
	move $v1,$s2
	lw $ra,0($sp)
	lw $s0,20($sp)
	lw,$s1,24($sp)
	lw $s2,28($sp)
	lw,$s3,32($sp)
	lw $s4,36($sp)
	addi $sp,$sp,40
	jr $ra
	
RING:	# power function call
	li $a0,5
	addi $a1,$t0,1
	jal power
	move $t0,$v0
	
	# print
	li $v0,1
	move $a0,$t0
	syscall
	li $v0,4
	la $a0,str_rings
	syscall
	
	# getLife function call
	
	add $a0,$s2,$t0      # numRings + r
	lw $a1,16($sp)       # ringsPerLife
	jal getLife
	
	move $s2,$v1         # numRings = R
	add $s1,$s1,$v0      # numLives += L
	j RETURN
	
ENEM1:	blez $s2,R1
	li $s2,0             # numRings = 0
	
	# print
	li $v0,4
	la $a0,str_enemy
	syscall
	li $v0,11
	move $a0,$s3
	syscall
	li $v0,4
	la $a0,str_gone
	syscall
	
	j RETURN

ENEM2:	addi $s1,$s1,-1           # numLives--
	
	blez $s1,LOST

	# print
	li $v0,4
	la $a0,str_enemy
	syscall
	
	li $v0,11
	move $a0,$s3
	syscall
	
	li $v0,4
	la $a0,str_life
	syscall

	j RETURN
	
LOST:	# epilogue
	lw $ra,0($sp)
	lw $s0,20($sp)
	lw,$s1,24($sp)
	lw $s2,28($sp)
	lw,$s3,32($sp)
	lw $s4,36($sp)
	addi $sp,$sp,40
	li $v0,-1
	li $v1,-1
	jr $ra