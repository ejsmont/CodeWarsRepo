from unittest import TestCase
from .molecule_to_atoms import parse_molecule


class TestParseModule(TestCase):
    def test_parse_molecule(self):
        str = '[a(aa{aaa}a}]'
        self.assertEquals(parse_molecule(str), '(a(aa(aaa)a))')

