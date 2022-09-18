.include "lab3_A_edtrinh.asm"
.include "lab3_B_edtrinh.asm"

.globl main
.text
main:
	la $a0, strings
	la $t0, n
	lw $a1, 0($t0)
	la $a2, enemy
	la $a3, ring
	jal playSonic

	li $v0, 10
	syscall

.data
strings: .word str_b, str_foo, str_world, str_hello, str_123, str_bar, str_help, str_abc
n: .word 6
enemy: .asciiz "!$#"
ring: .asciiz "oO0Q@"


str_foo: .asciiz "FOOoo00BAROOoo00"
str_bar: .asciiz "BARRRR"
str_hello: .asciiz "HeLLO!!"
str_world: .asciiz "@! wOrLd $!&"
str_abc: .asciiz "Abc"
str_123: .asciiz "123"
str_b: .asciiz "b"
str_help: .asciiz "HELP! HELP! HELP!"

.include "lab3_functions.asm"
