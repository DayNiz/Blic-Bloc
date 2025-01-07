# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pygame
import random
import time
import numpy as np


class Game():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((800, 600))
		self.clock = pygame.time.Clock()
		self.running = True
		self.grid = [[0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0]]
		# grid[y][x]
		# y; x------>
		#  |
		#  |
		#  |
		# \/
		
		self.tetrominos = {
			'L': [[1, 0, 0, 0],
				  [1, 0, 0, 0],
				  [1, 1, 0, 0],
				  [0, 0, 0, 0]],

			'Lr': [[0, 0, 1, 0],
				   [0, 0, 1, 0],
				   [0, 1, 1, 0],
				   [0, 0, 0, 0]],

			'T': [[1, 1, 1, 0],
				  [0, 1, 0, 0],
				  [0, 0, 0, 0],
				  [0, 0, 0, 0]],

			'Z': [[1, 1, 0, 0],
				  [0, 1, 1, 0],
				  [0, 0, 0, 0],
				  [0, 0, 0, 0]],

			'Zr': [[0, 1, 1, 0],
				   [1, 1, 0, 0],
				   [0, 0, 0, 0],
				   [0, 0, 0, 0]],
			
			'O': [[1, 1, 0, 0],
				  [1, 1, 0, 0],
				  [0, 0, 0, 0],
				  [0, 0, 0, 0]],
			
			'I': [[1, 0, 0, 0],
				  [1, 0, 0, 0],
				  [1, 0, 0, 0],
				  [1, 0, 0, 0]],
				}
		
		self.cell_type = ((0, 0, 0),        # EMPTY
						  (250, 50, 200),   # Pink
						  (120, 220, 240),  # Blue
						  (250, 220, 100),  # Orange
						  (160, 254, 80),   # Green
						  (200, 200, 200),  # White
						  (180, 60, 180),   # Purpe
						  )
		
		self.pixel_size = 64
		self.pl_x = 2
		self.pl_y = 0
		self.pl_curr_type = random.randint(1, len(self.cell_type)-1)
		self.pl_next = random.randint(1, len(self.cell_type)-1)
		self.pl_next_next = random.randint(1, len(self.cell_type)-1)
	
	def run(self, speed: int):
		self.tetrominos = self.rotate_all_shapes()
		update_countdown = round(30/speed)
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					break
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.move_left()
					if event.key == pygame.K_RIGHT:
						self.move_right()
					if event.key == pygame.K_DOWN:
						self.move_down()
			
			self.screen.fill((40, 20, 110))

			##GAME LOGIC
			# Randomize the tetrominos order, for mor fun xD
			tmp_rand_list = list(self.tetrominos.items())
			random.shuffle(tmp_rand_list)
			self.tetrominos = dict(tmp_rand_list)
			self.falling_block()
			self.draw_grid()
			self.draw_ui()
			update_countdown -= 1
			if update_countdown == 0:
				self.move_down()
				update_countdown = round(30/speed)

			pygame.display.flip()
			self.clock.tick(30) # Update at 30fps
		#time.sleep(2)
		pygame.quit()
	
	def draw_grid(self):
		"""
		Draw the game's grid with corresponding colors
		Does not draw the currently controled block
		"""
		for x in range(len(self.grid[0])):
			for y in range(len(self.grid)):
				pygame.draw.rect(self.screen, self.cell_type[self.grid[y][x]],
						[self.pixel_size*x+240, self.pixel_size*y+100, self.pixel_size, self.pixel_size])
		# Draw Player
		pygame.draw.rect(self.screen, self.cell_type[self.pl_curr_type],
				[self.pixel_size*self.pl_x+240, self.pixel_size*self.pl_y+100, self.pixel_size, self.pixel_size])
		
	def draw_ui(self):
		"""
		Draw various UI element on the screen
		Currently only draw 2 next shape
		"""
		pygame.draw.rect(self.screen, self.cell_type[self.pl_next], [600, 200, self.pixel_size, self.pixel_size])
		pygame.draw.rect(self.screen, self.cell_type[self.pl_next_next], [600, 296, self.pixel_size, self.pixel_size])

	def move_down(self) -> bool:
		"""Move down the currently controlled shape

		Returns:
			bool: return True if we go onto the next shape
		"""
		if self.pl_y >= len(self.grid)-1 or self.grid[self.pl_y+1][self.pl_x] != 0:
			if self.pl_y == 0:
				self.game_over()
			self.grid[self.pl_y][self.pl_x] = self.pl_curr_type
			for color in range(1, len(self.cell_type)):
				self.check_tetrominos(color)
			self.pl_x, self.pl_y = 2, 0
			self.pl_curr_type = self.pl_next
			self.pl_next = self.pl_next_next
			self.pl_next_next = random.randint(1, len(self.cell_type)-1)
			return True
			
		else:
			self.pl_y += 1
			return False
	
	def move_left(self):
		"""Move the currently controlled block to the left,
			within game's boundary.
		"""
		if self.pl_x <= 0 or self.grid[self.pl_y][self.pl_x-1] != 0:
			return
		else:
			self.pl_x -= 1

	def move_right(self):
		"""Move the currently controlled block to the right,
			within game's boundary.
		"""
		if self.pl_x >= len(self.grid[0])-1 or self.grid[self.pl_y][self.pl_x+1] != 0:
			return
		else:
			self.pl_x += 1
	
	def check_tetrominos(self, color) -> bool:
		"""Check if a tetrominos is created at the x and y coordonate
		
		Return:
			bool: If there was a shape at the coordonate
		"""
		for shape_name, shape in self.tetrominos.items():
			found, y, x = self.match_pattern(shape, color)
			if found:
				print(f"{shape_name} found at {y}::{x}!")
				self.destroy_tetromino(y, x, shape)
				return True
		return False

	def match_pattern(self, shape, color) -> (bool, int, int):
		"""Check within self.grid if there's the given shape in the grid

		Args:
			shape (array[int][int]): The shape to test
			color (int): The color of the shape
		
		Return:
			bool: if shape found,
			int, int: where it was found, else (False, False)
		"""
		rows, cols = len(self.grid), len(self.grid[0])
		shape_rows, shape_cols = len(shape), len(shape[0])

		for x in range(rows - shape_rows + 1):
			for y in range(cols - shape_cols + 1):
				match = True
				for i in range(shape_rows):
					for j in range(shape_cols):
						if shape[i][j] == 1 and self.grid[x + i][y + j] != color:
							match = False
							break
					if not match:
						break
				if match:
					print(f"Shape detected at position: ({x}, {y})")
					return (True, x, y)
		return (False, False, False)
	
	def rotate_all_shapes(self):
		new_tetrominos = {}
		for shape_name, base_shape in self.tetrominos.items():
			shape = base_shape
			for rot in range(1, 5):
				# rot = 0,1,2,3
				cleared_shape = [[0]]
				cleared_shape = self.clear_shape(shape)
				print("---")
				new_tetrominos[f"{shape_name}-{rot}"] = cleared_shape
				shape = self.rotate_shape(shape, rot)
		print(new_tetrominos)
		return new_tetrominos

	def rotate_shape(self, shape, nb):
		"""Rotate the shape 90° clockwise

		Args:
			shape (array[int][int]): The shape to rotate
			nb (int): The number of time to rotate 90°
		"""
		for _ in range(nb):
			shape = [[shape[j][i] for j in range(len(shape))] for i in range(len(shape[0])-1, -1, -1)]
		return shape
	
	def clear_shape(self, shape):
		np_shape = np.array(shape)
		while np.all(np_shape[-1] == 0):
			print("clearing last line")
			shape.pop()
			np_shape = np.array(shape)
		if shape == []:
			# Return empty array if shape was only 0
			return [[0]]
		for y in shape:
			if y[-1] != 0:
				print("shape after clearing: ", shape)
				return shape
		for y in range(len(shape)):
			new_y = np.delete(shape[y], -1)
			shape[y] = new_y.tolist()
		return self.clear_shape(shape)

	def destroy_tetromino(self, y, x, shape):
		"""Clears the blocks of a matching tetromino from the grid.

		Args:
			x (int): The X coordonates to check in the game's grid
			y (int): The Y coordonates to check in the game's grid
			shape (array[int][int]): The shape to test
		"""
		for j in range(len(shape)):
			for i in range(len(shape[0])):
				if shape[j][i] == 1:
					nx, ny = x + i, y + j
					# Clear block
					self.grid[ny][nx] = 0

	def falling_block(self):
		for y in range(len(self.grid)-1):
			for x in range(len(self.grid[0])-1):
				if self.grid[y+1][x] == 0 and self.grid[y][x] != 0:
					self.grid[y+1][x] = self.grid[y][x]
					self.grid[y][x] = 0
					print("Falling block", y, x)
		for color in range(1, len(self.cell_type)):
			self.check_tetrominos(color)


	def game_over(self):
		"""The game is Over!"""
		self.running = False

	
if __name__ == "__main__":
	blicBlock = Game()
	blicBlock.run(2)
