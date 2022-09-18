# Eric Dechant Trinh
# edtrinh

.data
newline: .asciiz "\n"
str_1: .asciiz "str:"
pattern_1: .asciiz "\tpattern:"
return00: .asciiz "return (0,0)\n"
return10: .asciiz "return (1,0)\n"
return_p1: .asciiz "return (1,"
return_p: .asciiz "return ("
p_endl: .asciiz ")\n"
comma: .asciiz ", "

.text

##############################
# PART 1 FUNCTIONS
##############################

find_glob:
	
	# prologue #######################################
	addi $sp, $sp,-24
	sw $ra,0($sp)
	sw $s0,4($sp)
	sw $s1,8($sp)
	sw $s2,12($sp)
	sw $s3,16($sp)
	sb $a2,20($sp)          # wildcard
	
	move $s0,$a0            # str
	move $s1,$a1            # pattern
	
	# body #######################################
	li $v0,4
	la $a0,str_1
	syscall
	
	li $v0,4
	move $a0,$s0
	syscall
	
	li $v0,4
	la $a0,pattern_1
	syscall
	
	li $v0,4
	move $a0,$s1
	syscall
	
	li $v0,4
	la $a0,newline
	syscall
	
	move $a0,$s0
	jal length
	move $s2,$v0        # length(str)
	
	move $a0,$s1
	jal length
	move $s3,$v0        # length(pattern)
	
	li $t0,0            # bool #1
	li $t1,0            # bool #2
	
	beqz $s2,S1
	li $t0,1
S1:	beqz $s3,S2
	li $t1,1
S2:	xor $t0,$t0,$t1
	beqz $t0,S3
	
	li $v0,4
	la $a0,return00
	syscall
	
	li $v0,0
	li $v1,0
	j FINISH
S3:	
	li $t0,0            # bool #1
	li $t1,0            # bool #2
	
	bne $s3,1,S4
	li $t0,1
S4:	lb $t2,0($s1)       # pattern[0]
	lb $t3,20($sp)      # wildcard
	bne $t2,$t3,S5
	li $t1,1
S5:	and $t0,$t0,$t1
	beqz $t0,S6
	
	li $v0,4
	la $a0,return_p1
	syscall
	li $v0,1
	move $a0,$s2
	syscall
	li $v0,4
	la $a0,p_endl
	syscall
	
	
	li $v0,1
	move $v1,$s2
	j FINISH
S6:	
	move $a0,$s0
	move $a1,$s1
	jal equals
	
	beqz $v0,S7
	
	li $v0,4
	la $a0,return10
	syscall
	
	li $v0,1
	li $v1,0
	j FINISH
S7:
	lb $t0,0($s0)
	lb $t1,0($s1)
	bne $t0,$t1,S8
	move $a0,$s0
	addi $a0,$a0,1
	move $a1,$s1
	addi $a1,$a1,1
	lb $a2,20($sp)  
	jal find_glob
	j FINISH
S8:	
	lb $t0,20($sp)  
	lb $t1,0($s1)
	bne $t0,$t1,S9             # if (pattern[0] != wildcard)
	move $a0,$s0
	move $a1,$s1
	addi $a1,$a1,1
	lb $a2,20($sp)  
	jal find_glob              # 
	
	beqz $v0,S10
	move $t0,$v0
	
	li $v0,4
	la $a0,return_p
	syscall
	
	li $v0,1
	move $a0,$t0
	syscall
	
	li $v0,4
	la $a0,comma
	syscall
	
	li $v0,1
	move $a0,$v1
	syscall
	
	li $v0,4
	la $a0,p_endl
	syscall
	
	move $v0,$t0
	j FINISH
	
S10:	move $a0,$s0
	addi $a0,$a0,1
	move $a1,$s1
	lb $a2,20($sp)  
	jal find_glob
	move $t0,$v0
	move $t1,$v1
	addi $t1,$t1,1
	
	li $v0,4
	la $a0,return_p
	syscall
	
	li $v0,1
	move $a0,$t0
	syscall
	
	li $v0,4
	la $a0,comma
	syscall
	
	li $v0,1
	move $a0,$t1
	syscall
	
	li $v0,4
	la $a0,p_endl
	syscall
	
	move $v0,$t0
	move $v1,$t1
	j FINISH
S9:	
	li $v0,4
	la $a0,return00
	syscall
	
	li $v0,0
	li $v1,0
	j FINISH
	
	# epilogue #######################################
FINISH:	lw $ra,0($sp)
	lw $s0,4($sp)
	lw $s1,8($sp)
	lw $s2,12($sp)
	lw $s3,16($sp)
	addi $sp, $sp, 24
	jr $ra

##############################
# PART 2 FUNCTIONS
##############################

preorder:
	# prologue
	addi $sp,$sp,-12
	sw $ra,0($sp)
	sw $s0,4($sp)
	sw $s1,8($sp)
	move $s0,$a0           # node
	move $s1,$a1           # index
	
	# body
	
	###########	
	sll $t0,$s1,2
	add $t0,$s0,$t0        # base address of current node
	lhu $t1,0($t0)          # value
	
	li $v0,1
	move $a0,$t1
	syscall
	
	li $v0,4
	la $a0,newline
	syscall
	
	lbu $t2,3($t0)           # left index

	bge $t2,255,L
	move $a0,$s0
	move $a1,$t2
	jal preorder
	
L:	sll $t0,$s1,2
	add $t0,$s0,$t0        # base address of current node
	lbu $t3,2($t0)           # right index
	
	bge $t3,255,R
	move $a0,$s0
	move $a1,$t3
	jal preorder

R:	# epilogue
	lw $ra,0($sp)
	lw $s0,4($sp)
	lw $s1,8($sp)
	addi $sp,$sp,12
	jr $ra
######################################################################
position:
	# prologue
	addi $sp,$sp,-4
	sw $ra,0($sp)
		
	# body	
	move $t9,$a0      # node
	move $t8,$a1      # curNodeIndex
	move $t7,$a2      # newValue
	
	sll $t0,$t8,2
	add $t0,$t0,$a0
	lhu $t0,0($t0)
	
	li $v0,1
	move $a0,$t0
	syscall	
	li $v0,4
	la $a0,newline
	syscall	
	
	bge $t7,$t0,RIGHT        # if newvalue >= currentValue
	
	
	sll $t0,$t8,2
	add $t0,$t0,$t9        # base address of current node
	lbu $t3,3($t0)         # left index
	
	bne $t3,255,C1
	move $v0,$t8
	li $v1,0
	j EPIC
	
C1:	move $a0,$t9
	move $a1,$t3
	move $a2,$t7
	jal position
	j EPIC
	
RIGHT:	
	sll $t0,$t8,2
	add $t0,$t0,$t9        # base address of current node
	lbu $t3,2($t0)         # left index
	
	bne $t3,255,C2
	move $v0,$t8
	li $v1,1
	j EPIC
	
C2:	move $a0,$t9
	move $a1,$t3
	move $a2,$t7
	jal position
	
EPIC:	# epilogue
	lw $ra,0($sp)
	addi $sp,$sp,4
	jr $ra
######################################################################
insertNode:
	# prologue
	addi $sp,$sp,-20
	sw $ra,0($sp)
	sw $s0,4($sp)
	sw $s1,8($sp)
	sw $s2,12($sp)
	sw $s3,16($sp)
	
	move $s0,$a0      # nodes
	move $s1,$a1      # rootIndex
	move $s2,$a2      # newValue
	
	# body
	sll $t0,$s1,2
	add $t0,$t0,$s0
	lw $t0,0($t0)
	
	bne $t0,-1,D1
	sll $t0,$s1,2
	add $t0,$t0,$s0
	li $t9,255
	sh $s2,0($t0)
	sb $t9,3($t0)
	sb $t9,2($t0)
	li $v0,1
	j EPID
	
D1:	move $s0,$a0
	jal find_empty
	move $s3,$v0      # newIndex
	bgez $v0,D2
	li $v0,0
	j EPID
	
D2:	move $a0,$s0
	move $a1,$s1
	move $a2,$s2
	jal position
	
	bnez $v1,NOPE
	sll $t0,$v0,2
	add $t0,$t0,$s0
	sb $s3,3($t0)
	j D3
	
NOPE:	sll $t0,$v0,2
	add $t0,$t0,$s0
	sb $s3,2($t0)	
	
D3:	sll $t0,$s3,2
	add $t0,$t0,$s0
	li $t9,255
	sh $s2,0($t0)
	sb $t9,3($t0)
	sb $t9,2($t0)
	li $v0,1
	
EPID:	# epilogue
	lw $ra,0($sp)
	lw $s0,4($sp)
	lw $s1,8($sp)
	lw $s2,12($sp)
	lw $s3,16($sp)
	addi $sp,$sp,20
	jr $ra
######################################################################
find_parent:
	# prologue
	addi $sp,$sp,-4
	sw $ra,0($sp)
	
	# $a0 - nodes
	# $a1 - curIndex
	# $a2 - childIndex
	# body
	sll $t0,$a2,2
	add $t0,$a0,$t0
	lhu $t0,0($t0)         # childValue
	
	sll $t1,$a1,2
	add $t1,$a0,$t1
	lhu $t1,0($t1)         # currentValue
	
	bge $t0,$t1,E1
	sll $t1,$a1,2
	add $t1,$a0,$t1
	lbu $t1,3($t1)         # leftIndex
	bne $t1,255,E2
	li $v0,-1
	li $v1,-1
	j EPIE
		
E2:	bne $t1,$a2,E3	
	move $v0,$a1
	li $v1,0
	j EPIE
	
E3:	move $a1,$t1
	jal find_parent
	j EPIE	
	
E1:	sll $t2,$a1,2
	add $t2,$a0,$t2
	lbu $t2,2($t2)         # rightIndex
	bne $t2,255,E4
	li $v0,-1
	li $v1,-1
	j EPIE

E4:	bne $t1,$a2,E5	
	move $v0,$a1
	li $v1,1
	j EPIE
	
E5:	move $a1,$t2
	jal find_parent
	j EPIE
	
EPIE:	# epilogue
	lw $ra,0($sp)
	addi $sp,$sp,4
	jr $ra
######################################################################
min:
	# prologue
	addi $sp,$sp,-4
	sw $ra,0($sp)
	
	# $a0 - nodes
	# $a1 - currentIndex
	
	# body
	sll $t0,$a1,2
	add $t0,$a0,$t0
	lbu $t0,3($t0)        # leftIndex
	bne $t0,255,F1
	
	sll $t1,$a1,2
	add $t1,$a0,$t1
	lbu $t1,2($t1)
	bne $t1,255,NOTLEAF
	move $v0,$a1
	li $v1,1
	j EPIF
	
NOTLEAF:move $v0,$a1
	li $v1,0
	j EPIF
	
F1:	move $a1,$t0
	jal min
	
EPIF:	# epilogue
	lw $ra,0($sp)
	addi $sp,$sp,4
	jr $ra
######################################################################
deleteNode:
	# prologue
	addi $sp,$sp,-24
	sw $ra,0($sp)
	sw $s0,4($sp)
	sw $s1,8($sp)
	sw $s2,12($sp)
	sw $s3,16($sp)
	sw $s4,20($sp)
	
	move $s0,$a0         # nodes
	move $s1,$a1         # rootIndex
	move $s2,$a2         # deleteIndex
	
	# body
	sll $t0,$s2,2
	add $t0,$s0,$t0
	lbu $t1,3($t0)       # leftIndex
	lbu $t2,2($t0)       # rightIndex
	
	bne $t1,255,G1       # 
	bne $t2,255,G1       # 
	# no children to relocate #############################################
	bne $s2,$s1,Z1       # if deleteIndex != rootIndex
	sll $t0,$s2,2
	add $t0,$t0,$s0
	li $t1,-1
	sw $t1,0($t0)
	j EPIG
	
Z1:	move $a0,$s0
	move $a1,$s1
	move $a2,$s2
	jal find_parent
	# $v0 - parentIndex
	# $v1 - leftorright
	
	li $t9,255
	sll $t0,$v0,2
	add $t0,$t0,$s0
	bnez $v1,Z2          # if leftOrRight != left
	sb $t9,3($t0)
	j Z3
	
Z2:	sb $t9,2($t0)
	
Z3:	sll $t0,$s2,2
	add $t0,$t0,$s0
	li $t9,-1
	sw $t9,0($t0)
	j EPIG
	
G1:	beq $t1,255,G2
	beq $t2,255,G2
	# two children ##########################################################
	move $a0,$s0        # nodes
	sll $t0,$s2,2
	add $t0,$t0,$s0
	lbu $a1,2($t0)      # nodes[deleteIndex].right
	jal min             # min function call
	
	move $s3,$v0        # minIndex
	move $s4,$v1        # minIsLeaf
	
	move $a0,$s0        # nodes
	move $a1,$s2        # deleteIndex
	move $a2,$s3        # minIndex
	jal find_parent     # find_parent function call
	# $v0 - parentIndex
	# $v1 - leftOrRight

	beqz $s4,Y1         # minIsLeaf != true
	li $t9,255
	sll $t0,$v0,2
	add $t0,$s0,$t0
	bnez $v1,Y2         # leftOrRight != left
	# left
	sb $t9,3($t0)
	j G11
	# right
Y2:	sb $t9,2($t0)	
	j G11	
	
Y1:	sll $t1,$s3,2
	add $t1,$t1,$s0
	lbu $t1,2($t1)        # node[minIndex].right	.
	
	sll $t0,$v0,2
	add $t0,$s0,$t0
	bnez $v1,Y3           # leftOrRight != left
	#left
	sb $t1,3($t0)
	j G11
	# right
Y3:	sb $t1,2($t0)

G11:	sll $t0,$s3,2
	add $t0,$t0,$s0      # nodes[minIndex]
	lhu $t0,0($t0)       # nodes[minIndex].value

	sll $t1,$s2,2
	add $t1,$t1,$s0
	sh $t0,0($t1)        # nodes[deleteIndex].value = nodes[minIndex].value

	sll $t0,$s3,2
	add $t0,$t0,$s0      # nodes[minIndex]
	li $t9,-1
	sw $t9,0($t0)
	j EPIG
	# one child ################################################################
G2:	sll $t0,$s2,2
	add $t0,$t0,$s0      # nodes[deleteIndex]
	lbu $t1,3($t0)       # nodes[deleteIndex].left
	beq $t1,255,X1       # if nodes[deleteIndex].left == 255
	move $s3,$t1         # childIndex
	j X2
X1:	lbu $s3,2($t0)

X2:	bne $s2,$s1,X3       # if deleteIndex != rootIndex
	sll $t0,$s3,2
	add $t0,$t0,$s0      # nodes[childIndex]
	lw $t9,0($t0)        # childNode
	
	sll $t1,$s2,2
	add $t1,$t1,$s0
	sw $t9,0($t1)        # nodes[deleteIndex] = childNode

	sll $t0,$s3,2
	add $t0,$t0,$s0      # nodes[childIndex]
	li $t9,-1
	sw $t9,0($t0)
	j EPIG

X3:	move $a0,$s0
	move $a1,$s1
	move $a2,$s2
	jal find_parent
	# $v0 - parentIndex
	# $v1 - leftOrRight
	
	sll $t0,$v0,2
	add $t0,$t0,$s0           # nodes[parentIndex]
	bnez $v1,X4               # if leftOrRight != left
	sb $s3,3($t0)
	j X5

X4:	sb $s3,2($t0)

X5:	sll $t0,$s2,2
	add $t0,$t0,$s0
	li $t9,-1
	sw $t9,0($t0)

EPIG:	# epilogue
	lw $ra,0($sp)
	lw $s0,4($sp)
	lw $s1,8($sp)
	lw $s2,12($sp)
	lw $s3,16($sp)
	lw $s4,20($sp)
	addi $sp,$sp,24
	jr $ra
######################################################################
.include "hw3_helpers.asm"
