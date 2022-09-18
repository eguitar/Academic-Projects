# TREAT THIS FILE AS A BLACK BOX. ASSUME YOU DO NOT SEE THIS CODE

.data 
stats_label1: .asciiz "Sonic has completed "
stats_label2: .asciiz " levels (strings). He has "
stats_label3: .asciiz " lives, and "
stats_label4: .asciiz " rings.\n"
getLife_label: .asciiz " Live(s) gained!\n"

.text
power:  
        add $t0, $zero, $zero
        li $v0, 1
power_loop: 
        beq $t0, $a1, power_exit    
        mul $v0, $v0, $a0 
        addi $t0, $t0, 1   
        j   power_loop
power_exit:     jr  $ra

#################################################

printStats:
	move $t0, $a0
	move $t1, $a1
	li $t3, 4
	li $t4, 1
	move $t7, $a2

	la $t2, stats_label1
	move $v0, $t3
	move $a0, $t2
	syscall	

	move $a0, $t0
	move $v0, $t4	
	syscall

	la $t5, stats_label2
	move $v0, $t3
	move $a0, $t5
	syscall

	move $a0, $t1
	move $v0, $t4	
	syscall

	la $t6, stats_label3
	move $v0, $t3
	move $a0, $t6
	syscall

	move $a0, $t7
	move $v0, $t4	
	syscall

	la $t6, stats_label4
	move $v0, $t3
	move $a0, $t6
	syscall

	jr $ra

#################################################

inString:
	li $v0, 0
	move $t6, $a0
	move $a0, $a1
inString_loop:
	lb $t8, 0($a0)
	beq $0, $t8, inString_done
	move $t7, $t8
	beq $t6, $t7, inString_found
	addi $a0, $a0, 1
	j inString_loop
inString_found:
	li $v0, 1
inString_done:
	jr $ra	

#################################################

indexString:
	li $v0, -1
	move $t6, $a0
	move $a0, $a1
indexString_loop:
	lb $t8, 0($a0)
	beq $0, $t8, indexString_done
	move $t7, $t8
	beq $t6, $t7, indexString_found
	addi $a0, $a0, 1
	j indexString_loop
indexString_found:
	sub $v0, $a0, $a1
indexString_done:
	jr $ra	


#################################################

getLife:
    bge $a0, $a1, getLife_calculate 
    li $v0, 0
    move $v1, $a0
    jr $ra

getLife_calculate:
	li $t3, 4
	li $t4, 1
    div $a0, $a1
    mflo $t7
    mfhi $t8

    blez $t7 getLife_done 

	move $a0, $t7
	move $v0, $t4	
	syscall

	la $t6, getLife_label
	move $v0, $t3
	move $a0, $t6
	syscall

getLife_done:
    move $v0, $t7
    move $v1, $t8
    jr $ra
