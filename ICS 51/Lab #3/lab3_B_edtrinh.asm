# Eric Dechant Trinh
# edtrinh

.data
# Declare your global variables here
str_passed: .asciiz "Passed Level: "
str_levelup: .asciiz "\nLevelUp! Life at "
str_gameover: .asciiz "Game Over! Sonic died on Level:"
str_win: .asciiz "You Win!\n"
str_newline: .asciiz "\n"

.text
playSonic:
	# prologue
	addi $sp,$sp,-48
	sw $ra,44($sp)
	
	sw $s0,40($sp)
	sw $s1,36($sp)
	sw $s2,32($sp)
	sw $s3,28($sp)
	sw $s4,24($sp)
	sw $s5,20($sp)
	
	sw $a0,16($sp)     # strArray
	sw $a2,12($sp)     # enemyStr
	sw $a3,8($sp)     # ringstr
	
	
	
	# body
	
	move $s1,$a1          # numStr
	li $s2,100            # ringsPerLife
	li $s3,1              # numLives
	li $s4,0              # numRings

	li $s0,-1              # i
			
LOOPB:	addi $s0,$s0,1
	bge $s0,$s1,DONE
	
	li $t0,4
	mul $t0,$t0,$s0
	
	lw $t1,16($sp)
	add $t0,$t0,$t1
	lw $s5,0($t0)
	
	move $a0,$s5
	lw $a1,8($sp)
	lw $a2,12($sp)
	move $a3,$s3
	sw $s4,4($sp)
	sw $s2,0($sp)
	jal sonicRun

	move $s3,$v0
	move $s4,$v1
	
	beq $s3,-1,END
	
	
	addi $s2,$s2,50
	li $v0,4
	la $a0,str_passed
	syscall
	
	li $v0,4
	move $a0,$s5
	syscall
	
	li $v0,4
	la $a0,str_levelup
	syscall
	
	li $v0,1
	move $a0,$s2
	syscall
	
	li $v0,4
	la $a0,str_newline
	syscall
	
	addi $a0,$s0,1
	move $a1,$s3
	move $a2,$s4
	jal printStats

	j LOOPB
	
DONE:	# epilogue	
	lw $ra,44($sp)
	
	lw $s0,40($sp)
	lw $s1,36($sp)
	lw $s2,32($sp)
	lw $s3,28($sp)
	lw $s4,24($sp)
	lw $s5,20($sp)
	addi $sp,$sp,48
	
	li $v0,4
	la $a0,str_win
	syscall
	
	jr $ra

END:	li $v0,4
	la $a0,str_gameover
	syscall
	
	li $v0,4
	move $a0,$s5
	syscall
	
	lw $ra,44($sp)
	
	lw $s0,40($sp)
	lw $s1,36($sp)
	lw $s2,32($sp)
	lw $s3,28($sp)
	lw $s4,24($sp)
	lw $s5,20($sp)
	addi $sp,$sp,48
	jr $ra
