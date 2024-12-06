# AssemblerForSDLX
On giving n lines of assembly code as input, we will get n lines of 32 bits binary instructions which can be used to implement on the FPGA board using the switches. Initially we printed only the 32 bits instruction line by line. Then, we printed the names of the opcodes alongside the 32 bits instruction to confirm whether the line corresponds to the correct opcode or not.
We have also taken care of the cases of the assembly code, i.e., the assembler will give the output independent of the case (uppercase or lowercase) in which the assembly code is written.


Example 1: ADD R1 R2 R3

The above line implies that R3 is the destination register where the value of R1+R2 is stored.

Example 2: ADDI R1 $4 R1

We have also used $ sign before immediate and offset values.
