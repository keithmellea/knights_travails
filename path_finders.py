import Node


class KnightPathFinder:
    def __init__(self, (0, 0)):
        self.root = (0, 0)
        self.considered_positions = set(self.root)
