from tkinter import Tk, Label, Button, Canvas
from tkinter import *  
from PIL import ImageTk,Image 
import random

from catan.types.resource_types import Wood, Wheat, Brick, Stone, Sheep, Desert, Water, EmptyResource

class MyFirstGUI:
	def __init__(self, master):
		pass

	

	
	

class Renderer(object):

	def __init__(self, asset_path="assets/hex-tiles/"):

		self.asset_path = asset_path

		self.resources = [Wood, Wheat, Brick, Stone, Sheep, Desert]
		
		self.create_window()

		
		self.load_imgs()


		self.hex_width = self.hex[Desert].width()
		self.hex_height = self.hex[Desert].height()

		#self.draw_img(
		#	self.hex[Water],
		#	self.width//2 - hex_width//2, self.height//2 - hex_height//2)

		self.draw_hex_tiles()   


		self.trade_button = Button(
			self.root,
			text="trade",
			command=self.greet
			)
		
		self.settlement_button = Button(
			self.root, text="build settlement",
			command=self.greet
			)

		self.road_button = Button(
			self.root,
			text="build road",
			command=self.greet
			)

		self.city_button = Button(
			self.root,
			text="build city",
			command=self.greet
			)

		self.development_button = Button(
			self.root,
			text="buy development card",
			command=self.greet
			)

		self.end_button = Button(
			self.root,
			text="end turn",
			command=self.greet
			)

		self.close_button = Button(
			self.root,
			text="Close",
			command=self.root.quit
			)

		self.trade_button.pack()
		self.settlement_button.pack()
		self.road_button.pack()
		self.city_button.pack()
		self.development_button.pack()
		self.close_button.pack()

		self.root.mainloop()

	def create_window(self):
		
		self.root = Tk()
		self.width = 3*self.root.winfo_screenwidth()//4
		self.height = 3*self.root.winfo_screenheight()//4

		self.root.title("Catan")

		self.canvas = Canvas(
			self.root,
			width = self.width,
			height = self.height
			)

		self.canvas.create_rectangle(
			0,
			0,
			self.width,
			self.height,
			fill="lightblue"
			)   

		self.canvas.pack()

	def draw_img(self, img, x, y):
		self.canvas.create_image(x, y, anchor=NW, image=img)

	def draw_hex_tiles(self):

		centerX = self.width//2 - self.hex_width//2
		centerY = self.height//2 - self.hex_height//2

		for i in range(-6, 7):
			for j in range(-5, 6):
				self.draw_img(self.hex[Water],
					centerX+i*self.hex_width+j*self.hex_width//2,
					centerY + centerY*j//2.46
					)


		for i in range(-2, 1):
				key = random.choice(self.resources)
				self.draw_img(self.hex[key],
					centerX+i*self.hex_width+2*self.hex_width//2,
					centerY - centerY*2//2.46
					)

		for i in range(-2, 2):
				key = random.choice(self.resources)
				self.draw_img(self.hex[key],
					centerX+i*self.hex_width+1*self.hex_width//2,
					centerY - centerY*1//2.46
					)

		for i in range(-2, 3):
				key = random.choice(self.resources)
				self.draw_img(self.hex[key],
					centerX+i*self.hex_width,
					centerY
					)

		for i in range(-2, 2):
				key = random.choice(self.resources)
				self.draw_img(self.hex[key],
					centerX+i*self.hex_width+1*self.hex_width//2,
					centerY + centerY*1//2.46
					)

		for i in range(-2, 1):
				key = random.choice(self.resources)
				self.draw_img(self.hex[key],
					centerX+i*self.hex_width+2*self.hex_width//2,
					centerY + centerY*2//2.46
					)
		

	def load_imgs(self):

		width = 2
		height = 2



		self.wheat_hex = PhotoImage(file=self.asset_path + "wheatHex.png")
		self.stone_hex = PhotoImage(file=self.asset_path + "oreHex.png")
		self.sheep_hex = PhotoImage(file=self.asset_path + "sheepHex.png")
		self.brick_hex = PhotoImage(file=self.asset_path + "clayHex.png")
		self.water_hex = PhotoImage(file=self.asset_path + "waterHex.png")
		self.desert_hex = PhotoImage(file=self.asset_path + "desertHex.png")
		self.wood_hex = PhotoImage(file=self.asset_path + "woodHex.png")

		self.wheat_hex = self.wheat_hex.subsample(width, height)
		print("scaled image")
		self.stone_hex = self.stone_hex.subsample(width, height)
		print("scaled image")
		self.sheep_hex = self.sheep_hex.subsample(width, height)
		print("scaled image")
		self.brick_hex = self.brick_hex.subsample(width, height)
		print("scaled image")
		self.water_hex = self.water_hex.subsample(width, height)
		print("scaled image")
		self.desert_hex = self.desert_hex.subsample(width, height)
		print("scaled image")
		self.wood_hex = self.wood_hex.subsample(width, height)
		print("scaled image")

		self.hex = {
		Wood:self.wood_hex,
		Stone:self.stone_hex,
		Sheep:self.sheep_hex,
		Brick:self.brick_hex,
		Water:self.water_hex,
		Desert:self.desert_hex,
		Wheat:self.wheat_hex
		}

	def greet(self):
		print("Greetings!")


	


		