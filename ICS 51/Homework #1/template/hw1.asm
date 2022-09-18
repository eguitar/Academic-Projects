# Homework 1
# Name: MY_FIRSTNAME MY_LASTNAME (e.g., John Doe)
# Net ID: MY_NET_ID (e.g., jdoe)
.globl main

.data
newline: .asciiz "\n"
err_string: .asciiz "INPUT ERROR"

prompt_type: .asciiz "Number (n/N) or ASCII String (a/A)? "
prompt_ascii: .asciiz "Enter a ASCII string (max 100 characters): "
prompt_find: .asciiz "Enter the find character: "
prompt_replace: .asciiz "Enter the replace character: "
prompt_number: .asciiz "Enter the number: "

number_even: .asciiz "The number is Even\n"
number_power: .asciiz "The number is a power of 2\n"
number_mult: .asciiz "The number is a multiple of 16\n"
number_binary1: .asciiz "There are "
number_binary2: .asciiz " 1's in the binary representation\n"
number_div4: .asciiz "The value/4 is "

ascii_length: .asciiz "Length of string: "
ascii_space: .asciiz "# of space characters: "
ascii_upper: .asciiz "# of uppercase letters: "
ascii_symbols: .asciiz "# of symbols: "

.text

main:
    # Your code goes here