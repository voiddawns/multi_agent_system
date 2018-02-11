import sys 
import pygame

def init(width=800, height=600):
	global size, speed, black, window, screen, agents
	pygame.init()

	size = width, height
	speed = [2, 2]
	black = 0, 0, 0

	window = pygame.display.set_mode(size)
	screen = pygame.Surface((size))

	agents = []
	return agents


def run():
	global size, speed, black, window, screen, agents
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill((50, 50, 50))

		for agent in agents:
			agent.run()

		window.blit(screen, (0, 0))
		pygame.display.flip()
		# pygame.time.delay(100)


class entity:
	def __init__(self,x_pos, y_pos, image_file):
		global window
		self.x = x_pos
		self.y = y_pos
		self.bitmap = pygame.image.load(image_file)
		self.width, self.heigth = self.bitmap.get_rect().size
		self.bitmap.set_colorkey((0, 0, 0))
		self.actions_to_do = []

	def render(self):
		screen.blit(self.bitmap, (self.x, self.y))

	def __step_left__(self, step=1):
		if self.x - step >= 0:
			self.x -= step

	def __step_right__(self, step=1):
		window_width = pygame.display.get_surface().get_width()
		if self.x + step <= window_width - self.width:
			self.x += step

	def __step_up__(self, step=1):
		if self.y - step >= 0:
			self.y -= step

	def __step_down__(self, step=1):
		window_heigth = pygame.display.get_surface().get_height()
		if self.y + step <= window_heigth - self.heigth:
			self.y += step

	# digit value - 1
	def go_left(self, step=1):
		self.actions_to_do.append((1, step))

	# digit value - 2
	def go_right(self, step=1):
		self.actions_to_do.append((2, step))

	# digit value - 3
	def go_up(self, step=1):
		self.actions_to_do.append((3, step))

	# digit value - 4
	def go_down(self, step=1):
		self.actions_to_do.append((4, step))

	def run(self):
		for direction, step in self.actions_to_do:
			if 1 == direction:
				self.__step_left__(step)
			elif 2 == direction:
				self.__step_right__(step)
			elif 3 == direction:
				self.__step_up__(step)
			elif 4 == direction:
				self.__step_down__(step)
		
		self.actions_to_do.clear()
		self.render()



if __name__ == '__main__':
	init()
	run()