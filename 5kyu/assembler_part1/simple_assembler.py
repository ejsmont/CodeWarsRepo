"""
We want to create a simple interpreter of assembler which will support the following instructions:

    mov x y - copies y (either a constant value or the content of a register) into register x
    inc x - increases the content of register x by one
    dec x - decreases the content of register x by one
    jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward),
              but only if x (a constant or a register) is not zero

Register names are alphabetical (letters only). Constants are always integers (positive or negative).

Note: the jnz instruction moves relative to itself.
For example, an offset of -1 would continue at the previous instruction,
while an offset of 2 would skip over the next instruction.

The function will take an input list with the sequence of
the program instructions and will return a dictionary with the contents of the registers.

Also, every inc/dec/jnz on a register will always be followed by
a mov on the register first, so you don't need to worry about uninitialized registers.

Example:
    simple_assembler(['mov a 5','inc a','dec a','dec a','jnz a -1','inc a'])

''' visualized:
mov a 5
inc a
dec a
dec a
jnz a -1
inc a
''''

The above code will:

    set register a to 5,
    increase its value by 1,
    decrease its value by 2,
    then decrease its value until it is zero (jnz a -1 jumps to the previous instruction if a is not zero)
    and then increase its value by 1, leaving register a at 1

So, the function should return

{'a': 1}
"""

__author__ = 'pejs'


def simple_assembler(program):
    """
    Function responsible for parsing and executing input commands. Models simple assembler.

    Handled commands:
        mov x y - copies y (either a constant value or the content of a register) into register x
        inc x - increases the content of register x by one
        dec x - decreases the content of register x by one
        jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward),
                but only if x (a constant or a register) is not zero
    :param program: list containing all commands to be executed
    :return: dictionary with the content of all registers
    """
    def mov(x, y, all_reg, step):
        if y.isalpha():
            all_reg[x] = all_reg[y]
        else:
            y = int(y)
            all_reg[x] = y
        step += 1
        return step

    def inc(x, _, all_reg, step):
        all_reg[x] += 1
        step += 1
        return step

    def dec(x, _, all_reg, step):
        all_reg[x] -= 1
        step += 1
        return step

    def jnz(x, y, all_reg, step):
        if all_reg[x] != 0:
            step += int(y)
        else:
            step += 1
        return step

    commands_dict = {
        'mov': mov,
        'inc': inc,
        'dec': dec,
        'jnz': jnz
    }
    all_registers = {}
    current_step = 0
    program_len = len(program)
    while current_step < program_len:
        command = program[current_step].split()
        register = command[1]
        operand = None
        if len(command) > 2:
            operand = command[2]
        current_step = commands_dict[command[0]](register, operand, all_registers, current_step)
    return all_registers
