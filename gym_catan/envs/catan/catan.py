import numpy as np

from .resource_types import Wood, Wheat, Brick, Stone, Sheep, Empty
from .board import Board


class Catan(object):

	def __init__(self):


		self.board = Board()
		self.players = Players()

