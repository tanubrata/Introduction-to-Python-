#Name- Tanubrata Dey
#Date- 27 April 2018
#My first MIPS program that prints: I love Python

ADDI $sp, $sp, -14
ADDI $t0, $zero, 73
SB $t0, 0($sp)
ADDI $t0, $zero, 32
SB $t0, 1($sp)
ADDI $t0, $zero, 108
SB $t0, 2($sp)
ADDI $t0, $zero, 111
SB $t0, 3($sp)
ADDI $t0, $zero, 118
SB $t0, 4($sp)
ADDI $t0, $zero, 101
SB $0, 5($sp)
ADDI $t0, $zero, 32
SB $t0, 6($sp)
ADDI $t0, $zero, 80
SB $t0, 7($sp)
ADDI $t0, $zero, 121
SB $t0, 8($sp)
ADDI $t0, $zero, 116
SB $t0, 9($sp)
ADDI $t0, $zero, 104
SB $t0, 10($sp)
ADDI $t0, $zero, 111
SB $t0, 11($sp)
ADDI $t0, $zero, 110
SB $t0, 12($sp)
ADDI $t0, $zero, 0
SB $t0, 13($sp)

ADDI $v0, $zero, 4
ADDI $a0, $sp, 0
syscall
