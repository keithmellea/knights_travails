class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    def add_child(self, node):
        self._children.append(node)
        if node not in self._children:
            self._parent = node
    
    def add_parents(self):
        return self._parent

    @parent.setter
    def parent(self, node):
       return self._parent.add_child(self)
