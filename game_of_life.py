class World(object):
    def __init__(self, cells = []):
        self.cells = set(map(lambda x: tuple(x), cells))

    def live_cells(self):
        return list(map(lambda x: list(x), self.cells))

    def is_alive(self, cell):
        return tuple(cell) in self.cells

    def next_iteration(self):
        next_gen = filter(
            lambda x: self._should_be_alive(x),
            self._to_be_tested()
        )
        return World(list(next_gen))

    def _neighbors(self, cell):
        x = cell[0]
        y = cell[1]

        return [
            (x - 1, y - 1), (x - 0, y - 1), (x + 1, y - 1),
            (x - 1, y - 0),                 (x + 1, y - 0),
            (x - 1, y + 1), (x - 0, y + 1), (x + 1, y + 1)
        ]

    def _to_be_tested(self):
        list_cells = list(self.cells)
        for cell in list_cells:
            list_cells = self._neighbors(cell) + list_cells
        return set(list_cells)

    def _count_live_neighbors(self, cell):
        count = 0
        for neighbor in self._neighbors(cell):
            if self.is_alive(neighbor):
                count += 1

        return count

    def _should_be_alive(self, cell):
        alive = self.is_alive(cell)
        neighbor_count = self._count_live_neighbors(cell)

        return (alive and neighbor_count == 2) or neighbor_count == 3
