import Node


class KnightPathFinder:
    def __init__(self, (0, 0)):
        self._root = (0, 0)
        self._considered_positions = set(self.root)

    def get_valid_moves(self, pos): 
        possible_moves = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]
        valid_moves = []
            for move in possible_moves:
                new_position = tuple(lambda i, j: i + j, pos, move)
                if new_position[0] in range(0, 7) and if new_position[1] in range(0, 7): 
                    valid_moves.append(new_position)
        return valid_moves
