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

	def init_mines(self):
		for dummy in self.nMines:
			start = time.clock()
			while:
				row,column = random.randint(0, self.rows), random.randint(0, self.columns)
				if self.board[row][column] != -1:
					self.board[row][column] = -1
					break
				end = time.clock()
				if start - end >= 10.0:
					raise Error("Mine initialize error: Timeout failure.")
					break
				start = end
	
	def set_numbers(self):
		pass

	def init_board(self):
		# Sets board to a row x column grid of zeros
		for row in xrange(self.rows):
			self.board[row] = [0] * self.columns
		init_mines()
		set_numbers()

	def is_Goal(self):
		"""
		Checks to see if current board configuration is the goal configuration 
		(i.e. all non-mine squares are clicked)
		"""
		pass




