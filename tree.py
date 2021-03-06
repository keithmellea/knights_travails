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

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            node.parent = self

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None

    def add_parents(self):
        return self._parent

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent is node:
            return
        if self._parent:
            self._parent.remove_child(self)
        self._parent = node
        if node is not None:
            node.add_child(self)

    def depth_search(self, value):
        if self._value == value:
            return self
        for child in self._children:
            node = child.depth_search(value)
            if node is not None:
                return node

    def breadth_search(self, value, queue=set()):

        queue.append(self)

        while queue:
            node = queue.pop(0)

            if node._value == value:
                return node

            for child in node.children:
                queue.append(child)

        return None


node1 = Node("root1")
# node2 = Node("root2")
node3 = Node("root3")

node1.add_child(node3)
print(node1.depth_search("root3"))
# node3.parent = node2

# print(node1.children)
# print(node2.children)
