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
	addi $sp,$sp,-4
	sw $ra,0($sp)
	jal win
	lw $ra,0($sp)
	addi $sp,$sp,4
	jr $ra

E1:	
	bne $a2,0,E2
	jr $ra

E2:	# prologue
	addi $sp,$sp,-32
	sw $ra,4($sp)
	sw $s0,8($sp)
	sw $s1,12($sp)
	sw $s2,16($sp)
	sw $s3,20($sp)
	sw $s4,24($sp)
	sw $s5,28($sp)
	
	move $s0,$a0       # row
	move $s1,$a1       # col
	move $s2,$a2       # game status
	move $s3,$a3       # array
	
	li $s4,-1

OUTE:	addi $s4,$s4,1
	beq $s4,10,EXITE
	li $s5,0
	j INE
	
INE:	beq $s5,10,OUTE

	li $t0,10
	mul $t0,$t0,$s4
	add $t0,$t0,$s5
	add $t0,$t0,$s3       # address of cell in MMIO
	
	lb $t1,0($t0)         # byte in array
	
	andi $t2,$t1,32
	beqz $t2,SKIP1
	# bomb section
	andi $t2,$t1,64
	beqz $t2,SKIP2
	# BOMB REVEALED CELL
	move $a0,$s4
	move $a1,$s5
	li $a2,'E'
	li $a3,0xF
	li $t0,0x9
	sw $t0,0($sp)
	jal setCell
	j CONTE
	
SKIP2:	andi $t2,$t1,16
	bnez $t2,SKIP3
	# BOMB NOT FLAGGED CELL
	move $a0,$s4
	move $a1,$s5
	li $a2,'B'
	li $a3,0x7
	li $t0,0x0
	sw $t0,0($sp)
	jal setCell
	j CONTE

SKIP3:	# BOMB FLAGGED CELL
	move $a0,$s4
	move $a1,$s5
	li $a2,'F'
	li $a3,0xC
	li $t0,0xA
	sw $t0,0($sp)
	jal setCell
	j CONTE	
		
SKIP1:	# non-bomb section
	andi $t2,$t1,16
	beqz $t2,SKIP4
	# NON-BOMB FLAGGED CELL
	move $a0,$s4
	move $a1,$s5
	li $a2,'F'
	li $a3,0xC
	li $t0,0x9
	sw $t0,0($sp)
	jal setCell
	j CONTE
		
SKIP4:	li $t9,0xF
	and $t8,$t1,$t9
	bnez $t8,SKIP5
	# EMPTY CELL
	move $a0,$s4
	move $a1,$s5
	li $a2,'\0'
	li $a3,0xF
	li $t0,0x0
	sw $t0,0($sp)
	jal setCell
	j CONTE

SKIP5:	# NUMBER CELL
	li $t9,0xF
	and $t8,$t1,$t9
	addi $t8,$t8,48
	
	move $a0,$s4
	move $a1,$s5
	move $a2,$t8
	li $a3,0xD
	li $t0,0x0
	sw $t0,0($sp)
	jal setCell
	
CONTE:	addi $s5,$s5,1
	j INE
	
EXITE:	move $a0,$s0
	move $a1,$s1
	li $a2,'E'
	li $a3,0xF
	li $t0,0x9
	sw $t0,0($sp)
	jal setCell

	lw $ra,4($sp)
	lw $s0,8($sp)
	lw $s1,12($sp)
	lw $s2,16($sp)
	lw $s3,20($sp)
	lw $s4,24($sp)
	lw $s5,28($sp)
	addi $sp,$sp,32
	jr $ra
#----------------------

##############################
# PART 4 FUNCTIONS
##############################

#----------------------
playerMove:
    	bltz $a1,ERRORF
    	bltz $a2,ERRORF
    	bgt $a1,9,ERRORF
    	bgt $a2,9,ERRORF
    	li $t0,'r'
    	beq $a3,$t0,PROF
    	li $t0,'R'
    	beq $a3,$t0,PROF
    	li $t0,'f'
    	beq $a3,$t0,PROF
    	li $t0,'F'
    	beq $a3,$t0,PROF
    	li $v0,-1
    	jr $ra
    	
    	lw $t0,4($sp)
    	lw $t1,0($sp)
PROF:   	# prologue
	addi $sp,$sp,-32
	sw $ra,4($sp)
	sw $s0,8($sp)
	sw $s1,12($sp)
	sw $s2,16($sp)
	sw $s3,20($sp)
	sw $s4,24($sp)
	sw $s5,28($sp)
	
	move $s0,$a0        # array
	move $s1,$a1        # row
	move $s2,$a2        # col
	move $s3,$a3        # action
	move $s4,$t0        # FG
	move $s5,$t1        # BG
	
	# body
	li $t0,10
	mul $t0,$t0,$s1
	add $t0,$t0,$s2
	add $t0,$t0,$s0       # address of cell in MMIO
	
	lb $t1,0($t0)         # byte in array
	andi $t2,$t1,64
	bnez $t2,ERREPIF      # if byte is alrdy revealed error
	
	li $t7,'f'
    	beq $a3,$t7,FL
    	li $t7,'F'
	beq $a3,$t7,FL
	# revealing-------------------------------------------
	addi $t2,$t1,64
	sb $t2,0($t0)
	
	andi $t2,$t1,16
	beqz $t2,A1
	addi $t2,$t1,-16	
	sb $t1,0($t0)
A1:	andi $t2,$t1,32
	beqz $t2,B1
	# bomb revealing
	move $a0,$s1
	move $a1,$s2
	li $a2,'B'
	li $a3,0x7
	li $t0,0x0
	sw $t0,0($sp)
	jal setCell
	
B1:	# non bomb revealing
	li $t9,0xF
	and $t8,$t1,$t9
	bnez $t8,B2
	# empty
	move $a0,$s1
	move $a1,$s2
	li $a2,'\0'
	li $a3,0xF
	li $t0,0x0
	sw $t0,0($sp)
	jal setCell
	
	j EPIF
B2:	# number
	addi $t8,$t8,48
	move $a0,$s1
	move $a1,$s2
	move $a2,$t8
	li $a3,0xD
	li $t0,0x0
	sw $t0,0($sp)
	jal setCell
		
	j EPIF
FL:	# flagging--------------------------------------------
	andi $t2,$t1,16
	beqz $t2,X1
	# flagged
	addi $t2,$t1,-16      # un flag
	sb $t2,0($t0)
	
	move $a0,$s1
	move $a1,$s2
	li $a2,'\0'
	move $a3,$s4
	move $t0,$s5
	sw $t0,0($sp)
	jal setCell
	
	j EPIF
X1:	# not flagged
	addi $t2,$t1,16       # flag
	sb $t2,0($t0)
	
	move $a0,$s1
	move $a1,$s2
	li $a2,'F'
	li $a3,0xC
	li $t0,0x7
	sw $t0,0($sp)
	jal setCell

	j EPIF
EPIF:	# epilogue
    	lw $ra,4($sp)
	lw $s0,8($sp)
	lw $s1,12($sp)
	lw $s2,16($sp)
	lw $s3,20($sp)
	lw $s4,24($sp)
	lw $s5,28($sp)
	addi $sp,$sp,32
    	li $v0,0
    	jr $ra
    	
ERREPIF:	# error - epilogue
	lw $ra,4($sp)
	lw $s0,8($sp)
	lw $s1,12($sp)
	lw $s2,16($sp)
	lw $s3,20($sp)
	lw $s4,24($sp)
	lw $s5,28($sp)
	addi $sp,$sp,32
    	li $v0,-1
    	jr $ra
  	
ERRORF:
	li $v0,-1
	jr $ra
#----------------------
gameStatus:
	li $t0,-1

OUTG:	addi $t0,$t0,1
	beq $t0,10,EXITG
	li $t1,0
	j ING
	
ING:	beq $t1,10,OUTG

	li $t2,10
	mul $t2,$t0,$t2
	add $t2,$t2,$a0
	add $t2,$t2,$t1       # address of cell in MMIO
	
	lb $t3,0($t2)         # byte in array
	
	andi $t4,$t3,32
	beqz $t4,NOTBOMB
	
	andi $t4,$t3,64
	beqz $t4,FLAG
	li $v0,-1
	jr $ra
FLAG:
	andi $t4,$t3,16
	bnez $t4,CONTG
	li $v0,0
	jr $ra
		
NOTBOMB:
	andi $t4,$t3,16
	beqz $t4,CONTG
	li $v0,0
	jr $ra
	
CONTG:	addi $t1,$t1,1
	j ING

EXITG:
	li $v0,1
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




