from unittest import TestCase
from .simple_assembler import simple_assembler


class TestSimpleAssembler(TestCase):
    def test_simple_assembler(self):
        program = ['mov a 5','inc a','dec a','dec a','jnz a -1','inc a']
        self.assertEquals(simple_assembler(program), {'a': 1})
        program = ['mov a 1', 'mov b 1']
        self.assertEquals(simple_assembler(program), {'a': 1, 'b': 1})
        code = '''\
            mov c 12
            mov b 0
            mov a 200
            dec a
            inc b
            jnz a -2
            dec c
            mov a b
            jnz c -5
            jnz 0 1
            mov c a'''
        program = code.splitlines()
        self.assertEquals(simple_assembler(program),{'a': 409600, 'c': 409600, 'b': 409600})
