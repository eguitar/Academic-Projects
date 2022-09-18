.data
nums: .word 5, 2, 4, 3, 1

.text 

main:
	la $a0, nums
	li $a1, 5
	jal sum
	
	move $a0, $v0
	li $v0, 1
	syscall
	
	li $v0, 10
	syscall
	
sum: 
	# Prologue
	addi $sp, $sp, -8    # Adjust sp
	addi $t0, $a1, -1    # Compute size - 1
	sw $t0, 0($sp) 	     # Save size - 1 to stack
	sw $ra, 4($sp)       # Save return address

	# Function Body
	bne $a1, $zero, else # Branch if size != 0 
	li $v0, 0            # Set return value to 0
	addi $sp, $sp, 8     # Adjust sp
	jr $ra               # Return
else: 
	move $a1, $t0        # Update second arg to size-1
	jal sum
	lw $t0, 0($sp)       # Restore size - 1 from stack
	sll $t1, $t0, 2      # Multiply size - 1 by 4
	add $t1, $t1, $a0    # Compute address of arr[size - 1 
	lw $t2, 0($t1)       # t2 = arr[size - 1]
	add $v0, $v0, $t2    # retval = $v0 + arr[size - 1]

	# Epilogue
	lw $ra, 4($sp)       # Restore return address from stack
	# We don't need to restore $t0 b/c it was saved for the function, not for whoever called sum
	addi $sp, $sp, 8     # Adjust sp
	jr $ra               # Return
