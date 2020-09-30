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

		#self.draw_img(
		#	self.hex[Water],
		#	self.width//2 - hex_width//2, self.height//2 - hex_height//2)

		self.draw_hex_tiles()   


		self.player1_stat = Label(self.root, height = 5, width = 5)
		self.player2_stat = Label(self.root, height = 5, width = 5) 
		self.player3_stat = Label(self.root, height = 5, width = 5) 
		self.player4_stat = Label(self.root, height = 5, width = 5)  

		self.player1_stat.grid(row = 0, column = 0, padx = 0, pady = 0)
		self.player2_stat.grid(row = 0, column = 1, padx = 0, pady = 0)
		self.player3_stat.grid(row = 0, column = 2, padx = 0, pady = 0)
		self.player4_stat.grid(row = 0, column = 3, padx = 0, pady = 0)

		"""
		self.player1_stat.insert(END, "")
		self.player2_stat.insert(END, "")
		self.player3_stat.insert(END, "")
		self.player4_stat.insert(END, "")
		"""

		self.trade_button = Button(
			self.root,
			text="trade",
			command=self.trade,
			image = self.trade_icon,
			compound = TOP 
			)
		
		self.settlement_button = Button(
			self.root, text="build settlement",
			command=self.build_settlement,
			image = self.settlement_icon,
			compound = TOP 
			)

		self.road_button = Button(
			self.root,
			text="build road",
			command=self.build_road
			)

		self.city_button = Button(
			self.root,
			text="build city",
			command=self.build_city,
			image = self.city_icon,
			compound = TOP 
			)

		self.development_button = Button(
			self.root,
			text="buy development card",
			command=self.buy_development
			)

		self.end_turn_button = Button(
			self.root,
			text="end turn",
			command=self.end_turn
			)

		"""
		self.close_button = Button(
			self.root,
			text="Close",
			command=self.root.quit
			)
		"""

		self.trade_button.grid(row = 2, column = 0, padx = 0, pady = 0)
		self.settlement_button.grid(row = 2, column = 1, padx = 0, pady = 0)
		self.road_button.grid(row = 2, column = 2, padx = 0, pady = 0)
		self.city_button.grid(row = 2, column = 3, padx = 0, pady = 0)
		self.development_button.grid(row = 2, column = 4, padx = 50, pady = 0)
		self.end_turn_button.grid(row = 2, column = 5, padx = 50, pady = 0)
		#self.close_button.grid(row = 1, column = 5, padx = 0, pady = 0)

		self.root.mainloop()

	def create_window(self):
		
		self.root = Tk()
		self.root.configure(bg='black')
		self.root['bg'] = 'black'
		self.width = 3*self.root.winfo_screenwidth()//5
		self.height = 3*self.root.winfo_screenheight()//5

		self.root.title("Catan")

		self.canvas = Canvas(
			self.root,
			width = self.width,
			height = self.height,
			highlightthickness=0
			)

		self.canvas.create_rectangle(
			0,
			0,
			self.width,
			self.height,
			fill="lightblue"
			)   

		self.canvas.grid(row = 1, column = 0, columnspan = 10, padx = 0, pady = 0)

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

		self.trade_icon = PhotoImage(
			file="assets/PNG/Pieces(Black)/pieceBlack.png"
			)

		self.settlement_icon = PhotoImage(
			file="assets/PNG/Pieces(Black)/settlementBlack.png"
			)

		self.city_icon = PhotoImage(
			file="assets/PNG/Pieces(Black)/cityBlack2.png"
			)


		self.wheat_hex = PhotoImage(file=self.asset_path + "wheatHex.png")
		self.stone_hex = PhotoImage(file=self.asset_path + "oreHex.png")
		self.sheep_hex = PhotoImage(file=self.asset_path + "sheepHex.png")
		self.brick_hex = PhotoImage(file=self.asset_path + "clayHex.png")
		self.water_hex = PhotoImage(file=self.asset_path + "waterHex.png")
		self.desert_hex = PhotoImage(file=self.asset_path + "desertHex.png")
		self.wood_hex = PhotoImage(file=self.asset_path + "woodHex.png")


		self.hex_width = self.desert_hex.width()
		self.hex_height = self.desert_hex.height()

		width = self.width/self.hex_width
		height = self.height/self.hex_height

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

		self.hex_width = self.hex[Desert].width()
		self.hex_height = self.hex[Desert].height()

	def greet(self):
		print("greet")

	def trade(self):
		print("Clicked Trade!")

	def build_road(self):
		print("Clicked Build Road!")

	def build_settlement(self):
		print("Clicked Build Settlement!")

	def build_city(self):
		print("Clicked Build City!")

	def buy_development(self):
		print("Clicked Buy Development!")

	def end_turn(self):
		print("Clicked End Turn!")


	


		