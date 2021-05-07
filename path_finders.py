import tree


class KnightPathFinder:
    def __init__(self, pos):
        self._pos = pos
        self._root = (0, 0)
        self._considered_positions = set(self._root)

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
        valid_moves = set()
        for move in possible_moves:
            new_position = tuple(map(lambda i, j: i + j, pos, move))
            if new_position[0] in range(0, 7) and new_position[1] in range(0, 7):
                valid_moves.add(new_position)
        return valid_moves

    def new_move_positions(self, pos):
        new_moves = self.get_valid_moves(
            pos).difference(self._considered_positions)
        self._considered_positions.union(new_moves)
        return new_moves


finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((0, 0)))
