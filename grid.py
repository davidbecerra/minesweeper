from __future__ import print_function

import numpy as np
from itertools import product


class Grid(object):
    def __init__(self, nrows=8, ncols=8, nmines=2):
        self.nrows = nrows
        self.ncols = ncols
        self.nmines = nmines
        self.grid = np.array([[Cell() for _ in xrange(ncols)] for _ in xrange(nrows)], dtype=object)
        self.populate_mines()

    def populate_mines(self):
        all_positions = list(product(xrange(self.nrows), xrange(self.ncols)))
        mine_indices = np.random.choice(xrange(self.nrows * self.ncols), size=self.nmines, replace=False)
        for mi in mine_indices:
            gindex = all_positions[mi]
            self.grid[gindex].value = -1
            self.populate_neighbors(gindex)

    def populate_neighbors(self, gindex):
        for dx, dy in product([-1, 0, 1], repeat=2):
            ix = gindex[0] + dx
            iy = gindex[1] + dy
            # Don't change gindex (dx and dy are both zero)
            # Out of bounds
            # Don't change a mine square
            if dx == dy == 0 or \
               ix < 0 or ix >= self.nrows or iy < 0 or iy >= self.ncols or \
               self.grid[ix, iy].is_mine():
                continue
            else:
                self.grid[ix, iy] += 1

    def print_grid(self):
        print('Game Board\n----------------------')
        for row in self.grid:
            print('|', end="")
            for cell in row:
                if cell.is_mine():
                    print('| X ', end="")
                else:
                    print('| %d ' % cell.value, end="")
            print('|')

class Cell(object):
    def __init__(self, value=0):
        self.value = value

    def is_mine(self):
        return self.value == -1

    def __iadd__(self, delta):
        self.value += delta
        return self
