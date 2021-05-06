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

    def add_child(self):
        self._children.append(self)
        if self not in self._children
