# Prints out number of vowels in the string str
.data
str:  .asciiz "long time ago in a galaxy far away"
end1: .asciiz "\n"
 

.text
.globl main
main:			# execution starts here

	la   $a0,str
	jal  vcount	# call int vcount (char* str)

	move $a0,$v0
	li   $v0,1
	syscall		# print answer

	la   $a0,end1
	li   $v0,4
	syscall		# print newline

	li   $v0,10
	syscall		# au revoir...


# vowelp - takes a single character as a parameter and returns 1 if the 
# character is a lower case vowel otherwise return 0.
vowelp:	#leaf function
	li $v0, 0
	beq $a0, 'a', yes
	beq $a0, 'e', yes
	beq $a0, 'i', yes
	beq $a0, 'o', yes
	beq $a0, 'u', yes
	jr $ra
yes:
	li $v0, 1
	jr $ra

#vcount
vcount: 
	# prologue
	# $ra, $s0, $s1, $a0
	addi $sp, $sp, -16
	sw $ra, 12($sp)
	sw $s0, 8($sp)
	sw $s1, 4($sp)
	sw $a0, 0($sp)  # not required to be saved per register conventions
		
	#body
	li $s0, 0
	move $s1, $a0

nextch:	
	lb $a0, 0($s1)
	beqz $a0, done
	
	jal vowelp
	
	add $s0, $s0, $v0
	addi $s1, $s1, 1
	j nextch
	
done:
	move $v0, $s0

	#epilogue
	lw $ra, 12($sp)
	lw $s0, 8($sp)
	lw $s1, 4($sp)
	lw $a0, 0($sp)  # not required to be restored per register conventions
	addi $sp, $sp, 16
	
	jr $ra