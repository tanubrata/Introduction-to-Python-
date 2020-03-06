#Name- Tanubrata Dey
#Date- 27 April 2018
#My second MIPS program that prints: Countdown

ADDI $s0, $zero, 10
ADDI $s1, $zero, 2
ADDI $s2, $zero, 0
AGAIN: SUB $s0, $s0, $s1
BEQ $s0, $s2, DONE
J AGAIN
DONE:
