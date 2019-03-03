__author__ = 'pejs'

def mov(x, y, all_reg, _):
    all_reg[x] = all_reg[y] if y.isalpha() else all_reg[x] = int(y)

def inc(x, y, all_reg, _):
    all_reg[x] += 1

def dec(x, _, all_reg, _):
    all_reg[x] -= 1

def add(x, y, all_reg, _):
    all_reg[x] += all_reg[y] if y.isalpha() else all_reg[x] += int(y)

def jnz(x, y, all_reg, step):
    if (not x.isalpha() and x != 0) or all_reg[x] != 0: step += int(y) - 1

commands_dict = {
    'mov': mov,
    'inc': inc,
    'dec': dec,
    'jnz': jnz
}

def simple_assembler(program):
    all_registers = {}
    current_step = 0
    program_len = len(program)
    while current_step < program_len:
        command = program[current_step].split()
        register = command[1]
        operand = None
        if len(command) > 2:
            operand = command[2]
        commands_dict[command[0]](register, operand, all_registers, current_step)
        current_step += 1
    return all_registers


def f(a, b, c):
    pass

args = [10, 12, 13]
f(args)
