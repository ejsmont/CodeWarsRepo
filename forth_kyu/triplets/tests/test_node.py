import unittest
from forth_kyu.triplets.node import Node


class TestNode(unittest.TestCase):

    def setUp(self):
        test_node = Node('a')
        test_node += Node('b')
        test_node += Node('c')
        self.test_node = test_node

    def test_property_letter(self):
        self.assertEqual(self.test_node.letter, 'a')

    def test_property_children(self):
        result = self.test_node.children
        assert len(result) == 2
        expected = ('b', 'c')
        assert any(node.letter in expected for node in result)
