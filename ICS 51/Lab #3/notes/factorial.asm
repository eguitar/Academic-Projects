.text 

main:
	li $a0, 5
	jal factorial
	
	move $a0, $v0
	li $v0, 1
	syscall
	
	li $v0, 10
	syscall
	
factorial: 

        #Prologue
	addi $sp, $sp, -8   # make room
        sw   $a0, 4($sp)    # store $a0
        sw   $ra, 0($sp)    # store $ra

        # Body #1
        li   $t0, 1         # check if a0 = 1
        bne  $t0, $a0, else # no: go to else  
        li   $v0, 1         # yes: return 1

        #Epilogue #1
        addi $sp, $sp, 8    # restore $sp
        jr   $ra            # return

else:   # Body #2   
	addi $a0, $a0, -1   # n = n - 1
        jal  factorial      # recursive call

        #Epilogue #2
        lw   $ra, 0($sp)    # restore $ra
        lw   $a0, 4($sp)    # restore $a0
        addi $sp, $sp, 8    # restore $sp
        
        mul  $v0, $a0, $v0  # n * factorial(n-1), Uses $a0 that was preserved on stack
        jr   $ra            # return
