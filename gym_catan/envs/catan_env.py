import gym
from gym import error, spaces, utils
from gym.utils import seeding
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame.locals import *
import numpy as np
from copy import copy

class CatanEnv(gym.Env):

	metadata = {'render.modes': ['human']}
	
	def __init__(self, size=16):
  		pass

def main():
	pass	

if __name__ == "__main__":
  
  main()