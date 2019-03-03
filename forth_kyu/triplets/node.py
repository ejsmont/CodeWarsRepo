class Node:

    def __init__(self, letter):
        self._letter = letter
        self._children = set()

    @property
    def letter(self):
        return self._letter

    @property
    def children(self):
        return self._children

    def __iadd__(self, other):
        self._children.add(other)
        return self

    def __str__(self):
        return self._letter

    def __repr__(self):
        children_str =  ','.join([str(node) for node in self._children])
        return str(self._letter) + ': ' + children_str
