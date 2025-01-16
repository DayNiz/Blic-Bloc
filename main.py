import pygame
import pygame_menu
from game import Game

class MainMenu:
	def __init__(self):
		pygame.init()
		self.win = pygame.display.set_mode((800, 600))
		self._speed = 4
		self.MIN = 1
		self._hard = 6
		self._impossible = 11
		self.MAX = 16

		self.levels = [(f"Easy ({lev})", lev) for lev in range(self.MIN, self._hard)]
		self.levels += [(f"Hard ({lev})", lev) for lev in range(self._hard, self._impossible)]
		self.levels += [(f"Impossible ({lev})", lev) for lev in range(self._impossible, self.MAX)]
		#TODO: persistent score stored on file
		self.score = 0
		self.game = Game()
		self.create_menu()

		while True:
			events = pygame.event.get()
			for event in events:
				if event.type == pygame.QUIT:
					exit()

			if self.menu.is_enabled():
				self.menu.update(events)
				self.menu.draw(self.win)

			pygame.display.update()

	def create_menu(self):
		self.menu = pygame_menu.Menu('Blic-Bloc', 790, 590,
				theme=pygame_menu.themes.THEME_ORANGE)

		self.menu.add.label("Welcome to Blic-Bloc!")
		self.score_label = self.menu.add.label(f"SCORE Total: {self.score}")
		self.menu.add.selector("Choose a level: ", self.levels, onchange=self.set_difficulty)
		self.menu.add.button('Play', self.start_game)

		#Run the menu
		# self.menu.mainloop(self.win)

	def start_game(self):
		self.game = Game()
		self.score += self.game.run(self._speed + 2)
		self.score_label.set_title(f"SCORE Total: {self.score}")

	def set_difficulty(self, name, value):
		if value < self.MIN: value = self.MIN
		if value > self.MAX: value = self.MAX
		self._speed = value

if __name__ == "__main__":
	menu = MainMenu()
