.data
nums: .word 1, 3, 5, 2, 4, 6, 1, 1

.text 
main:
	la $a0, nums
	li $a1, 8
	jal sumOdd
	
	move $a0, $v0
	li $v0, 1
	syscall
	
	li $v0, 10
	syscall
	
sumOdd: 
        	# base case (size == 0)
        bne  $a1, $zero, check_odd   # Branch (size != 0 )
        li   $v0, 0            # Set return value to 0
	jr   $ra               # Return

check_odd:  
        # Prologue
	addi $sp, $sp, -8      # Adjust sp (this is moved 2 positions to hold a value later in the code)
	addi $t0, $a1, -1      # Compute size - 1
        sw   $ra, 4($sp)       # Save return address

        # Function Body
        sll  $t1, $t0, 2       # Multiply size - 1 by 4
        add  $t1, $t1, $a0     # Compute address of arr[size - 1]
        lw   $t2, 0($t1)       # t2 = arr[size - 1]
        andi $t3, $t2, 1       # Is arr[size � 1] odd? 
        beq  $t3, $zero, even  # Branch if even 
        sw   $t2, 0($sp)       # Save arr[size - 1] on stack 
        move $a1, $t0          # Update second arg  
        jal  sumOdd 
        lw   $t2, 0($sp)       # Restore arr[size - 1] from stack 
        add  $v0, $v0, $t2     # Update return value

        # Epilogue 
Epilogue:       
        lw   $ra, 4($sp)       # Restore return address from stack         
	# Don't need to put other items back; they were for this function, not the caller function
        addi $sp, $sp, 8       # Adjust sp
        jr   $ra               # Return

even:  	move $a1, $t0          # Update second arg (size - 1)
	    jal  sumOdd 
        j Epilogue