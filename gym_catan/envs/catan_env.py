import gym
from gym import error, spaces, utils
from gym.utils import seeding
from os import environ
import numpy as np
from copy import copy
from catan.renderer import Renderer

class CatanEnv(gym.Env):

	metadata = {'render.modes': ['human']}
	
	def __init__(self, size=16):
		pass

def main():
	

	renderer = Renderer()


if __name__ == "__main__":

	main()


