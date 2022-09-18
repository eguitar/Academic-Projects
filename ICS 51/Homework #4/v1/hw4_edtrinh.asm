# Eric Dechant Trinh
# edtrinh

.text

##############################
# PART 1 FUNCTIONS
##############################

#----------------------
setCell: #  / $a0 - row / $a1 - col / $a2 - ch / $a3 - FG / ??? - BG
    	bltz $a0,ERRORA           # if row < 0
    	bltz $a1,ERRORA           # if col < 0
    	bgt $a0,9,ERRORA          # if row > 9
    	bgt $a1,9,ERRORA          # if col > 9
    	
    	blt $a3,0x00,ERRORA       # if FG < 0x00
    	bgt $a3,0x0F,ERRORA       # if FG > 0x0F
    	
    	lw $t0,0($sp)             # $t0 - BG
    	blt $t0,0x00,ERRORA       # if BG < 0x00
    	bgt $t0,0x0F,ERRORA       # if BG > 0x0F    	    		    	
    	
    	# body
    	
    	li $t9,0xFFFF0000
    	
    	li $t1,20
    	mul $t1,$a0,$t1
    	
    	li $t2,2
    	mul $t2,$a1,$t2
    	add $t5,$t1,$t2
    	add $t5,$t5,$t9           # $t5 has base address now
    	
    	sb $a2,0($t5)
    	
    	move $t9,$t0
    	sll $t9,$t9,4
    	add $t9,$t9,$a3

    	sb $t9,1($t5)

    	li $v0,0
    	jr $ra
    	
ERRORA:	li $v0,-1
	jr $ra
    	
#----------------------
initDisplay:

	# prologue
	addi $sp,$sp,-24
	sw $ra,20($sp)
	sw $s0,4($sp)
	sw $s1,8($sp)
	sw $s2,12($sp)
	sw $s3,16($sp)

	move $s0,$a0
	move $s1,$a1

	# body
	li $s2,-1

OUTER1B:
	addi $s2,$s2,1
	beq $s2,10,EPI1B
	
	li $s3,0
	j INNER1B
	
	j OUTER1B
	
INNER1B:	beq $s3,10,OUTER1B




	move $a0,$s2
	move $a1,$s3
	li $a2,0x00
	move $a3,$s0
	sw $s1,0($sp)
	jal setCell

	addi $s3,$s3,1
	j INNER1B
	
	

EPI1B:	# epilgoue
	lw $ra,20($sp)
	lw $s0,4($sp)
	lw $s1,8($sp)
	lw $s2,12($sp)
	lw $s3,16($sp)
	addi $sp,$sp,24
    	jr $ra
#----------------------
win:
	# prologue
	addi $sp,$sp,-8
	sw $ra,4($sp)
	
	# body
	
    	li $a0,15
    	li $a1,0	
    	jal initDisplay
    	
    	# ---------- U - YELLOW - BOMB
    	li $a2,'B'
    	li $a3,0x07
    	li $t0,0x0B
    	sw $t0,0($sp)
    	li $a0,0
    	li $a1,3
    	jal setCell
    	
    	li $a2,'B'
    	li $a3,0x07
    	li $t0,0x0B
    	sw $t0,0($sp)
    	li $a0,1
    	li $a1,3
    	jal setCell
    	
    	li $a2,'B'
    	li $a3,0x07
    	li $t0,0x0B
    	sw $t0,0($sp)
    	li $a0,2
    	li $a1,3
    	jal setCell
    	
    	li $a2,'B'
    	li $a3,0x07
    	li $t0,0x0B
    	sw $t0,0($sp)
    	li $a0,3
    	li $a1,3
    	jal setCell
    	
    	li $a2,'B'
    	li $a3,0x07
    	li $t0,0x0B
    	sw $t0,0($sp)
    	li $a0,3
    	li $a1,4
    	jal setCell
    	
    	li $a2,'B'
    	li $a3,0x07
    	li $t0,0x0B
    	sw $t0,0($sp)
    	li $a0,3
    	li $a1,5
    	jal setCell
    	
    	li $a2,'B'
    	li $a3,0x07
    	li $t0,0x0B
    	sw $t0,0($sp)
    	li $a0,3
    	li $a1,6
    	jal setCell
    	
    	li $a2,'B'
    	li $a3,0x07
    	li $t0,0x0B
    	sw $t0,0($sp)
    	li $a0,2
    	li $a1,6
    	jal setCell
    	
    	li $a2,'B'
    	li $a3,0x07
    	li $t0,0x0B
    	sw $t0,0($sp)
    	li $a0,1
    	li $a1,6
    	jal setCell
    	
    	li $a2,'B'
    	li $a3,0x07
    	li $t0,0x0B
    	sw $t0,0($sp)
    	li $a0,0
    	li $a1,6
    	jal setCell
    	# ---------- W - RED - BOOM
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,5
    	li $a1,0
    	jal setCell
    	
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,6
    	li $a1,0
    	jal setCell
    	
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,7
    	li $a1,0
    	jal setCell
    	
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,8
    	li $a1,0
    	jal setCell
    	
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,9
    	li $a1,0
    	jal setCell
    	
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,8
    	li $a1,1
    	jal setCell
    	
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,7
    	li $a1,2
    	jal setCell
    	
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,8
    	li $a1,3
    	jal setCell
    	
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,9
    	li $a1,4
    	jal setCell
    	
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,8
    	li $a1,4
    	jal setCell
    	
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,7
    	li $a1,4
    	jal setCell
    	
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,6
    	li $a1,4
    	jal setCell
    	
    	li $a2,'E'
    	li $a3,0xF
    	li $t0,0x1
    	sw $t0,0($sp)
    	li $a0,5
    	li $a1,4
    	jal setCell
    	# ---------- I - BLUE - FLAG
    	li $a2,'F'
    	li $a3,0xD
    	li $t0,0xC
    	sw $t0,0($sp)
    	li $a0,5
    	li $a1,5
    	jal setCell
    	
    	li $a2,'F'
    	li $a3,0xD
    	li $t0,0xC
    	sw $t0,0($sp)
    	li $a0,6
    	li $a1,5
    	jal setCell
    	
    	li $a2,'F'
    	li $a3,0xD
    	li $t0,0xC
    	sw $t0,0($sp)
    	li $a0,7
    	li $a1,5
    	jal setCell
    	
    	li $a2,'F'
    	li $a3,0xD
    	li $t0,0xC
    	sw $t0,0($sp)
    	li $a0,8
    	li $a1,5
    	jal setCell
    	
    	li $a2,'F'
    	li $a3,0xD
    	li $t0,0xC
    	sw $t0,0($sp)
    	li $a0,9
    	li $a1,5
    	jal setCell
    	# ---------- N - GREEN - EIGHT
    	li $a2,'8'
    	li $a3,0xF
    	li $t0,0x2
    	sw $t0,0($sp)
    	li $a0,5
    	li $a1,6
    	jal setCell
    	
    	li $a2,'8'
    	li $a3,0xF
    	li $t0,0x2
    	sw $t0,0($sp)
    	li $a0,6
    	li $a1,6
    	jal setCell
    	
    	li $a2,'8'
    	li $a3,0xF
    	li $t0,0x2
    	sw $t0,0($sp)
    	li $a0,7
    	li $a1,6
    	jal setCell
    	
    	li $a2,'8'
    	li $a3,0xF
    	li $t0,0x2
    	sw $t0,0($sp)
    	li $a0,8
    	li $a1,6
    	jal setCell
    	
    	li $a2,'8'
    	li $a3,0xF
    	li $t0,0x2
    	sw $t0,0($sp)
    	li $a0,9
    	li $a1,6
    	jal setCell
    	
    	li $a2,'8'
    	li $a3,0xF
    	li $t0,0x2
    	sw $t0,0($sp)
    	li $a0,6
    	li $a1,7
    	jal setCell
    	
    	li $a2,'8'
    	li $a3,0xF
    	li $t0,0x2
    	sw $t0,0($sp)
    	li $a0,7
    	li $a1,8
    	jal setCell
    	
    	li $a2,'8'
    	li $a3,0xF
    	li $t0,0x2
    	sw $t0,0($sp)
    	li $a0,5
    	li $a1,9
    	jal setCell
    	
    	li $a2,'8'
    	li $a3,0xF
    	li $t0,0x2
    	sw $t0,0($sp)
    	li $a0,6
    	li $a1,9
    	jal setCell
    	
    	li $a2,'8'
    	li $a3,0xF
    	li $t0,0x2
    	sw $t0,0($sp)
    	li $a0,7
    	li $a1,9
    	jal setCell
    	
    	li $a2,'8'
    	li $a3,0xF
    	li $t0,0x2
    	sw $t0,0($sp)
    	li $a0,8
    	li $a1,9
    	jal setCell
    	
    	li $a2,'8'
    	li $a3,0xF
    	li $t0,0x2
    	sw $t0,0($sp)
    	li $a0,9
    	li $a1,9
    	jal setCell
    	
    	# epilogue
    	lw $ra,4($sp)
    	addi $sp,$sp,8
    	jr $ra
#----------------------

##############################
# PART 2 FUNCTION
##############################

#----------------------
loadMap:
    	
    	# epilogue
    	addi $sp,$sp,-24
    	sw $ra,20($sp)
    	sw $s0,4($sp)
    	sw $s1,8($sp)
	sw $s2,12($sp)
	sw $s3,16($sp)

	move $s0,$a0       # filename
	move $s1,$a1       # array address
	
    	# body
    	li $t9,0x0080
    	
    	li $t0,-1          # row
OUTERD:	beq $t0,10,EXITD
	addi $t0,$t0,1
	li $t1,0           # col
	j INNERD
	
INNERD:	beq $t1,10,OUTERD
	
	li $t6,10
	mul $t5,$t0,$t6
	add $t4,$t5,$s1
	add $t4,$t4,$t1        # $t4 has address for each cell im MMIO
	
	sb $t9,0($t4)
	
	addi $t1,$t1,1
	j INNERD

EXITD:  li $v0,13      # ------- open file
    	move $a0,$s0   # address of filename
    	li $a1,0       # read
    	li $a2,0       # ignore mode
    	syscall
    	
    	move $s2,$v0   # file descriptor
    	bltz $s2,ERRORD

RLOOP:	li $v0,14
	move $a0,$s2
	move $a1,$sp
	li $a2,4
    	syscall
    	
    	beqz $v0,REXIT     # end of file
    	bltz $v0,FERROR

    	lb $t1,0($sp)      # num
    	blt $t1,0x30,FERROR
    	bgt $t1,0x39,FERROR
    	lb $t0,1($sp)      # ' '
    	bne $t0,0x20,FERROR
    	lb $t2,2($sp)      # num
    	blt $t2,0x30,FERROR
    	bgt $t2,0x39,FERROR
    	lb $t0,3($sp)      # null terminator
    	bne $t0,0x0A,FERROR
    	
    	addi $t1,$t1,-48   # row
    	addi $t2,$t2,-48   # col
    	
    	li $t0,10
    	mul $t0,$t1,$t0
    	add $t0,$t0,$t2
    	add $t0,$s1,$t0    # address of cell
    	
    	lb $t3,0($t0)
    	li $t7,0xA0
    	beq $t3,$t7,RLOOP
    	li $t4,0x20
    	add $t3,$t3,$t4
    	
    	sb $t3,0($t0)

	beq $t1,0,S1      # if row != 0
	addi $t7,$t1,-1
	addi $t8,$t2,0
	li $t0,10
    	mul $t0,$t7,$t0
    	add $t0,$t0,$t8
    	add $t0,$s1,$t0    # address of cell
	lb $t3,0($t0)
	addi $t3,$t3,1
	sb $t3,0($t0)
S1:	beq $t1,9,S2      # if row != 9
	addi $t7,$t1,1
	addi $t8,$t2,0
	li $t0,10
    	mul $t0,$t7,$t0
    	add $t0,$t0,$t8
    	add $t0,$s1,$t0    # address of cell
	lb $t3,0($t0)
	addi $t3,$t3,1
	sb $t3,0($t0)
S2:	beq $t2,0,S3      # if col != 0
	addi $t7,$t1,0
	addi $t8,$t2,-1
	li $t0,10
    	mul $t0,$t7,$t0
    	add $t0,$t0,$t8
    	add $t0,$s1,$t0    # address of cell
	lb $t3,0($t0)
	addi $t3,$t3,1
	sb $t3,0($t0)
S3:	beq $t2,9,S4      # if col != 9
	addi $t7,$t1,0
	addi $t8,$t2,1
	li $t0,10
    	mul $t0,$t7,$t0
    	add $t0,$t0,$t8
    	add $t0,$s1,$t0    # address of cell
	lb $t3,0($t0)
	addi $t3,$t3,1
	sb $t3,0($t0)
S4:	beq $t1,0,S5      # if row != 0
	beq $t2,0,S5      # if col != 0
	addi $t7,$t1,-1
	addi $t8,$t2,-1
	li $t0,10
    	mul $t0,$t7,$t0
    	add $t0,$t0,$t8
    	add $t0,$s1,$t0    # address of cell
	lb $t3,0($t0)
	addi $t3,$t3,1
	sb $t3,0($t0)
S5:	beq $t1,9,S6      # if row != 9
	beq $t2,9,S6      # if col != 9
	addi $t7,$t1,1
	addi $t8,$t2,1
	li $t0,10
    	mul $t0,$t7,$t0
    	add $t0,$t0,$t8
    	add $t0,$s1,$t0    # address of cell
	lb $t3,0($t0)
	addi $t3,$t3,1
	sb $t3,0($t0)
S6:	beq $t1,0,S7      # if row != 0
	beq $t2,9,S7      # if col != 9
	addi $t7,$t1,-1
	addi $t8,$t2,1
	li $t0,10
    	mul $t0,$t7,$t0
    	add $t0,$t0,$t8
    	add $t0,$s1,$t0    # address of cell
	lb $t3,0($t0)
	addi $t3,$t3,1
	sb $t3,0($t0)
S7:	beq $t1,9,S8      # if row != 9
	beq $t2,0,S8      # if col != 0
	addi $t7,$t1,1
	addi $t8,$t2,-1
	li $t0,10
    	mul $t0,$t7,$t0
    	add $t0,$t0,$t8
    	add $t0,$s1,$t0    # address of cell
	lb $t3,0($t0)
	addi $t3,$t3,1
	sb $t3,0($t0)
S8:
    	j RLOOP
    	
REXIT:	li $v0,16      # ------- close file
    	move $a0,$s2
    	syscall
    	
EPID:  	# prologue
    	lw $ra,20($sp)
    	lw $s0,4($sp)
    	lw $s1,8($sp)
	lw $s2,12($sp)
	lw $s3,16($sp)
	addi $sp,$sp,24
    	li $v0,0
    	jr $ra  	
    	
ERRORD:	
    	lw $ra,20($sp)
    	lw $s0,4($sp)
    	lw $s1,8($sp)
	lw $s2,12($sp)
	lw $s3,16($sp)
	addi $sp,$sp,24
    	li $v0,-1
    	jr $ra

FERROR:	li $v0,16      # ------- close file
    	move $a0,$s2
    	syscall
    	
    	lw $ra,20($sp)
    	lw $s0,4($sp)
    	lw $s1,8($sp)
	lw $s2,12($sp)
	lw $s3,16($sp)
	addi $sp,$sp,24
    	li $v0,-1
    	jr $ra
#----------------------

##############################
# PART 3 FUNCTION
##############################

#----------------------
mapReveal:
	bne $a2,1,E1
	jal win
	jr $ra	
E1:	bnez $a2,E2
	jr $ra
E2:	# epilogue
	addi $sp,$sp,-24
	
	sw $ra,4($sp)
	sw $s0,8($sp)
	sw $s1,12($sp)
	sw $s2,16($sp)
	sw $s3,20($sp)
	
	move $s0,$a0     # move row
	move $s1,$a1     # move col
	move $s2,$a2     # game status
	move $s3,$a3     # byte array

	# body
	
	

	
DONE:	

	
	lw $ra,4($sp)
	lw $s0,8($sp)
	lw $s1,12($sp)
	lw $s2,16($sp)
	lw $s3,20($sp)
	addi $sp,$sp,24
	jr $ra
#----------------------

##############################
# PART 4 FUNCTIONS
##############################

#----------------------
playerMove:
    	
    	
    	
    	# prologue
	
	
	# body
	
	
	
	
	
	# epilogue

    	
    	
    	
    	
    	li $v0, -200
    	jr $ra
#----------------------
gameStatus:

li $v0,1
li $a0,123
syscall



    	li $t0,0
OUT:	beq $t0,10,EPIG
	addi $t0,$t0,1
	li $t1,0
	j IN
	
IN:	beq $t1,10,OUT

	
	li $t2,10
    	mul $t2,$t0,$t2
    	add $t2,$t2,$t1
    	add $t2,$t2,$a0    # address of cell
    	
	lb $t3,0($t2)      # cell
	
	li $t4,32        # BOMB
	and $t5,$t3,$t4
	beq $t4,$t5,BOMB    
# -------------------------------------	
	li $t4,16        # FLAG
	and $t5,$t3,$t4
	bne $t4,$t5,CONTG
	li $v0,0
	jr $ra
# -------------------------------------	
BOMB:	
	li $t4,64           # REVEALED
	and $t5,$t3,$t5
	bne $t4,$t5,FLAGG
	li $v0,-1
	jr $ra
	
FLAGG:	li $t4,16           # FLAG
	and $t5,$t3,$t5
	beq $t4,$t5,CONTG
	li $v0,0
	jr $ra
# -------------------------------------
CONTG:
	addi $t1,$t1,1
	j IN
	
	
	
EPIG:	li $v0,1     # won
    	jr $ra
#----------------------

##############################
# PART EC FUNCTIONS
##############################

#----------------------
revealCells:
    	
    	
    	
    	# prologue
	
	
	# body
	
	
	
	
	
	# epilogue

    	
    	
    	
    	
    	jr $ra
#----------------------

#################################################################
# Student defined data section
#################################################################
.data
.align 2  # Align next items to word boundary
cells_array: .space 200




