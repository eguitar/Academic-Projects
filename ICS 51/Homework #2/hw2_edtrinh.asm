# Eric Dechant Trinh
# edtrinh

.text

reverseString:
	move $t9,$a0  # str original address
	move $t8,$a1  # rev new address
	li $t1,0 # find counter
	li $t2,0x00   # null terminator
	li $t5,0 # j counter
FIND:	add $t3,$t9,$t1
	lb $t3,0($t3)
	beq $t3,$t2,LOOP1A
	addi $t1,$t1,1
	j FIND
LOOP1A:	addi $t1,$t1,-1
	blt $t1,0,LOAD1A
	add $t3,$t9,$t1
	lb $t3,0($t3)
	add $t4,$t8,$t5
	sb $t3,0($t4)
	addi $t5,$t5,1
	j LOOP1A
LOAD1A:	add $t4,$t8,$t5
	sb $t2,0($t4)
DONE1A:	jr $ra
#------------------------------------------------------------------------------
shiftCipher:
	move $t8,$a0    # address of array of char
	move $t9,$a1    # integer n for shift
	li $t0,-1       # counter
	li $t5,0        # counter encrypt
	li $t7,0x00     # null terminator

LOOP1B: addi $t0,$t0,1   # increment i
	add $t1,$t0,$t8 # new address
	lb $t1,0($t1)	 # current char
	beq $t1,$t7,LOAD1B   # exit case
	ble $t1,0x40,LOOP1B
	ble $t1,0x5A,UPPER
	ble $t1,0x60,LOOP1B
	ble $t1,0x7A,LOWER
	j LOOP1B
UPPER:
	li $t6,'A'      # char A
	sub $t2,$t1,$t6
	add $t2,$t2,$t9	
	li $t6,26       # char ascii
	div $t2,$t6
	mfhi $t2
R1B1:	blt $t2,0,OVER1
	li $t6,'A'      # char A
	add $t2,$t2,$t6
	add $t1,$t0,$t8
	sb $t2,0($t1)
	addi $t5,$t5,1
	j LOOP1B
LOWER:
	li $t6,'a'      # char a
	sub $t2,$t1,$t6
	add $t2,$t2,$t9	
	li $t6,26       # char ascii
	div $t2,$t6
	mfhi $t2
R1B2:	blt $t2,0,OVER2
	li $t6,'a'      # char a
	add $t2,$t2,$t6
	add $t1,$t0,$t8
	sb $t2,0($t1)
	addi $t5,$t5,1
	j LOOP1B
OVER1:
	addi $t2,$t2,26
	j R1B1
OVER2:
	addi $t2,$t2,26
	j R1B2
LOAD1B:
	move $v0,$t0
	move $v1,$t5
	jr $ra
#------------------------------------------------------------------------------
countMultipleOf:
	ble $a1,0,ERROR2C
	ble $a2,0,ERROR2C
	move $t0,$a0   # address
	move $t1,$a1   # length
	move $t2,$a2   # multiple
	li $t9,-1    # counter
	li $t7,0            # counter of mult
	li $t8,0x80000000   # initial max
LOOP2C: addi $t9,$t9,1
	beq $t9,$t1,LOAD2C
	li $t4,4
	mul $t3,$t4,$t9
	add $t3,$t3,$t0
	lw $t3,0($t3)         # load the int
	beq $t3,$0,LOOP2C
	div $t3,$t2
	mfhi $t5
	beq $t5,$0,MULT
	j LOOP2C
MULT:
	addi $t7,$t7,1
	bgt $t3,$t8,MAX
	j LOOP2C 
MAX:
	move $t8,$t3
	j LOOP2C
LOAD2C:	move $v0,$t7
	beq $v0,$0,NONE
	move $v1,$t8	
DONE2C: jr $ra
NONE:	li $v1,0
	j DONE2C
ERROR2C:
	li $v0,-1
	li $v1,-1
	j DONE2C
#------------------------------------------------------------------------------
sumOfSubArray:
    	blt $a2,0,ERROR2D
	bge $a2,$a1,ERROR2D
	blt $a3,0,ERROR2D
	bge $a3,$a1,ERROR2D
	blt $a3,$a2,ERROR2D
	ble $a1,0,ERROR2D
	move $t0,$a0    # address of array
	move $t1,$a1    # length of array
	move $t2,$a2    # i counter
	move $t3,$a3    # j counter
	li $t9,0     # counter for sum
LOOP2D:	bgt $t2,$t3,LOAD2D
	li $t5,4
	mul $t6,$t2,$t5
	add $t6,$t0,$t6
	lw $t6,0($t6)
	add $t9,$t9,$t6     # add to sum
	addi $t2,$t2,1     #increment
	j LOOP2D
LOAD2D: move $v0,$t9
	li $v1,0
DONE2D: jr $ra
ERROR2D:
	li $v0,-1
	li $v1,-1
	j DONE2D
#------------------------------------------------------------------------------
statsOnStrings:
	ble $a1,0,ERROR3E
	li $t9,0x7F
	bgt $a2,$t9,ERROR3E
	move $t9,$a0       # address of array
	move $t8,$a1       # length of array	
	li $t6,0           # counter of chars
	li $t7,0           # counter for strings contain
	li $t2,0           # bool for contain char
	li $t0,0     # i counter
	li $t3,0     # j counter
LOOP3E:	beq $t0,$t8,LOAD3E
	li $t4,4
	mul $t4,$t0,$t4
	add $t1,$t9,$t4
	lw $t1,0($t1)
	j STR
R3E:	li $t3,0
	addi $t0,$t0,1
	beq $t2,0,LOOP3E
	li $t2,0               # reset bool
	addi $t7,$t7,1
	j LOOP3E
STR:	add $t4,$t1,$t3
	lb $t4,0($t4)
	li $t5,0x00
	beq $t4,$t5,R3E
	addi $t3,$t3,1
	addi $t6,$t6,1
	bne $t4,$a2,STR
	addi $t2,$t2,1
	j STR
LOAD3E:	move $v0,$t6
	move $v1,$t7
DONE3E:	jr $ra
ERROR3E:
	li $v0,-1
	li $v1,-1
	j DONE3E
#------------------------------------------------------------------------------
int2BCD:
	li $t9,99999999
	bgt $a0,$t9,ERROR3F
	li $t9,-99999999
	blt $a0,$t9,ERROR3F
	
	li $v0,0x00000000     # r variable
	
	li $t0,0              # k variable
	li $t1,0              # i variable
	
	#move v,$a0          # v variable
	
	bge $a0,0,LOOP1       # if v >= 0 skip
	sub $a0,$0,$a0        # v = 0 - v
########################################	
LOOP1:	beq $t0,32,DONE3F     
	
	li $t2,0              # msb variable
	
	bge $a0,0,S1          # v >= 0 skip
	li $t2,1              # msb = 1

S1:	sll $a0,$a0,1         # v = v << 1
	sll $v0,$v0,1         # r = r << 1
	
	beqz $t2,S2           # if !msb skip
	addi $v0,$v0,1        # r = r + 1
	
S2:	bge $t0,31,S3         # if k >= 31 skip
	beqz $v0,S3           # if r == 0 skip
	li $t3,0xF0000000     # mask variable
	li $t4,0x40000000     # cmp variable
	li $t5,0x30000000     # add variable
	j LOOP2
S3:	addi $t0,$t0,1        # k++
	li $t1,0              # reset i variable
	j LOOP1
########################################	
LOOP2:	beq $t1,8,S3
	and $t6,$t3,$v0           # mv variable
	
	ble $t6,$t4,S4            # if mv <= cmp skip
	add $v0,$v0,$t5           # r = r + add
S4:	srl $t3,$t3,4             # mask = mask >>> 4
	srl $t4,$t4,4             # cmp = cmp >>> 4
	srl $t5,$t5,4             # add = add >>> 4
	addi $t1,$t1,1            # i++
	j LOOP2
########################################
DONE3F:	
	jr $ra
########################################
ERROR3F:
	li $v0,-1
	j DONE3F
