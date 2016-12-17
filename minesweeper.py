from __future__ import print_function

import kivy
kivy.require('1.9.1')

from kivy.app import App


import argparse

from grid import Grid


class MineSweeperError(Exception):
    pass


class Minesweeper(object):
    def __init__(self, difficulty='easy'):
        if difficulty == 'easy':
            grid_params = {'nrows': 8, 'ncols': 8, 'nmines': 10}
        elif difficulty == 'medium':
            grid_params = {'nrows': 16, 'ncols': 16, 'nmines': 40}
        elif difficulty == 'hard':
            grid_params = {'nrows': 24, 'ncols': 24, 'nmines': 99}
        else:
            raise MineSweeperError('Unsupported difficulty setting: %s' % difficulty)
        self.game_board = Grid(**grid_params)
        self.game_board.print_grid()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--difficulty', choices=['easy', 'medium', 'hard'], default='easy')
    return parser.parse_args()

if __name__ == '__main__':
    print('Starting game...')
    args = parse_args()
    MS = Minesweeper(difficulty=args.difficulty)
