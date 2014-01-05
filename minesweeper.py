import game

import random
import time

class MinesweeperGame(object):
	"""
	Class for a Minesweeper game template.
	Hopefully this class is flexible enough to be implemented as various forms
	of Minesweeper (i.e. certain configurations or mines or stuff).
	"""
	def __init__(self, nMines, columns, rows):
		# super(MinesweeperGame, self).__init__()
		self.nMines = nMines
		self.columns = columns
		self.rows = rows
		self.board = []
		# try:
		self.init_board()
		# except Exception, e:
			# print "Caught error in board initialization:"
			# raise e

	def print_board(self, src = 'log.txt'):
		f = open(src, 'w')
		for row in xrange(self.rows):
			for col in xrange(self.columns):
				f.write(str(self.board[row][col]))
				f.write(" | ")
			f.write("\n")
		f.close()

	def init_mines(self):
		'''
		Randomly chooses a grid position to place each mine. 
		'''
		start = time.clock()
		for dummy in xrange(self.nMines):
			while True:
				row,column = random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)
				end = time.clock()
				if self.board[row][column] != -1:
					self.board[row][column] = -1
					break
				if start - end >= 10.0:
					raise Error("Mine initialize error: Timeout failure.")
					print	"Test in game.py init_mines method"
					break
			start = end

	def get_adjacent_mines(self, row, col):
		adj_mines = 0
		for row_i in xrange(row - 1, row + 2):
			for col_i in xrange(col - 1, col + 2):
				if (row_i != row or col_i != col) and row_i >= 0 and row_i < self.rows and col_i >= 0 and col_i	< self.columns:
					if self.board[row_i][col_i] is -1:
						adj_mines += 1
		return adj_mines

	def set_numbers(self):
		for row in xrange(self.rows):
			for col in xrange(self.columns):
				if self.board[row][col] is not -1:
					self.board[row][col] = self.get_adjacent_mines(row, col)

	def init_board(self):
		# Sets board to a row by column grid of zeros
		for row in xrange(self.rows):
			self.board.append([0] * self.columns)
		self.init_mines()
		self.print_board()
		self.set_numbers()
		self.print_board()


	def is_Goal(self):
		"""
		Checks to see if current board configuration is the goal configuration 
		(i.e. all non-mine squares are clicked)
		"""
		pass

def main():
	print "Welcome to Minesweeper"
	game = MinesweeperGame(2,4, 4)

if __name__ == '__main__':
	main()
