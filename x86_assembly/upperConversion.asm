#PURPOSE:    This program converts an input file
#            to an output file with all letters
#            converted to uppercase.
#
#PROCESSING: 1) Open the input file
#            2) Open the output file
#            4) While we're not at the end of the input file
#               a) read part of file into our memory buffer
#               b) go through each byte of memory
#                    if the byte is a lower-case letter,
#                    convert it to uppercase
#               c) write the memory buffer to output file

 .section .data

#######CONSTANTS#######

 #system call numbers
 .equ SYS_OPEN, 5
 .equ SYS_WRITE, 4
 .equ SYS_READ, 3
 .equ SYS_CLOSE, 6
 .equ SYS_EXIT, 1

 #options for open (look at
 #/usr/include/asm/fcntl.h for
 #various values. You can combine them
 #by adding them or ORing them)
 #This is discussed at greater length
 #in "Counting Like a Computer"
 .equ O_RDONLY, 0
 .equ O_CREAT_WRONLY_TRUNC, 03101

 #standard file descriptors
 .equ STDIN, 0
 .equ STDOUT, 1
