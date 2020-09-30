import numpy as np

from .hex_grid import HexGrid
from .resource_types import Wood, Wheat, Brick, Stone, Sheep, Desert, Water, EmptyResource
from .player_types import Red, Blue, White, Orange, EmptyPlayer

class Board(Grid):

	def __init__(self):
		pass

	def setup():
		"""
		sets up the game
		"""
		self.populate_tiles()

	def populate_tiles(self):

		"""

		populates each tile with a resource and roll number

		"""