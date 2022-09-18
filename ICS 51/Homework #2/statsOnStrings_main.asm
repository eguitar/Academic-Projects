.include "hw2_edtrinh.asm"

.globl main

# Data Section
.data
array: .word str_1, str_2, str_3
n: .word 3
c: .byte '!'

total: .asciiz "The total number of characters is "
total2: .asciiz " occurs "
total3: .asciiz " times.\n"
newline: .asciiz "\n"

str_1: .asciiz "ICS51"
str_2: .asciiz "is"
str_3: .asciiz "fun!!!!"
str_4: .asciiz "B"
str_5: .asciiz "Boo"

# Program 
.text
main:
    # load the value into the argument register
    la $a0, array
    la $a1, n
    lw $a1,0($a1)
    la $a2, c
    lb $a2, ($a2)

    # call the function
    jal statsOnStrings 

    # save the return value
    move $s0, $v0
    move $s1, $v1

    # print string
    li $v0, 4
    la $a0, total
    syscall

    # print return value
    li $v0, 1
    move $a0, $s0
    syscall

    # print newline
    li $v0, 4
    la $a0, newline
    syscall

    # print character
    li $v0, 11
    la $a0, c
    lb $a0, ($a0) 
    syscall

    # print string
    li $v0, 4
    la $a0, total2
    syscall

    # print return value
    li $v0, 1
    move $a0, $s1
    syscall

    # print string
    li $v0, 4
    la $a0, total3
    syscall

    # Exit the program
    li $v0, 10
    syscall
