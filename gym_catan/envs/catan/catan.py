import numpy as np

from .resource_types import Wood, Wheat, Brick, Stone, Sheep, Empty
from .board import Board


class Catan(object):

	def __init__(self):

		self.board = Board()
		self.players = Players()

	def play(self):


		# populate board

		# decide player order randomly

		# place initial settlements / roads

		# distribute final initial settlment resources

		# main game loop:

			# roll dice

			# distribute resource cards

			# turn loop:

				# actions:
				# ------------------------------
				# make trades (bank or player)
				# build settlement, roads, cities
				# get development card
				# end turn

		pass

